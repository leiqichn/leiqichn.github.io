---
title: clash在终端设置代理
date: 2023-09-12 23:38:32
modificationDate: 2023 九月 12日 星期二 23:38:32
categories: 
	- 工具
tags: []
sticky: []
hide: false
category_bar: true
---
# 前言

github 提交代码总是失败，还是老老实实使用VPN吧。但是VPN打开了，git终端命令还是不行，原来是要进行终端代理设置。一起来看看吧！
# 开启代理
前置条件：手动开打 clash 等VPN软件


```sh
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
```

对应的网址是在settings- static-Host; 对应port 为General-Prot
![](../../imgs/Pasted%20image%2020230913000142.png)
![](../../imgs/Pasted%20image%2020230913000136.png)
# 取消代理

```sh
unset http_proxy
unset http_proxy
```


# git 里设置开启代理 alias 命令别名
## 新建 .bashrc

```sh
cd ~
vi .bashrc

# 将以下内容复制进去
# .bashrc

# Source global definitions
if [ -f /etc/bash.bashrc ]; then
        . /etc/bash.bashrc
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions
// 别名设置，其他别名设置也是类似
alias proxyon="export http_proxy=http://127.0.0.1:7890;export https_proxy=http://127.0.0.1:7890"
alias proxyoff="unset http_proxy;unset http_proxy"
```

## 测试是否成功
可以在终端直接使用proxyon 打开代理，proxyoff关闭代理。
![](../../imgs/Pasted%20image%2020230912235632.png)
![](../../imgs/Pasted%20image%2020230912235612.png)
可以看到环境变量里边，有了我们设置的环境变量。通过代理设置，我们可以轻松解决github 代码推送的问题，方便生产开发。
![图 push成功](../../imgs/Pasted%20image%2020230913000956.png)