Name:     open62541
Version:  1.3.3
Release:  1%{?dist}
Summary:  OPC UA implementation
License:  MPLv2.0
URL:      http://open62541.org
Source0:  https://github.com/open62541/open62541/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: cmake3
BuildRequires: make
%if 0%{?rhel} != 7
BuildRequires: python3
BuildRequires: python3dist(six)
BuildRequires: python3dist(sphinx)
BuildRequires: python3dist(sphinx-rtd-theme)
%else
BuildRequires: python
BuildRequires: python-six
BuildRequires: python-sphinx
BuildRequires: python-sphinx_rtd_theme
%endif
BuildRequires: graphviz

%description
open62541 is a C-based library (linking with C++ projects is possible)
with all necessary tools to implement dedicated OPC UA clients and servers,
or to integrate OPC UA-based communication into existing applications.

%package  devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package   doc
Summary:   Documentation for %{name}
BuildArch: noarch

%description doc
The %{name}-doc package contains documentation for %{name}.

%prep
%autosetup -n %{name}-%{version}

%build
mkdir -p build
cd build
# The version is usually extracted from the git tag, which is not available in the tarball.
# Therefore we need to set it manually.
%cmake3 \
  -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
%if 0%{?rhel} != 7
  -DCMAKE_C_FLAGS="-Wno-error=cast-function-type -Wno-stringop-overflow"\
%endif
  -DOPEN62541_VERSION=v%{version} \
  -DUA_ENABLE_AMALGAMATION=ON ..

%cmake_build
cd %{__cmake_builddir}
%make_build doc

%install
mkdir stage-docs
cd build
%cmake_install
# Remove build files not belonging to docs
rm -rf doc/CMakeFiles doc/Makefile doc/*.cmake
# stage docs
cp -av %{__cmake_builddir}/doc/* ../stage-docs/

cd -
# Remove this from the examples installation
rm examples/CMakeLists.txt
rm -Rf %{buildroot}/usr/share/open62541/tools
# fix permission
chmod 0644 examples/nodeset/Opc.Ua.POWERLINK.NodeSet2.bsd

%ldconfig_scriptlets
%files
%license LICENSE
%doc AUTHORS README.md
%{_libdir}/libopen62541.so.1*

%files devel
%license LICENSE LICENSE-CC0
%doc FEATURES.md
%{_libdir}/libopen62541.so

%{_libdir}/pkgconfig/open62541.pc
%{_includedir}/open62541.h
%{_libdir}/cmake/open62541*

%files doc
%doc stage-docs/*
%doc examples/

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 10 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.5-1
- Update to 1.2.5

* Sun Feb 20 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.4-1
- Update to 1.2.4

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 15 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2 release

* Thu Jan 28 2021 Jens Reimann <jreimann@redhat.com> - 1.1.5-1
- Update to 1.1.5 release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Jens Reimann <jreimann@redhat.com> - 1.1.2-1
- Update to 1.1.2 release

* Tue Jun 02 2020 Charalampos Stratakis <cstratak@redhat.com> - 1.0.1-2
- Fix macro typo

* Wed Feb  5 2020 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.1-1
- Update to 1.0.1 release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 06 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.0-2
- Add doc subpackage

* Sun Oct 06 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.0-1
- Update to 1.0 release
- Explicitly set BuildType to RelWithDebInfo

* Sun Aug  4 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.1-1
- Update to 0.3.1 release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 13 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-4
- Use python3 on Fedora again

* Tue Feb 12 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.0-3
- Package fixes for el7

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 20 2018 Till Hofmann <thofmann@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0 release

* Wed Aug 22 2018 Jens Reimann <jreimann@redhat.com> - 0.3-0.4.rc2
- Upgraded to 0.3.rc2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.3.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Jens Reimann <jreimann@redhat.com> - 0.3-0.2.rc1
- Upgraded to 0.3.rc1, switch to cmake3

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 Jens Reimann <jreimann@redhat.com> - 0.2-1
- Initial version of the package

