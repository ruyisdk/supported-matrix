# Milk-V Duo 256M

## 测试环境

### 操作系统信息

- BuildRoot & FreeRTOS
  - 下载链接：https://github.com/milkv-duo/duo-buildroot-sdk/releases
    - Milk-V 官方提供的 BuildRoot SDK，同时包含了 FreeRTOS
  - 参考安装文档：https://github.com/milkv-duo/duo-buildroot-sdk
- Debian
  - 下载链接：https://github.com/Fishwaldo/sophgo-sg200x-debian
  - 参考安装文档：https://github.com/Fishwaldo/sophgo-sg200x-debian
- Fedora 41
  - 下载链接：https://mirror.iscas.ac.cn/fedora-riscv/dl/Milk-V/Duo256M/images/latest/milkv-duo-256m-fedora-minimal.img.gz
  - 参考安装文档：https://github.com/chainsx/fedora-riscv-builder
- FreeRTOS
  - 下载链接: https://github.com/milkv-duo/duo-buildroot-sdk/releases
  - 参考安装文档: https://github.com/milkv-duo/duo-buildroot-sdk
      - FreeRTOS: https://milkv.io/zh/docs/duo/getting-started/rtoscore
- RT-Thread / RT-Thread Smart
  - 源码链接：https://github.com/RT-Thread/rt-thread
  - 参考安装文档：https://github.com/RT-Thread/rt-thread/blob/master/bsp/cvitek/README.md
- Zephyr
  - 源码链接: https://github.com/zephyrproject-rtos/zephyr/tree/main
  - 参考安装文档:
      - https://docs.zephyrproject.org/latest/develop/getting_started/index.html
      - https://github.com/milkv-duo/duo-buildroot-sdk
- Alpine Linux 3.20.3/edge riscv64
  - 下载链接：
    - https://drive.google.com/file/d/1zhhB6AdgvjjuzBWjY6TchdX5b0uNWzP-/view
  
    或者
    
    - Alpine minirootfs: [https://alpinelinux.org/downloads/](https://dl-cdn.alpinelinux.org/alpine/v3.20/releases/riscv64/alpine-minirootfs-3.20.3-riscv64.tar.gz)
    - 最新的 Duo 256M Debian 镜像 (用于提取内核及其模块): [https://github.com/Fishwaldo/sophgo-sg200x-debian/releases/](https://github.com/Fishwaldo/sophgo-sg200x-debian/releases/download/v1.4.0/duo256_sd.img.lz4)
  - 参考安装文档：
    - [Alpine Wiki (Installation)](https://wiki.alpinelinux.org/wiki/Installation)
    - [Alpine Wiki (How to make a cross architecture chroot)](https://wiki.alpinelinux.org/wiki/How_to_make_a_cross_architecture_chroot)
- Ubuntu 22.04
  - 下载链接：https://drive.google.com/file/d/1mkzLhvtjJup3GbgWKZdwL80PZMMXg7n1/view?usp=drive_link
  - 参考安装文档：https://xyzdims.com/3d-printers/misc-hardware-notes/iot-milk-v-duo-risc-v-esbc-running-linux/#Ubuntu_Disk_Image
- Yocto
  - 源码链接：https://github.com/kinsamanka/meta-milkv
  - 参考安装文档：https://github.com/kinsamanka/meta-milkv/blob/master/README.md
- NixOS
  - 源码链接: https://github.com/NickCao/nixos-riscv
  - 参考安装文档: https://github.com/NickCao/nixos-riscv/README.md

### 硬件开发板信息

- Milk-V Duo (256M, SG2002)

## 测试结果

| 软件分类                       | 软件包名 | 测试结果（测试报告）                               |
| ------------------------------ | -------- | -------------------------------------------------- |
| BuildRoot 镜像启动             | N/A      | [成功][BuildRoot]                                  |
| FreeRTOS 启动                  | N/A      | [成功][FreeRTOS]（已包含在 BuildRoot 镜像内）      |
| Debian 镜像启动                | N/A      | [成功][Debian]                                     |
| Fedora 镜像启动                | N/A      | [成功][Fedora]                                     |
| RT-Thread 镜像构建及启动       | N/A      | [成功][RT-Thread]                                  |
| RT-Thread Smart 镜像构建及启动 | N/A      | [成功][RT-Thread]                                  |
| Zephyr 镜像构建及启动          | N/A      | [成功][Zephyr]                                     |
| Alpine Linux 启动              | N/A      | [成功][Alpine] （可使用社区镜像或手工构建 rootfs） |
| Ubuntu 启动                    | N/A      | [成功][Ubuntu]                                     |
| Yocto  镜像构建及启动          | N/A      | [成功][Yocto]                                      |
| NixOS  镜像构建及启动          | N/A      | [成功][NixOS]                                      |

[BuildRoot]: ./BuildRoot/README_zh.md
[Debian]: ./Debian/README_zh.md
[RT-Thread]: ./RT-Thread/README_zh.md
[RT-Smart]: ./RT-Thread/README_RTSmart_zh.md
[FreeRTOS]: ./FreeRTOS/README_zh.md
[Fedora]: ./Fedora/README_zh.md
[Zephyr]: ./Zephyr/README_zh.md
[Alpine]: ./Alpine/README_zh.md
[Ubuntu]: ./Ubuntu/README_zh.md
[Yocto]: ./Yocto/README_zh.md
[NixOS]: ./NixOS/README_zh.md