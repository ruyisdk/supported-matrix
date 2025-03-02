---
sys: openkylin
sys_ver: 2.0-SP1
sys_var: null

status: good
last_update: 2025-01-15
---

# openKylin 2.0 SP1 VisionFive 2 Test Report

## Test Environment

### Operating System Information

- System Version: openKylin 2.0 SP1
- Download Link: https://www.openkylin.top/downloads/index-en.html
- Reference Installation Document: https://docs.openkylin.top/zh/01_%E5%AE%89%E8%A3%85%E5%8D%87%E7%BA%A7%E6%8C%87%E5%8D%97/%E5%9C%A8riscv%E4%B8%8A%E5%AE%89%E8%A3%85/%E5%9C%A8VisionFive2%E4%B8%8A%E5%AE%89%E8%A3%85openKylin (Chinese)
### Hardware Information

- StarFive VisionFive 2
- A USB Power Adapter
- A USB-A to C or C to C Cable
- A microSD Card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont Wires

## Installation Steps

### Unzipping and Flashing Image to microSD Card

Assume `/dev/sdc` is the storage card.

```bash
xz -d openKylin-Embedded-V2.0-SP1-visionfive2-riscv64.img.xz
sudo dd if=openKylin-Embedded-V2.0-SP1-visionfive2-riscv64.img of=/dev/sda status=progress
```

### Boot Mode Selection

StarFive VisionFive 2 offers multiple boot modes, which can be configured via the onboard dip switch before powering on; the board itself has silkscreen labels.

To boot the openKylin image, select the 1-bit QSPI Nor Flash mode (i.e., `RGPIO_0 = 0`, `RGPIO_1 = 0`). Note that this mode may require updating the firmware within the Flash beforehand. If the boot fails, please refer to the official documentation for firmware upgrade instructions: [Updating SPL and U-Boot](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_QSG/spl_u_boot_0.html)

### Logging into the System

Logging into the system via the serial port.

Default username: `openkylin` 
Default password: `openkylin`

## Expected Results

The system should boot normally and allow login through the graphical interface.

## Actual Results

The system booted successfully and login through the graphical interface was successful.

### Boot Log

```log
openKylin 2.0 openkylin ttyS0

openkylin login: openkylin
密码： 
Welcome to openKylin 2.0 (GNU/Linux 6.6.20 riscv64)

 * Support:        https://openkylin.top

The programs included with the openKylin system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

openKylin comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

You do not have any new mail.
load environment: QT_ACCESSIBILITY=1
load environment: PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
openkylin@openkylin:~$ uname -a
Linux openkylin 6.6.20 #1 SMP Tue May 28 14:19:33 CST 2024 riscv64 riscv64 riscv64 GNU/Linux
openkylin@openkylin:~$ cat /etc/os-release 
NAME="openKylin"
FULL_NAME="openKylin"
VERSION="2.0 (nile)"
VERSION_US="2.0 (nile)"
ID=openkylin
PRETTY_NAME="openKylin 2.0"
VERSION_ID="2.0"
HOME_URL="https://www.openkylin.top/"
VERSION_CODENAME=nile
PRODUCT_FEATURES=3
openkylin@openkylin:~$ cat /proc/cpuinfo 
processor       : 0
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427

processor       : 1
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427

processor       : 2
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427

processor       : 3
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
```

![login](./image.png)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test Successful.
