---
title: JetBrians 全家桶设置文件header
date: 2023-10-05 16:41:46
modificationDate: 2023 十月 5日 星期四 16:41:46
categories: 
	- 工具
tags: []
sticky: []
hide: false
category_bar: true
---

# 前言
我们在写代码的时候一般会在文件的头部添加header，包括copyright 时间，和作者和描述等信息。接下来我们就来看看怎么添加。

先看下效果图
![](../../imgs/Pasted%20image%2020231005164404.png)

# 操作步骤

## 1. file- settings
![](../../imgs/Pasted%20image%2020231005164508.png)

# 找到Copyright - CopyrightProfiles
点击+ 号，新建一个name 为“copyRight” 的profile

![](../../imgs/Pasted%20image%2020231005164618.png)

profile 的内容粘贴下面的问文本, 替换自己的名字

```
Copyright (c) $originalComment.match("Copyright \(c\) (\d+)", 1, "-", "$today.year")$today.year YOUR NAME. All rights reserved.  
Author: YOUR NAME  
Description:  
Date: $today
```
# 点击Copyright 添加刚才的profile
![](../../imgs/Pasted%20image%2020231005165129.png)
## 点击应用即可 右键-generate-Copyright 插入
![](../../imgs/Pasted%20image%2020231005164944.png)

![](../../imgs/Pasted%20image%2020231005165025.png)