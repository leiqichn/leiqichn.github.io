---
title: 【sed】快速替换当前文件夹下文件中指定内容
date: 2025-01-13 23:40:59
modificationDate: 2025 一月 13日 星期一 23:40:59
categories: 
	- Linux
tags: []
sticky: []
hide: false
category_bar: true
---

在 Linux 中，可以使用以下命令来实现这个需求：

```bash
sed -i 's/hide: true/hide: false/g' *
```

解释一下这个命令：

- `sed` 是流编辑器，用于对文本进行过滤和转换。
- `-i` 选项表示直接修改文件，而不是输出到终端。
- `'s/hide: true/hide: false/g'` 是 sed 的替换命令，其中：
    - `s` 表示替换操作。
    - `hide: true` 是要被替换的字符串。
    - `hide: false` 是替换后的字符串。
    - `g` 表示全局替换，即在每一行中将所有匹配的 `hide: true` 都替换为 `hide: false`。
- `*` 表示当前文件夹下的所有文件。

需要注意的是，这个命令会修改当前文件夹下所有文件的内容，包括二进制文件等，可能会导致一些文件损坏。如果只想修改特定类型的文件，可以使用通配符指定文件类型，例如替换当前文件夹下所有 `.txt` 文件中的内容：

```bash
sed -i 's/hide: true/hide: false/g' *.txt
```

另外，如果当前文件夹下有子文件夹，并且也想修改子文件夹中文件的内容，可以使用 `find` 命令结合 `sed` 来实现，例如：

```bash
find . -type f -exec sed -i 's/hide: true/hide: false/g' {} +
```

这个命令会递归查找当前文件夹及其子文件夹下的所有文件（`-type f`），然后对每个文件执行 `sed` 命令进行替换。
