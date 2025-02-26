---
sys: bianbu
sys_ver: v2.1
sys_var: null

status: cft
last_update: 2025-02-26
---

# Bianbu BIT-BRICK K1 Test Report

## Test Environment

### System Information

- System version: v2.1
- Download Links: https://archive.spacemit.com/image/k1/version/bianbu/v2.1/
- Reference Installation Document: https://docs.bit-brick.com/docs/k1/getting-started/preparation

### Hardware Information

- BIT-BRICK K1
- Power Adapter
- A microSD Card
- A USB to UART Debugger

## Installation Steps

### Flashing the Image (SD Card)

**Please make sure to choose the file ending with `.img.zip`**
After downloading and extracting the image, use `dd` to flash the image to the microSD card.

```bash
unzip bianbu-24.04-minimal-k1-v2.1-release-20250124140410.img.zip
sudo dd if=/path/to/bianbu-24.04-minimal-k1-v2.1-release-20250124140410.img of=/dev/your-device bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

Default Username: `root`
Default Password: `bianbu`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

CFT

### Boot Log


```log
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT
