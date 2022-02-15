%global debug_package %{nil}

Name: redis-plus-plus
Version: 1.3.3
Release: 1%{?dist}
Summary: C++ client library for Redis

Group: Development/Libraries
License: ASL 2.0
Vendor: Travis CI
Packager: ESO <eltmgr@eso.org>

URL: https://docs.travis-ci.com/ 
SOURCE0: https://github.com/sewenew/redis-plus-plus/tags/%{version}#/%{name}-%{version}.tar.gz
patch0:  redis++.CMakeList.txt.patch
patch1:  redis++.pc.in.patch

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: hiredis-devel
Requires: hiredis-devel

%description
This is a C++ client library for Redis. It's based on [hiredis](https://github.com/redis/hiredis), and is compatible with C++ 17, C++ 14, and C++ 11.

%prep
%setup
%patch0 -p1 
%patch1 -p1

%package devel
Summary: C++ client library for Redis
%description devel
This is a C++ client library for Redis. It's based on [hiredis](https://github.com/redis/hiredis), and is compatible with C++ 17, C++ 14, and C++ 11.

%build
%cmake -DREDIS_PLUS_PLUS_CXX_STANDARD=11 -DCMAKE_INSTALL_PREFIX=/usr 
%cmake_build

%install
%cmake_install

%files devel
%{_includedir}/sw/redis++
%{_libdir}/libredis++*
%{_libdir}/pkgconfig/redis++.pc
%{_datadir}/cmake/redis++*
%license LICENSE

%changelog
* Tue Feb 15 2022 DevEnv 4.1 redis-plus-plus
- First version on Fedora-34
