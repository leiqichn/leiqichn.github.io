
---
title: 【工具】7小时代码编写机器claude code 安装
date: 2025-07-30 00:24:23
modificationDate: 2025 July 30th Wednesday 00:24:34
categories:
  - [综合, 工具]
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


# 更换API

-   
    手动编辑配置文件
    

```
       # Stpe1: 编辑或创建 Claude Code 的配置文件
       # MacOS & Linux 为 `~/.claude/settings.json`
       # Windows 为`用户目录/.claude/settings.json`
       # `MINIMAX_API_KEY` 需替换为您的 MiniMax API Key
       # 环境变量 `ANTHROPIC_AUTH_TOKEN` 和 `ANTHROPIC_BASE_URL` 优先级高于配置文件
       {
         "env": {
           "ANTHROPIC_BASE_URL": "https://api.minimaxi.com/anthropic",
           "ANTHROPIC_AUTH_TOKEN": "MINIMAX_API_KEY",
           "API_TIMEOUT_MS": "3000000",
           "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": 1,
           "ANTHROPIC_MODEL": "MiniMax-M2.7",
           "ANTHROPIC_SMALL_FAST_MODEL": "MiniMax-M2.7",
           "ANTHROPIC_DEFAULT_SONNET_MODEL": "MiniMax-M2.7",
           "ANTHROPIC_DEFAULT_OPUS_MODEL": "MiniMax-M2.7",
           "ANTHROPIC_DEFAULT_HAIKU_MODEL": "MiniMax-M2.7"
         }
       }
       # Step2: 编辑或新增 `.claude.json` 文件
       # MacOS & Linux 为 `~/.claude.json`
       # Windows 为`用户目录/.claude.json`
       # 新增 `hasCompletedOnboarding` 参数
       {
         "hasCompletedOnboarding": true
       }
```
  
API 配置

- 使用 cc-switch（推荐）
    
- 手动编辑配置文件
    

[cc-switch](https://github.com/farion1231/cc-switch) 是一个便捷的工具，可以快速切换 Claude Code 的 API 配置。**1. 安装 cc-switch**

- macOS / Linux
    
- Windows
    

```
brew tap farion1231/ccswitch
brew install --cask cc-switch
brew upgrade --cask cc-switch
```

**2. 添加 MiniMax 配置**启动 cc-switch，点击右上角 **”+”** ，选择预设的 MiniMax 供应商，并填写您的 MiniMax API Key。![choose](https://filecdn.minimax.chat/public/0acbfee9-8871-4171-af19-e318476456a4.png)**3. 配置模型名称**将模型名称全部改为 `MiniMax-M2.7`，完成后点击右下角的 **“添加”**。![add](https://filecdn.minimax.chat/public/1ceadee0-5488-44a1-82bb-94af0fc8d3b7.png)**4. 启用配置**回到首页，点击 **“启用”** 即可开始使用。![start](https://filecdn.minimax.chat/public/0c5cbe27-1a6d-4583-9ad9-b48222055c3b.png)**5. 编辑配置文件**编辑或新增 `.claude.json` 文件，MacOS & Linux 为 `~/.claude.json`，Windows 为`用户目录/.claude.json`

```
# 新增 `hasCompletedOnboarding` 参数
{
  "hasCompletedOnboarding": true
}
```

启动 Claude Code

配置完成后，进入工作目录，在终端中运行 `claude` 命令以启动 Claude Code

# 安装skill 

### 安装 skill-creator

首先安装 Anthropic 的 skills 集合。

npx skills add https://github.com/anthropics/skills --skill skill-creator

或者：

claude install anthropics/skills/skill-creator

安装完成后，你就可以在 Claude 中调用：

/skill-creator

其他skills 安装，可以从github克隆

```

git clone https://github.com/titanwings/colleague-skill ~/.claude/skills/create-colleague
```


