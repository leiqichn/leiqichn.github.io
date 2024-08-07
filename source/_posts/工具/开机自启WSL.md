---
title: 开机自启WSL
date: 2024-08-07 22:09:47
modificationDate: 2024 八月 7日 星期三 22:09:47
categories: 
	- 工具
tags: []
sticky: []
hide: false
category_bar: true
---
在C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp 目录下，新建vbs文件

![](../../imgs/Pasted%20image%2020240807221008.png)


文件内容拷贝下边内容，注意bash.exe 要替换为你电脑中的地址
```
Set ws = WScript.CreateObject("WScript.Shell")
cmd = "C:\Windows\System32\bash.exe -c ""bash /init.sh"""
'运行命令不显示cmd窗口
ws.Run cmd, 0, false
Set ws = Nothing
WScript.quit
```
