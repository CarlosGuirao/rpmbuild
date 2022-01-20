# Note: Uninstall any previous installation of this RPM before building it again:
#   rpm -e  eprosima-foonathan_memory_vendor --nodeps
# otherwise error in the build step
Name: eprosima-foonathan_memory_vendor
Version: 1.2.0
Release: 1%{?dist}
Summary: eProsima foonathan_memory_vendor library

Group: Development/Libraries
License: Apache License Ver.2.0
Vendor: eProsima
Packager: ESO <eltmgr@eso.org>
URL: https://www.eprosima.com/

Source: https://github.com/eProsima/foonothan_memory_vendor/archive/refs/tags/v%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: git

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
%setup -n foonathan_memory_vendor-%{version}

%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DBUILD_SHARED_LIBS=ON .
%cmake_build

%install
%cmake_install

%files
%{_prefix}/include/foonathan_memory
%{_prefix}/lib64/foonathan_memory
%{_prefix}/lib64/libfoonathan_memory-0.7.1.a
%{_prefix}/share/foonathan_memory_vendor
%{_prefix}/share/foonathan_memory
%{_prefix}/bin/nodesize_dbg

%doc %{_prefix}/share/foonathan_memory/LICENSE
%doc %{_prefix}/share/foonathan_memory/README.md



%clean
rm -fr $RPM_BUILD_ROOT

%changelog
* Tue Dec 28 2021 DevEnv 4.1 eprosima foonathan_memory_vendor 1.2.0
- First version on Fedora-34
