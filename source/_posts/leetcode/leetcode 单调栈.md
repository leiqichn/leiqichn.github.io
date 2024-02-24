---
title: leetcode 单调栈
date: 2024-02-24 23:57:54
modificationDate: 2024 二月 25日 星期日 00:52:27
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---
单调栈用途不太广泛，只处理一类典型的问题，比如「下一个更大元素」，「上一个更小元素」

输入一个数组 `nums`，请你返回一个等长的结果数组，结果数组中对应索引存储着下一个更大元素，如果没有更大的元素，就存 -1


```go
// 注意：go 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
// 本代码不保证正确性，仅供参考。如有疑惑，可以参照我写的 java 代码对比查看。

func nextGreaterElement(nums []int) []int {
    n := len(nums)
    // 存放答案的数组
    res := make([]int, n)
    // 倒着往栈里放
    s := make([]int, 0)

    for i := n - 1; i >= 0; i-- { // 倒着入栈是为了后边正着出栈
        // 判定个子高矮
        for len(s) > 0 && s[len(s)-1] <= nums[i] {
            // 矮个起开，反正也被挡着了。。。
            s = s[:len(s)-1]
        }
        // nums[i] 身后的更大元素
        if len(s) == 0 { // 没有更大的元素
            res[i] = -1
        } else {
            res[i] = s[len(s)-1] // 正着出栈
        }
        s = append(s, nums[i]) // 当前元素
    }
    return res
}


```
参考：
https://labuladong.online/algo/data-structure/monotonic-stack