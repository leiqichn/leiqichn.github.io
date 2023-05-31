---
title: leetcode 28.找出字符串中第一个匹配项的下标
date: 2023-05-31 22:27:00
modificationDate: 2023 五月 31日 星期三 22:27:00
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---

[28. 找出字符串中第一个匹配项的下标 - 力扣（Leetcode）](https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description/)
![](../../imgs/Pasted%20image%2020230531222721.png)

简单解法
利用split 函数
```go
func strStr(haystack string, needle string) int {
	// 使用split 函数，如果存在needle,则会把其切分为至少两个元素的切片
	splitList := strings.Split(haystack, needle)
	// 如果长度为1，且needle!=haystack 说明没找到匹配项，返回-1
	if len(splitList)== 1 && needle!=haystack {
		return -1
	}
	if len(splitList) > 1 {
		return len(splitList[0])
	}
	// needle 在haystack的最开头，返回0
	return 0
}
```
