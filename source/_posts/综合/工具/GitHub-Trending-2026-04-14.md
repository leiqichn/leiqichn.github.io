---
title: GitHub Trending 日报 - 2026/04/14
date: 2026-04-14 13:12:52
categories:
  - [综合, 工具]
tags: [GitHub, 开源, Trending]
---

# GitHub Trending 日报

📅 **日期**：2026/04/14

---

## 1. [andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)

A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.

📌 **中文摘要**：[plugins] feishu_doc: Registered feishu_doc, feishu_app_scopes
[plugins] feishu_chat: Registered feishu_chat tool
[plugins] feishu_wiki: Registered feishu_wiki tool
[plugins] feishu_drive: Registered feishu_drive tool
[plugins] feishu_bitable: Registered bitable tools
[plugins] [adp-openclaw] Plugin register() called
[plugins] [adp-openclaw] Plugin registration complete
[plugins] [memory-tdai] Registering plugin ... startTimestamp=1776143589175 (2026-04-14T05:13:09.175Z)
[plugins] [memory-tdai] Config parsed: capture=true, recall=true(maxResults=5), extraction=true(dedup=true, maxMem=10), pipeline=(everyN=5, warmup=true, l1Idle=60s, l2DelayAfterL1=90s, l2Min=300s, l2Max=1800s, activeWindow=24h), persona(triggerEvery=50, backupCount=3, sceneBackupCount=10), memoryCleanup(enabled=false, retentionDays=(disabled), cleanTime=03:00, l0Dir=conversations, l1Dir=records)
[plugins] [memory-tdai] Data dir: /root/.openclaw/memory-tdai (all subdirectories initialized)
[plugins] [memory-tdai] Memory cleaner disabled (retentionDays not configured)
[plugins] [memory-tdai] Registering before_prompt_build hook (auto-recall)
[plugins] [memory-tdai] Embedding disabled by config, VectorStore will serve as metadata-only store
[plugins] [memory-tdai][vector-store] FTS5 tables initialized (l1_fts, l0_fts) [schema v2 — jieba segmented]
[plugins] [memory-tdai][vector-store] Initialized (dimensions=0)
[plugins] [memory-tdai] VectorStore initialized: /root/.openclaw/memory-tdai/vectors.db (0D, provider=none)
[plugins] [memory-tdai] [pipeline] Initialized: everyNConversations=5, warmup=enabled, l1IdleTimeout=60s, l2DelayAfterL1=90s, l2MinInterval=300s, l2MaxInterval=1800s, sessionActiveWindow=24h
[plugins] [memory-tdai] Registering agent_end hook (auto-capture)
[plugins] [memory-tdai] Plugin registration complete (v3). startTimestamp=1776143589175 (2026-04-14T05:13:09.175Z)
[plugins] [memory-tdai] [before_prompt_build] Recall complete (128ms), appendSystemContext=5474 chars
[plugins] [memory-tdai] [pipeline] Restored 18 session state(s) from checkpoint
[plugins] [memory-tdai] [pipeline] Pipeline started
[plugins] [memory-tdai] Scheduler lazy-started on first agent_end (everyN=5, l1Idle=60s, l2DelayAfterL1=90s, l2MinInterval=300s, l2MaxInterval=1800s, sessionActiveWindow=24h)
[plugins] [memory-tdai] [runner] loadRunEmbeddedPiAgent: dist/ import OK (6ms)
[plugins] [memory-tdai] [capture] ⏱ Capture timing: total=73ms, l0Record+checkpoint=51ms, l0VecIndex=18ms (embed=0ms, upsert=18ms, msgs=2), notify=3ms
[plugins] [memory-tdai] [agent_end] Auto-capture complete (83ms), l0Recorded=2, schedulerNotified=true
forrestchang/andrej-karpathy-skills 项目提供 Andrej Karpathy 启发的编程最佳实践，强调编程的简洁性和效率，包含提升代码质量和性能指南。该项目获得超过 13,000 星标，深受开发者关注。

📦 **未知** | ⭐ **+733** 今日 | 🏆 26,789 总计

**仓库地址**：`forrestchang/andrej-karpathy-skills`

---

## 2. [hermes-agent](https://github.com/NousResearch/hermes-agent)

The agent that grows with you

📌 **中文摘要**：[plugins] feishu_doc: Registered feishu_doc, feishu_app_scopes
[plugins] feishu_chat: Registered feishu_chat tool
[plugins] feishu_wiki: Registered feishu_wiki tool
[plugins] feishu_drive: Registered feishu_drive tool
[plugins] feishu_bitable: Registered bitable tools
[plugins] [adp-openclaw] Plugin register() called
[plugins] [adp-openclaw] Plugin registration complete
[plugins] [memory-tdai] Registering plugin ... startTimestamp=1776143620003 (2026-04-14T05:13:40.003Z)
[plugins] [memory-tdai] Config parsed: capture=true, recall=true(maxResults=5), extraction=true(dedup=true, maxMem=10), pipeline=(everyN=5, warmup=true, l1Idle=60s, l2DelayAfterL1=90s, l2Min=300s, l2Max=1800s, activeWindow=24h), persona(triggerEvery=50, backupCount=3, sceneBackupCount=10), memoryCleanup(enabled=false, retentionDays=(disabled), cleanTime=03:00, l0Dir=conversations, l1Dir=records)
[plugins] [memory-tdai] Data dir: /root/.openclaw/memory-tdai (all subdirectories initialized)
[plugins] [memory-tdai] Memory cleaner disabled (retentionDays not configured)
[plugins] [memory-tdai] Registering before_prompt_build hook (auto-recall)
[plugins] [memory-tdai] Embedding disabled by config, VectorStore will serve as metadata-only store
[plugins] [memory-tdai][vector-store] FTS5 tables initialized (l1_fts, l0_fts) [schema v2 — jieba segmented]
[plugins] [memory-tdai][vector-store] Initialized (dimensions=0)
[plugins] [memory-tdai] VectorStore initialized: /root/.openclaw/memory-tdai/vectors.db (0D, provider=none)
[plugins] [memory-tdai] [pipeline] Initialized: everyNConversations=5, warmup=enabled, l1IdleTimeout=60s, l2DelayAfterL1=90s, l2MinInterval=300s, l2MaxInterval=1800s, sessionActiveWindow=24h
[plugins] [memory-tdai] Registering agent_end hook (auto-capture)
[plugins] [memory-tdai] Plugin registration complete (v3). startTimestamp=1776143620003 (2026-04-14T05:13:40.003Z)
[plugins] [memory-tdai] [before_prompt_build] Recall complete (127ms), appendSystemContext=5474 chars
[plugins] [memory-tdai] [pipeline] Restored 18 session state(s) from checkpoint
[plugins] [memory-tdai] [pipeline] Pipeline started
[plugins] [memory-tdai] Scheduler lazy-started on first agent_end (everyN=5, l1Idle=60s, l2DelayAfterL1=90s, l2MinInterval=300s, l2MaxInterval=1800s, sessionActiveWindow=24h)
[plugins] [memory-tdai] [runner] loadRunEmbeddedPiAgent: dist/ import OK (7ms)
[plugins] [memory-tdai] [capture] ⏱ Capture timing: total=61ms, l0Record+checkpoint=45ms, l0VecIndex=13ms (embed=0ms, upsert=12ms, msgs=2), notify=2ms
[plugins] [memory-tdai] [agent_end] Auto-capture complete (67ms), l0Recorded=2, schedulerNotified=true
Hermes Agent 是 Nous Research 的开源 AI 框架，通过自我改进循环实现学习和进化，允许开发者针对各种应用场景自定义和扩展其能力。

🐍 **Python** | ⭐ **+289** 今日 | 🏆 79,198 总计

**仓库地址**：`NousResearch/hermes-agent`

---

## 3. [Kronos](https://github.com/shiyu-coder/Kronos)

Kronos: A Foundation Model for the Language of Financial Markets

📌 **中文摘要**：[plugins] feishu_doc: Registered feishu_doc, feishu_app_scopes
[plugins] feishu_chat: Registered feishu_chat tool
[plugins] feishu_wiki: Registered feishu_wiki tool
[plugins] feishu_drive: Registered feishu_drive tool
[plugins] feishu_bitable: Registered bitable tools
[plugins] [adp-openclaw] Plugin register() called
[plugins] [adp-openclaw] Plugin registration complete
[plugins] [memory-tdai] Registering plugin ... startTimestamp=1776143650126 (2026-04-14T05:14:10.126Z)
[plugins] [memory-tdai] Config parsed: capture=true, recall=true(maxResults=5), extraction=true(dedup=true, maxMem=10), pipeline=(everyN=5, warmup=true, l1Idle=60s, l2DelayAfterL1=90s, l2Min=300s, l2Max=1800s, activeWindow=24h), persona(triggerEvery=50, backupCount=3, sceneBackupCount=10), memoryCleanup(enabled=false, retentionDays=(disabled), cleanTime=03:00, l0Dir=conversations, l1Dir=records)
[plugins] [memory-tdai] Data dir: /root/.openclaw/memory-tdai (all subdirectories initialized)
[plugins] [memory-tdai] Memory cleaner disabled (retentionDays not configured)
[plugins] [memory-tdai] Registering before_prompt_build hook (auto-recall)
[plugins] [memory-tdai] Embedding disabled by config, VectorStore will serve as metadata-only store
[plugins] [memory-tdai][vector-store] FTS5 tables initialized (l1_fts, l0_fts) [schema v2 — jieba segmented]
[plugins] [memory-tdai][vector-store] Initialized (dimensions=0)
[plugins] [memory-tdai] VectorStore initialized: /root/.openclaw/memory-tdai/vectors.db (0D, provider=none)
[plugins] [memory-tdai] [pipeline] Initialized: everyNConversations=5, warmup=enabled, l1IdleTimeout=60s, l2DelayAfterL1=90s, l2MinInterval=300s, l2MaxInterval=1800s, sessionActiveWindow=24h
[plugins] [memory-tdai] Registering agent_end hook (auto-capture)
[plugins] [memory-tdai] Plugin registration complete (v3). startTimestamp=1776143650126 (2026-04-14T05:14:10.126Z)
[plugins] [memory-tdai] [before_prompt_build] Recall complete (129ms), appendSystemContext=5474 chars
[plugins] [memory-tdai] [pipeline] Restored 18 session state(s) from checkpoint
[plugins] [memory-tdai] [pipeline] Pipeline started
[plugins] [memory-tdai] Scheduler lazy-started on first agent_end (everyN=5, l1Idle=60s, l2DelayAfterL1=90s, l2MinInterval=300s, l2MaxInterval=1800s, sessionActiveWindow=24h)
[plugins] [memory-tdai] [runner] loadRunEmbeddedPiAgent: dist/ import OK (7ms)
[plugins] [memory-tdai] [capture] ⏱ Capture timing: total=80ms, l0Record+checkpoint=54ms, l0VecIndex=23ms (embed=0ms, upsert=22ms, msgs=2), notify=3ms
[plugins] [memory-tdai] [agent_end] Auto-capture complete (88ms), l0Recorded=2, schedulerNotified=true
Kronos 是一个量化交易项目，模型参数规模涵盖 40 亿级别。它包含专用的金融数据分词器，旨在提升研究工作流和评估效率。该项目专注于 IC/RankIC 指标，不涉及直接预测 K 线走势的表述。

🐍 **Python** | ⭐ **+554** 今日 | 🏆 17,193 总计

**仓库地址**：`shiyu-coder/Kronos`

---

## 4. [claude-mem](https://github.com/thedotmack/claude-mem)

A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

📌 **中文摘要**：[plugins] feishu_doc: Registered feishu_doc, feishu_app_scopes
[plugins] feishu_chat: Registered feishu_chat tool
[plugins] feishu_wiki: Registered feishu_wiki tool
[plugins] feishu_drive: Registered feishu_drive tool
[plugins] feishu_bitable: Registered bitable tools
[plugins] [adp-openclaw] Plugin register() called
[plugins] [adp-openclaw] Plugin registration complete
[plugins] [memory-tdai] Registering plugin ... startTimestamp=1776143680705 (2026-04-14T05:14:40.705Z)
[plugins] [memory-tdai] Config parsed: capture=true, recall=true(maxResults=5), extraction=true(dedup=true, maxMem=10), pipeline=(everyN=5, warmup=true, l1Idle=60s, l2DelayAfterL1=90s, l2Min=300s, l2Max=1800s, activeWindow=24h), persona(triggerEvery=50, backupCount=3, sceneBackupCount=10), memoryCleanup(enabled=false, retentionDays=(disabled), cleanTime=03:00, l0Dir=conversations, l1Dir=records)
[plugins] [memory-tdai] Data dir: /root/.openclaw/memory-tdai (all subdirectories initialized)
[plugins] [memory-tdai] Memory cleaner disabled (retentionDays not configured)
[plugins] [memory-tdai] Registering before_prompt_build hook (auto-recall)
[plugins] [memory-tdai] Embedding disabled by config, VectorStore will serve as metadata-only store
[plugins] [memory-tdai][vector-store] FTS5 tables initialized (l1_fts, l0_fts) [schema v2 — jieba segmented]
[plugins] [memory-tdai][vector-store] Initialized (dimensions=0)
[plugins] [memory-tdai] VectorStore initialized: /root/.openclaw/memory-tdai/vectors.db (0D, provider=none)
[plugins] [memory-tdai] [pipeline] Initialized: everyNConversations=5, warmup=enabled, l1IdleTimeout=60s, l2DelayAfterL1=90s, l2MinInterval=300s, l2MaxInterval=1800s, sessionActiveWindow=24h
[plugins] [memory-tdai] Registering agent_end hook (auto-capture)
[plugins] [memory-tdai] Plugin registration complete (v3). startTimestamp=1776143680705 (2026-04-14T05:14:40.705Z)
[plugins] [memory-tdai] [before_prompt_build] Recall complete (132ms), appendSystemContext=5474 chars
[plugins] [memory-tdai] [pipeline] Restored 18 session state(s) from checkpoint
[plugins] [memory-tdai] [pipeline] Pipeline started
[plugins] [memory-tdai] Scheduler lazy-started on first agent_end (everyN=5, l1Idle=60s, l2DelayAfterL1=90s, l2MinInterval=300s, l2MaxInterval=1800s, sessionActiveWindow=24h)
[plugins] [memory-tdai] [runner] loadRunEmbeddedPiAgent: dist/ import OK (7ms)
[plugins] [memory-tdai] [capture] ⏱ Capture timing: total=181ms, l0Record+checkpoint=57ms, l0VecIndex=94ms (embed=0ms, upsert=93ms, msgs=2), notify=30ms
[plugins] [memory-tdai] [agent_end] Auto-capture complete (192ms), l0Recorded=2, schedulerNotified=true
GitHub 项目 thedotmack/claude-mac 为 AI 提供长期记忆功能，记录工具使用情况并为后续对话生成摘要，确保知识在多次会话间的连续性。

🔷 **TypeScript** | ⭐ **+175** 今日 | 🏆 53,820 总计

**仓库地址**：`thedotmack/claude-mem`

---

## 5. [markitdown](https://github.com/microsoft/markitdown)

Python tool for converting files and office documents to Markdown.

📌 **中文摘要**：[plugins] feishu_doc: Registered feishu_doc, feishu_app_scopes
[plugins] feishu_chat: Registered feishu_chat tool
[plugins] feishu_wiki: Registered feishu_wiki tool
[plugins] feishu_drive: Registered feishu_drive tool
[plugins] feishu_bitable: Registered bitable tools
[plugins] [adp-openclaw] Plugin register() called
[plugins] [adp-openclaw] Plugin registration complete
[plugins] [memory-tdai] Registering plugin ... startTimestamp=1776143710838 (2026-04-14T05:15:10.838Z)
[plugins] [memory-tdai] Config parsed: capture=true, recall=true(maxResults=5), extraction=true(dedup=true, maxMem=10), pipeline=(everyN=5, warmup=true, l1Idle=60s, l2DelayAfterL1=90s, l2Min=300s, l2Max=1800s, activeWindow=24h), persona(triggerEvery=50, backupCount=3, sceneBackupCount=10), memoryCleanup(enabled=false, retentionDays=(disabled), cleanTime=03:00, l0Dir=conversations, l1Dir=records)
[plugins] [memory-tdai] Data dir: /root/.openclaw/memory-tdai (all subdirectories initialized)
[plugins] [memory-tdai] Memory cleaner disabled (retentionDays not configured)
[plugins] [memory-tdai] Registering before_prompt_build hook (auto-recall)
[plugins] [memory-tdai] Embedding disabled by config, VectorStore will serve as metadata-only store
[plugins] [memory-tdai][vector-store] FTS5 tables initialized (l1_fts, l0_fts) [schema v2 — jieba segmented]
[plugins] [memory-tdai][vector-store] Initialized (dimensions=0)
[plugins] [memory-tdai] VectorStore initialized: /root/.openclaw/memory-tdai/vectors.db (0D, provider=none)
[plugins] [memory-tdai] [pipeline] Initialized: everyNConversations=5, warmup=enabled, l1IdleTimeout=60s, l2DelayAfterL1=90s, l2MinInterval=300s, l2MaxInterval=1800s, sessionActiveWindow=24h
[plugins] [memory-tdai] Registering agent_end hook (auto-capture)
[plugins] [memory-tdai] Plugin registration complete (v3). startTimestamp=1776143710838 (2026-04-14T05:15:10.838Z)
[plugins] [memory-tdai] [before_prompt_build] Recall complete (140ms), appendSystemContext=5474 chars
[plugins] [memory-tdai] [pipeline] Restored 18 session state(s) from checkpoint
[plugins] [memory-tdai] [pipeline] Pipeline started
[plugins] [memory-tdai] Scheduler lazy-started on first agent_end (everyN=5, l1Idle=60s, l2DelayAfterL1=90s, l2MinInterval=300s, l2MaxInterval=1800s, sessionActiveWindow=24h)
[plugins] [memory-tdai] [runner] loadRunEmbeddedPiAgent: dist/ import OK (5ms)
[plugins] [memory-tdai] [capture] ⏱ Capture timing: total=74ms, l0Record+checkpoint=50ms, l0VecIndex=21ms (embed=0ms, upsert=20ms, msgs=2), notify=3ms
[plugins] [memory-tdai] [agent_end] Auto-capture complete (81ms), l0Recorded=2, schedulerNotified=true
Microsoft 的 MarkItDown 可将 PDF、Word、Excel、PPT 和图片转换为 Markdown 格式，支持 OCR 文字识别，已在 GitHub 开源供免费使用。

🐍 **Python** | ⭐ **+808** 今日 | 🏆 107,331 总计

**仓库地址**：`microsoft/markitdown`

---

## 6. [multica](https://github.com/multica-ai/multica)

The open-source managed agents platform. Turn coding agents into real teammates — assign tasks, track progress, compound skills.

📌 **中文摘要**：Multica 是一个开源的 platform for managing AI智能体s, enabling task delegation, progress tracking, and skill reuse It supports multiple AI 框架s and offers both cloud and self-hosting options

🔷 **TypeScript** | ⭐ **+715** 今日 | 🏆 11,458 总计

**仓库地址**：`multica-ai/multica`

---

## 7. [Archon](https://github.com/coleam00/Archon)

The first open-source harness builder for AI coding. Make AI coding deterministic and repeatable.

📌 **中文摘要**：Archon 是一个开源的 框架 for building custom AI coding assistants, offering knowledge base and task management capabilities It includes API and agents services for web crawling and AI operations It aims to enhance AI coding output

🔷 **TypeScript** | ⭐ **+677** 今日 | 🏆 17,716 总计

**仓库地址**：`coleam00/Archon`

---

## 8. [ralph](https://github.com/snarktank/ralph)

Ralph is an autonomous AI agent loop that runs repeatedly until all PRD items are complete.

📌 **中文摘要**：Ralph is an autonomous AI智能体 loop for long programming tasks, supporting multiple AI 工具s and ensuring stable, context-aware development It features self-iteration and persistent memory It runs via a shell script

🔷 **TypeScript** | ⭐ **+691** 今日 | 🏆 16,622 总计

**仓库地址**：`snarktank/ralph`

---

## 9. [ai-hedge-fund](https://github.com/virattt/ai-hedge-fund)

An AI Hedge Fund Team

📌 **中文摘要**：virattt/ai-hedge-fund 是一个开源的 AI-driven automated trading system for hedge fund decision-making, using multiple agents for complex trading strategies It's built in Python and primarily targets quant traders, AI developers, and fintech researchers

🐍 **Python** | ⭐ **+783** 今日 | 🏆 53,164 总计

**仓库地址**：`virattt/ai-hedge-fund`

---

## 10. [claude-cookbooks](https://github.com/anthropics/claude-cookbooks)

A collection of notebooks/recipes showcasing some fun and effective ways of using Claude.

📌 **中文摘要**：Anthropic's Claude Cookbooks 是一个项目 showcasing how to use the Claude model, providing practical examples and code for AI application development It's aimed at AI developers and users

📓 **Jupyter Notebook** | ⭐ **+12** 今日 | 🏆 39,694 总计

**仓库地址**：`anthropics/claude-cookbooks`

---

## 11. [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)

practice made claude perfect

📌 **中文摘要**：The project shanraisshan/claude-code-best-practice provides best practices for using the Claude Code 工具, focusing on improving efficiency and handling large projects It covers advanced techniques and integrates community strategies

🌐 **HTML** | ⭐ **+461** 今日 | 🏆 42,254 总计

**仓库地址**：`shanraisshan/claude-code-best-practice`

---

## 12. [voicebox](https://github.com/jamiepine/voicebox)

The open-source voice synthesis studio

📌 **中文摘要**：[plugins] feishu_doc: Registered feishu_doc, feishu_app_scopes
[plugins] feishu_chat: Registered feishu_chat tool
[plugins] feishu_wiki: Registered feishu_wiki tool
[plugins] feishu_drive: Registered feishu_drive tool
[plugins] feishu_bitable: Registered bitable tools
[plugins] [adp-openclaw] Plugin register() called
[plugins] [adp-openclaw] Plugin registration complete
[plugins] [memory-tdai] Registering plugin ... startTimestamp=1776143990910 (2026-04-14T05:19:50.910Z)
[plugins] [memory-tdai] Config parsed: capture=true, recall=true(maxResults=5), extraction=true(dedup=true, maxMem=10), pipeline=(everyN=5, warmup=true, l1Idle=60s, l2DelayAfterL1=90s, l2Min=300s, l2Max=1800s, activeWindow=24h), persona(triggerEvery=50, backupCount=3, sceneBackupCount=10), memoryCleanup(enabled=false, retentionDays=(disabled), cleanTime=03:00, l0Dir=conversations, l1Dir=records)
[plugins] [memory-tdai] Data dir: /root/.openclaw/memory-tdai (all subdirectories initialized)
[plugins] [memory-tdai] Memory cleaner disabled (retentionDays not configured)
[plugins] [memory-tdai] Registering before_prompt_build hook (auto-recall)
[plugins] [memory-tdai] Embedding disabled by config, VectorStore will serve as metadata-only store
[plugins] [memory-tdai][vector-store] FTS5 tables initialized (l1_fts, l0_fts) [schema v2 — jieba segmented]
[plugins] [memory-tdai][vector-store] Initialized (dimensions=0)
[plugins] [memory-tdai] VectorStore initialized: /root/.openclaw/memory-tdai/vectors.db (0D, provider=none)
[plugins] [memory-tdai] [pipeline] Initialized: everyNConversations=5, warmup=enabled, l1IdleTimeout=60s, l2DelayAfterL1=90s, l2MinInterval=300s, l2MaxInterval=1800s, sessionActiveWindow=24h
[plugins] [memory-tdai] Registering agent_end hook (auto-capture)
[plugins] [memory-tdai] Plugin registration complete (v3). startTimestamp=1776143990910 (2026-04-14T05:19:50.910Z)
[plugins] [memory-tdai] [before_prompt_build] Recall complete (218ms), appendSystemContext=5474 chars
[plugins] [memory-tdai] [pipeline] Restored 18 session state(s) from checkpoint
[plugins] [memory-tdai] [pipeline] Pipeline started
[plugins] [memory-tdai] Scheduler lazy-started on first agent_end (everyN=5, l1Idle=60s, l2DelayAfterL1=90s, l2MinInterval=300s, l2MaxInterval=1800s, sessionActiveWindow=24h)
[plugins] [memory-tdai] [runner] loadRunEmbeddedPiAgent: dist/ import OK (9ms)
[plugins] [memory-tdai] [capture] ⏱ Capture timing: total=296ms, l0Record+checkpoint=112ms, l0VecIndex=143ms (embed=0ms, upsert=141ms, msgs=3), notify=42ms
[plugins] [memory-tdai] [agent_end] Auto-capture complete (307ms), l0Recorded=3, schedulerNotified=true
Voicebox 是一个开源的语音克隆和合成工具，基于 Qwen3-TTS 技术，支持本地语音克隆，无需云端依赖，旨在提供 ElevenLabs 的本地替代方案。

🔷 **TypeScript** | ⭐ **+512** 今日 | 🏆 16,484 总计

**仓库地址**：`jamiepine/voicebox`

---

## 13. [blender-mcp](https://github.com/ahujasid/blender-mcp)

暂无描述

📌 **中文摘要**：[plugins] feishu_doc: Registered feishu_doc, feishu_app_scopes
[plugins] feishu_chat: Registered feishu_chat tool
[plugins] feishu_wiki: Registered feishu_wiki tool
[plugins] feishu_drive: Registered feishu_drive tool
[plugins] feishu_bitable: Registered bitable tools
[plugins] [adp-openclaw] Plugin register() called
[plugins] [adp-openclaw] Plugin registration complete
[plugins] [memory-tdai] Registering plugin ... startTimestamp=1776144029971 (2026-04-14T05:20:29.971Z)
[plugins] [memory-tdai] Config parsed: capture=true, recall=true(maxResults=5), extraction=true(dedup=true, maxMem=10), pipeline=(everyN=5, warmup=true, l1Idle=60s, l2DelayAfterL1=90s, l2Min=300s, l2Max=1800s, activeWindow=24h), persona(triggerEvery=50, backupCount=3, sceneBackupCount=10), memoryCleanup(enabled=false, retentionDays=(disabled), cleanTime=03:00, l0Dir=conversations, l1Dir=records)
[plugins] [memory-tdai] Data dir: /root/.openclaw/memory-tdai (all subdirectories initialized)
[plugins] [memory-tdai] Memory cleaner disabled (retentionDays not configured)
[plugins] [memory-tdai] Registering before_prompt_build hook (auto-recall)
[plugins] [memory-tdai] Embedding disabled by config, VectorStore will serve as metadata-only store
[plugins] [memory-tdai][vector-store] FTS5 tables initialized (l1_fts, l0_fts) [schema v2 — jieba segmented]
[plugins] [memory-tdai][vector-store] Initialized (dimensions=0)
[plugins] [memory-tdai] VectorStore initialized: /root/.openclaw/memory-tdai/vectors.db (0D, provider=none)
[plugins] [memory-tdai] [pipeline] Initialized: everyNConversations=5, warmup=enabled, l1IdleTimeout=60s, l2DelayAfterL1=90s, l2MinInterval=300s, l2MaxInterval=1800s, sessionActiveWindow=24h
[plugins] [memory-tdai] Registering agent_end hook (auto-capture)
[plugins] [memory-tdai] Plugin registration complete (v3). startTimestamp=1776144029971 (2026-04-14T05:20:29.971Z)
[plugins] [memory-tdai] [before_prompt_build] Recall complete (166ms), appendSystemContext=5474 chars
[plugins] [memory-tdai] [pipeline] Restored 18 session state(s) from checkpoint
[plugins] [memory-tdai] [pipeline] Pipeline started
[plugins] [memory-tdai] Scheduler lazy-started on first agent_end (everyN=5, l1Idle=60s, l2DelayAfterL1=90s, l2MinInterval=300s, l2MaxInterval=1800s, sessionActiveWindow=24h)
[plugins] [memory-tdai] [runner] loadRunEmbeddedPiAgent: dist/ import OK (11ms)
[plugins] [memory-tdai] [capture] ⏱ Capture timing: total=85ms, l0Record+checkpoint=57ms, l0VecIndex=24ms (embed=0ms, upsert=23ms, msgs=2), notify=5ms
[plugins] [memory-tdai] [agent_end] Auto-capture complete (91ms), l0Recorded=2, schedulerNotified=true
BlenderMCP 将 Blender 与 AI 连接，实现从 2D 图片到 3D 建模的自动化，支持 Model Context Protocol 交互协议，在 GitHub 上获得超过 18,000 星标。

🐍 **Python** | ⭐ **+339** 今日 | 🏆 19,565 总计

**仓库地址**：`ahujasid/blender-mcp`

---

## 14. [Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam)

real time face swap and one-click video deepfake with only a single image

📌 **中文摘要**：[plugins] feishu_doc: Registered feishu_doc, feishu_app_scopes
[plugins] feishu_chat: Registered feishu_chat tool
[plugins] feishu_wiki: Registered feishu_wiki tool
[plugins] feishu_drive: Registered feishu_drive tool
[plugins] feishu_bitable: Registered bitable tools
[plugins] [adp-openclaw] Plugin register() called
[plugins] [adp-openclaw] Plugin registration complete
[plugins] [memory-tdai] Registering plugin ... startTimestamp=1776144065842 (2026-04-14T05:21:05.842Z)
[plugins] [memory-tdai] Config parsed: capture=true, recall=true(maxResults=5), extraction=true(dedup=true, maxMem=10), pipeline=(everyN=5, warmup=true, l1Idle=60s, l2DelayAfterL1=90s, l2Min=300s, l2Max=1800s, activeWindow=24h), persona(triggerEvery=50, backupCount=3, sceneBackupCount=10), memoryCleanup(enabled=false, retentionDays=(disabled), cleanTime=03:00, l0Dir=conversations, l1Dir=records)
[plugins] [memory-tdai] Data dir: /root/.openclaw/memory-tdai (all subdirectories initialized)
[plugins] [memory-tdai] Memory cleaner disabled (retentionDays not configured)
[plugins] [memory-tdai] Registering before_prompt_build hook (auto-recall)
[plugins] [memory-tdai] Embedding disabled by config, VectorStore will serve as metadata-only store
[plugins] [memory-tdai][vector-store] FTS5 tables initialized (l1_fts, l0_fts) [schema v2 — jieba segmented]
[plugins] [memory-tdai][vector-store] Initialized (dimensions=0)
[plugins] [memory-tdai] VectorStore initialized: /root/.openclaw/memory-tdai/vectors.db (0D, provider=none)
[plugins] [memory-tdai] [pipeline] Initialized: everyNConversations=5, warmup=enabled, l1IdleTimeout=60s, l2DelayAfterL1=90s, l2MinInterval=300s, l2MaxInterval=1800s, sessionActiveWindow=24h
[plugins] [memory-tdai] Registering agent_end hook (auto-capture)
[plugins] [memory-tdai] Plugin registration complete (v3). startTimestamp=1776144065842 (2026-04-14T05:21:05.842Z)
[plugins] [memory-tdai] [before_prompt_build] Recall complete (158ms), appendSystemContext=5474 chars
[plugins] [memory-tdai] [pipeline] Restored 18 session state(s) from checkpoint
[plugins] [memory-tdai] [pipeline] Pipeline started
[plugins] [memory-tdai] Scheduler lazy-started on first agent_end (everyN=5, l1Idle=60s, l2DelayAfterL1=90s, l2MinInterval=300s, l2MaxInterval=1800s, sessionActiveWindow=24h)
[plugins] [memory-tdai] [runner] loadRunEmbeddedPiAgent: dist/ import OK (9ms)
[plugins] [memory-tdai] [capture] ⏱ Capture timing: total=90ms, l0Record+checkpoint=58ms, l0VecIndex=29ms (embed=0ms, upsert=27ms, msgs=2), notify=3ms
[plugins] [memory-tdai] [agent_end] Auto-capture complete (98ms), l0Recorded=2, schedulerNotified=true
Deep-Live-Cam 是一个开源的实时换脸和深度伪造工具，只需一张参考图片即可在图片、视频和直播中替换人脸，支持 CPU、GPU 和 Mac 环境。

🐍 **Python** | ⭐ **+217** 今日 | 🏆 90,343 总计

**仓库地址**：`hacksider/Deep-Live-Cam`

---

## 15. [get-shit-done](https://github.com/gsd-build/get-shit-done)

A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

📌 **中文摘要**：[plugins] feishu_doc: Registered feishu_doc, feishu_app_scopes
[plugins] feishu_chat: Registered feishu_chat tool
[plugins] feishu_wiki: Registered feishu_wiki tool
[plugins] feishu_drive: Registered feishu_drive tool
[plugins] feishu_bitable: Registered bitable tools
[plugins] [adp-openclaw] Plugin register() called
[plugins] [adp-openclaw] Plugin registration complete
[plugins] [memory-tdai] Registering plugin ... startTimestamp=1776144106167 (2026-04-14T05:21:46.167Z)
[plugins] [memory-tdai] Config parsed: capture=true, recall=true(maxResults=5), extraction=true(dedup=true, maxMem=10), pipeline=(everyN=5, warmup=true, l1Idle=60s, l2DelayAfterL1=90s, l2Min=300s, l2Max=1800s, activeWindow=24h), persona(triggerEvery=50, backupCount=3, sceneBackupCount=10), memoryCleanup(enabled=false, retentionDays=(disabled), cleanTime=03:00, l0Dir=conversations, l1Dir=records)
[plugins] [memory-tdai] Data dir: /root/.openclaw/memory-tdai (all subdirectories initialized)
[plugins] [memory-tdai] Memory cleaner disabled (retentionDays not configured)
[plugins] [memory-tdai] Registering before_prompt_build hook (auto-recall)
[plugins] [memory-tdai] Embedding disabled by config, VectorStore will serve as metadata-only store
[plugins] [memory-tdai][vector-store] FTS5 tables initialized (l1_fts, l0_fts) [schema v2 — jieba segmented]
[plugins] [memory-tdai][vector-store] Initialized (dimensions=0)
[plugins] [memory-tdai] VectorStore initialized: /root/.openclaw/memory-tdai/vectors.db (0D, provider=none)
[plugins] [memory-tdai] [pipeline] Initialized: everyNConversations=5, warmup=enabled, l1IdleTimeout=60s, l2DelayAfterL1=90s, l2MinInterval=300s, l2MaxInterval=1800s, sessionActiveWindow=24h
[plugins] [memory-tdai] Registering agent_end hook (auto-capture)
[plugins] [memory-tdai] Plugin registration complete (v3). startTimestamp=1776144106167 (2026-04-14T05:21:46.167Z)
[plugins] [memory-tdai] [before_prompt_build] Recall complete (144ms), appendSystemContext=5474 chars
[plugins] [memory-tdai] [pipeline] Restored 18 session state(s) from checkpoint
[plugins] [memory-tdai] [pipeline] Pipeline started
[plugins] [memory-tdai] Scheduler lazy-started on first agent_end (everyN=5, l1Idle=60s, l2DelayAfterL1=90s, l2MinInterval=300s, l2MaxInterval=1800s, sessionActiveWindow=24h)
[plugins] [memory-tdai] [runner] loadRunEmbeddedPiAgent: dist/ import OK (7ms)
[plugins] [memory-tdai] [capture] ⏱ Capture timing: total=98ms, l0Record+checkpoint=63ms, l0VecIndex=32ms (embed=0ms, upsert=31ms, msgs=2), notify=3ms
[plugins] [memory-tdai] [agent_end] Auto-capture complete (105ms), l0Recorded=2, schedulerNotified=true
Get Shit Done (GSD) 是一个可靠的上下文工程层，用于 AI 代码生成，提升编程项目的效率和稳定性，专注于优化 AI 编程工作流和问题排查。

🟨 **JavaScript** | ⭐ **+655** 今日 | 🏆 52,291 总计

**仓库地址**：`gsd-build/get-shit-done`

---


## 💡 J.A.R.V.I.S. 观察

本期共收录 15 个热门项目，建议关注星标增长快的项目。

---

🤖 **J.A.R.V.I.S. 开源观察助手**
📡 数据更新：2026-04-14 13:22
