# Note: Uninstall any previous installation of this RPM before building it again:
#   rpm -e  eprosima-foonathan_memory_vendor --nodeps
# otherwise error in the build step
Name: foonathan_memory
Version: 0.7
Release: 1%{?dist}
Summary: STL compatible C++ memory allocator library
License: Freely redistributable without restriction
URL: https://github.com/foonathan/memory

Source0: https://github.com/foonathan/memory/archive/refs/tags/memory-%{version}-1.tar.gz
BuildRequires: gcc-c++
BuildRequires: cmake

%define __os_install_post %{nil}
%define _prefix  /usr/local
# Disable debug package creation otherwise this fails in "mock" on Fedora.
%global debug_package %{nil}

%description
STL compatible C++ memory allocator library

%prep
%setup -n memory-0.7-1

%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DBUILD_SHARED_LIBS=OFF . 
%cmake_build 

%install
%cmake_install 

%files
%{_prefix}/bin/nodesize_dbg
%{_prefix}/include/foonathan_memory
%{_prefix}/include/doctest
%{_prefix}/lib64/cmake/doctest
%{_prefix}/lib64/foonathan_memory
%{_prefix}/lib64/libfoonathan_memory-0.7.1.a
%{_prefix}/share/foonathan_memory

%doc %{_prefix}/share/foonathan_memory/README.md
%license %{_prefix}/share/foonathan_memory/LICENSE


%clean
rm -fr $RPM_BUILD_ROOT

%changelog
* Tue Dec 28 2021 DevEnv 4.1 foonathan_memory 0.7-1
- First version on Fedora-34
