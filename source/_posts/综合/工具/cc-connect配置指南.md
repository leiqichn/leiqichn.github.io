---
title: 【Agent工具】5分钟让你飞书远控Claude Code
date: 2026-04-15 08:55:00
tags:
  - 飞书
  - Claude Code
  - AI
  - 自动化
categories: AI
---

# 飞书机器人控制 Claude Code 实战

## 背景

本文介绍如何将 Claude Code 通过 cc-connect 桥接到飞书，实现通过飞书机器人与 Claude Code 对话。

## 架构概览

```
用户 → 飞书机器人 → cc-connect → Claude Code → MiniMax API
```

关键问题：Claude Code 默认使用 `claude-sonnet-4-6` 模型，但 MiniMax API 不支持此模型。需要通过本地代理进行模型名称转换。

## 安装步骤

### 1. 安装 cc-connect

```bash
npm install -g cc-connect
```

### 2. 安装 Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

### 3. 创建 MiniMax 模型代理

Claude Code 与 MiniMax API 模型名称不兼容，需要创建本地代理进行转换：

```javascript
// claude-model-proxy.js
const http = require('http');
const https = require('https');

const MINIMAX_TOKEN = 'your-minimax-token';
const MINIMAX_HOST = 'api.minimaxi.com';
const MINIMAX_PATH = '/anthropic/v1/messages';

const MODEL_MAP = {
    'claude-sonnet-4-6': 'abab6.5s',
    'claude-opus-4-7': 'abab6.5s',
    'claude-haiku-4-7': 'abab6.5s',
};

const server = http.createServer((req, res) => {
    if (req.method !== 'POST') {
        res.writeHead(404);
        res.end();
        return;
    }

    let body = '';
    req.on('data', chunk => body += chunk);
    req.on('end', () => {
        try {
            const data = JSON.parse(body);
            const originalModel = data.model;
            
            if (MODEL_MAP[data.model]) {
                data.model = MODEL_MAP[data.model];
                console.log(`[PROXY] Model mapped: ${originalModel} -> ${data.model}`);
            }

            const postData = JSON.stringify(data);
            const options = {
                hostname: MINIMAX_HOST,
                path: MINIMAX_PATH,
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${MINIMAX_TOKEN}`,
                    'Content-Type': 'application/json',
                    'anthropic-version': '2023-06-01',
                    'Content-Length': Buffer.byteLength(postData)
                }
            };

            const proxyReq = https.request(options, (proxyRes) => {
                let responseBody = '';
                proxyRes.on('data', chunk => responseBody += chunk);
                proxyRes.on('end', () => {
                    res.writeHead(proxyRes.statusCode, { 'Content-Type': 'application/json' });
                    res.end(responseBody);
                });
            });

            proxyReq.on('error', (e) => {
                res.writeHead(500);
                res.end(JSON.stringify({ error: e.message }));
            });

            proxyReq.write(postData);
            proxyReq.end();
        } catch (e) {
            res.writeHead(500);
            res.end(JSON.stringify({ error: e.message }));
        }
    });
});

server.listen(8080, '127.0.0.1', () => {
    console.log('[PROXY] Claude Code Model Alias Proxy running on http://127.0.0.1:8080');
    console.log('[PROXY] Maps: claude-sonnet-4-6 -> abab6.5s (MiniMax)');
});
```

启动代理：

```bash
node claude-model-proxy.js &
```

### 4. 配置飞书机器人

1. 访问 [飞书开放平台](https://open.feishu.cn) 创建企业应用
2. 启用**机器人**能力
3. 配置权限：
   - `im:message.receive_v1`
   - `im:message:send_as_bot`
4. 配置**事件订阅**：选择 WebSocket 长连接模式，添加事件 `im.message.receive_v1`
5. 发布应用
6. 复制 App ID 和 App Secret

### 5. 创建 cc-connect 配置文件

创建 `~/.cc-connect/config.toml`：

```toml
language = "zh"

[[projects]]
  name = "claude-feishu"
  
  [projects.agent]
    type = "claudecode"
    
  [projects.agent.options]
    mode = "bypassPermissions"
    
  [projects.agent.env]
    ANTHROPIC_AUTH_TOKEN = "your-minimax-token"
    ANTHROPIC_BASE_URL = "http://127.0.0.1:8080"

  [[projects.platforms]]
    type = "feishu"
    [projects.platforms.options]
      app_id = "cli_xxxxxxxxxxxx"
      app_secret = "xxxxxxxxxxxxxxxxxxxxxxxx"

[log]
  level = "debug"
```

### 6. 以非 root 用户运行 cc-connect

Claude Code 的 `--dangerously-skip-permissions` 参数不允许 root 用户使用。建议创建专用用户：

```bash
# 创建专用用户
useradd -m -s /bin/bash testuser

# 以该用户启动 cc-connect
su - testuser -c "cc-connect start"
```

## 验证配置

```bash
# 检查 cc-connect 状态
cc-connect status

# 检查代理是否运行
curl -s http://127.0.0.1:8080 >/dev/null && echo "Proxy OK"
```

日志显示以下内容表示成功：

```
✅ config loaded
✅ feishu: bot identified
✅ engine started (claudecode)
✅ connected to wss://msg-frontier.feishu.cn
```

## 常见问题

### 错误：--dangerously-skip-permissions cannot be used with root/sudo

Claude Code 安全限制不允许 root 用户使用 `--dangerously-skip-permissions`。解决方案：

1. 使用非 root 用户运行 cc-connect
2. 或在 `settings.json` 中预配置权限

### 模型不兼容错误

确保代理正在运行，并且 `ANTHROPIC_BASE_URL` 指向代理地址。

## 参考资料

- [cc-connect GitHub](https://github.com/chenhg5/cc-connect)
- [Claude Code 官方文档](https://docs.claude.com)

---

*本文档更新于 2026-04-15*
