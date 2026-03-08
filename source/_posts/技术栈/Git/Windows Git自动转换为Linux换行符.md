---
title: Windows Git自动转换为Linux换行符
date: 2025-04-28 21:15:32
modificationDate: 2025 四月 28日 星期一 21:15:32
categories:
  - [技术栈, Git]
tags: []
sticky: []
published: true
category_bar: true
---

在 Git 中处理不同操作系统（Windows/Linux/macOS）的换行符（`LF` 和 `CRLF`）时，自动转换是关键。以下是配置 Git 自动处理换行符的方法：

---

### **1. 核心配置：`core.autocrlf`**
通过设置 `core.autocrlf` 属性，让 Git 自动转换换行符：

#### **不同操作系统的推荐设置**
- **Windows（推荐）**：  
  ```bash
  git config --global core.autocrlf true
  # 提交时转换为 LF，检出时转换为 CRLF
  ```

- **Linux/macOS（推荐）**：  
  ```bash
  git config --global core.autocrlf input
  # 提交时转换为 LF，检出时不转换
  ```


### **2. 强制规范：`.gitattributes` 文件**
在项目根目录创建 `.gitattributes` 文件，**优先级高于全局配置**，适合团队协作。

#### **示例配置**：
```text
# 所有文本文件使用 LF 换行符
* text=auto eol=lf

# 排除二进制文件（避免误处理）
*.png binary
*.jpg binary
*.zip binary

# 指定特定文件类型（可选）
*.sh text eol=lf
*.bat text eol=crlf
```

- `text=auto`：Git 自动识别文本文件。
- `eol=lf` 或 `eol=crlf`：强制统一换行符。

---

### **3. 修复已存在的换行符问题**
#### **步骤：**
1. 删除缓存并重置文件：
   ```bash
   git rm --cached -r .  # 清除缓存
   git reset --hard      # 重置文件
   ```

2. 重新添加文件并提交：
   ```bash
   git add .
   git commit -m "fix: normalize line endings"
   ```

---

### **4. 检查换行符状态**
#### **检查文件换行符**：
- **Linux/macOS**：
  ```bash
  file yourfile.txt
  # 输出中包含 "LF" 或 "CRLF"
  ```

- **Windows（PowerShell）**：
  ```powershell
  Get-Content yourfile.txt -Encoding Byte | Select-String "0D 0A"
  # 存在 "0D 0A" 表示 CRLF
  ```

#### **查看 Git 换行符转换日志**：
```bash
git ls-files --eol
```

---

### **常见问题解决**
- **警告 `LF will be replaced by CRLF`**：  
  正常提示，表示 Git 正在按配置转换换行符。

- **文件被标记为已修改（仅换行符变化）**：  
  运行以下命令清除差异：
  ```bash
  git config --global core.whitespace cr-at-eol
  git add --renormalize .
  ```

- **混合换行符导致冲突**：  
  使用 `.gitattributes` 强制统一换行符，并重新提交文件。

---

### **最佳实践**
1. **团队协作**：在项目中添加 `.gitattributes` 文件，统一换行符规则。
2. **编辑器配置**：设置 IDE（如 VSCode）默认使用 `LF`（[配置示例](https://stackoverflow.com/a/44788470)）。
3. **Windows 用户**：安装 Git 时选择 `Checkout as-is, commit Unix-style line endings`。

---

通过上述配置，Git 会自动处理换行符，避免跨平台协作时的混乱！ 🛠️