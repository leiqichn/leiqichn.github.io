
---
title: 查询深度学习环境python torch cuda版本
date: 2024-08-08 22:55:03
modificationDate: 2024 八月 8日 星期四 22:55:27
categories: 
	- 工具
tags: []
sticky: []
hide: false
category_bar: true
---

```python
import sys
import torch

#sys模块提供了一系列有关Python运行环境的变量和函数。
print(sys.version)
print(torch.__version__)
print(torch.cuda.is_available())
```
![](../../imgs/Pasted%20image%2020240808225509.png)