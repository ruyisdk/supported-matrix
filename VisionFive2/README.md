---
product: VisionFive 2
cpu: JH7110
cpu_core: SiFive U74 + SiFive S7 + SiFive E24
---

# StarFive VisionFive 2

## Test Environment

### Operating System Information

- openEuler RISC-V 23.09 Preview
    - Download Link: https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Visionfive2/
    - Reference Installation Document: https://gitee.com/openeuler/RISC-V/blob/master/release/openEuler-23.03/Installation_Book/Visionfive2/README.md
- Debian bookworm (officially provided)
    - Download Link: https://debian.starfivetech.com/
- openKylin 2.0
    - Download Link: https://www.openkylin.top/downloads
    - Reference Installation Document：https://docs.openkylin.top/zh/01_%E5%AE%89%E8%A3%85%E5%8D%87%E7%BA%A7%E6%8C%87%E5%8D%97/%E5%9C%A8riscv%E4%B8%8A%E5%AE%89%E8%A3%85/%E5%9C%A8VisionFive2%E4%B8%8A%E5%AE%89%E8%A3%85openKylin (Chinese)
- Ubuntu 24.10 & 24.04.2 LTS
    - Download Link: https://ubuntu.com/download/risc-v
    - Reference Installation Document: https://wiki.ubuntu.com/RISC-V/StarFive%20VisionFive%202
- BuildRoot (VisionFive 2 SDK)
    - Download Link: https://github.com/starfive-tech/VisionFive2/releases
    - Reference Installation Document: https://github.com/starfive-tech/VisionFive2
- Arch Linux
    - Download Link: https://github.com/cwt-vf2/archlinux-image-vf2/releases/tag/cwt23
    - Reference Installation Document: https://forum.rvspace.org/t/arch-linux-image-for-visionfive-2/1459
- Fedora 41
  - Download Link: https://mirror.iscas.ac.cn/fedora-riscv/dl/StarFive/visionfive2/images/latest/fedora-disk-multi-desktops_starfive_vf2-sda.raw.gz
  - Reference Installation Document: https://images.fedoravforce.com/how-to-burn-images-to-sd-cards
- Gentoo
    - Download Link: https://drive.google.com/file/d/10TDsk2FwZDJv3yJvDAfCam5Wf9ibS6Eg/view?usp=sharing
    - Reference Installation Document: https://forum.rvspace.org/t/experimental-gentoo-image/1807
- openSUSE
    - Download Link: https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/StarFive:/VisionFive2/images/
    - Reference Installation Document: https://en.opensuse.org/HCL:VisionFive2
- OpenBSD
  - Download Link: https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/
  - Reference Installation Document: https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/INSTALL.riscv64
- Armbian Noble Minimal & Armbian Jammy Xfce
    - Download Link: https://www.armbian.com/visionfive2/
    - Reference Installation Document: https://www.armbian.com/visionfive2/
- OpenWrt SNAPSHOT
    - Download Link: https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=starfive%2Fgeneric&id=visionfive2-v1.3b
    - Reference Installation Document: https://doc.rvspace.org/VisionFive2/Application_Notes/VisionFive2_OpenWrt/VisionFive_2/openwrt/compile.html
- RT-Thread
    - Source Code Link: https://github.com/starfive-tech/VisionFive2
    - Reference Installation Docum- Source code link: https://github.com/NickCao/nixos-riscv
- Reference Installation Document: https://github.com/NickCao/nixos-riscv/README.mdent: https://doc.rvspace.org/VisionFive2/Application_Notes/RT-Thread/index.html
- Zephyr
    - Reference Installation Document: https://docs.zephyrproject.org/latest/boards/starfive/visionfive2/doc/index.html
- Deepin 23 preview
    - Download Link: https://cdimage.deepin.com/RISC-V/preview-20240613-riscv64/deepin-23-beige-preview-riscv64-visionfive2-20240613-125619.tar.xz
    - Reference Installation Document: https://cdimage.deepin.com/RISC-V/VisionFive-v2-image/README.txt
- NetBSD
    - Download Link: https://nyftp.netbsd.org/pub/NetBSD-daily/HEAD/latest/riscv-riscv64/binary/gzimg/
- Alpine
    - Download Link: https://dev.alpinelinux.org/~mps/riscv64/visionfive-v2-mmc.img.xz
    - Reference INstallation Document: https://arvanta.net/alpine/alpine-on-visionfive/
- DietPi
    - Download Link: https://dietpi.com/downloads/images/testing/DietPi_VisionFive2-RISC-V-Sid.img.xz
    - Reference Installation Document: https://dietpi.com/blog/?p=2629
- NixOS
    - Source code link: https://github.com/NickCao/nixos-riscv
    - Reference Installation Document: https://github.com/NickCao/nixos-riscv/README.md
- eweOS
    - Source code Link: https://github.com/panglars/eweos-vf2-mainline
    - Reference Installation Document: https://github.com/panglars/eweos-vf2-mainline/blob/main/README.md
    
    
### Hardware Information

- StarFive VisionFive 2

## Test Results

| Software Category     | Software Package | Test Results (Test Report)                        |
|-----------------------|------------------|---------------------------------------------------|
| openEuler/Base Image  | N/A              | [Successful][oERV]                                |
| openEuler/Xfce Image  | Xfce             | [Successful][oERV]                                |
| Debian Image          | N/A              | [Successful][Debian] (Official StarFive Image)    |
| openKylin Image       | N/A              | [Successful][oK] (Official Support)               |
| Ubuntu Image          | N/A              | [Successful][Ubuntu] (Official Support)           |
| Ubuntu LTS Image      | N/A              | [Successful][Ubuntu-LTS] (Official Support)       |
| BuildRoot Image       | N/A              | [Successful][BuildRoot] (Official StarFive Image) |
| Arch Linux Image      | N/A              | [Successful][Arch]                                |
| Fedora Image          | N/A              | [Successful][Fedora]                              |
| Gentoo Image          | N/A              | [Successful][Gentoo]                              |
| openSUSE Image        | N/A              | [Successful][openSUSE] (Official Support)         |
| OpenBSD Image         | N/A              | [Successful][OpenBSD]                             |
| Armbian/Minimal Image | N/A              | [Successful][Armbian]                             |
| Armbian/Xfce Image    | Xfce             | [Successful][Armbian]                             |
| OpenWrt Image         | N/A              | [Successful][OpenWrt]                             |
| RT-Thread Image       | N/A              | [Successful][RT-Thread] (Official Support)        |
| Zephyr Image          | N/A              | [Failure][Zephyr]                                 |
| NuttX Image           | N/A              | [Successful][NuttX]                               |
| Deepin Image          | N/A              | [Successful][Deepin]                              |
| NetBSD Image          | N/A              | [Successful][NetBSD]                              |
| Alpine Image          | N/A              | [Successful][Alpine]                              |
| DietPi Image          | N/A              | [Successful][DietPi]                              |
| NixOS Image           | N/A              | [Successful][NixOS]                               |
| eweOS Image           | N/A              | [Successful][eweOS]                               |

[oERV]: ./openEuler/README.md
[Debian]: ./Debian/README.md
[oK]: ./openKylin/README.md
[Ubuntu]: ./Ubuntu/README.md
[Ubuntu-LTS]: ./Ubuntu/Ubuntu_LTS.md
[BuildRoot]: ./BuildRoot/README.md
[Arch]: ./ArchLinux/README.md
[Fedora]: ./Fedora/README.md
[Gentoo]: ./Gentoo/README.md
[openSUSE]: ./openSUSE/README.md
[OpenBSD]: ./OpenBSD/README.md
[Armbian]: ./Armbian/README.md
[OpenWrt]: ./OpenWRT/README.md
[RT-Thread]: ./RT-Thread/README.md
[Zephyr]: ./Zephyr/README.md
[NuttX]: ./NuttX/README.md
[Deepin]: ./Deepin/README.md
[NetBSD]: ./NetBSD/README.md
[Alpine]: ./Alpine/README.md
[DietPi]: ./DietPi/README.md
[NixOS]: ./NixOS/README.md
[eweOS]: ./eweOS/README.md
