---
title: git 设置免密配置-全局免密-单仓库免密-SSH免密
date: 2024-01-01 14:56:28
modificationDate: 2024 一月 1日 星期一 14:56:33
categories: 
	- git
tags: []
sticky: []
hide: false
category_bar: true
---
# 介绍之前
我们要首先知道一个简单的概念:
https通过**记住账号密码免登**，ssh通过**校验生成的密钥免登**。 通常都用ssh校验。

查看通信方式

在项目目录中运行命令：

```text
git remote -v
```

如果出现提示是：

```bash
origin  https://gitee.com/xxx/xxx.git (fetch)
origin  https://gitee.com/xxx/xxx.git (push)
```

则证明是https 通信，这样每次都会提示输入用户名和密码，如果我们还是使用https则看下文，全局https免密 和单个仓库免密
如果我们git远端配置了ssh 配置; 我们将其修改为ssh的地址
![](../../imgs/Pasted%20image%2020240101151457.png)

# 一、https 方式及免密码配置
### 0. 项目中 git 基本配置

全局用户名密码配置

```text
git config --global user.name "xxx"
git config --global user.email "lei_qi@outlook.com"
```

项目初始化，生成 .git 目录，配置远程项目地址(前提已经在网页上新建了仓库)，完成首次提交。

```text
# 初始化仓库 适用于新库,如果你之前已经有文件并且使用git管理过,请勿使用该命令
git init
# 关联远程仓库
git remote add origin https://gitee.com/xxx/xxx.git
git add -A
git commit -m "初始化"
git push -u origin master
```

需要输入用户名，再输入密码，才能完成提交。以后每次都要输入用户名和密码。

这种方式如果要以后提交时免密码，只能将用户名和密码明文保存在本地，由 git 保管。因为本地没有加密，这种方式是不太安全的。
###  1.全局免密码配置

配置存储模式

```text
git config --global credential.helper store
```

执行之后会在用户主目录下的.gitconfig文件中多加 helper = store

Linux 下查看：

```text
 vim ~/.gitconfig
```

windows10 下当前用户路径：`%USERPROFILE%`
内容如下：

```text
[user]
        name = lenovo
        email = xxxx@outlook.com
[credential]
        helper = store
```

然后在项目目录，执行git pull/git push命令，会提示输入**账号密码**。这次输入账号密码之后，就会**记住**账号密码，并且会在当前用户根目录下生成一个.git-credentials文件，下一次就不用再输入账号密码了。
![](../../imgs/Pasted%20image%2020240101145902.png)
### 2、单项目免密码配置

编辑项目目录中.git 文件夹下的配置文件 config，修改其中 url 项：

```text
[remote "origin"]
url = https://gitee.com/xxx/xxx.git
```

修改为：

```text
[remote "origin"]   
url = https://yourusername:password@gitee.com/xxx/xxxx.git
```

也就是在 `https://` 之后，增加 `用户名:密码@`
# 二. SSH免密登录
如果之前是https 关联的,现在想使用ssh 方式关联,请先命令删除原有 origin 的通信方式,

```text
git remote rm origin
```
## 前提
github 网页增加本机SSH key

git ssh 方式免密提交方式需要将 `ssh-keygen` 生成的公钥放到服务器上

全局用户名密码配置

```text
git config --global user.name "xxx" 
git config --global user.email "xxx@qq.com"
```

项目初始化，生成 .git 目录，配置 ssh 远程项目地址。

```text
# 如果是新仓库需要git init ;否则不需要git init; git init
# git 关联远程仓库
git remote add origin git@gitee.com:xxx/xxx.git
```

## 生成公钥和私钥

1、首先需要检查你电脑是否已经有 SSH key

运行 git Bash 客户端，检查本机的ssh密钥。

```text
$ cd ~/.ssh 
$ ls
```

如果提示：No such file or directory ，说明是第一次使用 git。

如果不是第一次使用，已经存在 id_rsa.pub 或 id_dsa.pub 文件, 则不用重新生成,直接跳到步骤3。如果没有生成过 id_rsa.pub ,请执行下面的操作，生成ssh 密钥。

```text
$ mkdir key_backup   
$ cp id_rsa* key_backup   
$ rm id_rsa*
```

2、执行生成公钥和私钥的命令，生成新的密钥：

```text
ssh-keygen -t rsa -C "xxx"
```

代码参数：

-t 指定密钥类型，默认是 rsa ，可以省略。

-C 设置注释文字，比如邮箱。

执行命令时会提示要求输入邮箱密码，这个密码会在提交时使用，如果为空的话提交时则不用输入。这个设置是防止别人往你的项目里提交内容。我们自己的电脑，自己本机使用，当然不用密码了。

按默认为空，直接按回车3下，生成 id_rsa 和 id_rsa.pub 两个秘钥文件。

执行查看公钥信息：

```text
cat ~/.ssh/id_rsa.pub
```

Windows 系统，位置在用户目录下 .ssh文件夹中。`%USERPROFILE%`

## 复制公钥信息到远端仓库
**gitee**
打开 gitee，我的账户-设置-SSH 公钥，如下图所示，把公钥粘贴到公钥文本框中，标题自己定义，然后点击确定按键，输入密码。

![](https://pic3.zhimg.com/80/v2-8c26fae5769cb56da5e20c884a33c702_720w.webp)

**github**
Settings -SSH and GPG keys - New SSH key
![](app://db738d3bb1089e4d04f6eb022a68209f31bf/D:/obsidian_note/LeiQi_Blog/source/imgs/Pasted%20image%2020240101151324.png?1704093204312)
然后，提交时就不再需要用户名和密码了

```text
git add -A
git commit -m "ssh免密提交"
git push -u origin master
```

参考:
https://zhuanlan.zhihu.com/p/358721423