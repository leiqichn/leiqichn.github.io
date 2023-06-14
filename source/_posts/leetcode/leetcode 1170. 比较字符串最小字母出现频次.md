---
title: leetcode 1170. 比较字符串最小字母出现频次
date: 2023-06-14 23:28:09
modificationDate: 2023 六月 14日 星期三 23:28:09
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---
[1170. 比较字符串最小字母出现频次 - 力扣（Leetcode）](https://leetcode.cn/problems/compare-strings-by-frequency-of-the-smallest-character/description/)
![](../../imgs/Pasted%20image%2020230614235423.png)

后缀和（Prefix Sum）是一种常用于区间和计算的技巧。它通过预处理把一个数组的前缀和先计算出来，然后在查询某个区间的和时，只需要构造两个前缀和相减即可得到所求的区间和。

具体而言，假设有一个长度为 n 的整数数组 A，记 S[i] 为 A[0]+A[1]+...+A[i-1] 的前缀和，其中 0≤i<n。那么对于任何 0≤l≤r<n，A[l]+A[l+1]+...+A[r] = S[r+1]-S[l]。

在实际的应用中，如果需要进行多次区间和查询，可以利用后缀和技巧预处理出 A 数组的前缀和，并存储在一个新的数组 S 中。这样，对于任意区间 [l,] 查询，只需要计算 S[r+1]-S[l] 即可，时间复杂度为 O(1)。


不使用后缀和
```go
func f(s string) int {
    cnt := 0
    ch := 'z'
    for _, c := range s {
        if c < ch {
        ch = c
        cnt = 1
        } else if c == ch {
        cnt++
        }
    }
    return cnt
}

func numSmallerByFrequency(queries []string, words []string) []int {
    count := make([]int, 12)
    // 先计算word 里的每个数 f(s)是s字符串中最小字符串的数量
    for _, s := range words {
        count[f(s)] += 1
    }
    res := make([]int, len(queries))
    for i, s := range queries {
        for idx, c := range count { // 遍历count
            if c>0 && f(s) < idx {// 如果count>0,则说明该最小字符串数量(idx) 的个数为c。需要将res 加上这个数量c
                res[i]+=c
            }
        }
    }
    return res
}


```


```go
func f(s string) int {
    cnt := 0
    ch := 'z'
    for _, c := range s {
        if c < ch {
        ch = c
        cnt = 1
        } else if c == ch {
        cnt++
        }
    }
    return cnt
}

func numSmallerByFrequency(queries []string, words []string) []int {
    count := make([]int, 12)
    // 先计算word 里的每个数
    for _, s := range words {
        count[f(s)] += 1
    }
    // 计算后缀和,i+1 就是大于i位置的所有个数
    for i := 9; i >= 1; i-- {
        count[i] += count[i + 1]
    }
    res := make([]int, len(queries))
    for i, s := range queries {
        res[i] = count[f(s) + 1]
    }
    return res
}

```

**为什么是res[i] = count[f(s) + 1] ，而不是res[i] = count[f(s)]？**

在`numSmallerByFrequency`函数中， `count`数组记录的是各个不同频次出现的次数，因此 `count[i]`代表所有最小字母出现频次不于 i 的字符串的数量。

如果对于 `queries` 中的某个字符串 `s` ，它的最小字母出现频次为 `f(s)`，那么可以依据 `count` 数组计算比该字符串要小的字符串的数量。由于 count数组是累加的，所以要计算比这个字符串严格小的字符串数量，只需要累加从 `f(s)+1` 开始的所有频次出现次数即可：


`res[i] = count[f(s) + 1]`

这里使用的是 `f(s)+1` 而不是 `f(s)` 是因为对于频次相同时应该被视为相同大小，否则我们会算入一些等于当前获得的最小频率的字符串。