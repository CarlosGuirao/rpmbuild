Name: opentracing-cpp
Version: 1.6.0
Release: 1%{?dist}
Summary: Opentracing API for C++

Group: Development/Libraries
License: Apache License Ver.2.0
Vendor: Opentracing developers
Packager: ESO <eltmgr@eso.org>
URL: https://github.com/opentracing

Source: %{name}-%{version}.tar.gz 

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: cmake

%define __os_install_post %{nil}
# Disable debug package creation otherwise this fails in "mock" on Fedora.
%define _prefix /usr

%global debug_package %{nil}

%description

%prep
%setup -n %{name}-%{version}

%build
%cmake -DCMAKE_CXX_FLAGS=-fPIC -DBUILD_SHARED_LIBS=ON -DLIB_INSTALL_DIR=%{_prefix}/lib64 -DCMAKE_INSTALL_PREFIX=%{_prefix} .
%cmake_build

%install
%cmake_install

%files
%{_prefix}/lib64/cmake/OpenTracing
%{_prefix}/include/opentracing
%{_prefix}/lib64/libopentracing*
%{_prefix}/lib64/libopentracing_mocktracer*

%clean
rm -fr $RPM_BUILD_ROOT

%changelog
* Tue Dec 28 2021 DevEnv 4.1 opentracing-cpp for jaeger-client-cpp
- First version on Fedora-34
