---
title: leetcode 155.最小栈
date: 2023-10-13 00:07:58
modificationDate: 2023 十月 13日 星期五 00:07:58
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---

> Problem: [155. 最小栈](https://leetcode.cn/problems/min-stack/description/)

![](../../imgs/Pasted%20image%2020231013000854.png)
# 思路
> 栈

# 解题方法
> 描使用额外栈辅助， a b c d 入栈，如果d 在那么abc 必然在，所以每次入栈比较一个最小值，放入另一个栈就好

# 复杂度
- 时间复杂度:
> 添加时间复杂度, 示例： $O(n)$

- 空间复杂度:
> 添加空间复杂度, 示例： $O(n)$
  
# Code
```Go []

// 使用额外栈辅助， a b c d 入栈，如果d 在那么abc 必然在，所以每次入栈比较一个最小值，放入另一个栈就好
type MinStack struct {
	stack    []int // 主栈
	minStack []int // 辅助栈
}

func Constructor() MinStack {
	minStacks := MinStack{[]int{}, []int{math.MaxInt}}
	return minStacks
}

func (this *MinStack) Push(x int) {
	// 同时比较辅助站的的top元素，如果更小 则添加到辅助站
	this.stack = append(this.stack, x)
	minTmp := min(x, this.minStack[len(this.minStack)-1])
	this.minStack = append(this.minStack, minTmp)
}


func (this *MinStack) Pop() {
	this.stack = this.stack[:len(this.stack)-1]
	this.minStack = this.minStack[:len(this.minStack)-1]
}

func (this *MinStack) Top() int {
	return (this.stack[len(this.stack)-1])
}

func (this *MinStack) GetMin() int {
	return (this.minStack[len(this.minStack)-1])
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

```
  