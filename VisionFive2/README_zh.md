# StarFive VisionFive 2

## 测试环境

### 操作系统信息

- openEuler RISC-V 23.09 Preview
    - 下载链接：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Visionfive2/
    - 参考安装文档：https://gitee.com/openeuler/RISC-V/blob/master/release/openEuler-23.03/Installation_Book/Visionfive2/README_zh.md
- Debian bookworm（官方提供）
    - 下载链接：https://debian.starfivetech.com/
- openKylin 2.0
    - 下载链接：https://www.openkylin.top/downloads
- 参考安装文档：https://docs.openkylin.top/zh/01_%E5%AE%89%E8%A3%85%E5%8D%87%E7%BA%A7%E6%8C%87%E5%8D%97/%E5%9C%A8riscv%E4%B8%8A%E5%AE%89%E8%A3%85/%E5%9C%A8VisionFive2%E4%B8%8A%E5%AE%89%E8%A3%85openKylin
- Ubuntu 24.10 & 24.04.2 LTS
    - 下载链接：https://ubuntu.com/download/risc-v
    - 参考安装文档：https://wiki.ubuntu.com/RISC-V/StarFive%20VisionFive%202
- BuildRoot (VisionFive 2 SDK)
    - 下载链接：https://github.com/starfive-tech/VisionFive2/releases
    - 参考安装文档：https://github.com/starfive-tech/VisionFive2
- Arch Linux
    - 下载链接：https://github.com/cwt-vf2/archlinux-image-vf2/releases/tag/cwt23
    - 参考安装文档：https://forum.rvspace.org/t/arch-linux-image-for-visionfive-2/1459
- Fedora 41
  - 下载链接：https://mirror.iscas.ac.cn/fedora-riscv/dl/StarFive/visionfive2/images/latest/fedora-disk-multi-desktops_starfive_vf2-sda.raw.gz
  - 参考安装文档：https://images.fedoravforce.com/how-to-burn-images-to-sd-cards
- Gentoo
    - 下载链接：https://drive.google.com/file/d/10TDsk2FwZDJv3yJvDAfCam5Wf9ibS6Eg/view?usp=sharing
    - 参考安装文档：https://forum.rvspace.org/t/experimental-gentoo-image/1807
- openSUSE Tumbleweed
    - 下载链接：https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/StarFive:/VisionFive2/images/
    - 参考安装文档：https://en.opensuse.org/HCL:VisionFive2
- OpenBSD
  - 下载链接：https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/
  - 参考安装文档：https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/INSTALL.riscv64
- Armbian Noble Minimal & Armbian Jammy Xfce
    - 下载链接：https://www.armbian.com/visionfive2/
    - 参考安装文档：https://www.armbian.com/visionfive2/
- OpenWrt SNAPSHOT
    - 下载链接：https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=starfive%2Fgeneric&id=visionfive2-v1.3b
    - 参考安装文档：https://doc.rvspace.org/VisionFive2/Application_Notes/VisionFive2_OpenWrt/VisionFive_2/openwrt/compile.html
- RT-Thread
    - 源码链接：https://github.com/starfive-tech/VisionFive2
    - 参考安装文档：https://doc.rvspace.org/VisionFive2/Application_Notes/RT-Thread/index.html
- Zephyr
    - 参考安装文档：https://docs.zephyrproject.org/latest/boards/starfive/visionfive2/doc/index.html
- Deepin 23 preview
    - 下载链接：https://cdimage.deepin.com/RISC-V/preview-20240613-riscv64/deepin-23-beige-preview-riscv64-visionfive2-20240613-125619.tar.xz
    - 参考安装文档：https://cdimage.deepin.com/RISC-V/VisionFive-v2-image/README.txt
- NetBSD
    - 下载链接：https://nyftp.netbsd.org/pub/NetBSD-daily/HEAD/latest/riscv-riscv64/binary/gzimg/
- Alpine
    - 下载链接：https://dev.alpinelinux.org/~mps/riscv64/visionfive-v2-mmc.img.xz
    - 参考安装文档：https://arvanta.net/alpine/alpine-on-visionfive/
- DietPi
    - 下载链接：https://dietpi.com/downloads/images/testing/DietPi_VisionFive2-RISC-V-Sid.img.xz
    - 参考安装文档：https://dietpi.com/blog/?p=2629
- NixOS
    - 源码链接: https://github.com/NickCao/nixos-riscv
    - 参考安装文档: https://github.com/NickCao/nixos-riscv/README.md
- eweOS
    - 源码链接：https://github.com/panglars/eweos-vf2-mainline
    - 参考安装文档：https://github.com/panglars/eweos-vf2-mainline/blob/main/README.md


### 硬件开发板信息

- StarFive VisionFive 2

## 测试结果

| 软件分类                 | 软件包名 | 测试结果（测试报告）                   |
|--------------------------|----------|----------------------------------------|
| openEuler/Base 镜像启动  | N/A      | [成功][oERV]                           |
| openEuler/Xfce 镜像启动  | Xfce     | [成功][oERV]                           |
| Debian 镜像启动          | N/A      | [成功][Debian]（StarFive 厂商镜像）    |
| openKylin 镜像启动       | N/A      | [成功][oK]（官方支持）                 |
| Ubuntu 镜像启动          | N/A      | [成功][Ubuntu]（官方支持）             |
| Ubuntu LTS 镜像启动      | N/A      | [成功][Ubuntu-LTS]（官方支持）         |
| BuildRoot 镜像启动       | N/A      | [成功][BuildRoot]（StarFive 厂商镜像） |
| Arch Linux 镜像启动      | N/A      | [成功][Arch]                           |
| Fedora 镜像启动          | N/A      | [成功][Fedora]                         |
| Gentoo 镜像启动          | N/A      | [成功][Gentoo]                         |
| openSUSE 镜像启动        | N/A      | [成功][openSUSE]（官方支持）           |
| OpenBSD 镜像启动         | N/A      | [成功][OpenBSD]                        |
| Armbian/Minimal 镜像启动 | N/A      | [成功][Armbian]                        |
| Armbian/Xfce 镜像启动    | Xfce     | [成功][Armbian]                        |
| OpenWrt 镜像启动         | N/A      | [成功][OpenWrt]                        |
| RT-Thread 镜像构建及启动 | N/A      | [成功][RT-Thread]（官方支持）          |
| Zephyr 镜像构建及启动    | N/A      | [失败][Zephyr]                         |
| NuttX 镜像构建及启动     | N/A      | [成功][NuttX]                          |
| Deepin 镜像启动          | N/A      | [成功][Deepin]                         |
| NetBSD 镜像启动          | N/A      | [成功][NetBSD]                         |
| Alpine 镜像启动          | N/A      | [成功][Alpine]                         |
| DietPi 镜像启动          | N/A      | [成功][DietPi]                         |
| NixOS 镜像构建及启动     | N/A      | [成功][NixOS]                          |
| eweOS 镜像构建及启动     | N/A      | [成功][eweOS]                          |

[oERV]: ./openEuler/README_zh.md
[Debian]: ./Debian/README_zh.md
[oK]: ./openKylin/README_zh.md
[Ubuntu]: ./Ubuntu/README_zh.md
[Ubuntu-LTS]: ./Ubuntu/Ubuntu_LTS_zh.md
[BuildRoot]: ./BuildRoot/README_zh.md
[Arch]: ./ArchLinux/README_zh.md
[Fedora]: ./Fedora/README_zh.md
[Gentoo]: ./Gentoo/README_zh.md
[openSUSE]: ./openSUSE/README_zh.md
[OpenBSD]: ./OpenBSD/README_zh.md
[Armbian]: ./Armbian/README_zh.md
[OpenWrt]: ./OpenWRT/README_zh.md
[RT-Thread]: ./RT-Thread/README_zh.md
[Zephyr]: ./Zephyr/README_zh.md
[NuttX]: ./NuttX/README_zh.md
[Deepin]: ./Deepin/README_zh.md
[NetBSD]: ./NetBSD/README_zh.md
[Alpine]: ./Alpine/README_zh.md
[DietPi]: ./DietPi/README_zh.md
[NixOS]: ./NixOS/README_zh.md
[eweOS]: ./eweOS/README_zh.md
