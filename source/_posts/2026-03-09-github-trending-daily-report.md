---
title: GitHub Trending 每日热点追踪系统 - 自动化早晚报推送到飞书群
date: 2026-03-09 23:45:00
url: github-trending-daily-report
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

## 背景

GitHub Trending 是发现新技术趋势和热门项目的重要渠道。但每天手动查看很麻烦，所以我开发了一个自动化系统：

- 🌅 **早报**：早上 8:00 推送，了解最新热点
- 🌙 **晚报**：晚上 20:00 推送，回顾全天动态

## 系统架构

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────┐
│  GitHub         │────▶│  Python 脚本      │────▶│  OpenClaw   │
│  Trending 页面   │     │  (抓取+解析)       │     │  Cron 任务  │
└─────────────────┘     └──────────────────┘     └──────┬──────┘
                                                       │
                                                       ▼
                                               ┌─────────────┐
                                               │  飞书群通知  │
                                               └─────────────┘
```

## 核心代码

### 1. 数据抓取

使用 `requests` + `BeautifulSoup` 解析 GitHub Trending 页面：

```python
def fetch_trending():
    """抓取 GitHub Trending 页面"""
    headers = {
        "User-Agent": "Mozilla/5.0 ...",
    }
    response = requests.get(GITHUB_TRENDING_URL, headers=headers, timeout=30)
    return response.text

def parse_trending(html):
    """解析仓库信息"""
    soup = BeautifulSoup(html, "html.parser")
    repos = []
    
    for article in soup.select("article.Box-row"):
        repo_name = article.select_one("h2 a").get("href", "").strip("/")
        description = article.select_one("p.col-9").get_text(strip=True)
        language = article.select_one("[itemprop='programmingLanguage']").get_text(strip=True)
        
        # 今日新增 stars
        stars_span = article.select_one("span.float-sm-right")
        stars_today = re.search(r"([\d,]+)\s*stars today", stars_span.get_text())
        
        repos.append({
            "name": repo_name,
            "description": description,
            "language": language,
            "stars_today": stars_today.group(1) if stars_today else "0",
        })
    
    return repos
```

### 2. 报告格式化

生成带有多语言 Emoji 的 Markdown 报告：

```python
def format_report(repos, time_of_day):
    """格式化报告"""
    time_emoji = "🌅" if time_of_day == "morning" else "🌙"
    report = f"""# {time_emoji} GitHub Trending 日报

📅 **{datetime.now().strftime("%Y-%m-%d")}** | 今日热点仓库 Top 10

---"""
    
    for i, repo in enumerate(repos[:10], 1):
        lang_emoji = get_language_emoji(repo["language"])
        report += f"""
## {i}. [{repo['name']}](https://github.com/{repo['name']})

> {repo['description'][:100]}

{lang_emoji} **{repo['language']}** | ⭐ **+{repo['stars_today']}** 今日
---"""
    
    return report
```

### 3. Cron 任务配置

使用 OpenClaw 的 cron 功能设置定时任务：

```bash
# 早报 - 每天 8:00
openclaw cron add "github-trending-morning" \
  --schedule "0 8 * * *" \
  --command "python3 /root/.openclaw/workspace/github_trending_report.py morning" \
  --target "isolated"

# 晚报 - 每天 20:00
openclaw cron add "github-trending-evening" \
  --schedule "0 20 * * *" \
  --command "python3 /root/.openclaw/workspace/github_trending_report.py evening" \
  --target "isolated"
```

## 报告示例

### 早报格式

```markdown
🌅 **GitHub Trending 早安日报**

📅 2026-03-09 08:00 | 今日热点仓库 Top 10

---

## 1. [openclaw/openclaw](https://github.com/openclaw/openclaw)

> Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞

🔷 **TypeScript** | ⭐ **+9,123** 今日 | 🏆 288,811 总计

---

## 2. [666ghj/MiroFish](https://github.com/666ghj/MiroFish)

> A Simple and Universal Swarm Intelligence Engine, Predicting Anything.

🐍 **Python** | ⭐ **+2,222** 今日 | 🏆 9,825 总计

---
...
```

## 技术亮点

### 1. 编程语言 Emoji 映射

自动识别编程语言并显示对应 Emoji：

| 语言 | Emoji |
|------|-------|
| Python | 🐍 |
| TypeScript | 🔷 |
| JavaScript | 🟨 |
| Rust | 🦀 |
| Go | 🐹 |
| Jupyter | 📓 |

### 2. 智能简介截断

长简介自动截断并保持可读性：

```python
description[:100] + "..." if len(description) > 100 else description
```

### 3. 错误处理与重试

网络请求超时和解析失败的优雅处理：

```python
try:
    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()
except requests.Timeout:
    print("请求超时，稍后重试")
except requests.RequestException as e:
    print(f"请求失败: {e}")
```

## 部署到 OpenClaw

### 1. 脚本位置

```
/root/.openclaw/workspace/
├── github_trending_report.py    # 主脚本
└── reports/                      # 报告存档
    ├── github_trending_20260309_morning.md
    └── github_trending_20260309_evening.md
```

### 2. 依赖安装

```bash
pip install beautifulsoup4 requests
```

### 3. 测试运行

```bash
# 测试早报
python3 github_trending_report.py morning

# 测试晚报
python3 github_trending_report.py evening
```

## 扩展方向

1. **个性化订阅** - 支持按语言、话题过滤
2. **趋势对比** - 对比早晚变化，识别快速增长项目
3. **AI 摘要** - 使用 LLM 生成项目深度解读
4. **多平台推送** - 支持 Telegram、Discord、微信等

## 总结

这个系统让我每天能自动收到 GitHub 热点推送，不再错过重要技术趋势。结合 OpenClaw 的 cron 功能，部署简单、运行稳定。

---

**源码**：`/root/.openclaw/workspace/github_trending_report.py`

**相关文章**：
- [OpenClaw飞书群聊机器人@不响应问题排查与解决](/openclaw-feishu-group-bot-fix)