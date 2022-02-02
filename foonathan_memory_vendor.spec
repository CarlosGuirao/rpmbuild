Name: foonathan_memory_vendor
Version: 1.2.0
Release: 1%{?dist}
Summary: eProsima interface to foonathan_memory library

Group: Development/Libraries
License: ASL 2.0
Packager: ESO <eltmgr@eso.org>
URL: https://www.eprosima.com/

Source0: https://github.com/eProsima/foonothan_memory_vendor/archive/refs/tags/%{name}-%{version}.tar.gz
# BuildArch: noarch
BuildRequires: git
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: make

%define _prefix  /usr/local

%description
This package will download, patch, build and install foonathan_memory for its use with Fast-RTPS.

%prep
%setup 

%build
%cmake -DCMAKE_PREFIX_PATH=%{_prefix} -DCMAKE_INSTALL_PREFIX=%{_prefix} .
%cmake_build

%install
%cmake_install

%files
%{_prefix}/share/foonathan_memory_vendor
%{_prefix}/bin/nodesize_dbg
%{_prefix}/include/foonathan_memory
%{_prefix}/lib64/foonathan_memory
%{_prefix}/lib64/libfoonathan_memory-0.7.1.a
%{_prefix}/share/foonathan_memory

%clean
rm -fr $RPM_BUILD_ROOT

%changelog
* Tue Dec 28 2021 DevEnv 4.1 eprosima foonathan_memory_vendor 1.2.0
- First version on Fedora-34
