%global debug_package %{nil}

Name:           myftm
Version:        1.0.0
Release:        1%{?dist}
Summary:        Command-line factory test utility for Qualcomm WLAN devices

License:        Qualcomm.nologin.binaries.license
Source0:        https://qartifactory-edge.qualcomm.com/artifactory/qsc_releases/software/chip/component/wlan-service.qclinux.0.0/260825/prebuilt_resolute/ath6kl-utils_%{version}_arm64.tar.gz

ExclusiveArch:  aarch64

%description
myftm is a command-line utility for exercising Qualcomm WLAN devices in
Factory Test Mode (FTM). It provides a local interface for running WLAN
factory tests. The package also provides test command libraries and
development headers.

%prep
%autosetup -c -n %{name}-%{version}

%build
# Prebuilt payload package: nothing to compile.

%install
mkdir -p %{buildroot}
cp -a data/ath6kl-utils/arm64/. %{buildroot}/
# Install license documents separately with %license.
rm -f %{buildroot}%{_docdir}/ath6kl-utils/copyright
find %{buildroot} \( -type f -o -type l \) -printf '/%%P\n' | sort > %{name}.files

%files -f %{name}.files
%license data/ath6kl-utils/arm64/usr/share/doc/ath6kl-utils/copyright
%license data/LICENSE.qcom-2
%license data/NOTICE

%changelog
* Fri Aug 21 2026 Yu Zhang <yu.zhang@oss.qualcomm.com> - 1.0.0-1
- Initial prebuilt RPM packaging
