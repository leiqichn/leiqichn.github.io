
---
title: git stash
date: 2024-08-22 00:26:46
modificationDate: 2025 五月 8日 星期四 23:27:31
categories: 
	- git
tags: [git]
sticky: []
published: true
category_bar: true
---

当尝试使用 git pull -f 强制拉取远程仓库的更新时，Git 会警告你，因为本地有未提交的更改，这些更改可能会被覆盖。确定要取消对特定文件的保存，可以按照以下步骤操作：

放弃本地更改：使用 git checkout 命令来放弃对特定文件的更改。
```bash
git checkout -- .obsidian/workspace.json
```

再次尝试拉取：放弃更改后，可以再次尝试拉取远程仓库的更新。


```bash
git pull
```

如果不想放弃这些更改，而是想将它们暂时保存起来，可以使用 git stash 命令：

保存更改：使用 git stash 将更改保存到一个临时区域。



```
git stash
```

拉取远程更新：


```bash
git pull
```
恢复更改：在拉取更新后，你可以使用 git stash apply 来恢复之前保存的更改。


```bash
git stash apply
```



`git stash` 是 Git 中用于临时保存工作目录和暂存区改动的工具，适用于需要切换分支或处理其他任务但不想提交未完成工作的场景。

---

### **基本命令**
1. **保存当前改动**
   ```bash
   git stash                   # 默认保存，消息为自动生成
   git stash push -m "备注"    # 保存并添加自定义备注
   ```
   - **选项**：
     - `-u` 或 `--include-untracked`：包含未被跟踪的文件（新增但未 `git add` 的文件）。
     - `-a` 或 `--all`：包含所有文件（包括被 `.gitignore` 忽略的文件）。
     - `--keep-index`：仅保存工作区未暂存的改动，保留暂存区内容。

2. **查看保存的 stash 列表**
   ```bash
   git stash list
   ```
   - 输出示例：`stash@{0}: On main: 备注`

3. **恢复改动**
   - **恢复最近一次的 stash 并删除记录**：
     ```bash
     git stash pop
     ```
   - **恢复指定 stash 但不删除记录**：
     ```bash
     git stash apply stash@{n}  # n 为 stash 编号，如 stash@{0}
     ```

4. **删除 stash**
   - **删除指定 stash**：
     ```bash
     git stash drop stash@{n}
     ```
   - **清空所有 stash**：
     ```bash
     git stash clear
     ```

---

### **高级用法**
1. **从 stash 创建分支**
   ```bash
   git stash branch 分支名 stash@{n}
   ```
   - 基于指定 stash 创建新分支，并自动应用改动（适用于 stash 与当前分支冲突时）。

2. **查看 stash 的改动详情**
   ```bash
   git stash show stash@{n}    # 显示简略差异
   git stash show -p stash@{n} # 显示完整差异（类似 git diff）
   ```

---

### **注意事项**
- **默认行为**：
  - `git stash` 会保存 **工作区未提交的修改** 和 **暂存区的修改**。
  - 恢复时，已暂存的改动会重新回到暂存区，未暂存的改动保留在工作区。
- **未跟踪文件**：
  - 默认不保存未被跟踪的文件（需用 `-u` 或 `--include-untracked`）。
- **冲突处理**：
  - 如果恢复时发生冲突，需手动解决后执行 `git add` 和 `git restore --staged` 或提交。

---

### **示例场景**
1. **临时切换分支**：
   ```bash
   git stash -m "保存功能 A 的进度"
   git checkout 其他分支
   # 处理其他任务后返回
   git checkout 原分支
   git stash pop
   ```

2. **保存包含未跟踪文件**：
   ```bash
   git stash -u -m "包含新文件"
   ```

3. **恢复指定 stash**：
   ```bash
   git stash list              # 查看列表
   git stash apply stash@{2}  # 应用第三个 stash
   ```

---
