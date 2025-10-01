---
title: Obsidian配置代理
date: 2025-06-16 00:07:58
modificationDate: 2025 六月 16日 星期一 00:07:58
categories: 
	- 工具
tags: []
sticky: []
published: true
category_bar: true
---

在 Obsidian 中设置代理（Proxy）需要通过 **系统环境变量** 或 **插件** 来实现，因为 Obsidian 本身没有内置的代理设置选项。以下是几种方法：

---

## **方法 1：通过环境变量设置全局代理（推荐）**
Obsidian 是基于 Electron 的应用程序，它会遵循系统的 HTTP/HTTPS 代理设置。你可以通过以下方式设置：

### **Windows**
1. **临时设置（仅当前终端窗口有效）**  
   在 CMD/PowerShell 中运行：
   ```bash
   set http_proxy=http://127.0.0.1:7897
   set https_proxy=http://127.0.0.1:7897
   set all_proxy=socks5://127.0.0.1:7897
   ```
   然后启动 Obsidian：
   ```bash
   start "" "C:\path\to\Obsidian.exe"
   ```

2. **永久设置（系统环境变量）我使用的这个**  
   - 按 `Win + R`，输入 `sysdm.cpl` 打开 **系统属性**。
   - 进入 **高级 → 环境变量**。
   - 在 **用户变量** 或 **系统变量** 中添加：
     ```
     HTTP_PROXY=http://127.0.0.1:7897
     HTTPS_PROXY=http://127.0.0.1:7897
     ALL_PROXY=socks5://127.0.0.1:7897
     ```
   - 重启 Obsidian。

---

### **macOS/Linux**
1. **临时设置（终端启动）**  
   ```bash
   export http_proxy=http://127.0.0.1:7897
   export https_proxy=http://127.0.0.1:7897
   export all_proxy=socks5://127.0.0.1:7897
   ```
   然后启动 Obsidian：
   ```bash
   open -a Obsidian  # macOS
   obsidian &       # Linux（如果安装正确）
   ```

2. **永久设置（`.bashrc`/`.zshrc`）**  
   在 `~/.bashrc` 或 `~/.zshrc` 中添加：
   ```bash
   export http_proxy=http://127.0.0.1:7897
   export https_proxy=http://127.0.0.1:7897
   export all_proxy=socks5://127.0.0.1:7897
   ```
   然后运行：
   ```bash
   source ~/.bashrc  # 或 source ~/.zshrc
   ```
   重启 Obsidian。

---

## **方法 2：使用 Proxy 插件（如果 Obsidian 支持）**
Obsidian 本身没有官方代理插件，但你可以尝试：
1. **安装 `obsidian-proxy` 插件（如果存在）**  
   - 进入 `设置 → 社区插件 → 浏览`，搜索 `proxy`。
   - 安装并配置代理地址。

2. **使用第三方工具（如 Proxifier/Clash）**  
   - 在 Proxifier 中设置 Obsidian 走代理：
     ```
     规则：Obsidian.exe → SOCKS5 127.0.0.1:7897
     ```

---

## **方法 3：修改 Electron 启动参数（高级）**
如果 Obsidian 是基于 Electron 的，可以尝试修改启动参数：
```bash
obsidian --proxy-server="http://127.0.0.1:7897"
```
（需找到 Obsidian 的实际启动方式）

---

## **验证代理是否生效**
1. 在 Obsidian 中安装插件或同步数据，看是否正常访问。
2. 使用 `curl -v https://api.obsidian.md` 测试代理是否生效。

---

### **总结**
| 方法 | 适用场景 | 持久性 |
|------|---------|--------|
| **环境变量** | 推荐，全局生效 | ✅ 永久 |
| **终端临时设置** | 测试用 | ❌ 临时 |
| **Proxy 插件** | 如果 Obsidian 支持 | ⚠️ 依赖插件 |
| **Proxifier/Clash** | 强制代理所有流量 | ✅ 系统级 |

如果你的代理是 `http://127.0.0.1:7897` 或 `socks5://127.0.0.1:7897`（如 Clash/V2Ray），建议优先使用 **环境变量** 方法。