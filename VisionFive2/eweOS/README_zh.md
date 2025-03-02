# eweOS VisionFive 2 测试报告

## 测试环境

### 操作系统信息

- 系统版本：eweOS
- 下载链接：https://github.com/panglars/eweos-vf2-mainline
- 参考安装文档：https://github.com/panglars/eweos-vf2-mainline/blob/main/README.md

### 硬件信息

- StarFive VisionFive 2
- USB 电源适配器一个
- USB-A to C 或 C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 构建镜像

可能需要在 build.sh 中更改 `CROSS_COMPILE` 前缀,构建出的镜像为 `ewe-vf2.img`

``` bash
chmod +x ./build.sh
sudo ./build.sh
```

### 刷写镜像到 microSD 卡

```bash
sudo dd if=ewe-vf2.img of=/dev/<your-device> bs=1M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名：`ewe`
默认密码：`ewe`
Root 帐户密码:`ewe`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log

eweOS 6.13.4 (/dev/ttyS0)


eweos-diskimage login: ewe
Password: 

Welcome to eweOS!

 * Mainpage: https://os.ewe.moe
 * Wiki:     https://os-wiki.ewe.moe
 * Packages: https://os.ewe.moe/pkglist

[ewe@eweos-diskimage ~]$ uname -a
Linux eweos-diskimage 6.13.4 #1 SMP Sun Feb 23 16:30:35 UTC 2025 riscv64 GNU/Linux
[ewe@eweos-diskimage ~]$ cat /etc/os-release 
NAME="eweOS"
ID=ewe
PRETTY_NAME="eweOS"
BUILD_ID=rolling
ANSI_COLOR="0;36"
HOME_URL="https://os.ewe.moe"
SUPPORT_URL="https://os.ewe.moe"
BUG_REPORT_URL="https://os.ewe.moe"
LOGO=eweos-logo
[ewe@eweos-diskimage ~]$ cat /proc/cpuinfo 
processor       : 0
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 1
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 2
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 3
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

[ewe@eweos-diskimage ~]$ 
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
