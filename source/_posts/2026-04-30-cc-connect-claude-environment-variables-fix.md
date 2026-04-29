---
title: cc-connect 调用 claude 无输出的问题排查与解决
date: 2026-04-30 01:50:00
categories:
  - 技术
tags:
  - OpenClaw
  - cc-connect
  - Claude Code
  - 飞书
---

# 问题描述

使用 cc-connect 连接飞书机器人时，消息可以收到，但 Claude Code 进程运行后没有任何输出，日志显示 `agent process exited` 但 `response_len=0`。

## 排查过程

### 1. 确认服务状态

```bash
ps aux | grep cc-connect | grep testuser
ps aux | grep claude-model-proxy | grep testuser
```

服务都在运行，proxy 返回正常。

### 2. 测试 claude 命令

手动执行 `claude -p hi` 发现：
- 以 root 用户运行：有输出
- 以 testuser 运行（`su testuser -c`）：无输出

### 3. 检查环境变量

cc-connect 使用 `su testuser -c` 启动 claude 进程，这是一个**非登录 shell**，不会加载 `.bash_profile`。

testuser 的 `.bashrc` 和 `.profile` 中没有设置 ANTHROPIC_AUTH_TOKEN 和 ANTHROPIC_BASE_URL，导致 claude 无法调用 API。

### 4. 根本原因

cc-connect 在 `config.toml` 中配置了 `mode = "bypassPermissions"`，会调用 `claude` 命令。但：

1. `su testuser -c` 不会加载登录 shell 环境
2. wrapper 脚本 `/home/testuser/cc_bin/claude` 里设置的环境变量不会被 cc-connect 使用
3. 进程 PATH 中没有 node 路径（node 在 root 的 nvm 目录下）

## 解决方案

### 1. 创建全局 wrapper 链接

```bash
ln -sf /home/testuser/cc_bin/claude /usr/local/bin/claude
```

### 2. 修改 wrapper 脚本

```bash
#!/bin/bash
export PATH=/root/.nvm/versions/node/v22.22.0/bin:/home/testuser/cc_bin:/usr/local/bin:/usr/bin:/bin
export HOME=/home/testuser
export XDG_CONFIG_HOME=/home/testuser/.config
export XDG_DATA_HOME=/home/testuser/.local/share
export ANTHROPIC_AUTH_TOKEN="your-api-token"
export ANTHROPIC_BASE_URL="http://127.0.0.1:8080"
exec /root/.nvm/versions/node/v22.22.0/bin/claude "$@"
```

关键点：
- 添加 `/root/.nvm/versions/node/v22.22.0/bin` 到 PATH（testuser 无法访问 root 的 nvm bin 目录）
- 直接 exec claude.exe 避免 symlink 递归

### 3. 设置系统级环境变量

在 `/etc/environment` 中添加：

```
ANTHROPIC_AUTH_TOKEN="your-api-token"
ANTHROPIC_BASE_URL="http://127.0.0.1:8080"
```

## 验证

重启 cc-connect 后测试：

```bash
# 本地测试
su testuser -c '/home/testuser/cc_bin/claude -p hi'

# 查看 cc-connect 日志
tail -f /home/testuser/.cc-connect/cc-connect.log
```

日志中看到 `turn complete` 且 `response_len > 0` 即表示正常。

## 相关文件

- cc-connect 配置：`/home/testuser/.cc-connect/config.toml`
- claude wrapper：`/home/testuser/cc_bin/claude`
- claude-model-proxy：`/home/testuser/claude-model-proxy.js`
- 运行日志：`/home/testuser/.cc-connect/cc-connect.log`
- proxy 日志：`/home/testuser/.claude-proxy.log`

## 经验总结

1. **环境变量问题**：非登录 shell 不会加载 `.bash_profile`，设置环境变量要确保在 wrapper 脚本中 export
2. **PATH 问题**：`su user -c` 使用的 minimal PATH，需要手动添加所需路径
3. **node 路径**：nvm 安装在 root 下，testuser 无法直接访问，需要在 wrapper 中显式添加
