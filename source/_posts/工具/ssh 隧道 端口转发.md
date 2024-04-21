
---
title: ssh 隧道 端口转发
date: 2024-04-21 22:30:08
modificationDate: 2024 四月 21日 星期日 22:32:39
categories: 
	- 工具
tags: []
sticky: []
hide: false
category_bar: true
---

使用SSH端口转发
   如果物理机在远程，你需要使用SSH的端口转发功能来将远程物理机上的容器端口转发到你的PC上。这可以通过使用`-L`参数实现，如下所示：
   ```sh
   ssh -L 本地端口:localhost:13579 用户名@物理机IP
   ```
   其中“本地端口”是你希望在PC上使用的端口号，而“物理机IP”是物理机的IP地址。

例如：
我想直接登录110.43.203.19 上其中一个容器，而其没有放开对应容器的端口，我们就可以将端口映射到本地PC；

```
ssh -L 13579:localhost:13579 root@110.43.203.19 -p 30005 
// 
ssh -p 13579 root@localhost
```

