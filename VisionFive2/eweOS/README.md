---
sys: eweOS
sys_ver: null
sys_var: null

status: basic
last_update: 2025-03-02
---

# eweOS VisionFive 2 Test Report

## Test Environment

### Operating System Information

- System Version: eweOS
- Download Link: https://github.com/panglars/eweos-vf2-mainline
- Reference Installation Document: https://github.com/panglars/eweos-vf2-mainline/blob/main/README.md


### Hardware Information

- StarFive VisionFive 2
- A USB Power Adapter
- A USB-A to C or C to C Cable
- A microSD Card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont Wires

## Installation Steps

### Build Image 

You maybe change `CROSS_COMPILE` prefix in build.sh, the resulting image is `ewe-vf2.img`.

``` bash
chmod +x ./build.sh
sudo ./build.sh
```

### Flashing Image to microSD Card

```bash
sudo dd if=ewe-vf2.img of=/dev/<your-device> bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

Default username: `ewe` 
Default password: `ewe`
Root password: `ewe`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

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

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test Successful.
