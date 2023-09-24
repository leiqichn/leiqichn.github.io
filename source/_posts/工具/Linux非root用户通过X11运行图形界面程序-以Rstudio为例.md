---
title: Linux非root用户通过X11运行图形界面程序-以Rstudio为例
date: 2023-09-24 20:36:53
modificationDate: 2023 九月 24日 星期日 20:36:53
categories: 
	- 工具
tags: []
sticky: []
hide: false
category_bar: true
---

# 问题
由于使用单位或者学校的服务器，我们一般都没有root权限，导致一些Server版本的软件不能安装（例如数据分析领域的Rstudio-Server，需要root权限，新增端口给Rstudio-Server的web服务）。
但大家有没有发现，我们自己在本地的PC上安装桌面版本的Rstudio是并不要管理员权限的，是因为我们不需要开放端口，Rstudio直接在显示在图形界面上了。
那么理论上，我们可以在服务器上，通过模拟服务器的图形界面来直接运行桌面版的Rstudio。而这个模拟服务器的图形界面就可以使用X11！

> **X11**是一个用于在Unix和类Unix系统上实现图形用户界面的标准协议和窗口系统。它通过分布式性质允许在远程服务器上运行图形应用程序，并将图形数据传输到本地计算机上显示，从而实现了图形界面的远程访问和显示。
# 操作步骤
1. 使用mobaxTerm 登录对应服务器，需要显示X11 打开![](../../imgs/Pasted%20image%2020230924203748.png)
2. 创建虚拟环境
```sh
# 创建虚拟环境
 conda create -n rstudio
# 安装Ｒ
conda activate rstudio # 进入创建好的环境变量
conda install r-base
# 安装Rstudio
conda install rstudio-desktop
```

# 成功
 经过漫长的等待，直接运行rstudio 就会进入x11转发的图形界面
 ![](../../imgs/Pasted%20image%2020230924205521.png)
**画个图试试，顺利出图！开始愉快的coding吧！**
![](../../imgs/Pasted%20image%2020230924205559.png)

**已知问题：** 操作延迟较高，没有本地反应快，但是还可以接受，大家可以试试。

# 总结
我们可以通过**X11**来在服务器上运行图形化的程序，这个图形化的程序一般不需要很高的权限，不涉及外部端口新增。因此我们可以在服务器上运行很多图形化程序，例如Rstudio。甚至是我们的Pycharm、Goland、CLion 等Jetbrains的全家桶。大家快来试试吧！