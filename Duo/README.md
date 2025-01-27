---
vendor: milkv_duo
product: Milk-V Duo (64M)
cpu: CV1800B
cpu_core: XuanTie C906
---

# Milk-V Duo

## Test Environment

### Operating System Information

- BuildRoot & FreeRTOS
  - Download link: https://github.com/milkv-duo/duo-buildroot-sdk/releases
    - Official BuildRoot SDK provided by Milk-V, including FreeRTOS
  - Reference Installation Document: https://github.com/milkv-duo/duo-buildroot-sdk
- Arch Linux
  - Download link: https://drive.google.com/file/d/1Qf8ioR29KCsvt2MIWre168Um9Q8ot_z5/view?usp=sharing
  - Reference Installation Document: https://xyzdims.com/3d-printers/misc-hardware-notes/iot-milk-v-duo-risc-v-esbc-running-linux/#ArchLinux_Disk_Image
- Alpine Linux 3.19_alpha20230901 / 3.20.3 riscv64
  - Download Link: 
    - https://github.com/cwt/duo-buildroot-sdk/releases/download/poc1/MilkV-Duo-alpine.img.xz

    (Alternatively):
    - Alpine minirootfs: [https://alpinelinux.org/downloads/](https://dl-cdn.alpinelinux.org/alpine/v3.20/releases/riscv64/alpine-minirootfs-3.20.3-riscv64.tar.gz)
    - Official Buildroot image: [https://github.com/milkv-duo/duo-buildroot-sdk/releases](https://github.com/milkv-duo/duo-buildroot-sdk/releases/download/v1.1.3/milkv-duo-sd-v1.1.3-2024-0930.img.zip)
  - Reference Installation Document: 
    - [Alpine Wiki (Installation)](https://wiki.alpinelinux.org/wiki/Installation)
    - [Alpine Wiki (How to make a cross architecture chroot)](https://wiki.alpinelinux.org/wiki/How_to_make_a_cross_architecture_chroot)
    - [Milk-V forum thread](https://community.milkv.io/t/alpine-linux-on-the-duo/700/18)
- Debian trixie/sid
  - Download link: https://drive.google.com/file/d/1TqMuFsRo5Es2Y6-qAyxV8jnFdAkcCp4v/view?usp=sharing
  - Reference Installation Document: https://github.com/hongwenjun/riscv64/tree/main/milkv-duo
- Fedora 41
  - Download link: https://mirror.iscas.ac.cn/fedora-riscv/dl/Milk-V/Duo/images/latest/milkv-duo-fedora-minimal.img.gz
  - Reference Installation Document: https://fedoraproject.org/wiki/Architectures/RISC-V/Installing
- RT-Thread / RT-Thread Smart
  - Source Code Link: https://github.com/RT-Thread/rt-thread
  - Reference Installation Document: https://github.com/RT-Thread/rt-thread/blob/master/bsp/cvitek/README.md
- ThreadX
  - Source code link: https://github.com/saicogn/ThreadX-to-RISC-V64
  - Reference Installation Document: https://github.com/saicogn/ThreadX-to-RISC-V64/blob/main/README.md
- Zephyr
  - Source code link: https://github.com/zephyrproject-rtos/zephyr/tree/main
  - Reference Installation Document:
      - https://docs.zephyrproject.org/latest/develop/getting_started/index.html
      - https://github.com/milkv-duo/duo-buildroot-sdk
- openEuler 23.09 riscv64
  - Download links:
    - buildroot: https://github.com/milkv-duo/duo-buildroot-sdk.git
    - rootfs: https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/openeuler-rootfs.tar.gz
  - Reference Installation Document: https://blog.inuyasha.love/linuxeveryday/33.html
- UniProton
  - Download links: https://share.weiyun.com/0gIkzesF
  - Reference Installation Document: https://github.com/openeuler-riscv/duo-buildroot-sdk/blob/develop/uni_pedestal/WORK.md
- Ubuntu 22.04
  - Download Link: https://drive.google.com/file/d/1y1NQamzUDzot_kVT2yKkbusoJmtvH5tD/view?usp=sharing
  - Reference Installation Document:
    - https://xyzdims.com/3d-printers/misc-hardware-notes/iot-milk-v-duo-risc-v-esbc-running-linux/#Ubuntu_Disk_Image
    - https://github.com/bassusteur/milkv-duo-ubuntu
- Yocto
  - Source Code Link: https://github.com/kinsamanka/meta-milkv
  - Reference Installation Document: https://github.com/kinsamanka/meta-milkv/blob/master/README.md
- NixOS
  - Source code link: https://github.com/NickCao/nixos-riscv
  - Reference Installation Document: https://github.com/NickCao/nixos-riscv/README.md

### Hardware Information

- Milk-V Duo (64M, CV1800B)

## Test Results

| Software Category                    | Package Name | Test Results (Test Report)                                       |
| ------------------------------------ | ------------ | ---------------------------------------------------------------- |
| BuildRoot Image Boot                 | N/A          | [Success][Duo] (flashed via `ruyi` CLI)                          |
| FreeRTOS Boot                        | N/A          | [Success][FreeRTOS] (included in BuildRoot image)                |
| Arch Linux Image Boot                | N/A          | [Success][Arch]                                                  |
| Alpine Linux Boot                    | N/A          | [Success][Alpine] (use community image or build rootfs manually) |
| Debian Image Boot                    | N/A          | [Success][Debian]                                                |
| RT-Thread Image Build and Boot       | N/A          | [Success][RT-Thread]                                             |
| RT-Thread Smart Image Build and Boot | N/A          | [Success][RT-Smart]                                              |
| Fedora Image Boot                    | N/A          | [Success][Fedora]                                                |
| openEuler                            | N/A          | [Success][oE]                                                    |
| ThreadX Image Build and Boot         | N/A          | [Success][ThreadX]                                               |
| Zephyr Image Build and Boot          | N/A          | [Success][Zephyr]                                                |
| UniProton Boot                       | N/A          | [Success][UniProton]                                             |
| Ubuntu Boot                          | N/A          | [Success][Ubuntu]                                                |
| Yocto Image Build and Boot           | N/A          | [Success][Yocto]                                                 |
| NixOS Image Build and Boot           | N/A          | [Success][NixOS]                                                 |

[Duo]: ./BuildRoot/README.md
[Arch]: ./ArchLinux/README.md
[Alpine]: ./Alpine/README.md
[Debian]: ./Debian/README.md
[Fedora]: ./Fedora/README.md
[RT-Thread]: ./RT-Thread/README.md
[RT-Smart]: ./RT-Smart/README_RTSmart.md
[FreeRTOS]: ./FreeRTOS/README.md
[oE]: ./openEuler/README.md
[ThreadX]: ./ThreadX/README.md
[Zephyr]: ./Zephyr/README.md
[UniProton]: ./UniProton/README.md
[Ubuntu]: ./Ubuntu/README.md
[Yocto]: ./Yocto/README.md
[NixOS]: ./NixOS/README.md