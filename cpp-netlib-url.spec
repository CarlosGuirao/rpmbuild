%global project url
%global debug_package %{nil}

Name: cpp-netlib-url
Version: 1.13.0
Release: 1%{?dist}
Summary: WhatWG URL Library

Group: Development/Libraries
License: Boost Software License 1.0
Packager: ESO <eltmgr@eso.org>
URL: https://github.com/cpp-netlib/url

Source0: https://github.com/cpp-unit/url/archive/refs/tags/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: make
BuildRequires: nlohmann_json
BuildRequires: expected-devel
BuildRequires: Catch2-devel
BuildRequires: ninja-build
BuildRequires: range-v3-devel
BuildRequires: fmt-devel

Requires: nlohmann_json
Requires: expected-devel
Requires: Catch2-devel
Requires: ninja-build
Requires: range-v3-devel
Requires: fmt-devel

%define _prefix  /usr/local

%description
A C++ library that implements the WhatWG URL specification 

%prep
%setup -n %{project}-%version 

%build
%cmake -G "Ninja"
%cmake_build

%install
%cmake_install

%check
%cmake_build --target test

%files
%license LICENSE_1_0.txt
%{_prefix}/include/skyr
%{_prefix}/lib/libskyr-url.a
%{_prefix}/share/cmake/skyr-url

%changelog
* Tue Feb 10 2022 DevEnv 4.2 cpp-netlib url
- First version on Fedora-34
