%global debug_package %{nil}

Name:     cli
Version:  2.0.0
Release:  1%{?dist}
Summary:  A cross-platofrm header only C++14 for interactive command line interfaces

Group:    Development/Libraries
License:  Boost Software License 1.0
Vendor:   Travis CI
Packager: ESO <eltmgr@eso.org>

URL:      https://github.com/daniele77/cli 
SOURCE0:  https://github.com/daniele77/cli/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: boost-devel
Requires:      boost-devel

%description
A cross-platform header only C++14 library for interactive command line interfaces (Cisco style)

%prep
%setup

%package devel
Summary:  A cross-platofrm header only C++14 for interactive command line interfaces

%description devel
A cross-platform header only C++14 library for interactive command line interfaces (Cisco style)

%build
%cmake
%cmake_build

%install
%cmake_install

%files devel
%{_includedir}/cli
%{_libdir}/cmake/cli
%{_datadir}/pkgconfig/cli.pc
%license LICENSE

%changelog
* Tue Feb 15 2022 DevEnv 4.1 cli 
- First version on Fedora-34
