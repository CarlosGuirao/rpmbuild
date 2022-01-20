Name: eprosima-Fast-DDS
Version: 2.5.0
Release: 1%{?dist}
Summary: eProsima Fast-DDS library

Group: Development/Libraries
License: Apache License Ver.2.0
Vendor: eProsima
Packager: ESO <eltmgr@eso.org>
URL: https://www.eprosima.com/

Source: https://github.com/eProsima/Fast-DDS/archive/refs/tags/v%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: tinyxml2-devel >= 7.0.1
BuildRequires: asio-devel >= 1.16.1
BuildRequires: eprosima-foonathan_memory_vendor >= 1.2.0
BuildRequires: eprosima-Fast-CDR >= 1.0.23

Requires: eprosima-foonathan_memory_vendor >= 1.2.0
Requires: eprosima-Fast-CDR >= 1.0.23

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
%setup -n Fast-DDS-%{version}

%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_PREFIX_PATH=/usr/local -DSTRICT_REALTIME=ON -DFASTDDS_STATISTICS=ON .
%cmake_build

%install
%cmake_install
cd %{buildroot}/%{_prefix}/lib64
ln -s libfastrtps.so.2.5.0 libfastrtps.so.2

cd %{buildroot}
mkdir -p %{buildroot}\%{_prefix}/share/fastrtps/
cat << EOF >%{buildroot}\%{_prefix}/share/fastrtps/fastdds.lua
local fastddshome = "%{_prefix}"
append_path( "PATH", pathJoin(fastddshome,"/bin"))
append_path( "LD_LIBRARY_PATH",pathJoin(fastddshome,"/lib"))
EOF

cd %{buildroot}
mkdir -p %{buildroot}\%{_prefix}/lib64/pkgconfig/
cat << EOF >%{buildroot}\%{_prefix}/lib64/pkgconfig/fast_dds.pc
prefix=%{_prefix}

exec_prefix=\${prefix}
libdir=\${prefix}/lib64

Name: fast_dds
Description: Fast DDS
Version: 2.5.0

Cflags: -I\${prefix}/include -DUSE_FASTDDS 
Libs: -L\${libdir} -lfastrtps  -lfastcdr
EOF

%files
%{_prefix}/bin/fastdds*
%{_prefix}/bin/fast-discovery-server*
%{_prefix}/bin/ros-discovery
%{_prefix}/include/fastdds
%{_prefix}/include/fastrtps
%{_prefix}/share/fastrtps
%{_prefix}/tools/fastdds
%{_prefix}/lib64/libfast*
%{_prefix}/lib64/pkgconfig/fast_dds.pc

%clean
rm -fr $RPM_BUILD_ROOT

%changelog
* Tue Dec 28 2021 DevEnv 4.1 opt-eprosima
- First version on Fedora-34
