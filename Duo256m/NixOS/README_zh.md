# NixOS Milk-V Duo 256M 测试报告

## 测试环境

### 操作系统信息

- 系统版本：25.05.20250119
- 源码链接: https://github.com/NickCao/nixos-riscv
- 参考安装文档: https://github.com/NickCao/nixos-riscv/README.md

### 硬件信息

- Milk-V Duo 256M
- USB-A 电源一个
- USB-A to C 线缆一条
- microSD 卡一张
- microSD 读卡器一个
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 编译镜像

如果主机运行 NixOS, 使用 `nix build ".#hydraJobs.duo-256"` 编译镜像即可。
对于其他发行版，不建议直接安装并使用 `nix` 包管理器，推荐使用 Nix 的官方 Docker 镜像： 

```shell
docker run -ti -v $(pwd):/work ghcr.io/nixos/nix
```

在 Docker 容器中：

```shell
echo "max-jobs = auto" >> /etc/nix/nix.conf # 使用多核编译
echo "substituters = https://mirrors.tuna.tsinghua.edu.cn/nix-channels/store https://cache.nixos.org/" >> /etc/nix/nix.conf # 更换镜像源
cd /work
nix build ".#hydraJobs.duo-256" --extra-experimental-features nix-command --extra-experimental-features flakes
```

生成的镜像位于 `./result/sd-image/` 目录下，文件名形如 `nixos-image-sd-card-25.05.20250119.00e0195-riscv64-linux.img.zst`。

### 刷写镜像到 microSD 卡

使用 `dd` 将镜像写入至 microSD 卡。

### 登录系统

通过串口登录系统。

默认为无密码且自动登录。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

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

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
