Name: Fast-DDS-Monitor
Version: 1.1.0
Release: 1%{?dist}
Summary: eProsima Fast DDS Monitor App

Group: Development/Libraries
License: ASL 2.0
Vendor: eProsima
Packager: ESO <eltmgr@eso.org>
URL: https://www.eprosima.com/index.php/products-all/eprosima-fast-dds-monitor

Source: https://www.eprosima.com/index.php/component/ars/repository/eProsima_Fast-DDS-Monitor-%{version}-Linux.AppImage

%define _prefix  /usr/local

%description
eProsima Fast DDS Monitor is an open source graphical desktop application aimed to monitor DDS environments deployed using the eProsima Fast DDS library. Therefore, the user can track the status of publication/subscription communications between DDS entities in real-time, and also choose from a wide variety of communication parameters to be measured such as latency, throughput, packet loss and others. The Fast DDS Monitor can also record and compute statistical measurements on these parameters displaying mean, variance and standard deviation.

%prep

%build

%install
mkdir -p %{buildroot}/%{_prefix}/bin
cp %{SOURCE0} %{buildroot}/%{_prefix}/bin

cat << EOF >%{buildroot}/%{_prefix}/bin/fastddsMonitor
#!/bin/bash

QT_PLUGIN_PATH= LD_LIBRARY_PATH= %{_prefix}/bin/eProsima_Fast-DDS-Monitor-1.1.0-Linux.AppImage
EOF
chmod +x %{buildroot}/%{_prefix}/bin/fastddsMonitor

%files
%{_prefix}/bin/*

%changelog
* Tue Dec 28 2021 DevEnv 4.1 eProsima Fast-DDS-Monitor 1.1.0 
- First version on Fedora-34
