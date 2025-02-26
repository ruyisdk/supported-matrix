# Fedora 38 LPi4A Minimal 测试报告

## 测试环境

### 系统信息

- 系统版本：Fedora 41
- 下载链接：https://images.fedoravforce.org/LicheePi%204A
- 参考安装文档：https://fedoraproject.org/wiki/Architectures/RISC-V/T-Head

### 硬件信息

- Lichee Pi 4A (16G RAM + 128G eMMC)
- 电源适配器
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

使用 `gzip` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
gzip -d Fedora-Minimal-41-20250209114910.riscv64.Xuantie-TH1520.Sipeed-Lichee-Pi-4A.raw.gz 
sudo dd if=Fedora-Minimal-41-20250209114910.riscv64.Xuantie-TH1520.Sipeed-Lichee-Pi-4A.raw of=/dev/<your_device> bs=4M status=progress
```

### 刷写 bootloader

**在 LicheePi 4A 启动 Fedora 需要使用特殊的 uboot，可以在这里下载** :
https://mirror.iscas.ac.cn/fedora-riscv/dl/Sipeed/LicheePi4A/fw/u-boot-with-spl.bin

进入 fastboot。
- 正式版确认 boot 拨码开关为 eMMC。
- 按动 BOOT 同时上电。
- （详见官方教程）
使用 fastboot 按命令烧录 u-boot。

```bash
sudo fastboot flash ram u-boot-with-spl.bin 
sudo fastboot reboot

sudo fastboot flash uboot u-boot-with-spl.bin 
```

### 登录系统

通过串口登录系统。

默认用户名： `root`
默认密码： `riscv`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。能进入桌面。

### 启动信息

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

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
