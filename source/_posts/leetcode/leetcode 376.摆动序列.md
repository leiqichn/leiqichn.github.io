---
title: leetcode 376.摆动序列
date: 2023-05-24 01:05:07
modificationDate: 2023 五月 24日 星期三 01:05:07
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---
[376. 摆动序列 - 力扣（Leetcode）](https://leetcode.cn/problems/wiggle-subsequence/description/)
![](../../imgs/Pasted%20image%2020230524010708.png)

```go
func wiggleMaxLength(nums []int) int {
    var count, preDiff, curDiff int
    count = 1 // 初始化计数为1，至少有一个数字是有效的
    if len(nums) < 2 {
        return count // 如果数组长度小于2，直接返回计数值
    }
    for i := 0; i < len(nums)-1; i++ {
        curDiff = nums[i+1] - nums[i] // 计算当前数字之间的差值

        // 根据差值的正负和前一个差值的正负进行判断
        // 如果满足摆动序列的条件，更新前一个差值和计数值
        if (curDiff > 0 && preDiff <= 0) || (preDiff >= 0 && curDiff < 0) {
            preDiff = curDiff
            count++
        }
    }
    return count // 返回最终的计数值
}

```
