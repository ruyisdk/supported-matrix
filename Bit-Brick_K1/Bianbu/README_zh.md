# Bianbu BIT-BRICK K1 测试报告

## 测试环境

### 系统信息

- 系统版本：v2.1
- 下载链接：https://archive.spacemit.com/image/k1/version/bianbu/v2.1/
- 参考安装文档：https://docs.bit-brick.com/docs/k1/getting-started/preparation

### 硬件信息

- BIT-BRICK K1
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像（sd 卡）


**请务必选择以 `.img.zip` 结尾的压缩包**
下载并解压镜像后，使用 `dd` 将镜像写入 microSD 卡。

```bash
unzip bianbu-24.04-minimal-k1-v2.1-release-20250124140410.img.zip
sudo dd if=/path/to/bianbu-24.04-minimal-k1-v2.1-release-20250124140410.img of=/dev/your-device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名： `root`
默认密码： `bianbu`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

CFT

### 启动信息

```log
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFT
