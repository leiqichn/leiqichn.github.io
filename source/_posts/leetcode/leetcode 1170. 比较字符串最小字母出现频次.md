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
