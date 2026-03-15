---
title: Waline评论系统安装与Valine迁移完整指南
date: 2026-03-15 15:25:00
categories:
  - 综合
  - 工具
tags:
  - Waline
  - Valine
  - 博客
  - 评论系统
---

## 前言

最近将博客评论系统从Valine迁移到了Waline。Waline是从Valine衍生出的带有后端服务的评论系统，解决了Valine的一些痛点。本文记录完整的安装和迁移过程。

## 为什么选择Waline？

### Valine的问题
- 依赖LeanCloud存储，国内访问不稳定
- 没有后端，无法实现邮件通知等功能
- 安全性问题（暴露AppKey）

### Waline的优势
- 支持多种数据库（SQLite、MySQL、MongoDB等）
- 自建后端，数据完全可控
- 支持邮件通知、微信通知
- 支持评论审核、垃圾评论过滤
- 兼容Valine前端配置

## 一、安装Waline服务端

### 1. 安装Node.js

```bash
# 使用nvm安装
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.bashrc
nvm install --lts
```

### 2. 安装PM2进程管理

```bash
npm install -g pm2
```

### 3. 创建Waline目录

```bash
mkdir -p /var/www/waline
cd /var/www/waline
npm init -y
npm install @waline/vercel dotenv
```

### 4. 创建启动脚本

创建 `start.js`：

```javascript
// 加载环境变量
require('dotenv').config({ path: '/var/www/waline/.env' });

// 设置端口
process.env.PORT = process.env.PORT || '8360';

// 加载 Waline
require('@waline/vercel/vanilla.js');
```

### 5. 配置环境变量

创建 `.env` 文件：

```bash
# SQLite本地存储
SQLITE_PATH=/var/www/waline/data
PORT=8360
SECURE_DOMAINS=your-domain.com
SITE_URL=https://your-domain.com

# 邮件通知配置 (QQ邮箱)
SMTP_SERVICE=QQ
SMTP_USER=your-email@qq.com
SMTP_PASS=your-smtp-password
SITE_NAME=你的博客名称
AUTHOR_EMAIL=your-email@qq.com
```

### 6. 初始化SQLite数据库

```bash
sqlite3 /var/www/waline/data/waline.sqlite << 'EOF'
CREATE TABLE IF NOT EXISTS wl_Comment (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  url TEXT NOT NULL,
  nick TEXT NOT NULL,
  mail TEXT,
  link TEXT,
  comment TEXT NOT NULL,
  pid INTEGER,
  rid INTEGER,
  status TEXT DEFAULT 'approved',
  ua TEXT,
  ip TEXT,
  insertedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
  updatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
  user_id TEXT,
  sticky INTEGER DEFAULT 0,
  like INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS wl_Counter (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  url TEXT NOT NULL UNIQUE,
  time INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS wl_Users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  display_name TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE,
  password TEXT NOT NULL,
  type TEXT DEFAULT 'guest'
);
EOF
```

### 7. 使用PM2启动

```bash
pm2 start start.js --name waline
pm2 save
```

## 二、配置Nginx代理

### 为什么需要代理？

如果你的博客使用HTTPS，直接访问HTTP的Waline服务会被浏览器阻止（混合内容安全策略）。

### Nginx配置

```nginx
server {
    listen 80 default_server;
    server_name _;
    root /var/www/blog;
    
    # Waline 评论 API 代理
    location /waline/ {
        proxy_pass http://127.0.0.1:8360/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
    
    location / {
        try_files $uri $uri/ =404;
    }
}
```

## 三、配置博客前端

### Hexo Butterfly主题配置

编辑 `themes/butterfly/_config.yml`：

```yaml
comments:
  use: waline
  count: true
  card_post_count: true

waline:
  serverURL: /waline  # 使用相对路径，支持HTTPS
  pageview: true
  option:
    locale:
      placeholder: 欢迎评论~
    meta:
      - nick
      - mail
    requiredFields:
      - nick
      - mail
    emoji:
      - //unpkg.com/@waline/emojis@1.4.0/qq
      - //unpkg.com/@waline/emojis@1.4.0/bmoji
      - //unpkg.com/@waline/emojis@1.4.0/weibo
```

### 重要说明

**serverURL使用相对路径**：`/waline` 而不是 `http://ip:port`

这样无论博客使用HTTP还是HTTPS，都能正确加载评论。

## 四、从Valine迁移评论

### 1. 导出Valine评论

从LeanCloud后台导出评论数据，格式为JSON。

### 2. Valine表情映射

Valine使用 `:emotion:` 格式的表情，Waline使用emoji。需要转换：

```python
# Valine表情到Emoji的映射
VALINE_TO_EMOJI = {
    'whee': '😁',
    'clap': '👏',
    'poor': '😰',
    'tear': '😢',
    'happy': '😊',
    # ... 更多映射
}

def convert_emotion(text):
    import re
    def replace(match):
        emotion = match.group(1).strip().lower()
        return VALINE_TO_EMOJI.get(emotion, match.group(0))
    return re.sub(r':([a-zA-Z\s]+):', replace, text)
```

### 3. 迁移脚本

```python
import json
import sqlite3
from datetime import datetime

# 读取Valine导出数据
with open('valine_comments.json', 'r') as f:
    valine_comments = json.load(f)

# 连接Waline数据库
conn = sqlite3.connect('/var/www/waline/data/waline.sqlite')
cursor = conn.cursor()

# 清空现有评论
cursor.execute("DELETE FROM wl_Comment")

# ID映射表（处理回复关系）
id_map = {}

for vc in valine_comments:
    # 转换数据
    url = vc.get('url', '/')
    nick = vc.get('nick', 'Anonymous') or 'Anonymous'
    mail = vc.get('mail', '') or ''
    link = vc.get('link', '') or ''
    comment = convert_emotion(vc.get('comment', ''))
    
    # 处理回复关系
    pid = id_map.get(vc.get('pid')) if vc.get('pid') else None
    rid = id_map.get(vc.get('rid')) if vc.get('rid') else None
    
    cursor.execute('''
        INSERT INTO wl_Comment (url, nick, mail, link, comment, pid, rid, status, insertedAt, updatedAt)
        VALUES (?, ?, ?, ?, ?, ?, ?, 'approved', datetime('now'), datetime('now'))
    ''', (url, nick, mail, link, comment, pid, rid))
    
    id_map[vc['objectId']] = cursor.lastrowid

conn.commit()
conn.close()
print(f"迁移完成，共导入 {len(valine_comments)} 条评论")
```

## 五、验证与测试

### 检查服务状态

```bash
pm2 list
pm2 logs waline
```

### 测试API

```bash
curl http://127.0.0.1/waline/
```

### 检查评论

访问博客文章页面，确认历史评论是否正确显示。

## 六、常见问题

### Q: HTTPS页面评论不显示？

A: 确保serverURL使用相对路径，并通过nginx代理。

### Q: 邮件通知不工作？

A: 检查SMTP配置，QQ邮箱需要使用授权码而非登录密码。

### Q: 表情显示为文字？

A: Valine的表情格式需要转换为emoji或图片。

### Q: 评论数不准确？

A: 检查 `card_post_count: true` 配置，确保Waline的pageview功能开启。

## 七、维护命令

```bash
# 查看状态
pm2 status waline

# 重启服务
pm2 restart waline

# 查看日志
pm2 logs waline

# 备份数据库
cp /var/www/waline/data/waline.sqlite /backup/waline_$(date +%Y%m%d).sqlite
```

## 总结

Waline相比Valine有以下优势：

1. **数据自主可控** - 自建后端，数据存储在自己的服务器
2. **功能更丰富** - 支持邮件通知、评论审核、垃圾过滤
3. **更好的安全性** - 不暴露敏感信息
4. **HTTPS兼容** - 通过nginx代理解决混合内容问题

迁移过程相对简单，主要是数据格式转换和前端配置调整。希望这篇教程对你有帮助！

---

> 参考文档：
> - [Waline官方文档](https://waline.js.org/)
> - [Valine迁移指南](https://waline.js.org/migration/)
> - [Hexo Butterfly主题配置](https://butterfly.js.org/)