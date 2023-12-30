---
title: git强制拉取远端
date: 2023-10-22 17:53:57
modificationDate: 2023 十月 22日 星期日 17:53:57
categories:
- git
tags: []
sticky: []
hide: false
category_bar: true
---
```sh
git fetch origin
git reset --hard origin/<branch_name>
```
这里的 <branch_name> 应该替换为你想要拉取的远程分支的名称。这两个命令的作用如下：

git fetch origin：这个命令会从远程仓库（通常是"origin"，可以根据你的实际情况替换）获取最新的分支信息，但不会合并或应用任何更改到你的本地分支。

git reset --hard origin/<branch_name>：这个命令会将你的本地分支重置为与指定远程分支相同的状态，并且会放弃本地的任何更改。--hard 标志会强制应用这个重置，因此请小心使用，确保你不需要本地的更改。

这些命令将强制拉取远程分支的最新版本，并且会覆盖本地的任何更改。确保在执行这些命令之前，你没有重要的未提交更改，因为它们将永久丢失。





