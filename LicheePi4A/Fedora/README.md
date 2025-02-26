---
sys: fedora
sys_ver: 41
sys_var: minimal

status: basic 
last_update: 2025-02-26
---

# Fedora 41 LPi4A Minimal Test Report

## Test Environment

### System Information

- System Version: Fedora 41
- Download Link: https://images.fedoravforce.org/LicheePi%204A
- Reference Installation Document: https://fedoraproject.org/wiki/Architectures/RISC-V/T-Head

### Hardware Information

- Lichee Pi 4A (16GB RAM + 128GB eMMC)
- Power Adapter
- A USB to UART Debugger

## Installation Steps

### Flashing Image

Use `gzip` to extract the image.
Use `dd` to flash the image to the microSD card.

```bash
gzip -d Fedora-Minimal-41-20250209114910.riscv64.Xuantie-TH1520.Sipeed-Lichee-Pi-4A.raw.gz 
sudo dd if=Fedora-Minimal-41-20250209114910.riscv64.Xuantie-TH1520.Sipeed-Lichee-Pi-4A.raw of=/dev/<your_device> bs=4M status=progress
```

### Flashing Bootloader

**Booting Fedora in LicheePi 4A requires a special uboot, which can be downloaded here** : https://mirror.iscas.ac.cn/fedora-riscv/dl/Sipeed/LicheePi4A/fw/u-boot-with-spl.bin

Enter fastboot.
- Make sure the boot switch on the production version is set to eMMC.
- Press BOOT while powering on.
- (Refer to official tutorials)
Use fastboot command to flash u-boot.

```bash
sudo fastboot flash ram u-boot-with-spl.bin 
sudo fastboot reboot

sudo fastboot flash uboot u-boot-with-spl.bin 
```

### Logging into the System

Logging into the System via serial port.

Default Username: `root`
Default Password: `riscv`

## Expected Results

The system boots up correctly and can be accessed via the onboard serial port.

## Actual Results

The system boots up correctly, successfully logged in via the onboard serial port, and can access the desktop.

### Boot Log

```log

Welcome to the Fedora-V Force disk image
https://images.fedoravforce.org/

Build date: Sun Feb  9 11:55:21 UTC 2025

Kernel 6.6.66-g1c6721ec2918-dirty on an riscv64 (ttyS0)

The root password is 'riscv'.
root password logins are disabled in SSH starting Fedora.

If DNS isn’t working, try editing ‘/etc/resolv.conf’ or using 'resolvctl'.

For updates and latest information read:
https://fedoraproject.org/wiki/Architectures/RISC-V

Fedora RISC-V
-------------
fedora login: root
Password: 
[root@fedora ~]# uname -a
Linux fedora 6.6.66-g1c6721ec2918-dirty #1 SMP PREEMPT Thu Jan 16 20:49:59 CST 2025 riscv64 GNU/Linux
[root@fedora ~]# cat /etc/os-release 
NAME="Fedora Linux"
VERSION="41 (Forty One)"
RELEASE_TYPE=stable
ID=fedora
VERSION_ID=41
VERSION_CODENAME=""
PLATFORM_ID="platform:f41"
PRETTY_NAME="Fedora Linux 41 (Forty One)"
ANSI_COLOR="0;38;2;60;110;180"
LOGO=fedora-logo-icon
CPE_NAME="cpe:/o:fedoraproject:fedora:41"
DEFAULT_HOSTNAME="fedora"
HOME_URL="https://fedoraproject.org/"
DOCUMENTATION_URL="https://docs.fedoraproject.org/en-US/fedora/f41/system-administrators-guide/"
SUPPORT_URL="https://ask.fedoraproject.org/"
BUG_REPORT_URL="https://bugzilla.redhat.com/"
REDHAT_BUGZILLA_PRODUCT="Fedora"
REDHAT_BUGZILLA_PRODUCT_VERSION=41
REDHAT_SUPPORT_PRODUCT="Fedora"
REDHAT_SUPPORT_PRODUCT_VERSION=41
SUPPORT_END=2025-12-15
[root@fedora ~]# cat /proc/cpuinfo 
processor       : 0
hart            : 0
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_xtheadvector
mmu             : sv39
uarch           : thead,c910
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 1
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_xtheadvector
mmu             : sv39
uarch           : thead,c910
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 2
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_xtheadvector
mmu             : sv39
uarch           : thead,c910
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 3
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_xtheadvector
mmu             : sv39
uarch           : thead,c910
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

[root@fedora ~]# 
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

