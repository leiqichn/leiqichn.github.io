---
title: LeetCode 1071. 字符串的最大公因子
date: 2024-01-03 23:12:16
modificationDate: 2024 一月 3日 星期三 23:12:51
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---

[1071. 字符串的最大公因子](https://leetcode.cn/problems/greatest-common-divisor-of-strings/)

![](../../imgs/Pasted%20image%2020240103231323.png)

**解题思路：**

## 暴力解法
```go
func gcdOfStrings(str1 string, str2 string) string {
    n1, n2 := len(str1), len(str2)

    // 从最长的可能的子串长度开始尝试
    for i := min(n1, n2); i > 0; i-- {
        if n1%i == 0 && n2%i == 0 {
            commonSubstring := str1[:i]

            // 检查是否满足条件
            if checkDivisible(str1, commonSubstring) && checkDivisible(str2, commonSubstring) {
                return commonSubstring
            }
        }
    }

    return ""
}

// 检查字符串是否能够整除
func checkDivisible(s string, sub string) bool {
    repeats := len(s) / len(sub)
    concatenated := repeatString(sub, repeats)
    return s == concatenated
}

// 重复字符串
func repeatString(s string, count int) string {
    result := ""
    for i := 0; i < count; i++ {
        result += s
    }
    return result
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}


```

## 数学方法


```go
func gcdOfStrings(str1 string, str2 string) string {
    if str1 + str2 != str2 + str1 {
        return ""
    }
    gcd := gcd(len(str1), len(str2))
    return str1[0:gcd]
}

  

func gcd(a, b int) int {
    for b != 0 {
        a, b = b, a % b
    }
    return a
}

```
