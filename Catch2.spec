#
# spec file for package Catch2
#
# Copyright (c) 2021 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#
%global debug_package %{nil}

Name:           Catch2
Version:        2.13.8
Release:        1%{?dist}
Summary:        A modern, C++-native, header-only, test framework for unit-tests, TDD and BDD
License:        BSL-1.0
URL:            https://github.com/catchorg/%{name}/
Source:         https://github.com/catchorg/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.5
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
Catch2 stands for C++ Automated Test Cases in a Header and is a multi-paradigm
test framework for C++. which also supports Objective-C (and maybe C).
It is primarily distributed as a single header file, although certain
extensions may require additional headers.

%prep
%autosetup

%package devel
Summary:        A modern, C++-native, header-only, test framework for unit-tests, TDD and BDD

%description devel
Catch2 stands for C++ Automated Test Cases in a Header and is a multi-paradigm
test framework for C++. which also supports Objective-C (and maybe C).
It is primarily distributed as a single header file, although certain
extensions may require additional headers.

%build
%cmake -DCMAKE_BUILD_TYPE=Release \
       -DCMAKE_INSTALL_DOCDIR=%{_defaultdocdir}/%{name} \
       -DPKGCONFIG_INSTALL_DIR=%{_libdir}/pkgconfig
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%license LICENSE.txt
%doc README.md CODE_OF_CONDUCT.md
%doc %{_defaultdocdir}/%{name}
%{_datadir}/%{name}
%{_includedir}/catch2
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/catch2.pc

%changelog
* Mon May  3 2021 Ferdinand Thiessen <rpm@fthiessen.de>
- Update to version 2.13.6
  * Disabling all signal handlers no longer breaks compilation
  * catch_discover_tests should handle escaped semicolon (;) better
* Tue Apr 13 2021 Luigi Baldoni <aloisio@gmx.com>
- Update to version 2.13.5
  Improvements:
  * Added workaround for bug in XLC 16.1.0.1
  * Add detection for LCC when it is masquerading as GCC
  * Modified posix signal handling so it supports newer libcs
    + `MINSIGSTKSZ` was no longer usable in constexpr context.
  Fixes:
  * Fixed compilation of benchmarking when `min` and `max`
    macros are defined
    + Including `windows.h` without `NOMINMAX` remains a really
    bad idea, don't do it
  Miscellaneous:
  * `Catch2WithMain` target (static library) is no longer built
    by default
    + Building it by default was at best unnecessary overhead
    for people not using it, and at worst it caused trouble
    with install paths
    + To have it built, set CMake option
    `CATCH_BUILD_STATIC_LIBRARY` to `ON`
  * The check whether Catch2 is being built as a subproject is
    now more reliable
    + The problem was that if the variable name used internally
    was defined the project including Catch2 as subproject, it
    would not be properly overwritten for Catch2's CMake.
  version 2.13.4
  Improvements:
  * Improved the hashing algorithm used for shuffling test cases
    + `TEST_CASE`s that differ only in the last character should
    be properly shuffled
    + Note that this means that v2.13.4 gives you a different
    order of test cases than 2.13.3, even given the same seed.
  Miscellaneous:
  * Deprecated `ParseAndAddCatchTests` CMake integration
    + It is impossible to implement it properly for all the
    different test case variants Catch2 provides, and there
    are better options provided.
    + Use `catch_discover_tests` instead, which uses runtime
    information about available tests.
  * Fixed bug in `catch_discover_tests` that would cause it to
    fail when used in specific project structures
  * Added Bazel build file
  * Added an experimental static library target to CMake
* Tue Dec  1 2020 aloisio@gmx.com
- Update to version 2.13.3
  Fixes:
  * Fixed possible infinite loop when combining generators with
    section filter (`-c` option)
  Miscellaneous:
  * Fixed `ParseAndAddCatchTests` not finding `TEST_CASE`s
    without tags
  * `ParseAndAddCatchTests` supports `CMP0110` policy for
    changing behaviour of `add_test`
    + This was the shortlived change in CMake 3.18.0 that
    temporarily broke `ParseAndAddCatchTests`
  version 2.13.2
  Improvements:
  * Implemented workaround for NVCC ICE
  Fixes:
  * Fixed detection of `std::uncaught_exceptions` support under
    non-msvc platforms
  Miscellaneous:
  * `catch_discover_tests` has been improved significantly
    + You can now specify which reporter should be used
    + You can now modify where the output will be written
    + `WORKING_DIRECTORY` setting is respected
  * `ParseAndAddCatchTests` now supports `TEMPLATE_TEST_CASE`
    macros
  * Various documentation fixes and improvements
  version 2.13.1
  Improvements:
  * `ParseAndAddCatchTests` handles CMake v3.18.0 correctly
  * Improved autodetection of `std::byte`
  * Simplified implementation of templated test cases
    + This should have a tiny positive effect on its compilation
    throughput
  Fixes:
  * Automatic stringification of ranges handles sentinel ranges
    properly
* Fri Aug 14 2020 Luigi Baldoni <aloisio@gmx.com>
- Update to version 2.13.0
  Improvements:
  * `GENERATE` can now follow a `SECTION` at the same level of
    nesting
    + The `SECTION`(s) before the `GENERATE` will not be run
    multiple times, the following ones will.
  * Added `-D`/`--min-duration` command line flag
    + If a test takes longer to finish than the provided value,
    its name and duration will be printed.
    + This flag is overriden by setting `-d`/`--duration`.
  Fixes:
  * `TAPReporter` no longer skips successful assertions
  version 2.12.4:
  * `GENERATE` nested in a for loop no longer creates multiple
    generators
  * Fixed copy paste error breaking `TEMPLATE_TEST_CASE_SIG` for
    6 or more arguments
  * Fixed potential UB when handling non-ASCII characters in CLI
    args
  * There can be multiple calls to `GENERATE` on a single line
  * Improved `fno-except` support for platforms that do not
    provide shims for exception-related std functions
    + E.g. the Green Hills C++ compiler
  * XmlReporter now also reports test-case-level statistics
    + This is done via a new element, `OverallResultsCases`
  * Added `.clang-format` file to the repo
  * Rewrote contributing docs
    + They should explain the different levels of testing and so
    on much better
  version 2.12.2:
  * Fixed compilation failure if `is_range` ADL found deleted
    function
  * Fixed potential UB in `CAPTURE` if the expression contained
    non-ASCII characters
  * `std::result_of` is not used if `std::invoke_result` is
    available
  * JUnit reporter writes out `status` attribute for tests
  * Suppresed clang-tidy's `hicpp-vararg` warning
    + Catch2 was already suppressing the
    `cppcoreguidelines-pro-type-vararg` alias of the warning
  version 2.12.1:
  * Vector matchers now support initializer list literals better
  * Added support for `^` (bitwise xor) to `CHECK` and `REQUIRE`
  version 2.12.0:
  * Running tests in random order (`--order rand`) has been
    reworked significantly
    + Given same seed, all platforms now produce the same order
    + Given same seed, the relative order of tests does not
    change if you select only a subset of them
  * Vector matchers support custom allocators
  * `|` and `&` (bitwise or and bitwise and) are now supported
    in `CHECK` and `REQUIRE`
    + The resulting type must be convertible to `bool`
  * Fixed computation of benchmarking column widths in
    ConsoleReporter
  * Suppressed clang-tidy's `cppcoreguidelines-pro-type-vararg`
    in assertions
    + It was a false positive trigered by the new warning
    support workaround
  * Fixed bug in test specification parser handling of OR'd
    patterns using escaping
  * Worked around IBM XL's codegen bug
    + It would emit code for _destructors_ of temporaries in an
    unevaluated context
  * Improved detection of stdlib's support for
    `std::uncaught_exceptions`
  version 2.11.2:
  * GCC and Clang now issue warnings for suspicious code in
    assertions
    + E.g. `REQUIRE( int != unsigned int )` will now issue mixed
    signedness comparison warning
    + This has always worked on MSVC, but it now also works for
    GCC and current Clang versions
  * Colorization of "Test filters" output should be more robust
    now
  * `--wait-for-keypress` now also accepts `never` as an option
  * Reporters no longer round-off nanoseconds when reporting
    benchmarking results
  * It is now possible to customize benchmark's warm-up time
    when running the test binary
    + `--benchmark-warmup-time {ms}`
  * User can now specify how Catch2 should break into debugger
  * Fixes missing `<random>` include in benchmarking
  * Fixed missing `<iterator>` include in benchmarking
  * Hidden test cases are now also tagged with `[!hide]` as per
    documentation
  * Detection of whether libc provides `std::nextafter` has been
    improved
  * Composing already-composed matchers no longer modifies the
    partially-composed matcher expression
    + This bug has been present for the last ~2 years and nobody
    reported it
  version 2.11.1:
  * `google-build-using-namespace` clang-tidy warning is
    suppressed
  * `ObjectStorage` now behaves properly in `const` contexts
  * `GENERATE_COPY(a, b)` now compiles properly
  * Some more cleanups in the benchmarking support
* Wed Jan  8 2020 Luigi Baldoni <aloisio@gmx.com>
- Use only %%license
* Wed Dec 25 2019 Luigi Baldoni <aloisio@gmx.com>
- Update to version 2.11.0
  Improvements:
  * JUnit reporter output now contains more details in case of
    failure (#1347, #1719)
  * Added SonarQube Test Data reporter (#1738)
    + It is in a separate header, just like the TAP, Automake,
    and TeamCity reporters
  * `range` generator now allows floating point numbers (#1776)
  * Reworked part of internals to increase throughput
  Fixes:
  * The single header version should contain full benchmarking
    support (#1800)
  * `[.foo]` is now properly parsed as `[.][foo]` when used on
    the command line (#1798)
  * Fixed compilation of benchmarking on platforms where
    `steady_clock::period` is not `std::nano` (#1794)
  version 2.10.2
  Improvements:
  * Catch2 will now compile on platform where `INFINITY` is
    double (#1782)
  Fixes:
  * Warning suppressed during listener registration will no
    longer leak
  version 2.10.1
  Improvements:
  * Catch2 now guards itself against `min` and `max` macros from
    `windows.h` (#1772)
  * Templated tests will now compile with ICC (#1748)
  * `WithinULP` matcher now uses scientific notation for
    stringification (#1760)
  Fixes:
  * Templated tests no longer trigger `-Wunused-templates`
    (#1762)
  * Suppressed clang-analyzer false positive in context getter
    (#1230, #1735)
  Miscellaneous:
  * CMake no longer prohibits in-tree build when Catch2 is used
    as a subproject (#1773, #1774)
  version 2.10.0
  Fixes:
  * `TEMPLATE_LIST_TEST_CASE` now properly handles non-copyable
    and non-movable types (#1729)
  * Fixed compilation error on Solaris caused by a system header
    defining macro `TT` (#1722, #1723)
  * `REGISTER_ENUM` will now fail at compilation time if the
    registered enum is too large
  * Removed use of `std::is_same_v` in C++17 mode (#1757)
  * Fixed parsing of escaped special characters when reading
    test specs from a file (#1767, #1769)
  Improvements:
  * Trailing and leading whitespace in test/section specs are
    now ignored.
  * Writing to Android debug log now uses `__android_log_write`
    instead of `__android_log_print`
  * Android logging support can now be turned on/off at compile
    time (#1743)
    + The toggle is `CATCH_CONFIG_ANDROID_LOGWRITE`
  * Added a generator that returns elements of a range
    + Use via `from_range(from, to)` or `from_range(container)`
  * Added support for CRTs that do not provide `std::nextafter`
    (#1739)
    + They must still provide global `nextafter{f,l,}`
    + Enabled via `CATCH_CONFIG_GLOBAL_NEXTAFTER`
  * Special cased `Approx(inf)` not to match non-infinite values
    + Very strictly speaking this might be a breaking change,
    but it should match user expectations better
  * The output of benchmarking through the Console reporter when
    `--benchmark-no-analysis` is set is now much simpler (#1768)
  * Added a matcher that can be used for checking an exceptions
    message (#1649, #1728)
    + The matcher helper function is called `Message`
    + The exception must publicly derive from `std::exception`
    + The matching is done exactly, including case and whitespace
  * Added a matcher that can be used for checking relative
    equality of floating point numbers (#1746)
    + Unlike `Approx`, it considers both sides when determining
    the allowed margin
    + Special cases `NaN` and `INFINITY` to match user
    expectations
    + The matcher helper function is called `WithinRel`
  * The ULP matcher now allows for any possible distance between
    the two numbers
  * The random number generators now use Catch-global instance
    of RNG (#1734, #1736)
    + This means that nested random number generators actually
    generate different numbers
  Miscellaneous:
  * In-repo PNGs have been optimized to lower overhead of using
    Catch2 via git clone
  * Catch2 now uses its own implementation of the URBG concept
    + In the future we also plan to use our own implementation
    of the distributions from `<random>` to provide
    cross-platform repeatability of random results
  version 2.9.2
  Fixes:
  * `ChunkGenerator` can now be used with chunks of size 0
    (#1671)
  * Nested subsections are now run properly when specific
    section is run via the `-c` argument (#1670, #1673)
  * Catch2 now consistently uses `_WIN32` to detect Windows
    platform (#1676)
  * `TEMPLATE_LIST_TEST_CASE` now support non-default
    constructible type lists (#1697)
  * Fixed a crash in the XMLReporter when a benchmark throws
    exception during warmup (#1706)
  * Fixed a possible infinite loop in CompactReporter (#1715)
  * Fixed `-w NoTests` returning 0 even when no tests were
    matched (#1449, #1683, #1684)
  * Fixed matcher compilation under Obj-C++ (#1661)
  Improvements:
  * `RepeatGenerator` and `FixedValuesGenerator` now fail to
    compile when used with `bool` (#1692)
    + Previously they would fail at runtime.
  * Catch2 now supports Android's debug logging for its debug
    output (#1710)
  * Catch2 now detects and configures itself for the RTX
    platform (#1693)
    + You still need to pass `--benchmark-no-analysis` if you
    are using benchmarking under RTX
  * Removed a "storage class is not first" warning when
    compiling Catch2 with PGI compiler (#1717)
  Miscellaneous:
  * Documentation now contains indication when a specific
    feature was introduced (#1695)
    + These start with Catch2 v2.3.0, (a bit over a year ago).
    + `docs/contributing.md` has been updated to provide
    contributors guidance on how to add these to newly written
    documentation
  * Various other documentation improvements
    + ToC fixes
    + Documented `--order` and `--rng-seed` command line options
    + Benchmarking documentation now clearly states that it
    requires opt-in
    + Documented `CATCH_CONFIG_CPP17_OPTIONAL` and
    `CATCH_CONFIG_CPP17_BYTE` macros
    + Properly documented built-in vector matchers
    + Improved `*_THROWS_MATCHES` documentation a bit
  * CMake config file is now arch-independent even if
    `CMAKE_SIZEOF_VOID_P` is in CMake cache (#1660)
  * `CatchAddTests` now properly escapes `[` and `]` in test
    names (#1634, #1698)
  * Reverted `CatchAddTests` adding tags as CTest labels (#1658)
    + The script broke when test names were too long
    + Overwriting `LABELS` caused trouble for users who set them
    manually
    + CMake does not let users append to `LABELS` if the test
    name has spaces
  version 2.9.1
  Fixes:
  * Fix benchmarking compilation failure in files without
    `CATCH_CONFIG_EXTERNAL_INTERFACES` (or implementation)
  version 2.9.0
  Improvements:
  * The experimental benchmarking support has been replaced by
    integrating Nonius code (#1616)
    + This provides a much more featurefull micro-benchmarking
    support.
    + Due to the compilation cost, it is disabled by default.
    See the documentation for details.
    + As far as backwards compatibility is concerned, this
    feature is still considered experimental in that we might
    change the interface based on user feedback.
  * `WithinULP` matcher now shows the acceptable range (#1581)
  * Template test cases now support type lists (#1627)
  version 2.8.0
  Improvements:
  * Templated test cases no longer check whether the provided
    types are unique (#1628)
    + This allows you to e.g. test over `uint32_t`, `uint64_t`,
    and `size_t` without compilation failing
  * The precision of floating point stringification can be
    modified by user (#1612, #1614)
  * We now provide `REGISTER_ENUM` convenience macro for
    generating `StringMaker` specializations for enums
    + See the "String conversion" documentation for details
  * Added new set of macros for template test cases that enables
    the use of NTTPs (#1531, #1609)
    + See "Test cases and sections" documentation for details
  Fixes:
  * `UNSCOPED_INFO` macro now has a
    prefixed/disabled/prefixed+disabled versions (#1611)
  * Reporting errors at startup should no longer cause a
    segfault under certain circumstances (#1626)
  Miscellaneous:
  * CMake will now prevent you from attempting in-tree build
    (#1636, #1638)
    + Previously it would break with an obscure error message
    during the build step
- Drop _service file
* Sat May 18 2019 Kira Marie Backes <kira@kiralein.de> - 2.7.2
- Finalize .spec of Catch2 v 2.7.2
* Sat May 18 2019 Kira Marie Backes <kira@kiralein.de>
- Try to setup Catch2 as OBS project
