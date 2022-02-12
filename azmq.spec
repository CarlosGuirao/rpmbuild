%global debug_package %{nil}

Name:           azmq
Version:        1.0.3
Release:        1%{?dist}
Summary:        The azmq library provides Boost Asio style bindings for ZeroMQ
License:        BSL-1.0
URL:            https://github.com/zeromq/azmq
Source:         https://github.com/zeromq/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake 
BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  zeromq-devel

Requires:  boost-devel
Requires:  zeromq-devel

%description
This library is built on top of ZeroMQ's standard C interface and is intended to work well with C++ applications which use the Boost libraries in general, and Asio in particular.

%prep
%autosetup

%package devel
Summary:        The azmq library provides Boost Asio style bindings for ZeroMQ

%description devel
This library is built on top of ZeroMQ's standard C interface and is intended to work well with C++ applications which use the Boost libraries in general, and Asio in particular.

The main abstraction exposed by the library is azmq::socket which provides an Asio style socket interface to the underlying zeromq socket and interfaces with Asio's io_service(). The socket implementation participates in the io_service's reactor for asynchronous IO and may be freely mixed with other Asio socket types (raw TCP/UDP/Serial/etc.).

%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix}  .
%cmake_build

%install
%cmake_install

%check
%ctest

# %cmake_build --target test

%files devel
%license LICENSE-BOOST_1_0
%{_includedir}/azmq

%changelog
* Tue Feb 08 2022 DevEnv 1.0.3 azmq-devel
- First version on Fedora-34
