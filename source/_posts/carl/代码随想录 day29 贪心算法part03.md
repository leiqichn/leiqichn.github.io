---
title: 代码随想录 day29 贪心算法part03
date: 2024-11-27 23:39:43
modificationDate: 2024 十一月 27日 星期三 23:39:43
categories: 
	- carl
tags: []
sticky: []
published: false
category_bar: true
---


# 第八章 贪心算法 part03

### 134. 加油站

本题有点难度，不太好想，推荐大家熟悉一下方法二

https://programmercarl.com/0134.%E5%8A%A0%E6%B2%B9%E7%AB%99.html

```go
func canCompleteCircuit(gas []int, cost []int) int {
	curSum := 0
	totalSum := 0
	start := 0
	for i := 0; i < len(gas); i++ { // 这里不用模拟环吗  一次环就行
		curSum += gas[i] - cost[i]
		totalSum += gas[i] - cost[i]
		if curSum < 0 {
			start = i+1
			curSum = 0
		}
	}
	if totalSum < 0 {
		return -1
	}
	return start
}

```

### 135. 分发糖果

本题涉及到一个思想，就是想处理好一边再处理另一边，不要两边想着一起兼顾，后面还会有题目用到这个思路

https://programmercarl.com/0135.%E5%88%86%E5%8F%91%E7%B3%96%E6%9E%9C.html

### 860.柠檬水找零

本题看上好像挺难，其实很简单，大家先尝试自己做一做。

https://programmercarl.com/0860.%E6%9F%A0%E6%AA%AC%E6%B0%B4%E6%89%BE%E9%9B%B6.html

### 406.根据身高重建队列

本题有点难度，和分发糖果类似，不要两头兼顾，处理好一边再处理另一边。

https://programmercarl.com/0406.%E6%A0%B9%E6%8D%AE%E8%BA%AB%E9%AB%98%E9%87%8D%E5%BB%BA%E9%98%9F%E5%88%97.html