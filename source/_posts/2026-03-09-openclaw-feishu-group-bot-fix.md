---
title: OpenClaw飞书群聊机器人@不响应问题排查与解决
date: 2026-03-09 23:05:00
url: openclaw-feishu-group-bot-fix
categories:
  - 技术栈
  - DevOps
tags:
  - OpenClaw
  - 飞书
  - 机器人
  - 问题排查
---

## 问题背景

在飞书群聊中 @OpenClaw 机器人时，机器人没有响应。日志显示：

```
message in group oc_xxx did not mention bot, recording to history
```

消息被记录到历史，但没有触发回复。

## 问题分析

### 1. 权限检查

首先确认飞书应用权限配置正确：

- `im:message` ✅
- `im:message:send_as_bot` ✅
- `im:message.group_at_msg:readonly` ✅
- `contact:contact.base:readonly` ✅

所有必要权限都已授权。

### 2. 日志分析

查看 Gateway 日志发现关键问题：

```
[feishu] feishu[default]: message in group oc_xxx did not mention bot, recording to history
```

这表明机器人收到了消息，但没有识别到被 @提及。

### 3. 源码分析

查看 OpenClaw 飞书扩展源码 (`bot.ts`)：

```typescript
function checkBotMentioned(event: FeishuMessageEvent, botOpenId?: string): boolean {
  if (!botOpenId) return false;  // 关键：没有 botOpenId 直接返回 false
  const mentions = event.message.mentions ?? [];
  if (mentions.length > 0) {
    return mentions.some((m) => m.id.open_id === botOpenId);
  }
  // ...
}
```

**根本原因**：`botOpenId` 没有配置，导致 `checkBotMentioned` 函数直接返回 `false`。

## 解决方案

### 1. 获取机器人 Open ID

```bash
# 获取 tenant_access_token
curl -s "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal" \
  -H "Content-Type: application/json" \
  -d '{"app_id":"cli_xxx","app_secret":"xxx"}'

# 获取机器人信息
curl -s "https://open.feishu.cn/open-apis/bot/v3/info" \
  -H "Authorization: Bearer $TOKEN"
```

返回结果：

```json
{
  "bot": {
    "open_id": "ou_c0224f261ab61714eaafe98ac6edd0a1",
    "app_name": "贾维斯"
  }
}
```

### 2. 更新配置

在 `~/.openclaw/openclaw.json` 中添加 `botOpenId`：

```json
{
  "channels": {
    "feishu": {
      "enabled": true,
      "appId": "cli_xxx",
      "appSecret": "xxx",
      "domain": "feishu",
      "groupPolicy": "open",
      "botOpenId": "ou_c0224f261ab61714eaafe98ac6edd0a1"
    }
  }
}
```

### 3. 重启 Gateway

```bash
# 重启 OpenClaw Gateway
pkill -9 -f openclaw-gateway
openclaw gateway start
```

### 4. 验证

重启后日志显示：

```
[feishu] feishu[default]: bot open_id resolved: ou_c0224f261ab61714eaafe98ac6edd0a1
```

机器人在群聊中 @ 后可以正常回复了！

## 经验总结

1. **日志是最好的调试工具** - 通过日志定位到 "did not mention bot" 的关键信息
2. **理解源码逻辑** - 查看 `checkBotMentioned` 函数发现问题根源
3. **配置完整性** - 飞书机器人需要配置 `botOpenId` 才能正确识别群聊 @提及
4. **官方文档可能遗漏** - 这个配置项在 OpenClaw 文档中可能没有明确说明

## 其他相关问题

### 磁盘空间清理

在排查过程中发现磁盘已满 (100%)：

```bash
# 清理大文件
rm -rf node_modules/venv/.git  # 根据实际情况清理

# 清理系统缓存
journalctl --vacuum-size=50M
npm cache clean --force
```

### 项目备份

使用 GitHub 备份重要项目：

```bash
# 创建私有仓库并推送
gh repo create project-name --private --source=. --push
```

---

希望这篇文章对你有帮助！如果你也遇到类似问题，欢迎交流。

