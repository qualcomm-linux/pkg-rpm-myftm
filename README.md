<!--
Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.
SPDX-License-Identifier: BSD-3-Clause
-->
# myftm RPM - CentOS Stream 10

This branch contains the CentOS Stream 10 RPM packaging for myftm from a Qualcomm Linux release tarball.

## Package

| Field | Value |
|---|---|
| Package | myftm |
| Version | 1.0.0 |
| Source | ath6kl-utils_1.0.0_arm64.tar.gz |
| Source checksum | See sources |

The prebuilt payload installs:

- /usr/bin/myftm
- /usr/include/ath6kl-utils/*
- /usr/lib/aarch64-linux-gnu/libtcmd.a
- /usr/lib/aarch64-linux-gnu/libtestcmd6174.a
- /usr/lib/aarch64-linux-gnu/libtlv2.a
- /usr/lib/aarch64-linux-gnu/libtlvutil.a
- /usr/lib/aarch64-linux-gnu/pkgconfig/ath6kl-utils.pc

## Files

- myftm.spec
- sources
- .github/workflows/build-on-pr.yml
- .github/workflows/pkg-release.yml

Do not commit source tarballs or built RPMs. The source tarball is resolved from the dist-git `sources` file and the spec `Source0` URL.

## Build

Local validation can be run with qcom-rpm-utils:

    /path/to/qcom-rpm-utils/scripts/build-rpm.sh \
      --tarball /path/to/ath6kl-utils_1.0.0_arm64.tar.gz \
      --spec myftm.spec \
      --output /path/to/output

For CI, open a PR against this c10s branch. The build-on-pr workflow builds RPM artifacts but does not publish them.

## Release

After the PR is merged, run Actions -> Release on the c10s branch. The release workflow publishes the generated RPMs to Artifactory after approval.
