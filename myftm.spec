%global debug_package %{nil}

Name:           myftm
Version:        1.0.0
Release:        3%{?dist}
Summary:        Qualcomm WLAN myftm factory test utility

License:        Qualcomm-Technologies-Inc.-Proprietary
Source0:        https://qartifactory-edge.qualcomm.com/artifactory/qsc_releases/software/chip/component/wlan-service.qclinux.0.0/260825/prebuilt_resolute/ath6kl-utils_%{version}_arm64.tar.gz

ExclusiveArch:  aarch64

%description
myftm is packaged from a Qualcomm Linux release tarball.

%prep
%autosetup -c -n %{name}-%{version}

%build
# Prebuilt payload package: nothing to compile.

%install
mkdir -p %{buildroot}
cp -a data/ath6kl-utils/arm64/. %{buildroot}/
find %{buildroot} \( -type f -o -type l \) -printf '/%%P\n' | sort > %{name}.files

%files -f %{name}.files

%changelog
* Fri Aug 21 2026 Yu Zhang <yu.zhang@oss.qualcomm.com> - 1.0.0-1
- Initial prebuilt RPM packaging
