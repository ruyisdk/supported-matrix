---
sys: freertos
sys_ver: null
sys_var: null

status: basic
last_update: 2025-02-24
---

# LiteOS CH32V307 Test Report

## Test Environment

The test environment is Ubuntu 22.04.5 LTS

### Operating System Information

- Source Code Link: [https://github.com/Community-PIO-CH32V/ch32-pio-projects](https://github.com/Community-PIO-CH32V/ch32-pio-projects)
- Reference Installation Document:
    - PlatformIO Core: [https://docs.platformio.org/en/latest/core/installation/index.html](https://docs.platformio.org/en/latest/core/installation/index.html)
    - PlatformIO CH32V: [https://pio-ch32v.readthedocs.io/en/latest/installation.html](https://pio-ch32v.readthedocs.io/en/latest/installation.html)
    - LiteOS：[https://github.com/LiteOS/LiteOS](https://github.com/LiteOS/LiteOS)

### Hardware Information

- CH32V307V-EVT-R1-1v1
- A USB to UART Debugger (not required, available on official EVT development board)
- A WCH-Link or WCH-LinkE (not required, available on official EVT development board)

## Installation Steps

### Install PlatformIO Core

Install using an installation script (PlatformIO installed with apt lacks some features such as pkg)

Before installing PlatformIO, install Python and the Python virtual environment (venv)

```bash
curl -fsSL -o get-platformio.py https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py
python3 get-platformio.py
```

Try wget if you have network problems

```bash
wget -O get-platformio.py https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py
python3 get-platformio.py
```

### PlatformIO Environment Configuration

Install CH32V development environment:
```bash
pio pkg install -g -p https://github.com/Community-PIO-CH32V/platform-ch32v.git
```

Add udev rules and apply (may need to change GROUP according to the distribution):
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

Add user groups:
- For Debian-based systems:
```bash
sudo usermod -a -G dialout $USER
sudo usermod -a -G plugdev $USER
```
- For Arch-based systems:
```bash
sudo usermod -a -G uucp $USER
sudo usermod -a -G lock $USER
```

### Prepare Project Repository

Clone the relevant repositories:
```bash
git clone https://github.com/Community-PIO-CH32V/platform-ch32v.git
```

### Code Compilation

Compile the code using pio:
```bash
cd platform-ch32v/examples/hello-world-harmony-liteos
pio run
```

The output when the compilation is successful

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

### Flashing Image

After confirming the connection of WCH-Link(E) to the SWD debug port, manually specify the development board using pio and burn the image:
```bash
pio run -e your_board --target upload
```

If the official EVT development board is used, you can directly connect the USB of the onboard WCH-Link and use pio for image burning

```bash
pio run -e ch32v307_evt --target upload
```

The output information when the image is successfully burned

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


#### Common Issues

- **Error: error writing to flash at address 0x00000000 at offset 0x00000000**
    - This is due to the low firmware version of WCH-Link. (See [important-notices](https://github.com/Community-PIO-CH32V/platform-ch32v?tab=readme-ov-file#important-notices)).
    - Please use [WCH-Link Utility](https://www.wch.cn/downloads/WCH-LinkUtility_ZIP.html) to connect once with W2 and CH-Link to update automatically. **This tool currently only has a Windows version.**
- **Error: Read-Protect Status Currently Enabled**
    - This is caused by the write protection enabled on the chip. On Windows, we can use [WCH-Link Utility](https://www.wch.cn/downloads/WCH-LinkUtility_ZIP.html) to remove the protection, and on Linux, OpenOCD can be used:
    ```bash
    cd ~/.platformio/packages/tool-openocd-riscv-wch/bin
    ./openocd -f wch-riscv.cfg -c init -c halt -c "flash protect wch_riscv 0 last  off " -c exit
    cd -
    ```
- Error: Can not install PlatformIO Core due to a missed `venv` module in your Python installation.
    - Missing Python-venv package,  install venv of the corresponding python version (3.10 as example) :
    ```bash
    sudo apt-get install python3.10-venv
    ```

### Logging into the System

Connect to the development board via serial port.

## Expected Results

The system starts normally, and information can be viewed via the onboard serial port.

## Actual Results

The system starts normally, and information can be viewed via the onboard serial port.

### Boot Log

```log
SystemClk:96000000
ChipID: 30700528
entering kernel init...Entering schedulertaskSampleEntry1 running,task1 SP:20002084taskSampleEntry1 running,task1 SP:20002084taskSampleEntry1 running,task1 SP:20002084taskSampleEntry1 running,task1 SP:20002084taskSampleEntry2 running,task2 SP:2000258ctaskSampleEntry1 running,task1 SP:20002084taskSampleEntry1 running,task1 SP:20002084taskSampleEntry1 running,task1 SP:20002084taskSampleEntry1 running,task1 SP:20002084taskSampleEntry1 running,task1 SP:20002084taskSampleEntry2 running,task2 SP:2000258ctaskSampleEntry1 running,task1 SP:20002084taskSampleEntry1 running,task1 SP:20002084taskSampleEntry1 running,task1 SP:20002084taskSampleEntry1 running,task1 SP:20002084taskSampleEntry1 running,task1 SP:20002084taskSampleEntry2 running,task2
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
