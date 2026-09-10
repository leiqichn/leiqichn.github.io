---
title: 【Github Trending 日报】深度解析 - 2026/09/10
date: 2026-09-10 08:00:09
categories:
  - [综合, 工具]
tags: [GitHub, 开源, Trending, 日报]
keywords: GitHub Trending, 开源项目, 技术日报, 2026/09/10
---

# 【Github Trending 日报】深度解析

📅 **日期**：2026/09/10

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
                <h3 class="card-title"><a href="https://github.com/ayghri/i-have-adhd" target="_blank">i-have-adhd</a></h3>
            </div>
            <p class="card-desc">A skill to stop your coding agent from burying the answer. ADHD-friendly output.</p>
            <div class="card-meta">
                <span class="card-lang">🐍 Python</span>
                <span class="card-stars">⭐ +4650 今日</span>
                <span class="card-total">🏆 34,525</span>
            </div>
            <div class="card-repo">📦 ayghri/i-have-adhd</div>
            <div class="card-ai-insight">
                <details>
                    <summary>💡 分析</summary>
                    <div class="insight-content">这个项目意外走红，核心原因在于它精准戳中了大量开发者使用AI编程助手时的普遍痛点——AI常常给出冗长、绕弯子的答案，而ADHD群体或注意力容易分散的人尤其渴望直接、简洁、不埋没关键信息的输出。它本质上是一种“提示词技能”或输出规范，通过约束AI的表达方式（比如先用一句话说结论、避免铺垫、高亮关键点），显著提升了信息获取效率。

值得借鉴的地方是：项目从真实的用户认知特点出发，反向设计交互规范，这启发我们在开发任何工具或AI交互时，都应考虑不同人群的信息处理习惯，用“少即是多”的思维优化输出结构，甚至可以为用户提供可切换的“专注模式”或“极简模式”。此外，项目虽然小，但证明了聚焦一个细微但真实的需求，也能引发病毒式传播。</div>
                </details>
            </div>
        </div>
        <div class="trending-card">
            <div class="card-header">
                <span class="card-number">2</span>
                <h3 class="card-title"><a href="https://github.com/Tencent/teamai-cli" target="_blank">teamai-cli</a></h3>
            </div>
            <p class="card-desc">Make Every Team AI Native</p>
            <div class="card-meta">
                <span class="card-lang">🔷 TypeScript</span>
                <span class="card-stars">⭐ +556 今日</span>
                <span class="card-total">🏆 2,956</span>
            </div>
            <div class="card-repo">📦 Tencent/teamai-cli</div>
            <div class="card-ai-insight">
                <details>
                    <summary>💡 分析</summary>
                    <div class="insight-content">腾讯的 teamai-cli 之所以在 GitHub Trending 上快速升温，一方面得益于其“Make Every Team AI Native”的清晰定位，切中了当下团队协作与 AI 工具融合的热点需求；另一方面作为 Tencent 出品的 TypeScript 项目，天然带有大厂背书和可信度，加上 CLI 形态让开发者能快速在终端体验 AI 驱动的团队工作流，拉低了上手门槛。这个项目值得借鉴的地方在于它把 AI 能力从单点工具抽象为团队协作的基础设施，通过命令行封装成可复用的轻量接口，同时强调“原生”而非“外挂”的集成思路，为团队级 AI 落地提供了简洁而可扩展的范式。</div>
                </details>
            </div>
        </div>
        <div class="trending-card">
            <div class="card-header">
                <span class="card-number">3</span>
                <h3 class="card-title"><a href="https://github.com/obra/superpowers" target="_blank">superpowers</a></h3>
            </div>
            <p class="card-desc">An agentic skills framework & software development methodology that works.</p>
            <div class="card-meta">
                <span class="card-lang">🐚 Shell</span>
                <span class="card-stars">⭐ +688 今日</span>
                <span class="card-total">🏆 284,011</span>
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
                <span class="card-number">4</span>
                <h3 class="card-title"><a href="https://github.com/pascalorg/editor" target="_blank">editor</a></h3>
            </div>
            <p class="card-desc">Open-source 3D architectural editor with a local CLI, MCP tools, and practical workflows for humans and AI agents.</p>
            <div class="card-meta">
                <span class="card-lang">🔷 TypeScript</span>
                <span class="card-stars">⭐ +107 今日</span>
                <span class="card-total">🏆 22,898</span>
            </div>
            <div class="card-repo">📦 pascalorg/editor</div>
            <div class="card-ai-insight">
                <details>
                    <summary>💡 分析</summary>
                    <div class="insight-content">这个项目之所以在GitHub Trending上火起来，主要是因为它提供了一个轻量但功能完整的3D建筑设计编辑器，并且支持直接分享项目，满足了建筑师、设计师和爱好者快速可视化与协作的需求。值得借鉴的地方在于其采用TypeScript构建，保证了代码的可维护性和类型安全；同时通过将复杂的3D渲染与直观的UI结合，降低了非专业用户的使用门槛，这种“专业能力+易用性”的设计思路对同类工具的开发很有参考价值。</div>
                </details>
            </div>
        </div>
        <div class="trending-card">
            <div class="card-header">
                <span class="card-number">5</span>
                <h3 class="card-title"><a href="https://github.com/earthtojake/text-to-cad" target="_blank">text-to-cad</a></h3>
            </div>
            <p class="card-desc">A library of agent skills for CAD, CAE and CAM</p>
            <div class="card-meta">
                <span class="card-lang">🐍 Python</span>
                <span class="card-stars">⭐ +124 今日</span>
                <span class="card-total">🏆 15,023</span>
            </div>
            <div class="card-repo">📦 earthtojake/text-to-cad</div>
            <div class="card-ai-insight">
                <details>
                    <summary>💡 分析</summary>
                    <div class="insight-content">text-to-cad 能迅速登上 GitHub Trending，核心在于它精准地踩中了“大语言模型 + 工业设计”这个前沿交叉点——用户只需输入自然语言就能生成 CAD 模型，大幅拉低了传统三维建模和机器人硬件设计的学习门槛，让非专业用户也能快速参与设计。该项目最值得借鉴的是其“Agent Skills”模块化架构，它将复杂的工业设计流程拆解为可独立调用的技能单元，这种设计既方便开发者按需组合和扩展功能，也为其他垂直领域（如建筑、电气自动化）构建 AI 代理提供了清晰的复用范式。</div>
                </details>
            </div>
        </div>
        <div class="trending-card">
            <div class="card-header">
                <span class="card-number">6</span>
                <h3 class="card-title"><a href="https://github.com/cathrynlavery/diagram-design" target="_blank">diagram-design</a></h3>
            </div>
            <p class="card-desc">38 editorial diagram types for Claude Code, Codex, and Pi. Self-contained HTML + SVG. No shadows. No Mermaid slop.</p>
            <div class="card-meta">
                <span class="card-lang">🌐 HTML</span>
                <span class="card-stars">⭐ +2249 今日</span>
                <span class="card-total">🏆 36,560</span>
            </div>
            <div class="card-repo">📦 cathrynlavery/diagram-design</div>
            <div class="card-ai-insight">
                <details>
                    <summary>💡 分析</summary>
                    <div class="insight-content">这个项目在GitHub Trending上迅速走红，因为它精准抓住了AI编程工具生成图表时的痛点——提供了29种自带编辑级设计的HTML+SVG图表模板，彻底告别了Mermaid千篇一律的“塑料感”，让Claude Code能直接产出高颜值、无多余阴影的干净图表，恰好满足了开发者对AI输出审美升级的强烈需求。值得借鉴的地方在于它将“可复用的设计系统”与“提示工程”深度绑定，每个模板都是自包含的代码文件，既方便用户直接套用，又为AI提供了明确的风格约束，这种“以代码定义设计规范”的思路对任何AI辅助创作工具都很有参考价值。</div>
                </details>
            </div>
        </div>
        <div class="trending-card">
            <div class="card-header">
                <span class="card-number">7</span>
                <h3 class="card-title"><a href="https://github.com/TauricResearch/TradingAgents" target="_blank">TradingAgents</a></h3>
            </div>
            <p class="card-desc">TradingAgents: Multi-Agents LLM Financial Trading Framework</p>
            <div class="card-meta">
                <span class="card-lang">🐍 Python</span>
                <span class="card-stars">⭐ +367 今日</span>
                <span class="card-total">🏆 103,929</span>
            </div>
            <div class="card-repo">📦 TauricResearch/TradingAgents</div>
            <div class="card-ai-insight">
                <details>
                    <summary>💡 分析</summary>
                    <div class="insight-content">TradingAgents 之所以在 GitHub Trending 上迅速升温，核心在于它精准踩中了两个热门赛道：大语言模型（LLM）的多智能体协作，以及自动化金融交易。这个框架让多个 LLM 驱动的 Agent 分别承担市场分析、策略生成、风险控制等不同角色，通过对话和投票机制共同决策，展示了一种新颖且可落地的“AI 协同交易”范式，正好满足了开发者对 Agentic AI 应用在金融场景中的好奇心与实操需求。

项目最值得借鉴的地方是其模块化的 Agent 架构设计——它将复杂的交易流程拆解为独立的智能体单元，每个 Agent 配备专门的角色提示词、工具集和记忆能力，使得整个系统既灵活又可扩展。此外，它还内置了数据接入、回测引擎和风控模块，让开发者能快速上手验证交易策略，这种“架构清晰 + 实用闭环”的思路非常适合借鉴到其他需要多智能体协作的领域（如机器人控制、咨询分析等）。</div>
                </details>
            </div>
        </div>
        <div class="trending-card">
            <div class="card-header">
                <span class="card-number">8</span>
                <h3 class="card-title"><a href="https://github.com/liquidslr/system-design-notes" target="_blank">system-design-notes</a></h3>
            </div>
            <p class="card-desc">Notes of the book System Desgin Interview - An Insider's Guide</p>
            <div class="card-meta">
                <span class="card-lang">📦 Unknown</span>
                <span class="card-stars">⭐ +1397 今日</span>
                <span class="card-total">🏆 17,975</span>
            </div>
            <div class="card-repo">📦 liquidslr/system-design-notes</div>
            <div class="card-ai-insight">
                <details>
                    <summary>💡 分析</summary>
                    <div class="insight-content">这个项目能在GitHub Trending上飙升，主要是因为它精准切中了大量工程师准备系统设计面试的刚需——作者将经典书籍《System Design Interview》的要点整理成精简笔记，让读者无需通读原书就能快速掌握核心框架与案例，实用价值极高，因此迅速获得口碑传播。值得借鉴的是，它展示了“高质量个人学习笔记开源化”的巨大影响力：通过提炼知识、结构化组织并辅以自己的理解，就能形成对他人极具帮助的免费资源，同时也能反向促使作者本人持续深入思考，是一种极佳的学习输出方式。</div>
                </details>
            </div>
        </div>
        <div class="trending-card">
            <div class="card-header">
                <span class="card-number">9</span>
                <h3 class="card-title"><a href="https://github.com/openai/plugins" target="_blank">plugins</a></h3>
            </div>
            <p class="card-desc">OpenAI Plugins</p>
            <div class="card-meta">
                <span class="card-lang">🟨 JavaScript</span>
                <span class="card-stars">⭐ +498 今日</span>
                <span class="card-total">🏆 6,184</span>
            </div>
            <div class="card-repo">📦 openai/plugins</div>
            <div class="card-ai-insight">
                <details>
                    <summary>💡 分析</summary>
                    <div class="insight-content">这个项目作为OpenAI官方发布的插件系统参考实现，近期在GitHub Trending上热度上升主要是因为OpenAI生态的持续扩张和开发者对插件扩展机制的广泛兴趣，尤其是ChatGPT插件功能的开放吸引了大量尝鲜者。值得借鉴的地方在于其清晰展示了如何构建与OpenAI模型交互的外部工具接口，包括鉴权、API调用规范和插件元数据结构，为开发者快速集成第三方服务提供了标准化模板。</div>
                </details>
            </div>
        </div>
        <div class="trending-card">
            <div class="card-header">
                <span class="card-number">10</span>
                <h3 class="card-title"><a href="https://github.com/freestylefly/awesome-gpt-image-2" target="_blank">awesome-gpt-image-2</a></h3>
            </div>
            <p class="card-desc">Prompt as Code | GPT-Image2 工业级提示词引擎与模板库，530+ 个案例逆向工程，20+ 套工业级模板，并提炼出Skills，持续更新中</p>
            <div class="card-meta">
                <span class="card-lang">🟨 JavaScript</span>
                <span class="card-stars">⭐ +705 今日</span>
                <span class="card-total">🏆 30,016</span>
            </div>
            <div class="card-repo">📦 freestylefly/awesome-gpt-image-2</div>
            <div class="card-ai-insight">
                <details>
                    <summary>💡 分析</summary>
                    <div class="insight-content">这个项目之所以在GitHub Trending上火起来，是因为它精准踩中了GPT-4o图像生成功能爆发带来的巨大需求，通过“Prompt as Code”的工程化思路，将470多个真实案例逆向工程成可复用的模板与Skills，让用户无需摸索提示词就能直接产出高质量的工业级图片，实用价值极高。值得借鉴的地方在于它把零散的创意经验系统化、模块化，并用持续更新的方式构建社区粘性，同时用JavaScript实现工具链，降低了非AI从业者的使用门槛，这种“解法沉淀+模板化交付”的思路非常适合做工具类开源项目。</div>
                </details>
            </div>
        </div>
        <div class="trending-card">
            <div class="card-header">
                <span class="card-number">11</span>
                <h3 class="card-title"><a href="https://github.com/rohitg00/ai-engineering-from-scratch" target="_blank">ai-engineering-from-scratch</a></h3>
            </div>
            <p class="card-desc">Learn it. Build it. Ship it for others.</p>
            <div class="card-meta">
                <span class="card-lang">🐍 Python</span>
                <span class="card-stars">⭐ +343 今日</span>
                <span class="card-total">🏆 53,673</span>
            </div>
            <div class="card-repo">📦 rohitg00/ai-engineering-from-scratch</div>
            <div class="card-ai-insight">
                <details>
                    <summary>💡 分析</summary>
                    <div class="insight-content">这个项目之所以在GitHub Trending上大火，是因为它精准抓住了当下AI学习者的核心诉求——从零动手实践、真正把AI工程落地，而不仅仅是停留在理论或跑demo上。它的“Learn it. Build it. Ship it for others.”三阶段理念非常清晰，让初学者能沿着一条完整的路径从基础走到产出可交付的产品。值得借鉴的地方在于其高度的结构化和可操作性：每一个环节都配有代码和说明，不仅教你怎么写，还教你怎么部署和分享，这种端到端的工程化思维是很多教程欠缺的。</div>
                </details>
            </div>
        </div>
        <div class="trending-card">
            <div class="card-header">
                <span class="card-number">12</span>
                <h3 class="card-title"><a href="https://github.com/vastsa/PI-Desktop" target="_blank">PI-Desktop</a></h3>
            </div>
            <p class="card-desc">Local-first AI coding agent desktop: Electron + Rust host core + pi Agent Harness + user-installable plugins</p>
            <div class="card-meta">
                <span class="card-lang">🔷 TypeScript</span>
                <span class="card-stars">⭐ +417 今日</span>
                <span class="card-total">🏆 1,648</span>
            </div>
            <div class="card-repo">📦 vastsa/PI-Desktop</div>
            <div class="card-ai-insight">
                <details>
                    <summary>💡 分析</summary>
                    <div class="insight-content">PI-Desktop之所以在GitHub Trending上快速升温，既踩中了当前AI编程助手的热潮，又凭借“本地优先”的定位直击开发者对代码隐私和数据安全的痛点，同时Electron加Rust的混合架构与可插拔的Agent Harness设计，展现了在桌面端构建高性能、可扩展AI代理的完整思路。值得借鉴的是其将核心逻辑与宿主解耦、通过插件生态吸引第三方贡献的做法，既保证了底层执行效率，又降低了功能扩展的门槛，这种兼顾性能与灵活性的分层架构思路对同类桌面级AI工具很有参考价值。</div>
                </details>
            </div>
        </div>
        <div class="trending-card">
            <div class="card-header">
                <span class="card-number">13</span>
                <h3 class="card-title"><a href="https://github.com/affaan-m/ECC" target="_blank">ECC</a></h3>
            </div>
            <p class="card-desc">The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.</p>
            <div class="card-meta">
                <span class="card-lang">🟨 JavaScript</span>
                <span class="card-stars">⭐ +1133 今日</span>
                <span class="card-total">🏆 255,154</span>
            </div>
            <div class="card-repo">📦 affaan-m/ECC</div>
            <div class="card-ai-insight">
                <details>
                    <summary>💡 分析</summary>
                    <div class="insight-content">这个项目之所以在GitHub Trending上迅速走红，主要得益于它精准抓住了当前AI编程助手（如Claude Code、Codex、Cursor等）生态爆发的痛点——开发者需要一套高效、安全的“Agent harness”来协调多个AI工具的性能、记忆和安全策略，而ECC以模块化的“技能、本能、记忆、安全”框架提供了直接可用的优化方案。值得借鉴的地方在于它的设计思路：将AI代理的行为拆解为可独立迭代的原子能力（如安全校验、上下文记忆管理），并通过统一的性能监控层来适配不同底层模型，这种“松耦合+多平台兼容”的架构对于构建复杂的AI工作流非常有参考价值。</div>
                </details>
            </div>
        </div></div>{% endraw %}
---

## 🔍 今日精选项目：i-have-adhd

**项目地址**：[https://github.com/ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)

**作者**：ayghri

**描述**：A skill to stop your coding agent from burying the answer. ADHD-friendly output.

**语言**：Python

**今日新增星标**：+4650

**总星标数**：34,525

---

### 📝 深度分析

## 🎯 项目本质
其实质是一个针对编码 AI Agent（如 Claude Code）的**“上下文与输出约束规则文件”**。它的核心逻辑很纯粹：当 Agent 回答问题时，强制采用“结论优先、流程裁弯取直”的输出格式。它解决的是 AI 程序员在完成任务时，由于长输出和繁杂的解构逻辑，导致最关键的“答案”被淹没，从而给用户带来极高认知负荷的问题。

## 🔥 为什么火
它精准命中了当下 Agent 编码时代最痛的**“注意力稀缺”**痛点。AI 编程工具越来越强，但大模型的输出动辄几十行日志、计划与分析，这逼迫开发者进行“超长阅读”。项目名为“ADHD”，实际上抓住了所有渴望“秒懂结论”的普通人的诉求——今天的 656 星与 3 万+总量，证明了这是编码平权的需求，开发者渴望 AI 彻底倒逼机制遵守“断舍离”而非输出冗长的“流水账”。

## 💡 核心创新
技术内核并不是某一算法突破，而是**“认知友好型提示词工程”**。它利用极简的命令词与前置提示，将传统 `system prompt` 中的“允许你...”逆转为“禁用无意义推理层”，迫使输出侧进行“压缩率”和解构格式的重构。这是一次极有效的“后端软性逻辑内核”创新，把人类神经系统的阅读带宽转换成了 Agent 的刚性规范。

## 📈 可借鉴价值
对于个人开发者，这不仅是脚本，更是一面镜子。它印证了在 AI 原生开发中，**最强的代码不是计算逻辑，而是“元沟通规则”**。我们可以学会将自身的刚需（如注意力易碎、时间紧张）编译成 Prompt 规则，驱动 Agent 提供即拿即用的“速览”结果。真正有价值的开源，是深刻理解人类认知边界后，为机器言语“降噪”——这是每位 AI 使用者的必修课。

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

📡 数据更新：2026-09-10 08:00:46
🔗 数据来源：[GitHub Trending](https://github.com/trending)
