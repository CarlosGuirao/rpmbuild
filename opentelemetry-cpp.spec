%global debug_package %{nil}

Name:           opentelemetry-cpp
Version:        1.6.0
Release:        1%{?dist}
Summary:        The C++ OpenTelemetry client
License:        ASL 2.0
URL:            https://github.com/open-telemetry/opentelemetry-cpp
Source:         https://github.com/open-telemetry/opentelemetry-cpp/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake 
BuildRequires:  gcc-c++

%description
The OpenTelemetry C++ provides a mechanism to instrument, generate, collect, and export telemetry data (metrics, logs, and traces) to help you analyze your software’s performance and behavior.

%prep
%autosetup

%package devel
Summary:        Open

%description devel
The OpenTelemetry C++ API and SDK provided as a header-only and shared libraries

%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
  -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install

%check
ctest

# %cmake_build --target test

%files devel
%license LICENSE
%doc README.md
%{_libdir}/*.so
%{_libdir}/cmake
%{_includedir}/opentelemetry

%changelog
* Mon Aug 29 2022 opentelemetry implementation
- First version on Fedora-34
