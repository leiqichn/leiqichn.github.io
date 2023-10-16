---
title: Leetcode 136.只出现一次的数字
date: 2023-10-16 23:23:24
modificationDate: 2023 十月 16日 星期一 23:23:24
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---

> Problem: [136. 只出现一次的数字](https://leetcode.cn/problems/single-number/description/)
![](../../imgs/Pasted%20image%2020231016232403.png)
[TOC]

# 思路
> 如何才能做到线性时间复杂度和常数空间复杂度呢？

答案是使用位运算。对于这道题，可使用异或运算。异或运算有以下三个性质。

任何数和 0做异或运算，结果仍然是原来的数
任何数和其自身做异或运算，结果是 0
![image.png](https://pic.leetcode.cn/1697469725-QtsjoA-image.png)


# 解题方法
> 描述你的解题方法

# 复杂度
- 时间复杂度:
> 添加时间复杂度, 示例： $O(n)$

- 空间复杂度:
> 添加空间复杂度, 示例： $O(1)$
  


# Code
1. hash
```Go []
func singleNumber(nums []int) int {
	numsMap := make(map[int]int)
	for _, val := range nums {
		numsMap[val] += 1
	}
	for key, val := range numsMap {
		if val == 1 {
			return key

		}
	}
	return 0
}

```

2. 位运算
```Go []

func singleNumber(nums []int) int {
    single := 0
    for _, num := range nums {
        single ^= num
    }
    return single
}

```
  