# Lichee Pi 4A

## 测试环境

### 操作系统信息

- openEuler RISC-V 24.03 Preview
    - 下载链接：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/testing/2403LTS-test/v1/lpi4a/
    - 参考安装文档：https://docs.openeuler.org/zh/docs/24.03_LTS/docs/Installation/RISC-V-LicheePi4A.html
- RevyOS 20240110
    - 下载链接：https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/
    - 参考安装文档：https://docs.revyos.dev/
- openKylin 2.0 SP1
    - 下载链接：https://www.openkylin.top/downloads/index-cn.html
    - 参考安装文档：https://docs.openkylin.top/zh/01_%E5%AE%89%E8%A3%85%E5%8D%87%E7%BA%A7%E6%8C%87%E5%8D%97/%E5%9C%A8riscv%E4%B8%8A%E5%AE%89%E8%A3%85/%E5%9C%A8LicheePi4A%E4%B8%8A%E5%AE%89%E8%A3%85openKylin
- Fedora 41
  - 下载链接：https://images.fedoravforce.org/LicheePi%204A
  - 参考安装文档：https://fedoraproject.org/wiki/Architectures/RISC-V/T-Head
- Armbian (Ubuntu 20.04 LTS)
    - 下载链接：https://github.com/chainsx/armbian-riscv-build/tree/main
    - 参考安装文档：https://github.com/chainsx/armbian-riscv-build/blob/main/doc/licheepi-4a-install-guide_ch.md
- Arch Linux
    - 下载链接：[https://mirror.iscas.ac.cn/archriscv/images/](https://mirror.iscas.ac.cn/archriscv/images/)
    - 参考安装文档：[ArchWiki](https://wiki.archlinux.org/title/General_recommendations)
- Deepin 25-beige-preview 20250122
    - 下载链接：https://deepin-community.github.io/sig-deepin-ports/images/riscv/download
    - 参考安装文档：https://cdimage.deepin.com/RISC-V/preview-20240517-riscv64/README.md
    
### 硬件开发板信息

- Lichee Pi 4A 16GB RAM + 128GB eMMC
- Lichee Pi 4A 8GB RAM + 32GB eMMC

## 测试结果

| 软件分类                  | 软件包名 | 测试结果（测试报告）          |
| ------------------------- | -------- | ----------------------------- |
| openEuler/Base 镜像启动   | N/A      | [成功][oERV]                  |
| openEuler/Xfce 镜像启动   | Xfce     | [成功][oERV]                  |
| RevyOS 桌面镜像启动       | N/A      | [成功][RevyOS]（官方支持）    |
| Fedora 桌面镜像启动       | N/A      | [成功][Fedora]（官方支持）    |
| openKylin 桌面镜像启动    | N/A      | [成功][openKylin]（官方支持） |
| Armbian (Ubuntu) 镜像启动 | N/A      | [成功][Armbian]               |
| OpenWRT 镜像启动          | N/A      | [成功][OpenWRT]               |
| Arch Linux 桌面镜像启动   | N/A      | [成功][ArchLinux]             |
| Deepin 桌面镜像启动       | N/A      | [成功][Deepin]                |

[oERV]: ./openEuler/README_zh.md
[RevyOS]: ./RevyOS/README_zh.md
[Fedora]: ./Fedora/README_zh.md
[Armbian]: ./Armbian/README_zh.md
[openKylin]: ./openKylin/README_zh.md
[OpenWRT]: ./OpenWRT/README_zh.md
[ArchLinux]: ./ArchLinux/README_zh.md
[Deepin]: ./Deepin/README_zh.md
