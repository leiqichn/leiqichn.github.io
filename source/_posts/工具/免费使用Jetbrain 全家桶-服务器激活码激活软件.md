---
title: 免费使用Jetbrain 全家桶-服务器激活码激活软件
date: 2023-12-30 23:08:29
modificationDate: 2023 十二月 30日 星期六 23:15:53
categories: 
	- 工具
tags: []
sticky: []
hide: false
category_bar: true
---

众所周知，PyCharm和IDEA Goland CLion 都是Jetbrain 公司的产品,非常适合开发项目.但是这个软件确是收费的,而且还不低. 本文就是介绍一种方法可以免费使用的方法,如果大家有余力的,还是希望购买正版产品.

Jetbrain 是针对公司这种大客户是有对应的License Server的，这样方便很多用户使用。而我们可以通过输入这些License 从而免费使用。
- [https://search.censys.io/](https://search.censys.io/)     搜索：`services.http.response.headers.location: account.jetbrains.com/fls-auth`
- [https://www.shodan.io](https://www.shodan.io/)  搜索：
`Location: https://account.jetbrains.com/fls-auth`
- [https://fofa.info/](https://fofa.info/)     搜索：`fls-auth`

随便点进去一个搜索结果，找到状态为302的网址和端口，复制到对应的JetBrains 软件的License Server里. 我下边使用的是[https://search.censys.io/](https://search.censys.io/) 网站, 搜索 

```
services.http.response.headers.location: account.jetbrains.com/fls-auth
```


![](../../imgs/Pasted%20image%2020231230231034.png)
例如上边就是 http://111.231.22.61:1024

![](../../imgs/Pasted%20image%2020231230231326.png)

# 激活成功
激活成功，请开始愉快的编码吧！
![](../../imgs/Pasted%20image%2020231230231349.png)