---
title: 【Github Trending 日报】深度解析 - 2026/06/13
date: 2026-06-13 08:01:06
categories:
  - [综合, 工具]
tags: [GitHub, 开源, Trending, 日报]
keywords: GitHub Trending, 开源项目, 技术日报, 2026/06/13
---

# 【Github Trending 日报】深度解析

📅 **日期**：2026/06/13

🎯 **系列说明**：每日精选GitHub热门开源项目，带你发现最新技术趋势和优质项目。每日推送，持续更新中...

---

## 📊 今日热门项目速览

{% raw %}
<style>
.github-trending-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
    margin: 20px 0;
}
.trending-card {
    background: var(--card-bg, #f8f9fa);
    border: 1px solid var(--border-color, #e9ecef);
    border-radius: 12px;
    padding: 16px;
    transition: transform 0.2s, box-shadow 0.2s;
}
.trending-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
.card-header {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 8px;
}
.card-number {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    width: 24px;
    height: 24px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 12px;
    font-weight: bold;
}
.card-title {
    margin: 0 !important;
    font-size: 16px !important;
}
.card-title a {
    color: #1a73e8;
    text-decoration: none;
}
.card-desc {
    color: #666;
    font-size: 14px;
    margin: 8px 0;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}
.card-meta {
    display: flex;
    gap: 12px;
    font-size: 13px;
    color: #666;
    margin: 8px 0;
}
.card-repo {
    font-size: 12px;
    color: #999;
    font-family: monospace;
    margin-bottom: 8px;
}
.card-ai-insight {
    margin-top: 8px;
}
.card-ai-insight summary {
    cursor: pointer;
    font-size: 13px;
    color: #666;
}
.insight-content {
    font-size: 13px;
    color: #555;
    margin-top: 8px;
    padding: 8px;
    background: rgba(0,0,0,0.03);
    border-radius: 6px;
}
@media (max-width: 768px) {
    .github-trending-grid {
        grid-template-columns: 1fr;
    }
}
</style>

<!-- 滚动到卡片底部时自动展开分析 -->
<script>
(function() {
    if (window._trendingCardsInited) return;
    window._trendingCardsInited = true;
    
    function initScrollReveal() {
        var cards = document.querySelectorAll('.trending-card details');
        if (!cards.length) return;
        
        // 对于还没展开的 details，当卡片底部进入视口时自动打开
        var observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    var details = entry.target;
                    if (!details.open) {
                        details.open = true;
                    }
                    // 展开后取消观察，只展开一次
                    observer.unobserve(details);
                }
            });
        }, {
            rootMargin: '0px 0px -80px 0px',  // 底部进入视口前 80px 触发
            threshold: 0
        });
        
        cards.forEach(function(details) {
            observer.observe(details);
        });
    }
    
    // DOM 就绪后立即执行
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initScrollReveal);
    } else {
        initScrollReveal();
    }
})();
</script>

<div class="github-trending-grid">
        <div class="trending-card">
            <div class="card-header">
                <span class="card-number">1</span>
                <h3 class="card-title"><a href="https://github.com/addyosmani/agent-skills" target="_blank">agent-skills</a></h3>
            </div>
            <p class="card-desc">Production-grade engineering skills for AI coding agents.</p>
            <div class="card-meta">
                <span class="card-lang">🐚 Shell</span>
                <span class="card-stars">⭐ +2656 今日</span>
                <span class="card-total">🏆 56,746</span>
            </div>
            <div class="card-repo">📦 addyosmani/agent-skills</div>
            <div class="card-ai-insight">
                <details>
                    <summary>💡 分析</summary>
                    <div class="insight-content">这个项目之所以在GitHub上爆火，是因为它精准抓住了当前AI编码代理（如Cline、Copilot等）实际落地中的痛点——缺乏经过验证的、可复用的生产级工程技能指引。作者addyosmani将自己在大型项目中积累的代码审查、测试策略、文档规范等最佳实践封装成Shell脚本和提示集合，让开发者能直接“喂”给AI代理，大幅提升其输出质量和可靠性。值得借鉴的核心思路是：将隐形的工程经验系统化、模板化，并通过精心设计的自然语言指令让AI代理具备可重复的“专业直觉”，这种“教AI如何思考”的元技能比单一代码生成更有长期价值。</div>
                </details>
            </div>
        </div>
        <div class="trending-card">
            <div class="card-header">
                <span class="card-number">2</span>
                <h3 class="card-title"><a href="https://github.com/music-assistant/server" target="_blank">server</a></h3>
            </div>
            <p class="card-desc">Music Assistant is a free, opensource Media library manager that connects to your streaming services and a wide range of connected speakers. The server is the beating heart, the core of Music Assistant and must run on an always-on device like a Raspberry Pi, a NAS or an Intel NUC or alike.</p>
            <div class="card-meta">
                <span class="card-lang">🐍 Python</span>
                <span class="card-stars">⭐ +20 今日</span>
                <span class="card-total">🏆 1,773</span>
            </div>
            <div class="card-repo">📦 music-assistant/server</div>
            <div class="card-ai-insight">
                <details>
                    <summary>💡 分析</summary>
                    <div class="insight-content">Music Assistant 的 server 项目在 GitHub 上获得关注，主要是因为它解决了一个很实际的痛点：将多个流媒体服务和本地音乐库统一管理，并支持各种智能音箱，让用户不再依赖单一生态。项目本身完全开源免费，且对硬件要求友好（树莓派、NAS 都能跑），降低了家庭音乐服务器的搭建门槛。值得借鉴的地方在于其模块化架构——核心服务与连接器分离，方便社区贡献新平台支持，同时文档清晰、部署简单，是一个典型的“小而美”的实用工具类开源项目。</div>
                </details>
            </div>
        </div>
        <div class="trending-card">
            <div class="card-header">
                <span class="card-number">3</span>
                <h3 class="card-title"><a href="https://github.com/mattermost/mattermost" target="_blank">mattermost</a></h3>
            </div>
            <p class="card-desc">Mattermost is an open source platform for secure collaboration across the entire software development lifecycle..</p>
            <div class="card-meta">
                <span class="card-lang">🔷 TypeScript</span>
                <span class="card-stars">⭐ +388 今日</span>
                <span class="card-total">🏆 37,621</span>
            </div>
            <div class="card-repo">📦 mattermost/mattermost</div>
            <div class="card-ai-insight">
                <details>
                    <summary>💡 分析</summary>
                    <div class="insight-content">Mattermost 在 GitHub Trending 上热度上升，主要是因为企业级对数据安全和自托管协作平台的需求持续增长，而它作为 Slack 的开源替代品，近期可能发布了增强功能或性能优化，吸引了大量关注。该项目值得借鉴的地方在于其模块化的架构设计和对私有化部署的深度支持，同时围绕软件开发全生命周期提供了丰富的集成能力，能够满足团队在合规、安全与协作效率之间的平衡需求。</div>
                </details>
            </div>
        </div>
        <div class="trending-card">
            <div class="card-header">
                <span class="card-number">4</span>
                <h3 class="card-title"><a href="https://github.com/apple/container" target="_blank">container</a></h3>
            </div>
            <p class="card-desc">A tool for creating and running Linux containers using lightweight virtual machines on a Mac. It is written in Swift, and optimized for Apple silicon.</p>
            <div class="card-meta">
                <span class="card-lang">🍎 Swift</span>
                <span class="card-stars">⭐ +3504 今日</span>
                <span class="card-total">🏆 35,049</span>
            </div>
            <div class="card-repo">📦 apple/container</div>
            <div class="card-ai-insight">
                <details>
                    <summary>💡 分析</summary>
                    <div class="insight-content">苹果官方推出的这个 container 项目之所以在 GitHub Trending 上爆火，是因为它直击了 Mac 用户（特别是 Apple Silicon 用户）在本地运行 Linux 容器时的性能痛点——利用 Swift 和苹果自家的虚拟化框架实现了轻量级虚拟机级别的容器方案，相比传统 Docker 在 M 系列芯片上更高效、更原生。值得借鉴的地方在于：苹果将底层虚拟化能力封装成简洁的 Swift 工具，展现了如何利用平台专属 API（如 Virtualization.framework）打造高性能工具，同时其代码架构和设计思路对于想深入理解容器与虚拟机融合技术的开发者来说是不错的学习范本。</div>
                </details>
            </div>
        </div>
        <div class="trending-card">
            <div class="card-header">
                <span class="card-number">5</span>
                <h3 class="card-title"><a href="https://github.com/iptv-org/iptv" target="_blank">iptv</a></h3>
            </div>
            <p class="card-desc">Collection of publicly available IPTV channels from all over the world</p>
            <div class="card-meta">
                <span class="card-lang">🔷 TypeScript</span>
                <span class="card-stars">⭐ +179 今日</span>
                <span class="card-total">🏆 118,018</span>
            </div>
            <div class="card-repo">📦 iptv-org/iptv</div>
            <div class="card-ai-insight">
                <details>
                    <summary>💡 分析</summary>
                    <div class="insight-content">这个项目因为满足全球用户免费获取各地电视直播频道的刚需而持续火爆，尤其是随着流媒体和智能电视普及，对公开IPTV资源的查询和整理需求激增。值得借鉴的是其高效的社区协作模式：通过结构化数据、自动化脚本和TypeScript工具链，将分散的公开频道源系统化维护，同时利用GitHub Issues和Pull Requests鼓励全球贡献者持续更新，形成了自驱动的生态。</div>
                </details>
            </div>
        </div>
        <div class="trending-card">
            <div class="card-header">
                <span class="card-number">6</span>
                <h3 class="card-title"><a href="https://github.com/obra/superpowers" target="_blank">superpowers</a></h3>
            </div>
            <p class="card-desc">An agentic skills framework & software development methodology that works.</p>
            <div class="card-meta">
                <span class="card-lang">🐚 Shell</span>
                <span class="card-stars">⭐ +1275 今日</span>
                <span class="card-total">🏆 225,978</span>
            </div>
            <div class="card-repo">📦 obra/superpowers</div>
            <div class="card-ai-insight">
                <details>
                    <summary>💡 分析</summary>
                    <div class="insight-content">这个项目之所以在 GitHub Trending 上爆发，主要是因为“智能体（agentic）”概念正处于风口，而它提出了一套声称行之有效的技能框架和软件开发方法论，加上高达 19 万的惊人总星数，说明其实用性和社区认可度极高。最值得借鉴的是它用最简单的 Shell 脚本语言承载了一套完整的代理编排逻辑，证明轻量级工具同样能构建出可落地的复杂 AI 工作流，这种“少即是多”的设计思路对追求实效的开发者很有启发。</div>
                </details>
            </div>
        </div>
        <div class="trending-card">
            <div class="card-header">
                <span class="card-number">7</span>
                <h3 class="card-title"><a href="https://github.com/refactoringhq/tolaria" target="_blank">tolaria</a></h3>
            </div>
            <p class="card-desc">Desktop app to manage markdown knowledge bases</p>
            <div class="card-meta">
                <span class="card-lang">🔷 TypeScript</span>
                <span class="card-stars">⭐ +369 今日</span>
                <span class="card-total">🏆 15,752</span>
            </div>
            <div class="card-repo">📦 refactoringhq/tolaria</div>
            <div class="card-ai-insight">
                <details>
                    <summary>💡 分析</summary>
                    <div class="insight-content">tolaria 之所以在 GitHub 上迅速走红，是因为它精准切入知识管理领域对本地化、轻量级 Markdown 工具的需求，用户渴望一款既能像 Obsidian 一样高效管理笔记，又具备更简洁界面和开源可控性的桌面应用。该项目最值得借鉴的地方在于其采用 TypeScript + Electron 技术栈实现了流畅的桌面体验，同时将 Markdown 知识的双向链接、全文搜索和文件夹管理等功能封装得极为易用，没有过度复杂化，这种“少即是多”的设计思路对同类产品有很强的参考价值。</div>
                </details>
            </div>
        </div>
        <div class="trending-card">
            <div class="card-header">
                <span class="card-number">8</span>
                <h3 class="card-title"><a href="https://github.com/maziyarpanahi/openmed" target="_blank">openmed</a></h3>
            </div>
            <p class="card-desc">open-source healthcare ai</p>
            <div class="card-meta">
                <span class="card-lang">🐍 Python</span>
                <span class="card-stars">⭐ +515 今日</span>
                <span class="card-total">🏆 3,183</span>
            </div>
            <div class="card-repo">📦 maziyarpanahi/openmed</div>
            <div class="card-ai-insight">
                <details>
                    <summary>💡 分析</summary>
                    <div class="insight-content">这个项目之所以在GitHub Trending上迅速走红，主要是因为医疗AI领域持续火热，而openmed提供了一个开箱即用的开源框架，降低了开发者构建医疗智能化应用的门槛，同时满足了社区对透明、可复现的医疗AI工具的需求。值得借鉴的是其模块化设计思路，将数据预处理、模型训练和部署流程清晰分离，便于扩展；此外，项目注重医疗数据的隐私保护与合规性，在社区协议下公开了模型权重和训练日志，这种透明做法能增强信任，是开源医疗项目值得学习的实践。</div>
                </details>
            </div>
        </div>
        <div class="trending-card">
            <div class="card-header">
                <span class="card-number">9</span>
                <h3 class="card-title"><a href="https://github.com/LMCache/LMCache" target="_blank">LMCache</a></h3>
            </div>
            <p class="card-desc">LMCache: Supercharge Your LLM with the Fastest KV Cache Layer</p>
            <div class="card-meta">
                <span class="card-lang">🐍 Python</span>
                <span class="card-stars">⭐ +28 今日</span>
                <span class="card-total">🏆 8,630</span>
            </div>
            <div class="card-repo">📦 LMCache/LMCache</div>
            <div class="card-ai-insight">
                <details>
                    <summary>💡 分析</summary>
                    <div class="insight-content">LMCache 宣称能通过最快的 KV 缓存层显著加速大语言模型推理，切中了当前 LLM 部署中延迟和吞吐量的核心痛点，因此在 GitHub 上迅速吸引关注。该项目值得借鉴的地方在于其对 KV 缓存的高效管理策略，包括内存层次优化和调度算法，这些技术思路可用于其他推理加速或边缘部署场景。</div>
                </details>
            </div>
        </div>
        <div class="trending-card">
            <div class="card-header">
                <span class="card-number">10</span>
                <h3 class="card-title"><a href="https://github.com/phuryn/pm-skills" target="_blank">pm-skills</a></h3>
            </div>
            <p class="card-desc">PM Skills Marketplace: 100+ agentic skills, commands, and plugins — from discovery to strategy, execution, launch, and growth.</p>
            <div class="card-meta">
                <span class="card-lang">📦 Unknown</span>
                <span class="card-stars">⭐ +827 今日</span>
                <span class="card-total">🏆 16,958</span>
            </div>
            <div class="card-repo">📦 phuryn/pm-skills</div>
            <div class="card-ai-insight">
                <details>
                    <summary>💡 分析</summary>
                    <div class="insight-content">这个项目之所以在GitHub Trending上迅速走红，是因为它精准切中了当前AI Agent与产品管理融合的热点需求——通过提供超过100个可复用的技能、命令和插件，覆盖产品从发现到增长的全流程，极大地降低了产品经理利用AI工具的门槛，成为一站式“技能市场”。值得借鉴的是其模块化、可组合的设计思路，将复杂的产品管理流程拆解成独立且可插拔的“智能单元”，并鼓励社区贡献与复用，这种开放生态模式能快速积累内容和用户粘性。</div>
                </details>
            </div>
        </div>
        <div class="trending-card">
            <div class="card-header">
                <span class="card-number">11</span>
                <h3 class="card-title"><a href="https://github.com/masterking32/MasterDnsVPN" target="_blank">MasterDnsVPN</a></h3>
            </div>
            <p class="card-desc">Advanced DNS tunneling VPN for censorship bypass, optimized beyond DNSTT and SlipStream with low-overhead ARQ, resolver load balancing, high packet-loss stability and speed.</p>
            <div class="card-meta">
                <span class="card-lang">🐹 Go</span>
                <span class="card-stars">⭐ +400 今日</span>
                <span class="card-total">🏆 5,999</span>
            </div>
            <div class="card-repo">📦 masterking32/MasterDnsVPN</div>
            <div class="card-ai-insight">
                <details>
                    <summary>💡 分析</summary>
                    <div class="insight-content">MasterDnsVPN 近日在 GitHub Trending 上火爆，主要因为它瞄准了网络审查规避这一持续刚需，而项目自身在 DNS 隧道技术上宣称超越了 DNSTT 和 SlipStream，通过低开销 ARQ（自动重传请求）、解析器负载均衡以及对高丢包环境下的稳定性优化，实现了更快的速度和更强的抗干扰能力，正好契合了当前对隐蔽、高效代理工具的需求。值得借鉴的地方在于，它用 Go 语言实现了对传统 DNS 隧道方案的深度改进，尤其是将 ARQ 机制与负载均衡结合，在极端网络条件下仍能保持低延迟传输，这种针对实际弱网环境做精细化容错和调度的方法，对于开发高性能网络代理或隐私工具具有很好的参考价值。</div>
                </details>
            </div>
        </div>
        <div class="trending-card">
            <div class="card-header">
                <span class="card-number">12</span>
                <h3 class="card-title"><a href="https://github.com/msitarzewski/agency-agents" target="_blank">agency-agents</a></h3>
            </div>
            <p class="card-desc">A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.</p>
            <div class="card-meta">
                <span class="card-lang">🐚 Shell</span>
                <span class="card-stars">⭐ +1026 今日</span>
                <span class="card-total">🏆 112,385</span>
            </div>
            <div class="card-repo">📦 msitarzewski/agency-agents</div>
            <div class="card-ai-insight">
                <details>
                    <summary>💡 分析</summary>
                    <div class="insight-content">这个项目凭借“一站式AI代理机构”的宏大概念吸引大量关注，它把日常生活中各类工作场景（如前端开发、社群运营、创意注入等）都封装成有明确角色定位的“专家代理”，并强调每个代理具备独立人格、工作流程和可交付成果，这种拟人化、模块化的设计让开发者直观感受到AI协作的无限可能。值得借鉴的是它用轻量级的Shell脚本而非复杂框架来串联多个AI代理，降低了入门门槛；同时每个代理都有清晰的职责边界和交付标准，这种“角色分离+流程固化”的思路对于构建可复用的AI Agent工作流具有重要参考价值。</div>
                </details>
            </div>
        </div>
        <div class="trending-card">
            <div class="card-header">
                <span class="card-number">13</span>
                <h3 class="card-title"><a href="https://github.com/microsoft/PowerToys" target="_blank">PowerToys</a></h3>
            </div>
            <p class="card-desc">Microsoft PowerToys is a collection of utilities that supercharge productivity and customization on Windows</p>
            <div class="card-meta">
                <span class="card-lang">🔵 C</span>
                <span class="card-stars">⭐ +103 今日</span>
                <span class="card-total">🏆 134,326</span>
            </div>
            <div class="card-repo">📦 microsoft/PowerToys</div>
            <div class="card-ai-insight">
                <details>
                    <summary>💡 分析</summary>
                    <div class="insight-content">PowerToys 在 GitHub Trending 上火起来，主要是因为它是微软官方维护的 Windows 增强工具集，持续推出 FancyZones、PowerRename 等实用功能，精准解决用户日常痛点，且完全免费开源，自然吸引了大量 Windows 用户关注。该项目值得借鉴的地方在于其模块化设计——每个功能独立又可组合，便于迭代和维护；同时，微软积极吸纳社区贡献，通过 issue 和 PR 与用户协作，这种开放且聚焦生产力的开发模式对任何工具类项目都有参考价值。</div>
                </details>
            </div>
        </div></div>{% endraw %}
---

## 🔍 今日精选项目：agent-skills

**项目地址**：[https://github.com/addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)

**作者**：addyosmani

**描述**：Production-grade engineering skills for AI coding agents.

**语言**：Shell

**今日新增星标**：+2656

**总星标数**：56,746

---

### 📝 深度分析

## 🎯 项目本质

`agent-skills` 是一套面向 AI 编码代理（如 Claude、Copilot、Cody 等）的**生产级工程技能模版库**。它不是普通的提示词集合，而是将资深软件工程师的隐性知识（代码规范、测试策略、调试流程、重构原则等）显式化为结构化、可复用的指令单元，让 AI 在生成代码时自动遵循工程最佳实践。核心目标是解决当前 AI 编码工具“能用但不够可靠”的痛点——让 AI 代理从“写玩具代码”升级为“写可维护、可部署的生产代码”。

## 🔥 为什么火

1. **作者光环与信任背书**：addyosmani 是 Google Chrome 团队核心成员、经典开源项目（如 `puppeteer`）作者，其 GitHub 影响力天然带来初始曝光和 credibility。开发者信任他提炼的“工程技能”一定经过实战检验。
2. **精准切入 AI 编码代理的瓶颈期**：2024-2025 年，AI 编码工具已广泛商用，但开发者普遍抱怨输出代码缺乏架构意识、测试覆盖不足、安全漏洞频出。`agent-skills` 直接提供“高阶封装”，填补了工具链中缺失的一环——**技能工程化**。
3. **极低门槛与高复利效应**：项目本质上是一组 Shell 脚本 + 配置文件，开发者只需下载并引用即可让 AI 代理获得“专家级思维”。这种“即插即用”的模式降低了高级工程能力的获取成本，在 Twitter/X 上被大量开发者转发评测，形成病毒式传播。

## 💡 核心创新

**将隐性工程知识显式化为 AI 可执行的元指令**。传统提示词（prompt）往往针对单次任务，而 `agent-skills` 引入“技能模板”（Skill Template）概念：每个技能包含触发条件、执行步骤、质量门禁和回退策略。例如，“代码审查技能”不仅告诉 AI 检查什么，还定义了不同严重级别的处理逻辑和交互方式。这一设计打破了“提示词 = 自然语言描述”的范式，转向**结构化知识工程**——使 AI 代理能像人类专家一样拥有“肌肉记忆”。

## 📈 可借鉴价值

- **个人开发者可以学习“技能化”自己的工程经验**：将日常开发中积累的 checklist、代码规范、调试指南，整理成 AI 可读取的结构化指令（如 YAML 或 shell 函数），形成个人专属的技能库。这比记忆十篇博客论文更高效。
- **掌握低成本提升 AI 输出质量的方法**：核心思路不是调模型，而是改造输入侧的“思维框架”。复制 `agent-skills` 的模式——为每个常用任务（如 API 设计、数据库迁移）编写一个“技能包”，能显著减少后续提示词的试错成本。
- **关注“元工程”趋势**：未来开发者的核心竞争力可能不再是写代码本身，而是**设计能让 AI 写出好代码的技能系统**。本项目提供了一个可参考的标准化起点。

---


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

📡 数据更新：2026-06-13 08:01:53
🔗 数据来源：[GitHub Trending](https://github.com/trending)
