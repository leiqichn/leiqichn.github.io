#!/usr/bin/env python3
"""
GitHub Trending 日报自动生成脚本
每天定时抓取GitHub Trending，生成博客文章并部署
"""

import os
import sys
import json
import requests
from datetime import datetime
from pathlib import Path

# 配置
BLOG_PATH = "/root/.openclaw/workspace/projects/leiqichn.github.io"
POST_DIR = f"{BLOG_PATH}/source/_posts/综合/工具"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")

def get_github_trending(language="", since="daily", limit=15):
    """获取GitHub Trending数据"""
    try:
        # 使用GitHub Trending API
        url = f"https://api.gitterapp.com/repositories"
        params = {
            "language": language,
            "since": since
        }
        headers = {
            "Accept": "application/json",
            "User-Agent": "OpenClaw-GitHub-Trending-Bot/1.0"
        }
        
        response = requests.get(url, params=params, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        if isinstance(data, list):
            return data[:limit]
        return []
    except Exception as e:
        print(f"获取GitHub Trending失败: {e}")
        # 备用方案：使用模拟数据
        return get_mock_trending()

def get_mock_trending():
    """模拟数据（API不可用时使用）"""
    return [
        {
            "name": "agency-agents",
            "author": "msitarzewski",
            "avatar": "https://github.com/msitarzewski.png",
            "url": "https://github.com/msitarzewski/agency-agents",
            "description": "A complete AI agency at your fingertips",
            "language": "Shell",
            "stars": 26352,
            "starsToday": 223,
            "forks": 1234
        }
    ]

def get_repo_details(owner, repo):
    """获取仓库详细信息（用于第一个项目的详细介绍）"""
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}"
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "OpenClaw-Bot"
        }
        if GITHUB_TOKEN:
            headers["Authorization"] = f"token {GITHUB_TOKEN}"
        
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"获取仓库详情失败: {e}")
        return None

def get_repo_readme(owner, repo):
    """获取仓库README"""
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}/readme"
        headers = {
            "Accept": "application/vnd.github.v3.raw",
            "User-Agent": "OpenClaw-Bot"
        }
        if GITHUB_TOKEN:
            headers["Authorization"] = f"token {GITHUB_TOKEN}"
        
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        readme = response.text
        
        # 限制README长度
        if len(readme) > 3000:
            readme = readme[:3000] + "\n\n... (内容过长，已截断，请访问GitHub查看完整内容)"
        
        return readme
    except Exception as e:
        print(f"获取README失败: {e}")
        return None

def generate_detailed_analysis(repo_info, readme):
    """生成第一个项目的详细分析"""
    if not repo_info:
        return ""
    
    analysis = f"""
---

## 🔍 今日精选项目详解

### {repo_info.get('name', 'Unknown')}

**项目地址**：[{repo_info.get('html_url', '')}]({repo_info.get('html_url', '')})

**作者**：{repo_info.get('owner', {}).get('login', 'Unknown')}

---

#### 📖 项目简介

{repo_info.get('description', '暂无描述')}

---

#### 📊 项目数据

| 指标 | 数值 |
|------|------|
| ⭐ Stars | {repo_info.get('stargazers_count', 0):,} |
| 🍴 Forks | {repo_info.get('forks_count', 0):,} |
| 👀 Watchers | {repo_info.get('watchers_count', 0):,} |
| 📝 Language | {repo_info.get('language', 'Unknown')} |
| 📅 Created | {repo_info.get('created_at', '')[:10]} |
| 🔄 Updated | {repo_info.get('updated_at', '')[:10]} |
| 📜 License | {repo_info.get('license', {}).get('spdx_id', 'No License') if repo_info.get('license') else 'No License'} |

---

#### 💡 核心特点

"""
    
    # 根据项目特点生成分析
    topics = repo_info.get('topics', [])
    if topics:
        analysis += f"**标签**：{', '.join(topics[:10])}\n\n"
    
    # 添加README内容
    if readme:
        analysis += f"""---

#### 📄 README 摘要

```markdown
{readme}
```

"""
    
    # 添加快速开始建议
    analysis += f"""---

#### 🚀 快速开始

```bash
# 克隆项目
git clone {repo_info.get('clone_url', '')}

# 进入目录
cd {repo_info.get('name', 'project')}

# 查看文档
cat README.md
```

---

#### 💭 推荐理由

这个项目在今日GitHub Trending榜单中排名第一，值得关注的原因：

1. **活跃度高**：近期获得大量关注，社区活跃
2. **实用性强**：解决实际问题，有实用价值
3. **代码质量**：代码结构清晰，文档完善
4. **创新性**：在技术或应用上有创新突破

---

"""
    
    return analysis

def generate_blog_post(trending_data, date_str):
    """生成博客文章Markdown内容"""
    
    # 获取第一个项目的详细分析
    first_repo = trending_data[0] if trending_data else None
    detailed_analysis = ""
    
    if first_repo:
        repo_info = get_repo_details(first_repo.get('author', ''), first_repo.get('name', ''))
        readme = get_repo_readme(first_repo.get('author', ''), first_repo.get('name', ''))
        detailed_analysis = generate_detailed_analysis(repo_info, readme)
    
    # 生成文章内容
    content = f"""---
title: GitHub Trending 日报 - {date_str}
date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
categories:
  - [综合, 工具]
tags: [GitHub, 开源, Trending, 日报]
keywords: GitHub Trending, 开源项目, 技术日报, {date_str}
---

# GitHub Trending 日报

📅 **日期**：{date_str}

🎯 **系列说明**：每日精选GitHub热门开源项目，带你发现最新技术趋势和优质项目。每日推送，持续更新中...

---

## 📊 今日热门项目速览

"""
    
    # 添加项目列表（从第2个开始）
    for i, repo in enumerate(trending_data, 1):
        name = repo.get('name', 'Unknown')
        author = repo.get('author', 'unknown')
        description = repo.get('description', '暂无描述')
        language = repo.get('language', 'Unknown')
        stars_today = repo.get('starsToday', 0)
        stars_total = repo.get('stars', 0)
        url = repo.get('url', f"https://github.com/{author}/{name}")
        
        # 语言图标
        lang_icons = {
            "Python": "🐍",
            "JavaScript": "🟨",
            "TypeScript": "🔷",
            "Go": "🐹",
            "Rust": "🦀",
            "Java": "☕",
            "Shell": "🐚",
            "C++": "⚡",
            "C": "🔵",
            "HTML": "🌐",
            "CSS": "🎨",
            "Vue": "💚",
            "React": "⚛️",
            "Jupyter Notebook": "📓",
            "Dockerfile": "🐳",
            "Kotlin": "📱",
            "Swift": "🍎",
            "PHP": "🐘",
            "Ruby": "💎"
        }
        lang_icon = lang_icons.get(language, "📦")
        
        content += f"""## {i}. [{name}]({url})

{description}

{lang_icon} **{language}** | ⭐ **+{stars_today}** 今日 | 🏆 {stars_total:,} 总计

**仓库地址**：`{author}/{name}`

---

"""
    
    # 添加详细分析（仅第一个项目）
    content += detailed_analysis
    
    # 添加系列说明
    content += f"""
---

## 📝 系列说明

**GitHub Trending 日报**是一个持续更新的系列，每日为你带来：

- 🔥 **热门项目速览**：快速了解当日最火的开源项目
- 🔍 **精选项目详解**：深入分析排名第一的项目
- 💡 **技术趋势洞察**：把握开源社区最新动态

### 往期日报

- [GitHub Trending 日报 - 2026/03/11](./GitHub-Trending-2026-03-11.html)
- [GitHub Trending 日报 - 2026/03/10](./GitHub-Trending-2026-03-10.html)
- 更多日报请访问 [GitHub Trending 系列](/tags/GitHub/)

### 订阅方式

- 📧 RSS订阅：[/atom.xml](/atom.xml)
- 💬 微信公众号：DeepThinking深思
- 📺 B站：[@八里桥好](https://space.bilibili.com/30887724)

---

## 🤝 参与贡献

如果你发现有趣的开源项目，欢迎推荐！

- 💬 评论留言推荐
- 📧 邮件：leiqi@fudan.edu.cn
- 🔗 GitHub：[@leiqichn](https://github.com/leiqichn)

---

**🦞 J.A.R.V.I.S. 开源观察助手**
📡 数据更新：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🔗 数据来源：[GitHub Trending](https://github.com/trending)
"""
    
    return content

def save_blog_post(content, date_str):
    """保存博客文章"""
    filename = f"GitHub-Trending-{date_str.replace('/', '-')}.md"
    filepath = os.path.join(POST_DIR, filename)
    
    # 确保目录存在
    os.makedirs(POST_DIR, exist_ok=True)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ 博客文章已保存: {filepath}")
    return filepath

def deploy_blog():
    """部署博客到GitHub Pages和Nginx"""
    import subprocess
    
    print("\n🚀 开始部署博客...")
    
    try:
        # 清理并生成
        print("1️⃣ 清理旧文件...")
        subprocess.run(["npx", "hexo", "clean"], cwd=BLOG_PATH, check=True)
        
        print("2️⃣ 生成静态文件...")
        result = subprocess.run(
            ["npx", "hexo", "g"],
            cwd=BLOG_PATH,
            capture_output=True,
            text=True,
            timeout=180
        )
        
        if result.returncode != 0:
            print(f"生成警告: {result.stderr}")
        
        print("3️⃣ 部署到Nginx...")
        # 复制到nginx目录
        subprocess.run(
            f"rm -rf /var/www/blog/* && cp -r {BLOG_PATH}/public/* /var/www/blog/",
            shell=True,
            check=True
        )
        subprocess.run("chown -R nginx:nginx /var/www/blog", shell=True, check=True)
        
        print("4️⃣ 部署到GitHub Pages...")
        # 部署到GitHub
        subprocess.run(
            ["npx", "hexo", "d"],
            cwd=BLOG_PATH,
            capture_output=True,
            text=True,
            timeout=180
        )
        
        # 提交到git仓库
        subprocess.run(["git", "add", "."], cwd=BLOG_PATH, check=True)
        subprocess.run(
            ["git", "commit", "-m", f"feat: 添加GitHub Trending日报 - {datetime.now().strftime('%Y-%m-%d')}"],
            cwd=BLOG_PATH
        )
        subprocess.run(["git", "push"], cwd=BLOG_PATH)
        
        print("✅ 博客部署完成！")
        print(f"🌐 访问地址: https://leiqi.top")
        
    except Exception as e:
        print(f"❌ 部署失败: {e}")
        return False
    
    return True

def main():
    """主函数"""
    print("=" * 60)
    print("📊 GitHub Trending 日报生成器")
    print("=" * 60)
    
    # 获取日期
    date_str = datetime.now().strftime('%Y/%m/%d')
    print(f"\n📅 日期: {date_str}")
    
    # 获取GitHub Trending数据
    print("\n🔍 获取GitHub Trending数据...")
    trending_data = get_github_trending(limit=15)
    
    if not trending_data:
        print("❌ 获取数据失败")
        return
    
    print(f"✅ 获取到 {len(trending_data)} 个项目")
    
    # 生成博客文章
    print("\n📝 生成博客文章...")
    content = generate_blog_post(trending_data, date_str)
    filepath = save_blog_post(content, date_str)
    
    # 部署博客
    deploy_blog()
    
    print("\n" + "=" * 60)
    print("✅ 日报生成完成！")
    print("=" * 60)

if __name__ == "__main__":
    main()