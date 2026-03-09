---
title: GitHub Trending 每日热点追踪系统 - 自动化早晚报推送到飞书群
date: 2026-03-09 23:45:00
permalink: 2026-03-09-github-trending-daily-report.html
categories:
  - 技术栈
  - 自动化
tags:
  - Python
  - GitHub
  - OpenClaw
  - 自动化
  - 飞书
---

## 项目背景

GitHub Trending 是发现热门开源项目的重要渠道。本文介绍如何使用 OpenClaw 的定时任务功能，自动抓取 GitHub Trending 并推送到飞书群聊。

## 系统架构

\`\`\`
GitHub Trending API → Python Script → OpenClaw Cron → 飞书群聊
\`\`\`

## 核心功能

1. 自动抓取 GitHub Trending 榜单
2. 生成格式化报告
3. 定时推送到飞书群聊
4. 支持早报/晚报两种推送时间

## 实现细节

### 1. GitHub Trending API

使用 GitHub Trending API 获取热门项目：

\`\`\`python
import requests

def get_trending(language=None, since='daily'):
    url = f"https://api.gitterapp.com/repositories?language={language}&since={since}"
    response = requests.get(url)
    return response.json()
\`\`\`

### 2. 飞书推送

使用飞书开放 API 发送消息到群聊：

\`\`\`python
def send_to_feishu(message, chat_id):
    # 获取 token
    # 发送消息
    pass
\`\`\`

### 3. OpenClaw Cron 配置

\`\`\`bash
openclaw cron add --name "GitHub Trending 早报" --schedule "0 8 * * *" --message "运行 GitHub Trending 早报"
\`\`\`

## 效果展示

每天早上 8:00 和晚上 20:00，飞书群聊会自动收到 GitHub Trending 报告。

---

欢迎交流！
