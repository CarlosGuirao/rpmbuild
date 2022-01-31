Name: foonathan_memory_vendor
Version: 1.2.0
Release: 1%{?dist}
Summary: eProsima interface to foonathan_memory library

Group: Development/Libraries
License: Apache license
Packager: ESO <eltmgr@eso.org>
URL: https://www.eprosima.com/

Source0: https://github.com/eProsima/foonothan_memory_vendor/archive/refs/tags/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: foonathan_memory >= 0.7-1
Requires: foonathan_memory >= 0.7-1

%define __os_install_post %{nil}
%define _prefix  /usr/local
# Disable debug package creation otherwise this fails in "mock" on Fedora.
%global debug_package %{nil}

%description

%prep
%setup 

%build
%cmake -DCMAKE_PREFIX_PATH=%{_prefix} -DCMAKE_INSTALL_PREFIX=%{_prefix} .
%cmake_build

%install
%cmake_install

%files
%{_prefix}/share/foonathan_memory_vendor


%clean
rm -fr $RPM_BUILD_ROOT

%changelog
* Tue Dec 28 2021 DevEnv 4.1 eprosima foonathan_memory_vendor 1.2.0
- First version on Fedora-34
