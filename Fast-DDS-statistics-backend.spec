%global project Fast-DDS-statistics-backend
%global soversion 1

Name: Fast-DDS-statistics-backend
Version: 0.4.0
Release: 1%{?dist}
Summary: eProsima Fast-DDS statistics backend library

Group: Development/Libraries
License: ASL 2.0
Vendor: eProsima
Packager: ESO <eltmgr@eso.org>
URL: https://www.eprosima.com/

Source: https://github.com/eProsima/Fast-DDS-statitics/archive/refs/tags/%{name}-%{version}.tar.gz

Source: %{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: make
BuildRequires: foonathan_memory_vendor >= 1.2.0
BuildRequires: Fast-CDR >= 1.0.23
BuildRequires: Fast-DDS >= 2.5.0

Requires: foonathan_memory_vendor >= 1.2.0
Requires: Fast-CDR >= 1.0.23
Requires: Fast-DDS >= 2.5.0

# %define __os_install_post %{nil}
%define _prefix  /usr/local
# Disable debug package creation otherwise this fails in "mock" on Fedora.
# %global debug_package %{nil}

%description
Fast DDS is a standalone Cpp middleware implementation providing both the 
OMG DDS 1.4 and the OMG RTPS 2.2 interoperable wire-protocol standards.

eProsima Fast DDS is striking fast, beating alternatives such as ZeroMQ 
and other DDS middleware solutions in both Windows and Linux.

The framework generates the Publish/Subscribe code from the topic definition 
using an Interface Definition Language (IDL) allowing the developer to focus 
on his application logic without bothering about the networking details.

eProsima Fast DDS is a free & open source software (Apache License 2.0) with 
a large variety of features and tools, and the option of commercial support.

%prep
%setup

%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_PREFIX_PATH=%{_prefix}
%cmake_build

%install
%cmake_install

%files
%{_prefix}/include/fastdds_statistics_backend
%{_prefix}/lib64/cmake/fastdds_statistics_backend
%{_prefix}/lib64/libfastdds_statistics_backend*
%license %{_prefix}/share/fastdds_statistics_backend/LICENSE

# %clean
# rm -fr $RPM_BUILD_ROOT

%changelog
* Tue Dec 28 2021 DevEnv 4.1 opt-eprosima
- First version on Fedora-34
