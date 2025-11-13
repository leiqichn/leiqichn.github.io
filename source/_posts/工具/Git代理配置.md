---
title: 【Git】Git代理配置
date: 2025-11-13 23:24:53
modificationDate: 2025 十一月 13日 星期四 23:24:53
categories: 
	- 工具
tags: [git]
sticky: []
published: true
category_bar: true
---
配置 Git 插件使用代理，有几种方法可以实现：

## 方法一：通过 Git 全局配置代理（推荐）

在终端中执行以下命令：

```bash
# 设置 Git 全局代理
git config --global http.proxy http://127.0.0.1:7897
git config --global https.proxy http://127.0.0.1:7897

# 如果需要设置不使用代理的地址（如内网地址）
git config --global http.proxy http://127.0.0.1:7897
git config --global https.proxy http://127.0.0.1:7897

# 查看配置是否生效
git config --global --list | grep proxy
```

## 方法二：为特定仓库配置代理

如果只想为 Obsidian 仓库设置代理，进入仓库目录后执行：

```bash
cd /path/to/your/obsidian/vault
git config http.proxy http://127.0.0.1:7897
git config https.proxy http://127.0.0.1:7897
```

## 方法三：通过环境变量（临时方案）

创建启动脚本，在启动 Obsidian 前设置环境变量：

```bash
# 创建启动脚本 obsidian-with-proxy.sh
#!/bin/bash
export http_proxy=http://127.0.0.1:7897
export https_proxy=http://127.0.0.1:7897
# 启动 Obsidian（路径根据实际情况调整）
open /Applications/Obsidian.app
```

## 方法四：优化 alias

将您的 alias 扩展为更完整的功能：

```bash
# 添加到 ~/.bashrc 或 ~/.zshrc
alias proxyon='export http_proxy=http://127.0.0.1:7897 https_proxy=http://127.0.0.1:7897; git config --global http.proxy http://127.0.0.1:7897; git config --global https.proxy http://127.0.0.1:7897'
alias proxyoff='unset http_proxy https_proxy; git config --global --unset http.proxy; git config --global --unset https.proxy'
alias proxyinfo='echo "HTTP Proxy: $http_proxy"; echo "HTTPS Proxy: $https_proxy"; git config --global --get http.proxy; git config --global --get https.proxy'
```

## 方法五：验证代理是否生效

配置完成后，可以通过以下命令测试：

```bash
# 测试 Git 连接
git clone https://github.com/username/test-repo.git

# 或者使用 curl 测试
curl -I --proxy http://127.0.0.1:7897 https://github.com
```

## 注意事项

1. **端口号确认**：确保 `7897` 代理软件的实际端口
2. **代理协议**：根据您的代理类型，可能需要使用 `socks5://` 而不是 `http://`
3. **排除内网地址**：如果需要访问内网 Git 仓库，可以设置排除规则：

```bash
git config --global http.proxy http://127.0.0.1:7897
git config --global http."https://github.com".proxy ""  # GitHub 不使用代理
```

推荐使用**方法一和二**，因为 Git 插件会直接读取 Git 的配置，这样设置后  Git 插件就会自动使用代理进行网络操作。