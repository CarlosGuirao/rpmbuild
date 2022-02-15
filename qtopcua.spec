# git clone http://code.qt.io/qt/qtopcua.git
# cd qtopcua
# git checkout 5.15.2
# cd ..
# tar czf qtopcua-5.15.2.tar.gz ./qtopcua
# 
# "make docs" requires a change in the file
# qtopcua/src/opcua/opcua.pro
# INCLUDEPATH += /usr/lib/gcc/x86_64-redhat-linux/11/include

%global debug_package %{nil}

Name:           qtopcua
Version:        5.15.2
Release:        1%{?dist}
Summary:        The Qt OPC UA module implements a Qt API to interact with OPC UA on top of a 3rd party OPC UA stack.
License:        GNU Lesser General Public License, version 3
Vendor:         The Qt Company
Packager:       ESO <eltmgr@eso.org>
URL:            https://code.qt.io/cgit/qt/qtopcua.git/
Source0:        https://code.qt.io/cgit/qt/qtopcua.git/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         qtopcua-open62541.pri.patch
BuildRequires:  cmake 
BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtbase-gui
BuildRequires:  qt5-doctools
BuildRequires:  open62541-devel

Requires:       qt5-qtbase-devel
Requires:       qt5-qtbase-gui
Requires:       open62541-devel

%description
OPC UA is a protocol for data modelling and exchange of data in industrial applications.

An OPC UA server offers access to data that is organized in a mesh of nodes connected by references. The use of different reference types and nodes containing metadata enable a client to navigate and interpret the data without knowing their structure in advance.

Each node has a unique identifier and attributes that can be read and written. Among others, there are Variable nodes that store values and callable Method nodes with attached nodes describing parameters and return values. Notifications in case of events and monitoring of Variable nodes for value changes are offered too.

Complex objects can be created by combining nodes using references. Inheritance is also possible. OPC UA offers support for pre-made models that can be extended to fit special needs.

OPC UA is the platform-independent successor of OPC Classic intended for usage on all levels, from embedded sensors up to manufacturing execution and enterprise resource planning systems. It has a service-oriented architecture based on standardized messages for service requests and responses. There are different ways for these messages to be encoded and transported over the network. The most common way is binary encoding over TCP.

%prep
%setup -n %{name}
%patch -p1

%build
qmake-qt5 .
make 

%install
cd %{_builddir}/%{name}
tar cf - ./LICENSE.LGPLv3 ./include/QtOpcUa ./lib ./examples/opcua ./plugins/opcua/libopen62541_backend.so | (cd  %{buildroot}; tar xf -)
cd %{buildroot}
mkdir usr
mv lib usr/lib64
mkdir usr/lib64/qt5
mv plugins usr/lib64/qt5
mv include usr
mv examples usr/lib64/qt5
mkdir -p usr/share/licenses/qtopcua
mv LICENSE.LGPLv3 usr/share/licenses/qtopcua

%files
%license LICENSE.LGPLv3
%{_includedir}/QtOpcUa
%{_libdir}/cmake/Qt5OpcUa
%{_libdir}/libQt5OpcUa*
%{_libdir}/qt5/plugins/opcua
%{_libdir}/qt5/examples
%{_libdir}/pkgconfig/Qt5OpcUa.pc

%changelog
* Tue Dec 28 2021 DevEnv 4.1 opt-eprosima
- First version on Fedora-34
