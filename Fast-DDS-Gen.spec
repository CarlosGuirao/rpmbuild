Name: Fast-DDS-Gen
Version: 2.1.0
Release: 1%{?dist}
Summary: Fast-DDS Gen library

Group: Development/Libraries
License: ASL 2.0
Vendor: eProsima
Packager: ESO <eltmgr@eso.org>
URL: https://www.eprosima.com/

Source0: https://github.com/eProsima/Fast-DDS-Gen/archive/refs/tags/%{name}-%{version}.tar.gz
Source1: https://github.com/eProsima/IDL-Parser/archive/refs/tags/IDL-Parser-1.1.1.tar.gz

BuildRequires: java
BuildRequires: git

Requires: java

%define _prefix  /usr/local
# %define debug_package %{nil}

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
cd thirdparty ; tar xf %{SOURCE1}
rmdir idl-parser ; ln -s IDL-Parser-1.1.1 idl-parser
cd ..
./gradlew assemble

%install
./gradlew install --install_path %{buildroot}%{_prefix}

%files
%{_prefix}/bin/fastddsgen
%{_prefix}/share/fastddsgen

%changelog
* Tue Dec 28 2021 DevEnv 4.2 opt-eprosima 
- First version on Fedora-34
