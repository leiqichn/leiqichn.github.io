---
title: comet 生成临时文件导致磁盘满
date: 2025-05-01 21:50:34
modificationDate: 2025 五月 1日 星期四 21:51:05
categories: 
	- 比赛
tags: []
sticky: []
published: true
category_bar: true
---

---

### **解决方案**

出现 `OSError: [Errno 28] No space left on device` 错误的原因是系统磁盘空间不足，尤其是在临时目录（如 `/tmp`）中。以下是分步解决方案：

---

#### **1. 检查磁盘空间**
在终端运行以下命令，查看磁盘使用情况：
```bash
df -h
```

#### **2. 清理临时文件**
删除临时目录中的旧文件（确保无重要进程依赖这些文件）：
```bash
sudo rm -rf /tmp/*
```

---

#### **3. 查找并删除大文件**
使用以下命令定位大文件：
```bash
# 查看根目录下各文件夹的大小
sudo du -sh /* | sort -hr

# 查找当前目录下大于 1GB 的文件
find / -type f -size +1G -exec ls -lh {} \;
```
删除不再需要的大文件（如旧日志、缓存等）。

---

#### **4. 清理系统缓存和日志**
```bash
# 清理 APT 缓存（适用于 Ubuntu/Debian）
sudo apt-get clean

# 清理旧版 Linux 内核（谨慎操作）
sudo apt-get autoremove --purge

# 清理系统日志（保留最近7天）
sudo journalctl --vacuum-time=7d
```

---

#### **5. 更改临时目录路径**
如果 `/tmp` 所在分区空间不足，可以将临时目录指向其他分区：

**方法一：在代码中设置临时目录**
```python
import tempfile
tempfile.tempdir = "/path/to/your/large/disk/tmp"  # 替换为有足够空间的路径
```

**方法二：通过环境变量设置**
在运行脚本前设置：
```bash
export TMPDIR=/path/to/your/large/disk/tmp
```

---

#### **6. 调整 Comet.ml 的存储路径**
在初始化 `Experiment` 时指定日志和临时文件目录：
```python
experiment = Experiment(
    "H62QCY6dW6Vg9lLl27jZn4C2O",
    project_name="IDRsPredictor-transformer",
    log_code=True,
    log_dir="/path/to/large/disk/comet_logs"  # 指定存储路径
)
```


参考：chatGPT