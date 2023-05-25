---
title: leetcode 53.最大子数和
date: 2023-05-25 23:08:24
modificationDate: 2023 五月 25日 星期四 23:08:24
categories: 
	- leetcode
tags: [贪心,动态规划]
sticky: []
hide: false
category_bar: true
---


> Problem: [53. 最大子数组和](https://leetcode.cn/problems/maximum-subarray/description/)

**个人网站：** https://leiqicn.gitee.io/categories/leetcode/
![image.png](https://pic.leetcode.cn/1685028457-IOzjjG-image.png)
[TOC]
# 思路
> 这里是经典的最大子序和的问题。我们可以很容易想到贪心的思想。就是如果前边的子序和是正数，则我们会把当前的数添加到前面的自序和上。否则，重新从当前位置开始子序和，丢弃前边的子序和。


# 解题方法

> 方法1  算法通过遍历整个数组nums，维护一个当前连续子序列的和count，同时记录一个最大值res。每遍历一个元素，就将其加入到count中，并比较它与之前计算过的最大子序和res的大小关系，如果大于res，则更新res。并且当count变成负数时，就说明需要重新寻找连续子序列，因此将count重置为0。

> 方法2 使用了类似动态规划的思想，用nums 数组代表dp数组; dp[i]含义：dp 表示最大子序列，i 代表当前位置的最大子序列的值；dp[i+1] = dp[i] +dp[i+1] ;max 初始化为第一个元素nums[0](dp[0]); 遍历顺序，从idx = 1 开始遍历。


# 复杂度
- 时间复杂度: 
>  $O(n)$

- 空间复杂度: 
>  $O(1)$

# Code
```Go []
// 方法1 使用了类似动态规划的思想
func maxSubArray(nums []int) int {
	count := 0
	res := math.MinInt32

	for i := 0; i < len(nums); i++ {
		count += nums[i]
		if count > res {
			res = count
		}
		
		if count < 0 {
			count = 0
		}
	}
	return res
}
// 方法2 
// 定义 nums[i] 当前元素，nums[i-1] 前序列之和
func maxSubArray(nums []int) int {
	max := nums[0] //初始化最大值为前边一个元素
	// 是判断当前连续子序列能否对后面的数字产生增益的条件，在算法中起到非常重要的作用。
	for i:= 0 ;i <len(nums)-1; i++ {
		if nums[i+1] + nums[i] > nums[i+1] {
			nums[i+1] = nums[i+1] + nums[i]
		}
		// 超过最大值，则更新
		if nums[i+1] >  max {
			max = nums[i+1]
		}
	}
	return max
}
```
