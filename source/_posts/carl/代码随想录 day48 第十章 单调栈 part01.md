---
title: 代码随想录 day48 第十章 单调栈 part01
date: 2024-12-16 23:44:58
modificationDate: 2024 十二月 16日 星期一 23:44:58
categories: 
	- carl
tags: []
sticky: []
hide: true
category_bar: true
---

第十章 单调栈part01

 739. 每日温度 

今天正式开始单调栈，这是单调栈一篇扫盲题目，也是经典题。

大家可以读题，思考暴力的解法，然后在看单调栈的解法。 就能感受出单调栈的巧妙

https://programmercarl.com/0739.%E6%AF%8F%E6%97%A5%E6%B8%A9%E5%BA%A6.html  

请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

使用单调栈的思路遍历保存值

```go

func dailyTemperatures(t []int) []int {
    var res []int
    for i := 0; i < len(t)-1; i++ {
        j := i + 1
        for ; j < len(t); j++ {
            // 如果之后出现更高，说明找到了
            if t[j] > t[i] {
                res = append(res, j-i)
                break
            }
        }
        // 找完了都没找到
        if j == len(t) {
            res = append(res, 0)
        }
    }
    // 最后一个肯定是 0
    return append(res, 0)
}

```


 496.下一个更大元素 I 

本题和 739. 每日温度 看似差不多，其实 有加了点难度。

https://programmercarl.com/0496.%E4%B8%8B%E4%B8%80%E4%B8%AA%E6%9B%B4%E5%A4%A7%E5%85%83%E7%B4%A0I.html  
[力扣题目链接(opens new window)](https://leetcode.cn/problems/next-greater-element-i/)

给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。

请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。

nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。

示例 1:

输入: nums1 = [4,1,2], nums2 = [1,3,4,2].  
输出: [-1,3,-1]  
解释:  
对于 num1 中的数字 4 ，你无法在第二个数组中找到下一个更大的数字，因此输出 -1 。  
对于 num1 中的数字 1 ，第二个数组中数字1右边的下一个较大数字是 3 。  
对于 num1 中的数字 2 ，第二个数组中没有下一个更大的数字，因此输出 -1 。

示例 2:  
输入: nums1 = [2,4], nums2 = [1,2,3,4].  
输出: [3,-1]  
解释:  
对于 num1 中的数字 2 ，第二个数组中的下一个较大数字是 3 。  
对于 num1 中的数字 4 ，第二个数组中没有下一个更大的数字，因此输出-1 。

提示：

- 1 <= nums1.length <= nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 10^4
- nums1和nums2中所有整数 互不相同
- nums1 中的所有整数同样出现在 nums2 中




```go
func nextGreaterElement(nums1 []int, nums2 []int) []int {
    res := make([]int, len(nums1))
    for i := range res { res[i] = -1 }
    m := make(map[int]int, len(nums1))
    for k, v := range nums1 { m[v] = k }

    stack := []int{0}
    for i := 1; i < len(nums2); i++ {
        top := stack[len(stack)-1]
        if nums2[i] < nums2[top] {
            stack = append(stack, i)
        } else if nums2[i] == nums2[top] {
            stack = append(stack, i)
        } else {
            for len(stack) != 0 && nums2[i] > nums2[top] {
                if v, ok := m[nums2[top]]; ok {
                    res[v] = nums2[i]
                }
                stack = stack[:len(stack)-1]
                if len(stack) != 0 {
                    top = stack[len(stack)-1]
                }
            }
            stack = append(stack, i)
        }
    }
    return res
}

```




503.下一个更大元素II 

这道题和 739. 每日温度 几乎如出一辙，可以自己尝试做一做

https://programmercarl.com/0503.%E4%B8%8B%E4%B8%80%E4%B8%AA%E6%9B%B4%E5%A4%A7%E5%85%83%E7%B4%A0II.html  



```go

func nextGreaterElements(nums []int) []int {
    length := len(nums)
    result := make([]int,length)
    for i:=0;i<len(result);i++{
        result[i] = -1
    }
    //单调递减，存储数组下标索引
    stack := make([]int,0)
    for i:=0;i<length*2;i++{
        for len(stack)>0&&nums[i%length]>nums[stack[len(stack)-1]]{
            index := stack[len(stack)-1]
            stack = stack[:len(stack)-1] // pop
            result[index] = nums[i%length]
        }
        stack = append(stack,i%length)
    }
    return result
}

```
