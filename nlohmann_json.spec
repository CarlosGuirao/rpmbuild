Name: nlohmann_json
%define myname json
Version: 3.10.4
Release: 1%{?dist}
Summary: JSON library for jaeger client

Group: Development/Libraries
License: MIT License
Vendor: Niels Lohman
Packager: ESO <eltmgr@eso.org>
URL: https://json.org

Source: %{myname}-%{version}.tar.gz 

BuildRequires: gcc
BuildRequires: make
BuildRequires: cmake


%define __os_install_post %{nil}
# Disable debug package creation otherwise this fails in "mock" on Fedora.
%define _prefix /usr/local

%global debug_package %{nil}

%description
JSON (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write. It is easy for machines to parse and generate. It is based on a subset of the JavaScript Programming Language Standard ECMA-262 3rd Edition - December 1999. JSON is a text format that is completely language independent but uses conventions that are familiar to programmers of the C-family of languages, including C, C++, C#, Java, JavaScript, Perl, Python, and many others. These properties make JSON an ideal data-interchange language.

%prep
%setup -n %{myname}-%{version}

%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix}
%cmake_build

%install
%cmake_install

%files
%{_prefix}/include/nlohmann
%{_prefix}/lib64/cmake/nlohmann_json/
%{_prefix}/lib64/pkgconfig/nlohmann_json.pc

%clean
rm -fr $RPM_BUILD_ROOT

%changelog
* Tue Dec 28 2021 DevEnv 4.1 opt JSON jaeger-client-cpp
- First version on Fedora-34
