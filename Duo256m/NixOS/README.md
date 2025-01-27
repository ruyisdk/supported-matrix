---
sys: NixOS
sys_ver: null
sys_var: null

status: basic
last_update: 2025-01-27
---

# NixOS Milk-V Duo 256M Test Report

## Test Environment

### Operating System Information

- System version: 25.05.20250119
- Source code link: https://github.com/NickCao/nixos-riscv
- Reference Installation Document: https://github.com/NickCao/nixos-riscv/README.md

### Hardware Information

- Milk-V Duo 256M
- A USB-A Power Adapter
- A USB-A to C Cable
- A microSD Card
- A microSD Card Reader
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three DuPont Wires

## Installation Steps

### Compiling Image

Run `nix build ".#hydraJobs.duo-256"` if you happen to be using NixOS on your host.

It is not recommended to install and use the `nix` package manager on other distributions. Try using e.g. the official Docker image instead:
```shell
docker run -ti -v $(pwd):/work ghcr.io/nixos/nix
```

Inside the Docker container:

```shell
echo "max-jobs = auto" >> /etc/nix/nix.conf # Enable multi-threaded compilation
echo "substituters = https://mirrors.tuna.tsinghua.edu.cn/nix-channels/store https://cache.nixos.org/" >> /etc/nix/nix.conf # Switch to another mirror
cd /work
nix build ".#hydraJobs.duo-256" --extra-experimental-features nix-command --extra-experimental-features flakes
```

The resulting image will reside at `./result/sd-image/`, with a filename similar to `nixos-image-sd-card-25.05.20250119.00e0195-riscv64-linux.img.zst`。

### Flashing Image to microSD Card

Use `dd` to flash the image to the microSD card.

### Logging into the System

Logging into the system via the serial port.

No password are set and will automatically login by default.

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

```log
<<< Welcome to NixOS sd-card-25.05.20250119.00e0195 (riscv64) - ttyS0 >>>

Run 'nixos-help' for the NixOS manual.

nixos-duo login: root (automatic login)

[root@nixos-duo:~]# uname -a
Linux nixos-duo 5.10.4 #1-NixOS PREEMPT Tue Jan 1 00:00:00 UTC 1980 riscv64 GNU/Linux

[root@nixos-duo:~]# cat /etc/os-release 
ANSI_COLOR="0;38;2;126;186;228"
BUG_REPORT_URL="https://github.com/NixOS/nixpkgs/issues"
BUILD_ID="25.05.20250119.00e0195"
CPE_NAME="cpe:/o:nixos:nixos:25.05"
DEFAULT_HOSTNAME=nixos
DOCUMENTATION_URL="https://nixos.org/learn.html"
HOME_URL="https://nixos.org/"
ID=nixos
ID_LIKE=""
IMAGE_ID=""
IMAGE_VERSION=""
LOGO="nix-snowflake"
NAME=NixOS
PRETTY_NAME="NixOS 25.05 (Warbler)"
SUPPORT_URL="https://nixos.org/community.html"
VARIANT=""
VARIANT_ID=""
VENDOR_NAME=NixOS
VENDOR_URL="https://nixos.org/"
VERSION="25.05 (Warbler)"
VERSION_CODENAME=warbler
VERSION_ID="25.05"

[root@nixos-duo:~]# lscpu
Architecture:          riscv64
  Byte Order:          Little Endian
CPU(s):                1
  On-line CPU(s) list: 0

[root@nixos-duo:~]# 

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
