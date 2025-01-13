---
title: 代码随想录 day 9  字符串part 02
date: 2024-11-08 00:09:44
modificationDate: 2024 November 8th Friday 00:24:29
categories: 
	- carl
tags: []
sticky: []
hide: false
category_bar: true
---

● 151.翻转字符串里的单词

● 卡码网：55.右旋转字符串

● 28. 实现 strStr()

● 459.重复的子字符串

● 字符串总结

● 双指针回顾

## 详细布置

### 151.翻转字符串里的单词

建议：这道题目基本把 刚刚做过的字符串操作 都覆盖了，不过就算知道解题思路，本题代码并不容易写，要多练一练。

题目链接/文章讲解/视频讲解：[https://programmercarl.com/0151.%E7%BF%BB%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2%E9%87%8C%E7%9A%84%E5%8D%95%E8%AF%8D.html](https://programmercarl.com/0151.%E7%BF%BB%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2%E9%87%8C%E7%9A%84%E5%8D%95%E8%AF%8D.html)



```go
import (
	"fmt"
)

func reverseWords(s string) string {
	//1.使用双指针删除冗余的空格
	slowIndex, fastIndex := 0, 0
	b := []byte(s)
	//删除头部冗余空格
	for len(b) > 0 && fastIndex < len(b) && b[fastIndex] == ' ' {
		fastIndex++
	}
    //删除单词间冗余空格
	for ; fastIndex < len(b); fastIndex++ {
		if fastIndex-1 > 0 && b[fastIndex-1] == b[fastIndex] && b[fastIndex] == ' ' {
			continue
		}
		b[slowIndex] = b[fastIndex]
		slowIndex++
	}
	//删除尾部冗余空格
	if slowIndex-1 > 0 && b[slowIndex-1] == ' ' {
		b = b[:slowIndex-1]
	} else {
		b = b[:slowIndex]
	}
	//2.反转整个字符串
	reverse(b)
	//3.反转单个单词  i单词开始位置，j单词结束位置
	i := 0
	for i < len(b) {
		j := i
		for ; j < len(b) && b[j] != ' '; j++ {
		}
		reverse(b[i:j])
		i = j
		i++
	}
	return string(b)
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

### 卡码网：55.右旋转字符串

建议：题解中的解法如果没接触过的话，应该会想不到

题目链接/文章讲解：

[https://programmercarl.com/kama55.%E5%8F%B3%E6%97%8B%E5%AD%97%E7%AC%A6%E4%B8%B2.html](https://programmercarl.com/kama55.%E5%8F%B3%E6%97%8B%E5%AD%97%E7%AC%A6%E4%B8%B2.html)


先反转整个字符串，再反转前部分和后部分。


```go

package main
import "fmt"

func reverse (strByte []byte, l, r int){
    for l < r {
        strByte[l], strByte[r] = strByte[r], strByte[l]
        l++
        r--
    }
}


func main(){
    var str string
    var target int
    
    fmt.Scanln(&target)
    fmt.Scanln(&str)
    strByte := []byte(str)
    
    reverse(strByte, 0, len(strByte) - 1)
    reverse(strByte, 0, target - 1)
    reverse(strByte, target, len(strByte) - 1)
    
    fmt.Printf(string(strByte))
}

```
