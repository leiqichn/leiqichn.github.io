---
title: 设置github 同步到gitee
date: 2024-07-21 22:15:47
modificationDate: 2024 July 21st Sunday 22:15:47
categories: 

	- git
tags: []
sticky: []
hide: false
category_bar: true
---

1.  复制自己电脑的**私钥**到github
2. 复制自己电脑的**公钥**到gitee![](../../imgs/Pasted%20image%2020240721222254.png)
3. 获取gitee 的私人令牌
4. 创建.github/workflows/xxx.ymal
![](../../imgs/Pasted%20image%2020240721221805.png)



```yaml
name: Pages

on:
  push:
    branches:
      - master # default branch

jobs:
  pages:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v2
      - name: Sync to Gitee
        uses: wearerequired/git-mirror-action@master
        env:
          # 注意在 Settings->Secrets 配置 GITEE_RSA_PRIVATE_KEY
          SSH_PRIVATE_KEY: ${{ secrets.GITEE_RSA_PRIVATE_KEY }}
        with:
          # 注意替换为你的 GitHub 源仓库地址
          source-repo: git@github.com:leiqichn/novelBigModel.git
          # 注意替换为你的 Gitee 目标仓库地址
          destination-repo: git@gitee.com:leiqichn/novelBigModel.git

```
