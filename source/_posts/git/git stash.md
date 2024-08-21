
---
title: git stash
date: 2024-08-22 00:26:46
modificationDate: 2024 八月 22日 星期四 00:27:00
categories: 
	- git
tags: []
sticky: []
hide: false
category_bar: true
---
当尝试使用 git pull -f 强制拉取远程仓库的更新时，Git 会警告你，因为本地有未提交的更改，这些更改可能会被覆盖。确定要取消对特定文件的保存，可以按照以下步骤操作：

放弃本地更改：使用 git checkout 命令来放弃对特定文件的更改。

bash
git checkout -- .obsidian/workspace.json
再次尝试拉取：放弃更改后，可以再次尝试拉取远程仓库的更新。

bash
git pull
如果不想放弃这些更改，而是想将它们保存起来，可以使用 git stash 命令：

保存更改：使用 git stash 将更改保存到一个临时区域。


git stash
拉取远程更新：


```bash
git pull
```
恢复更改：在拉取更新后，你可以使用 git stash apply 来恢复之前保存的更改。


```bash
git stash apply
```

请注意，使用 git stash apply 可能不会总是成功，在这种情况下，可能需要手动解决冲突。
