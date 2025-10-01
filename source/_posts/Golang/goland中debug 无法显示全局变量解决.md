---
title: goland中debug 无法显示全局变量解决
date: 2024-05-08 00:22:44
modificationDate: 2024 五月 8日 星期三 00:22:44
categories: 
	- Golang
tags: []
sticky: []
hide: false
category_bar: true
---

![](../../imgs/Pasted%20image%2020240508002347.png)实际只会有局部变量，没有全局变量test

![](../../imgs/Pasted%20image%2020240508002425.png)

解决方法：

右键  选择+ New Watch ； 或者 按按键 Insert 

添加变量 test 即可

![](../../imgs/Pasted%20image%2020240508002502.png)![](../../imgs/Pasted%20image%2020240508002708.png)
# 添加成功
![](../../imgs/Pasted%20image%2020240508002737.png)
之后每次单步执行都会显示变量结果：
![](../../imgs/Pasted%20image%2020240508002814.png)