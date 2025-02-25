# LiteOS CH32V307 测试报告

## 测试环境

测试环境为Ubuntu 22.04.5 LTS

### 操作系统信息
- 源码链接：https://github.com/Community-PIO-CH32V/ch32-pio-projects
- 参考文档：
    - PlatformIO Core：https://docs.platformio.org/en/latest/core/installation/index.html
    - PlatformIO CH32V：https://pio-ch32v.readthedocs.io/en/latest/installation.html
    - LiteOS：[https://github.com/LiteOS/LiteOS](https://github.com/LiteOS/LiteOS)

### 硬件信息

- CH32V307V-EVT-R1-1v1
- USB to UART 调试器一个（非必须，官方EVT开发板自带）
- WCH-Link或WCH-LinkE 一个（非必须，官方EVT开发板自带）

## 安装步骤

### 安装 PlatformIO Core

使用安装脚本安装（使用apt安装的PlatformIO缺少如pkg等的部分功能）

安装PlatformIO前，需要先安装Python和Python虚拟环境venv

```bash
curl -fsSL -o get-platformio.py https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py
python3 get-platformio.py
```

如果出现网络问题可以尝试wget

```bash
wget -O get-platformio.py https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py
python3 get-platformio.py
```

### 配置 PlatformIO 环境

安装 ch32v 开发环境：

```bash
pio pkg install -g -p https://github.com/Community-PIO-CH32V/platform-ch32v.git
```

添加 udev 规则并应用（根据发行版不同可能需要更改 GROUP）：

```bash
curl -fsSL https://raw.githubusercontent.com/platformio/platformio-core/develop/platformio/assets/system/99-platformio-udev.rules | sudo tee /etc/udev/rules.d/99-platformio-udev.rules
cat << EOF | sudo tee -a /etc/udev/rules.d/99-platformio-udev.rules
SUBSYSTEM=="usb", ATTR{idVendor}="1a86", ATTR{idProduct}=="8010", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}="4348", ATTR{idProduct}=="55e0", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}="1a86", ATTR{idProduct}=="8012", GROUP="plugdev"
EOF
sudo udevadm control --reload-rules
sudo udevadm trigger
```

添加用户组：
- Debian 系：
```bash
sudo usermod -a -G dialout $USER
sudo usermod -a -G plugdev $USER
```
- Arch 系：
```bash
sudo usermod -a -G uucp $USER
sudo usermod -a -G lock $USER
```

### 准备工程仓库

clone 相关仓库：
```bash
git clone https://github.com/Community-PIO-CH32V/platform-ch32v.git
```

### 编译代码

使用 pio 编译代码：
```bash
cd platform-ch32v/examples/hello-world-harmony-liteos
pio run
```
编译成功时的输出信息
```log
Building .pio/build/genericCH32L103C8T6/firmware.bin
========================= [SUCCESS] Took 1.76 seconds =========================

Environment          Status    Duration
-------------------  --------  ------------
genericCH32V103C8T6  SUCCESS   00:00:01.559
genericCH32V203K8T6  SUCCESS   00:00:01.630
genericCH32V208CBU6  SUCCESS   00:00:01.462
ch32v307_evt         SUCCESS   00:00:01.639
genericCH32V303CBT6  SUCCESS   00:00:01.632
genericCH32V305FBP6  SUCCESS   00:00:01.666
genericCH32V307WCU6  SUCCESS   00:00:01.551
genericCH32X035C8T6  SUCCESS   00:00:01.786
genericCH32L103C8T6  SUCCESS   00:00:01.758
========================= 9 succeeded in 00:00:14.682 =========================
```

### 烧写镜像

确认 WCH-Link(E) 连接到 SWD 调试口后，使用 pio 手动指定开发板后烧录：
```bash
pio run -e your_board --target upload
```
若使用官方EVT开发板，则可以直接连接板载WCH-Link的USB，使用pio进行镜像烧录
```bash
pio run -e ch32v307_evt --target upload
```
镜像烧录成功时的输出信息
```log
[wch_riscv.cpu.0] Target successfully examined.
** Programming Started **
** Programming Finished **
** Verify Started **
** Verified OK **
** Resetting Target **
shutdown command invoked
========================= [SUCCESS] Took 4.31 seconds =========================

Environment    Status    Duration
-------------  --------  ------------
ch32v307_evt   SUCCESS   00:00:04.306
========================= 1 succeeded in 00:00:04.306 =========================

```

#### 常见问题

- Error: error writing to flash at address 0x00000000 at offset 0x00000000
    - 这是由于 WCH-Link 固件版本过低造成的。（见[important-notices](https://github.com/Community-PIO-CH32V/platform-ch32v?tab=readme-ov-file#important-notices)）。
    - 请使用[WCH-Link 工具链](https://www.wch.cn/downloads/WCH-LinkUtility_ZIP.html)连接一次 W2 有 CH-Link 即可自动更新。**该工具目前仅有 Windows 版本**
- Error: Read-Protect Status Currently Enabled
    - 这是由于芯片开启了写保护导致的。Winodws 下我们可以使用 [WCH-Link 工具链](https://www.wch.cn/downloads/WCH-LinkUtility_ZIP.html)解保护，Linux 下可以使用 OpenOCD 解保护：
    ```bash
    cd ~/.platformio/packages/tool-openocd-riscv-wch/bin
    ./openocd -f wch-riscv.cfg -c init -c halt -c "flash protect wch_riscv 0 last  off " -c exit
    cd - # 回到工作目录
    ```
- Error: Can not install PlatformIO Core due to a missed `venv` module in your Python installation.
    - 缺少python-venj软件包，安装对应python版本的venv（以3.10为例）：
    ```bash
    sudo apt-get install python3.10-venv
    ```


### 登录系统

使用串口调试软件，通过串口连接开发板（默认波特率115200）。若为官方EVT开发板则同样使用板载WCH-Link的USB，兼做默认输出串口。

## 预期结果

系统正常启动，能够通过板载串口查看信息。

## 实际结果

系统正常启动，能够通过板载串口查看信息。

### 启动信息

```log
SystemClk:96000000
ChipID: 30700528
entering kernel init...Entering schedulertaskSampleEntry1 running,task1 SP:20002084taskSampleEntry1 running,task1 SP:20002084taskSampleEntry1 running,task1 SP:20002084taskSampleEntry1 running,task1 SP:20002084taskSampleEntry2 running,task2 SP:2000258ctaskSampleEntry1 running,task1 SP:20002084taskSampleEntry1 running,task1 SP:20002084taskSampleEntry1 running,task1 SP:20002084taskSampleEntry1 running,task1 SP:20002084taskSampleEntry1 running,task1 SP:20002084taskSampleEntry2 running,task2 SP:2000258ctaskSampleEntry1 running,task1 SP:20002084taskSampleEntry1 running,task1 SP:20002084taskSampleEntry1 running,task1 SP:20002084taskSampleEntry1 running,task1 SP:20002084taskSampleEntry1 running,task1 SP:20002084taskSampleEntry2 running,task2
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功