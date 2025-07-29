
---
title: 7小时代码编写机器claude code 安装
date: 2025-07-30 00:24:23
modificationDate: 2025 July 30th Wednesday 00:24:34
categories: 
	- 工具
tags: []
sticky: []
hide: false
category_bar: true
---


## 安装Node macOS 用户


```text
sudo xcode-select --install # 安装 Xcode 命令行工具
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" # 安装 Homebrew
brew install node
node --version
```

18版本以上即可

## 安装 Claude Code



```text
npm install -g @anthropic-ai/claude-code
```

验证是否成功

```text
claude --version
```



# 大功告成 启动！


```
claude

```

![](../../imgs/截屏2025-07-30%20上午12.27.40.png)