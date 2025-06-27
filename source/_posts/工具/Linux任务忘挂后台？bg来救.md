---
title: Linux任务忘挂后台？bg来救
date: 2025-06-28 00:34:18
modificationDate: 2025 六月 28日 星期六 00:34:18
categories: 
	- 工具
tags: []
sticky: []
published: true
category_bar: true
---
### 方法 1：直接挂起当前任务到后台（推荐）

1. **暂停任务**：  
    按组合键 `Ctrl + Z`，将当前前台任务**暂停**（挂起），此时终端会显示类似：
    
    

```
    [1]+  Stopped                 python code/bert_baseline.py
```

    
2. **将任务切换到后台运行**：  
    输入命令 `bg`（将最近暂停的任务放到后台运行），终端显示：
    

```
	(base) root@gpu-1092425eb65d87e4b97a1-1-b6nqycupjgmy:~/IDRsPredictor# bg
	[1]+ python code/bert_baseline.py &
```

此时任务会在后台继续运行
![](../../imgs/Pasted%20image%2020250628003523.png)


