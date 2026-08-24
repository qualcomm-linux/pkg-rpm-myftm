%global debug_package %{nil}

Name:           myftm
Version:        1.0.0
Release:        2%{?dist}
Summary:        Qualcomm WLAN myftm factory test utility

License:        Qualcomm-Technologies-Inc.-Proprietary
Source0:        %{name}-prebuilt-%{version}.tar.gz

ExclusiveArch:  aarch64

%description
myftm is packaged from a prebuilt payload tarball for Qualcomm Linux platforms.

%prep
%autosetup -n %{name}-prebuilt-%{version}

%build
# Prebuilt payload package: nothing to compile.

%install
mkdir -p %{buildroot}
cp -a . %{buildroot}/
find %{buildroot} \( -type f -o -type l \) -printf '/%%P\n' | sort > %{name}.files

%files -f %{name}.files

%changelog
* Mon Aug 24 2026 Yu Zhang <yu.zhang@oss.qualcomm.com> - 1.0.0-2
- Rebuild prebuilt payload from source package with vendored diag build inputs

* Fri Aug 21 2026 Yu Zhang <yu.zhang@oss.qualcomm.com> - 1.0.0-1
- Initial prebuilt RPM packaging
