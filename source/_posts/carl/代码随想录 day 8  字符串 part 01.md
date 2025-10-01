---
title: 代码随想录 day 8  字符串 part 01
date: 2025-01-05 22:26:21
modificationDate: 2025 一月 5日 星期日 22:26:21
categories: 
	- carl
tags: []
sticky: []
published: false
category_bar: true
---

# 第四章 字符串part01

## 今日任务

●  344.反转字符串

●  541. 反转字符串II

●  卡码网：54.替换数字

## 详细布置

### 344.反转字符串

建议： 本题是字符串基础题目，就是考察 reverse 函数的实现，同时也明确一下 平时刷题什么时候用 库函数，什么时候 不用库函数

题目链接/文章讲解/视频讲解：[https://programmercarl.com/0344.%E5%8F%8D%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2.html](https://programmercarl.com/0344.%E5%8F%8D%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2.html)


```go

func reverseString(s []byte) {
    left := 0
    right := len(s)-1
    for left < right {
        s[left], s[right] = s[right], s[left]
        left++
        right--
    }
}

```


### 541. 反转字符串II

建议：本题又进阶了，自己先去独立做一做，然后在看题解，对代码技巧会有很深的体会。

题目链接/文章讲解/视频讲解：[https://programmercarl.com/0541.%E5%8F%8D%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2II.html](https://programmercarl.com/0541.%E5%8F%8D%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2II.html)


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
#JavaScript:


```


### 卡码网：54.替换数字

建议：对于线性数据结构，填充或者删除，后序处理会高效的多。好好体会一下。

题目链接/文章讲解：[替换数字](https://programmercarl.com/kamacoder/0054.%E6%9B%BF%E6%8D%A2%E6%95%B0%E5%AD%97.html)



```go

package main

import "fmt"

func main(){
    var strByte []byte
    
    fmt.Scanln(&strByte)
    
    for i := 0; i < len(strByte); i++{
        if strByte[i] <= '9' && strByte[i] >= '0' {
            inserElement := []byte{'n','u','m','b','e','r'}
            strByte = append(strByte[:i], append(inserElement, strByte[i+1:]...)...)
            i = i + len(inserElement) -1
        }
    }
    
    fmt.Printf(string(strByte))
}

```
