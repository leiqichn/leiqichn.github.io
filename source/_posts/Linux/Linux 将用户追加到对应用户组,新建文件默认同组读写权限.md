---
title: Linux 将用户追加到对应用户组
date: 2023-09-17 14:02:54
modificationDate: 2023 九月 17日 星期日 14:02:54
categories: 
	- Linux
tags: []
sticky: []
hide: false
category_bar: true
---
# 前言
本文目的是为了将多个用户设置同组用户，并且同组内用户**新建文件的默认权限**是同组内用户可读写。
# 解决方案
1. 将test 添加到GroupA

```sh
usermod -a -G GroupName UserName
# 例如将test 追加到GroupA
usermod -a -G GroupA test

```

2. 修改新建文件的默认权限

在.bashrc 里添加

```sh
umask 003 // 文件夹具体权限 则为 777 - 003 = 774 （rwxrwxr--） 文件默认权限为 666 - 003 = 663(rw-rw-r--)
```

```sh
source ~/.bashrc
```
