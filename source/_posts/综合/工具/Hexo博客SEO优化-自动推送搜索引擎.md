---
title: Hexo博客SEO优化 - 自动推送搜索引擎
date: 2026-03-11 07:57:00
modificationDate: 2026 三月 11日 星期二 07:57:00
categories:
  - [综合, 工具]
tags: [Hexo, SEO, 百度, Bing, Google]
sticky: []
published: true
category_bar: true
---

为了让博客文章更快被搜索引擎收录，我们可以使用 `hexo-seo-submit` 插件自动推送链接到百度、Bing 和 Google。

## 安装插件

```bash
npm install hexo-seo-submit --save
```

## 配置文件

在 Hexo 根目录创建 `_config.hexo-seo-submit.yml`：

```yaml
# hexo-seo-submit 配置
# 文档: https://github.com/tardis-ksh/hexo-seo-submit

# 站点URL
url: https://your-domain.com

# Bing配置
bing:
  enable: true
  path: bing.json
  apiKey: "your-bing-api-key"

# 百度配置
baidu:
  enable: true
  path: baidu.txt
  token: "your-baidu-token"

# Google配置
google:
  enable: true
  path: google.txt
  accountKeysJsonFile: "google-service-account.json"
```

## 获取各平台密钥

### 百度站长平台

1. 访问 [百度搜索资源平台](https://ziyuan.baidu.com/)
2. 添加网站并验证所有权
3. 进入「普通收录」→「资源提交」→「API提交」
4. 复制接口调用地址中的 `token` 参数

接口格式：
```
http://data.zz.baidu.com/urls?site=https://your-domain.com&token=YOUR_TOKEN
```

### Bing Webmaster

1. 访问 [Bing Webmaster Tools](https://www.bing.com/webmasters/)
2. 添加网站并验证
3. 进入「设置」→「API 访问」
4. 生成 API Key

### Google Search Console

1. 访问 [Google Search Console](https://search.google.com/search-console)
2. 添加网站并验证
3. 创建 Service Account 并下载 JSON 密钥文件
4. 将 Service Account 邮箱添加为 Search Console 网站的所有者

## 配置 _config.yml

在 `_config.yml` 中添加 deploy 配置：

```yaml
deploy:
  - type: git
    repo: https://github.com/username/username.github.io.git
    branch: gh-pages
  - type: hexo-seo-submit
```

## 使用方法

每次部署时自动推送：

```bash
hexo clean && hexo g && hexo d
```

或单独推送：

```bash
npx hexo-seo-submit baidu -t "your-token" -f public/baidu.txt
npx hexo-seo-submit bing -k "your-api-key" -f public/bing.json
```

## 注意事项

1. **百度配额限制**：每天推送数量有限制，超过会返回 `over quota`
2. **sitemap.xml**：确保 sitemap 正常生成，插件会从中读取链接
3. **推送时机**：建议每次发布新文章后执行推送

## 常见问题

### sitemap.xml 为空

检查 `_config.yml` 中的 sitemap 配置，移除自定义模板：

```yaml
sitemap:
  path: sitemap.xml
```

### 百度返回 over quota

每天配额用完，明天重置后可继续推送。

## 参考链接

- [hexo-seo-submit GitHub](https://github.com/tardis-ksh/hexo-seo-submit)
- [百度搜索资源平台](https://ziyuan.baidu.com/)
- [Bing Webmaster Tools](https://www.bing.com/webmasters/)
- [Google Search Console](https://search.google.com/search-console)