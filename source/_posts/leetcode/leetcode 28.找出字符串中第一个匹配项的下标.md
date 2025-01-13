---
title: leetcode 28.找出字符串中第一个匹配项的下标
date: 2023-05-31 22:27:00
modificationDate: 2023 五月 31日 星期三 22:27:00
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---

[28. 找出字符串中第一个匹配项的下标 - 力扣（Leetcode）](https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description/)
![](../../imgs/Pasted%20image%2020230531222721.png)

# 简单解法
利用split 函数，判断是否能够拆分，如果
```go
func strStr(haystack string, needle string) int {
	// 使用split 函数，如果存在needle,则会把其切分为至少两个元素的切片
	splitList := strings.Split(haystack, needle)
	// 如果长度为1，且needle!=haystack 说明没找到匹配项，返回-1
	if len(splitList)== 1 && needle!=haystack {
		return -1
	}
	if len(splitList) > 1 {
		return len(splitList[0])
	}
	// needle 在haystack的最开头，返回0
	return 0
}
```


```go

  
func main() {  
    haystack := "good"  
    needle := "go"  
    splitList := strings.Split(haystack, needle) // 如果在首位相同，前边会有个空字符串。  
    fmt.Println(splitList, len(splitList))  
    fmt.Println("tmp:", splitList[0])  
}

// [""  "od"] 2

```

# 双指针解法
朴素解法
直观的解法的是：枚举原串 ss 中的每个字符作为「发起点」，每次从原串的「发起点」和匹配串的「首位」开始尝试匹配：

匹配成功：返回本次匹配的原串「发起点」。
匹配失败：枚举原串的下一个「发起点」，重新尝试匹配。


```go
func strStr(haystack string, needle string) int {
    cur := 0

    for cur < len(haystack) {
        p1 := cur
        p2 := 0

        for p1 < len(haystack) && p2 < len(needle) && needle[p2] == haystack[p1] {
            p1++
            p2++
        }

        if p2 == len(needle) {
            return cur
        }

        cur++
    }

    return -1
}

```

可以修改为for 循环

```go
func strStr(haystack string, needle string) int {
    if len(haystack) < len(needle) {
        return -1
    }

    for i:= 0; i < len(haystack); i++ {
        p1 := i
        p2 := 0

        for p1 < len(haystack) && p2 < len(needle) && needle[p2] == haystack[p1] {
            p1++
            p2++
        }

        if p2 == len(needle) {
            return i
        }

    }

    return -1
}

```


# TODO　KMP 算法
