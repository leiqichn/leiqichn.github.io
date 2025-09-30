---
title: leetcode 2460.对数组执行操作 2023.05.06每日一题
date: 2023-06-05 22:46:05
modificationDate: 2023 六月 5日 星期一 22:46:05
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---
[2460. 对数组执行操作 - 力扣（Leetcode）](https://leetcode.cn/problems/apply-operations-to-an-array/description/)
![](../../imgs/Pasted%20image%2020230605224628.png)

# 思路
直接模拟

# Code
第一版
时间复杂度：O(n)
空间复杂度：O(n)
```go
func applyOperations(nums []int) []int {
	var res []int
	res = make([]int, len(nums))
	index := 0
	// 第一次遍历 进行赋值操作
	for i := 0; i < len(nums)-1; i++ {
		if nums[i] == nums[i+1] {
			nums[i] *= 2
			nums[i+1] = 0
		}
	}
	// 第二次遍历 将非0移动到前边
	for i := 0; i < len(nums); i++ {
		if nums[i] != 0 {
			res[index] = nums[i]
			index++
		}
	}
	return res
}

```
第二版
时间复杂度：O(n)
空间复杂度：O(1)

```go
func applyOperations(nums []int) []int {
    n := len(nums)
    j := 0
    for i := 0; i < n; i++ {
        if i+1 < n && nums[i] == nums[i+1] {
            nums[i] *= 2
            nums[i + 1] = 0
        }
        if nums[i] != 0 {
            nums[i], nums[j] = nums[j], nums[i]
            j++
        }
    }
    return nums
}

```
