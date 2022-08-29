%global project uri
%global debug_package %{nil}

Name: cpp-netlib-uri
Version: 1.1.0
Release: 3%{?dist}
Summary: WhatWG URL Library

Group: Development/Libraries
License: Boost Software License 1.0
Packager: ESO <eltmgr@eso.org>
URL: https://github.com/cpp-netlib/uri

Source0: https://github.com/cpp-netlib/uri/archive/refs/tags/v%{version}.tar.gz#/%{project}-%{version}.tar.gz
Source1: cpp-netlib-uri.pc

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: make
BuildRequires: boost-devel

Requires: boost

%description
A deprecated, unmaintained library. Don't use it.

A URI builder to build consistent URIs from parts, including case, percent encoding and path normalization

%prep
%setup -n %{project}-%{version} 
rm -rf src/boost

%build
CXXFLAGS="-fPIC -DNETWORK_URI_EXTERNAL_BOOST"
%cmake -DUri_BUILD_TESTS=OFF -DUri_BUILD_DOCS=OFF 
%cmake_build

%install
%cmake_install
cd %{buildroot}
mv usr/lib usr/lib64
mkdir usr/lib64/pkgconfig
cp %{SOURCE1} usr/lib64/pkgconfig

%check
%ctest

%files
%doc README.rst
%license LICENSE_1_0.txt
%{_includedir}/network
%{_libdir}/libnetwork-uri.so
%{_libdir}/pkgconfig/cpp-netlib-uri.pc

%changelog
* Mon Aug 29 2022 DevEnv 4.1.0 cpp-netlib-uri
- First version on Fedora-34
