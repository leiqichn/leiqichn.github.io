---
title: Linux 命令 将前台任务挂到后台运行
date: 2023-03-19
categories: 
	- Linux
tags: [linux命令]
sticky: []
category_bar: true
---

# 背景
   很多任务有时不能直接进行挂后台任务（比如需要输入密码的scp 命令），或者一时大意忘了直接挂后台。那么还有一个解救方式。使用`bg`  挂后台的命令。
   
**第一步：ctrl + z**

**第二步：jobs  查看任务id

**第三步： bg %任务id**

![](source/assets/img/微信图片_20230319125819.png)