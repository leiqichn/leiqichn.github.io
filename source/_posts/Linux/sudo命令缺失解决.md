
---
title: sudo命令缺失解决
date: 2025-06-22 18:50:58
modificationDate: 2025 六月 22日 星期日 18:50:58
categories: 
	- Linux
tags: []
sticky: []
published: true
category_bar: true
---

问题：


```
root@799b7657ed3c:/app# sudo apt update
sudo apt install iputils-ping
bash: sudo: command not found
bash: sudo: command not found
```


通过以下步骤在 Ubuntu（或 Debian 系统）中安装 `sudo` 命令：

1. **切换到 root 用户**（如果你还不是 root，提示符应该是 `#`，如果是 `$` 需要切换）：
   ```bash
   su
   ```
   然后输入 root 密码。

2. **更新软件包列表**：
   ```bash
   apt update
   ```

3. **安装 sudo**：
   ```bash
   apt install sudo
   ```

4. **（可选）将你的用户添加到 sudo 用户组**（假设你的用户名是 `yourusername`，请替换为实际用户名）：
   ```bash
   usermod -aG sudo yourusername
   ```
   这样你下次用 `yourusername` 登录时就可以使用 `sudo` 了。

5. **重新登录** 或者执行 `su - yourusername` 让组权限生效。
