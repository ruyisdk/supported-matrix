---
vendor: milkv_duo256m
product: Milk-V Duo (256M)
cpu: SG2002
cpu_core: XuanTie C906 + ARM Cortex-A53
---

# Milk-V Duo 256M

## Test Environment

### Operating System Information

- BuildRoot & FreeRTOS
  - Download link: [https://github.com/milkv-duo/duo-buildroot-sdk/releases](https://github.com/milkv-duo/duo-buildroot-sdk/releases)
    - Official Milk-V provided BuildRoot SDK, which also includes FreeRTOS.
  - Reference Installation Document: [https://github.com/milkv-duo/duo-buildroot-sdk](https://github.com/milkv-duo/duo-buildroot-sdk)
- Debian
  - Download link: [https://github.com/Fishwaldo/sophgo-sg200x-debian](https://github.com/Fishwaldo/sophgo-sg200x-debian)
  - Reference Installation Document: [https://github.com/Fishwaldo/sophgo-sg200x-debian](https://github.com/Fishwaldo/sophgo-sg200x-debian)
- Fedora 41
  - Download Link: https://mirror.iscas.ac.cn/fedora-riscv/dl/Milk-V/Duo256M/images/latest/milkv-duo-256m-fedora-minimal.img.gz
  - Reference Installation Document: https://github.com/chainsx/fedora-riscv-builder
- FreeRTOS
  - Download link: https://github.com/milkv-duo/duo-buildroot-sdk/releases
  - Reference Installation Document: https://github.com/milkv-duo/duo-buildroot-sdk
      - FreeRTOS: https://milkv.io/zh/docs/duo/getting-started/rtoscore
- RT-Thread / RT-Thread Smart
  - Source code link: [https://github.com/RT-Thread/rt-thread](https://github.com/RT-Thread/rt-thread)
  - Reference Installation Document: [https://github.com/RT-Thread/rt-thread/blob/master/bsp/cvitek/README.md](https://github.com/RT-Thread/rt-thread/blob/master/bsp/cvitek/README.md)
- Zephyr
  - Source code link: https://github.com/zephyrproject-rtos/zephyr/tree/main
  - Reference Installation Document:
      - https://docs.zephyrproject.org/latest/develop/getting_started/index.html
      - https://github.com/milkv-duo/duo-buildroot-sdk
- Alpine Linux 3.20.3/edge riscv64
  - Download Link: 
    - https://drive.google.com/file/d/1zhhB6AdgvjjuzBWjY6TchdX5b0uNWzP-/view

    (Alternatively):
    
    - Alpine minirootfs: [https://alpinelinux.org/downloads/](https://dl-cdn.alpinelinux.org/alpine/v3.20/releases/riscv64/alpine-minirootfs-3.20.3-riscv64.tar.gz)
    - Latest Duo 256M Debian image (for the kernel and its modules): [https://github.com/Fishwaldo/sophgo-sg200x-debian/releases/](https://github.com/Fishwaldo/sophgo-sg200x-debian/releases/download/v1.4.0/duo256_sd.img.lz4)
  - Reference Installation Document: 
    - [Alpine Wiki (Installation)](https://wiki.alpinelinux.org/wiki/Installation)
    - [Alpine Wiki (How to make a cross architecture chroot)](https://wiki.alpinelinux.org/wiki/How_to_make_a_cross_architecture_chroot)
- Ubuntu 22.04
  - Download Link: https://drive.google.com/file/d/1mkzLhvtjJup3GbgWKZdwL80PZMMXg7n1/view?usp=drive_link
  - Reference Installation Document: https://xyzdims.com/3d-printers/misc-hardware-notes/iot-milk-v-duo-risc-v-esbc-running-linux/#Ubuntu_Disk_Image
- Yocto
  - Source Code Link: https://github.com/kinsamanka/meta-milkv
  - Reference Installation Document: https://github.com/kinsamanka/meta-milkv/blob/master/README.md
- NixOS
  - Source code link: https://github.com/NickCao/nixos-riscv
  - Reference Installation Document: https://github.com/NickCao/nixos-riscv/README.md

### Hardware Information

- Milk-V Duo (256M, SG2002)

## Test Results

| Software Category                  | Package Name | Test Result (Report)                                             |
| ---------------------------------- | ------------ | ---------------------------------------------------------------- |
| BuildRoot Image Boot               | N/A          | [Success][BuildRoot]                                             |
| FreeRTOS Boot                      | N/A          | [Success][FreeRTOS] (Included in BuildRoot image)                |
| Debian Image Boot                  | N/A          | [Success][Debian]                                                |
| Fedora Image Boot                  | N/A          | [Success][Fedora]                                                |
| RT-Thread Image Build & Boot       | N/A          | [Success][RT-Thread]                                             |
| RT-Thread Smart Image Build & Boot | N/A          | [Success][RT-Smart]                                              |
| Zephyr Image Build & Boot          | N/A          | [Success][Zephyr]                                                |
| Alpine Linux Boot                  | N/A          | [Success][Alpine] (use community image or build rootfs manually) |
| Ubuntu Boot                        | N/A          | [Success][Alpine] (use community image or build rootfs manually) |
| Yocto Image Build and Boot         | N/A          | [Success][Yocto]                                                 |
| NixOS Image Build and Boot         | N/A          | [Success][NixOS]                                                 |

[BuildRoot]: ./BuildRoot/README.md
[Debian]: ./Debian/README.md
[Fedora]: ./Fedora/README.md
[RT-Thread]: ./RT-Thread/README.md
[RT-Smart]: ./RT-Thread/README_RTSmart.md
[FreeRTOS]: ./FreeRTOS/README.md
[Zephyr]: ./Zephyr/README.md
[Alpine]: ./Alpine/README.md
[Ubuntu]: ./Ubuntu/README.md
[Yocto]: ./Yocto/README.md
[NixOS]: ./NixOS/README.md