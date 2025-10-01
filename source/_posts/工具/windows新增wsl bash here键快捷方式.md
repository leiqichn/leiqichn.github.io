---
title: windows新增wsl bash here键快捷方式
date: 2024-01-01 18:23:10
modificationDate: 2024 一月 1日 星期一 18:37:41
categories: 
	- 工具
tags: []
sticky: []
hide: false
category_bar: true
---

win + R 输入regedit
![](../../imgs/Pasted%20image%2020240101182355.png)
输入到 计算机\HKEY_CLASSES_ROOT\Directory\Background\shell

# 新建wsl_bash_here目录, 设置如下默认值
![](../../imgs/Pasted%20image%2020240101183252.png)
# 新建command新建项，输入wsl.exe 的地址

![](../../imgs/Pasted%20image%2020240101183246.png)
# 成功
可以看到右侧是有wsl bash here的选项的
![](../../imgs/Pasted%20image%2020240101183634.png)
**在当面目录打开wsl 成功**
![](../../imgs/Pasted%20image%2020240101183645.png)
原理和添加git bash here 类似, 参考:
[手动添加Git Bash Here到右键菜单（超详细）_gitbash添加到右键-CSDN博客](https://blog.csdn.net/Passerby_Wang/article/details/120881670)
