---
title: 企业微信 github 提醒机器人
date: 2024-07-07 12:39:36
modificationDate: 2024 July 7th Sunday 12:39:36
categories: 
	- 工具
tags: []
sticky: []
hide: true
category_bar: true
---

```shell
 curl 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=66afffa6-d741-4293-b65d-3f5b5f529a56' \
   -H 'Content-Type: application/json' \
   -d '
   {
        "msgtype": "text",
        "text": {
            "content": "你好，github提醒测试"
        }
   }'

```


![](../../imgs/Pasted%20image%2020240707124018.png)
![](../../imgs/Pasted%20image%2020240707124004.png)
