---
title: 本地生成hexo 网页
date: 2025-03-09 23:28:49
modificationDate: 2025 三月 9日 星期日 23:28:49
categories: 
	- 前端
tags: []
sticky: []
published: false
category_bar: true
---

使用 npm 一键安装 Hexo 博客程序：

```text
npm install -g hexo-cli
```

Mac 用户需要管理员权限（sudo），运行这条命令：

```text
sudo npm install -g hexo-cli
```

安装时间有点久（真的很慢！），界面也没任何反应，**耐心等待**，安装完成后如下图。

![](https://pic4.zhimg.com/v2-01e7fc8bb9280437deb437bf73a190a1_1440w.jpg)

### **# 4.2 Hexo 初始化和本地预览**

**初始化并安装所需组件：**

```text
hexo init      # 初始化
npm install    # 安装组件
```

完成后依次输入下面命令，**启动本地服务器进行预览**：

```text
hexo g   # 生成页面
hexo s   # 启动预览
```

**访问** `http://localhost:4000`**，出现 Hexo 默认页面，本地博客安装成功！**




npm install hexo-all-minifier --save

https://registry.npmjs.org/

npm set registry https://registry.npmjs.org/

## 本地部署调测
`hexo clean`、`hexo g`、`hexo d`

hexo cl && hexo g && hexo s

hexo new page guestbook

hexo-generator-json-content

安装：npm install --save hexo-generator-json-content
