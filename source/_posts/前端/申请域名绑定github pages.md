---
title: 申请域名绑定github pages
date: 2024-09-01 10:17:17
modificationDate: 2024 九月 1日 星期日 10:17:17
categories: 
	- 前端
tags: []
sticky: []
hide: false
category_bar: true
---

你是否想让自己的github 个人博客拥有自己的个性域名，而不是很长的github.io 域名呢？快来看看吧！
## 前置需求

1. 在[Cheap Domain Names & Web Hosting Starting at $0.99! | NameSilo](https://www.namesilo.com/)完成了域名的购买
2. 完成了GitHub Pages的设置，有了可用的[http://username.github.io](https://link.zhihu.com/?target=http%3A//username.github.io)库之后，可以访问 Github Pages

## 正文
###  0. 进入我的账户
![](../../imgs/Pasted%20image%2020240901102308.png)

### **1. 无论是什么域名服务商，找到DNS Management页面**

如果是namesilo购买的域名，可以通过以下步骤：
![](../../imgs/Pasted%20image%2020240901102340.png)
点击“domain manager”
![](../../imgs/Pasted%20image%2020240901102510.png)
点击这个蓝色的小球（Manage DNS for this domain）

### **2. 写入 type A 的DNS记录**

- **如果厂商提供了写入模板**，这一步就很简单了。拿namesilo举例，在Manage DNS页面往下滑动可以看到namesilo支持的很多 **DNS Templates**。

![](https://pic4.zhimg.com/80/v2-b84d88c38c06b6081f02cafbd0dac24b_720w.webp)

找到GitHub的template，点击“**Apply Template**”，然后在弹出的窗口里直接点击“**Accept**”，你就会发现4条A记录已经自动写入了。

![](https://pic1.zhimg.com/80/v2-c731fadefaf3d3a2268e6566d6196558_720w.webp)

- **如果厂商不能自动添加**，也可以手动添加，并不麻烦。打开下面的网址，滑动到第五个步骤，可以看到下图

[Managing a custom domain for your GitHub Pages site - GitHub Docs​docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site#configuring-an-apex-domain!

![](https://pica.zhimg.com/80/v2-1a618fec2900e4f23039c153d8ab03da_720w.webp)

上面圈起来的四个地址就是需要等会儿手动输入的。

不同厂商之间的手动添加方法不一样，但只要记住 **type 后填“A”**，**address/points to或其他同义表达后填这四个地址中的一个**，**其他默认**就好了，一共需要添加**四条**，可以复制粘贴。

添加之后会多出四个![](../../imgs/Pasted%20image%2020240901102815.png)### 3. 创建CNAME文件

这一步也有其他方法，比如直接通过上一步类似的方法来添加，只要选择CNAME type，把address写成[http://username.github.io](https://link.zhihu.com/?target=http%3A//username.github.io)，

> 上面的方法 save 之后看到报错不要慌，[让子弹飞](https://zhida.zhihu.com/search?q=%E8%AE%A9%E5%AD%90%E5%BC%B9%E9%A3%9E&zhida_source=entity&is_preview=1)一会儿就好了

![](../../imgs/Pasted%20image%2020240901102714.png)
![](../../imgs/Pasted%20image%2020240901102745.png)

最终有这些配置即可：
![](../../imgs/Pasted%20image%2020240901102848.png)


### github 填写域名地址
在GitHub库的Settings-->Pages-->Custom Domain里填上自己的域名，把Enforce HTTPS打上勾即可。
![](../../imgs/Pasted%20image%2020240901103216.png)
![](../../imgs/Pasted%20image%2020240901103241.png)
### 即刻访问你自己的域名网站吧！
![](../../imgs/Pasted%20image%2020240901103553.png)

参考：
[将自己的域名绑定在GitHub的个人网页库中（以namesilo为例） - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/448781791)