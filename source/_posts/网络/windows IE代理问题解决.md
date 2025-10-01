---
title: windows IE代理问题解决
date: 2024-04-05 13:11:29
modificationDate: 2024 April 5th Friday 13:11:29
categories: 
	- 网络
tags: []
sticky: []
hide: false
category_bar: true
---

CMD **检查系统代理配置**：
    
    - 通过命令提示符运行`netsh winhttp show proxy`来查看当前的系统代理设置。
    - 如果需要更改系统代理，可以使用`netsh winhttp set proxy`命令进行设置。