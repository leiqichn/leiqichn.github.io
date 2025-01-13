---
title: 代码随想录 day8  字符串part 01
date: 2024-11-08 00:26:03
modificationDate: 2024 November 8th Friday 00:50:56
categories: 
	- carl
tags: []
sticky: []
hide: true
category_bar: true
---
## 今日任务

●  344.反转字符串

●  541. 反转字符串II

●  卡码网：54.替换数字

## 详细布置

### 344.反转字符串

建议： 本题是字符串基础题目，就是考察 reverse 函数的实现，同时也明确一下 平时刷题什么时候用 库函数，什么时候 不用库函数

题目链接/文章讲解/视频讲解：[https://programmercarl.com/0344.%E5%8F%8D%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2.html](https://programmercarl.com/0344.%E5%8F%8D%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2.html)

**思路就是双指针，首尾调换**
```go
// 一把过
func reverseString(s []byte)  {
    left, right := 0, len(s)-1

    for left < right {
        s[left],s[right] = s[right], s[left]
        left++
        right--
    }
}

```


```go
// 正常简写方案
func reverseString(s []byte)  {

    for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
        s[i], s[j] = s[j], s[i]
    }

}
```


### 541. 反转字符串II

建议：本题又进阶了，自己先去独立做一做，然后在看题解，对代码技巧会有很深的体会。

题目链接/文章讲解/视频讲解：[https://programmercarl.com/0541.%E5%8F%8D%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2II.html](https://programmercarl.com/0541.%E5%8F%8D%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2II.html)

从字符串开头算起, 每计数至 2k 个字符，就反转这 2k 个字符中的前 k 个字符。

如果剩余字符少于 k 个，则将剩余字符全部反转。

比较巧妙的是，直接按照2k 为step， 如果i+k <= length ，则反转前k(这个时候是直到i开始位置的，所以可以方便的反转前k个)

```go
func reverseStr(s string, k int) string {
    ss := []byte(s)
    length := len(s)
    for i := 0; i < length; i += 2 * k {
     // 1. 每隔 2k 个字符的前 k 个字符进行反转
     // 2. 剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符
        if i + k <= length {
            reverse(ss[i:i+k])
        } else {
            reverse(ss[i:length])
        }
    }
    return string(ss)
}

func reverse(b []byte) {
    left := 0
    right := len(b) - 1
    for left < right {
        b[left], b[right] = b[right], b[left]
        left++
        right--
    }
}
```

### 卡码网：54.替换数字

建议：对于线性数据结构，填充或者删除，后序处理会高效的多。好好体会一下。

题目链接/文章讲解：[https://programmercarl.com/kama54.%E6%9B%BF%E6%8D%A2%E6%95%B0%E5%AD%97.html](https://programmercarl.com/kama54.%E6%9B%BF%E6%8D%A2%E6%95%B0%E5%AD%97.html)

思路：
很多数组填充类的问题，做法一般是预先给数组留好位置，然后再进行填充。
go 语言的技巧，利用byte数组传入number byte, 

```go

import "fmt"

func main(){
    var strByte []byte
    
    fmt.Scanln(&strByte)
    
    for i := 0; i < len(strByte); i++{
        if strByte[i] <= '9' && strByte[i] >= '0' {
            inserElement := []byte{'n','u','m','b','e','r'}
            strByte = append(strByte[:i], append(inserElement, strByte[i+1:]...)...)
            i = i + len(inserElement) -1 // 记得跟新i跳过number的位置
        }
    }
    
    fmt.Printf(string(strByte))
}

```
