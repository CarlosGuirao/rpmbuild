# NOTE:  The RPM generated by this SPEC file is not necessary for Fast-DDS. 
#        Fast-CDR is included in Fast-DDS RPM as its build uses the opcion -DTHIRDPARTY=FORCE
Name: eprosima-Fast-CDR
Version: 1.0.23
Release: 1%{?dist}
Summary: eProsima Fast-CDR library

Group: Development/Libraries
License: Apache License Ver.2.0
Vendor: eProsima
Packager: ESO <eltmgr@eso.org>
URL: https://www.eprosima.com/

Source: https://github.com/eProsima/Fast-CDR/archive/refs/tags/v%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: cmake

%define __os_install_post %{nil}
%define _prefix  /usr/local
# Disable debug package creation otherwise this fails in "mock" on Fedora.
%global debug_package %{nil}

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
%setup -n Fast-CDR-%{version}

%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} .
%cmake_build

%install
%cmake_install

%files
%{_prefix}/include/fastcdr
%{_prefix}/lib64/libfastcdr.*
%{_prefix}/lib64/cmake/fastcdr
%doc %{_prefix}/share/fastcdr/LICENSE


%clean
rm -fr $RPM_BUILD_ROOT

%changelog
* Tue Dec 28 2021 DevEnv 4.1 eProsima Fast-CDR 1.0.23
- First version on Fedora-34
