---
title: 主机密钥变更客户端无法ssh连接
date: 2025-06-22 18:20:15
modificationDate: 2025 六月 22日 星期日 18:20:15
categories: 
	- Linux
tags: []
sticky: []
published: true
category_bar: true
---

 SSH 报告了“**REMOTE HOST IDENTIFICATION HAS CHANGED!**”这个错误。具体内容如下：

```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
...
Offending ECDSA key in C:\\Users\\QiLei/.ssh/known_hosts:9
Host key for [xxxxxx]:20032 has changed and you have requested strict checking.
Host key verification failed.
```

### 问题原因

这是 SSH 的安全机制。它检测到你之前连接的远程主机（10.152.255.101:20032）的主机密钥和现在的不一样。可能的原因有：

- 远程主机重装过系统或 SSH 服务，主机密钥发生了变化。
- 你连接的其实不是同一台机器（IP 被复用）。
- 有人试图进行中间人攻击（一般内网环境下很少见）。

### 解决办法

**如果你确认远程主机的变更是正常的（比如重装过系统或 SSH 服务），可以按照如下步骤操作：**

1. 打开命令行，输入以下命令，删除有问题的 known_hosts 记录（第9行）：

   ```bash
   ssh-keygen -R [10.152.255.101]:20032
   ```

   或者手动编辑 `C:\Users\QiLei\.ssh\known_hosts` 文件，删除第9行。

2. 重新用 VS Code Remote-SSH 连接远程主机，系统会提示你接受新的主机密钥，输入 `yes` 即可。

---
