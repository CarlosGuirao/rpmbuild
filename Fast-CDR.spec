%global project Fast-CDR
%global soversion 1

Name: Fast-CDR
Version: 1.0.23
Release: 1%{?dist}
Summary: Fast Common Data Representation (CDR) Serialization Library

Group: Development/Libraries
License: ASL 2.0
Vendor: eProsima
Packager: ESO <eltmgr@eso.org>
URL: https://www.eprosima.com/

Source: https://github.com/eProsima/Fast-CDR/archive/refs/tags/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: make

# %define __os_install_post %{nil}
%define _prefix  /usr/local
# Disable debug package creation otherwise this fails in "mock" on Fedora.
# %global debug_package %{nil}

%description
eProsima FastCDR is a C++ library that provides two serialization mechanisms.
One is the standard CDR serialization mechanism, while the other is a faster
implementation that modifies the standard.

%package devel
Summary:    Development files and libraries for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files and libraries for %{name}

%prep
%setup 

%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} .
%cmake_build

%install
%cmake_install

%files
%license %{_prefix}/share/fastcdr/LICENSE
%{_prefix}/lib64/*.so.%{version}
%{_prefix}/lib64/*.so.%{soversion}
%{_prefix}/lib64/cmake/fastcdr

%files devel
%{_prefix}/lib64/*.so
%{_prefix}/include/fastcdr
%{_prefix}/lib64/cmake/fastcdr


# %clean
# rm -fr $RPM_BUILD_ROOT

%changelog
* Tue Dec 28 2021 DevEnv 4.1 eProsima Fast-CDR 1.0.23
- First version on Fedora-34
