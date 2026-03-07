
---
title: 贾维斯AI助手OpenClaw(clawdBot moltBot) 安装
date: 2026-02-01 21:35:52
modificationDate: 2026 二月 1日 星期日 21:37:27
categories: 
	- 个人贾维斯助手ClawdBot(moltBot
tags: []
sticky: []
published: true
category_bar: true
---

#  安装Nodejs
下载地址：[https://nodejs.org/zh-cn/download](https://cloud.tencent.com/developer/tools/blog-entry?target=https%3A%2F%2Fnodejs.org%2Fzh-cn%2Fdownload&objectId=2626160&objectType=1&contentType=undefined)
![](../../../imgs/Pasted%20image%2020260201214118.png)
# 安装

管理员运行powershell
![](../../../imgs/Pasted%20image%2020260201214201.png)

 在终端中运行执行命令

```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser 
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

如果有对应VPN，可以在终端打开代理，因为openclaw 是国外软件
我这里使用的v2ray




```
set http_proxy=http://127.0.0.1:7897
set https_proxy=http://127.0.0.1:7897
set all_proxy=socks5://127.0.0.1:7897

set HTTP_PROXY=http://127.0.0.1:7897
set HTTPS_PROXY=http://127.0.0.1:7897
set ALL_PROXY=socks5://127.0.0.1:7897

```
#### 一键安装

复制命令到窗口，并执行：

```powershell
iwr -useb https://openclaw.ai/install.ps1 | iex
```

![](../../../imgs/Pasted%20image%2020260201213653.png)显示安装成功：
![](../../../imgs/Pasted%20image%2020260201214654.png)
![](../../../imgs/Pasted%20image%2020260201215226.png)![](../../../imgs/Pasted%20image%2020260201215324.png)

# 更新openclaw

```
npm i openclaw@latest
```


# 进入终端

```
openclaw tui
```


# Windows 打开网页端

```
openclaw onboard
```


# WSL 打开映射端口

```
openclaw gateway run --port 18789

http://localhost:18789
```
