---
title: 下载huggingface模型
date: 2025-06-23 22:53:29
modificationDate: 2025 六月 23日 星期一 22:53:29
categories: 
	- AI学习
tags: []
sticky: []
published: true
category_bar: true
---

### 使用 `huggingface_hub` 工具

1. **安装工具库**：
    
    bash
    
    复制
    
    下载
    
    pip install huggingface_hub
    
2. **通过命令行下载**：
    
    bash
    
    复制
    
    下载
    
    huggingface-cli download Rostlab/prot_bert --local-dir ./prot_bert_model
    
    - `--local-dir`：指定本地保存路径（如 `./prot_bert_model`）。

![](../../imgs/Pasted%20image%2020250623225401.png)