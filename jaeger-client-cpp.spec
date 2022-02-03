Name: jaeger-client-cpp
Version: 0.8.0
Release: 1%{?dist}
Summary: Opentracing API for C++

Group: Development/Libraries
License: ASL 2.0
Vendor: Uber Technologies
Packager: ESO <eltmgr@eso.org>
URL: https://www.jaegertracing.io

Source0: %{name}-%{version}.tar.gz 
Source1: %{name}-thrift-stdcxx.h
Patch: %{name}-%{version}-CMakelists.txt.patch

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: cmake
BuildRequires: boost-devel 
BuildRequires: thrift-devel >= 0.14.0
BuildRequires: opentracing-cpp >= 1.6.0
BuildRequires: nlohmann_json >= 3.10.4

Requires: boost-devel 
Requires: thrift >= 0.14.0
Requires: opentracing-cpp >= 1.6.0
Requires: nlohmann_json >= 3.10.4

%define __os_install_post %{nil}
# Disable debug package creation otherwise this fails in "mock" on Fedora.
%define _prefix /usr
%define _flags "%{_prefix}/json; %{_prefix}/opentracing-cpp"

%global debug_package %{nil}

%description
Jaeger, inspired by Dapper and OpenZipkin, is a distributed tracing system released as open source by Uber Technologies. It is used for monitoring and troubleshooting microservices-based distributed systems, including:

    Distributed context propagation
    Distributed transaction monitoring
    Root cause analysis
    Service dependency analysis
    Performance / latency optimization

%prep
%setup -n %{name}-%{version}
%patch -p0

%build
mkdir src/thrift
cp %{SOURCE1} src/thrift/stdcxx.h
#export nlohmann_json_DIR=%{_prefix}/json
#%cmake -DHUNTER_ENABLED=OFF -DBUILD_SHARED_LIBS=ON -DCMAKE_PREFIX_PATH=%{_prefix}/opentracing-cpp/cmake -DBUILD_TESTING=OFF -DCMAKE_INSTALL_PREFIX=%{_prefix}/%{name} .
%cmake -DHUNTER_ENABLED=OFF -DBUILD_SHARED_LIBS=ON -DBUILD_TESTING=OFF -DCMAKE_INSTALL_PREFIX=%{_prefix} .
%cmake_build


%install
%cmake_install
cd %{buildroot}
mkdir -p usr/lib64/pkgconfig ; cd usr/lib64/pkgconfig
cat << EOF >opentracing_api.pc
prefix=%{_prefix}

prefix_opentracingapi=\${prefix}
libdir_opentracingapi=\${prefix_opentracingapi}/lib64
includedir_opentracingapi=\${prefix_opentracingapi}/include

Name: opentracing_api
Description: Open tracing - API 
Version: 
Libs: -L\${libdir_opentracingapi} -lopentracing 
Cflags: -I\${includedir_opentracingapi}
EOF
cat << EOF >opentracing_jaeger.pc
prefix=%{_prefix}

prefix_jaeger_client=\${prefix}

libdir_jaeger_client=\${prefix_jaeger_client}/lib64

includedir_jaeger_client=\${prefix_jaeger_client}/include

Name: opentracing 
Description: Open tracing - Jaeger 
Version: 
Libs: -L\${libdir_jaeger_client} -ljaegertracing -lthrift -lyaml-cpp
Cflags: -I\${includedir_jaeger_client} 
EOF
cat << EOF >opentracing_mocktracer.pc
prefix=%{_prefix}

prefix_opentracingapi=\${prefix}
libdir_opentracingapi=\${prefix_opentracingapi}/lib64
includedir_opentracingapi=\${prefix_opentracingapi}/include

Name: opentracing mock tracer 
Description: Open tracing - mock tracer
Version: 
Libs: -L\${libdir_opentracingapi} -lopentracing_mocktracer
Cflags: -I\${includedir_opentracingapi}
EOF

%files
%{_prefix}/include/jaegertracing
%{_prefix}/lib64/libjaegertracing*
%{_prefix}/lib64/cmake/jaegertracing
%{_prefix}/lib64/pkgconfig/opentracing_api.pc
%{_prefix}/lib64/pkgconfig/opentracing_jaeger.pc
%{_prefix}/lib64/pkgconfig/opentracing_mocktracer.pc

%clean
rm -fr $RPM_BUILD_ROOT

%changelog
* Tue Dec 28 2021 DevEnv 4.1 opt opentracing-cpp for jaeger-client-cpp
- First version on Fedora-34
