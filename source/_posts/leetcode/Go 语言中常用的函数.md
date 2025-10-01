---
title: Go 语言中常用的函数
date: 2023-05-15 21:44:43
modificationDate: 2023 五月 15日 星期一 21:44:43
categories: 
	- leetcode
tags: []
sticky: []
published: false
category_bar: true
---

## strings.ReplaceAll

这个函数是 Go 语言 strings 包中的一个函数，它的作用是将字符串中所有出现的指定子字符串替换为另外一个字符串。

在此函数中，第一个参数 address 是需要进行替换的原始字符串，第二个参数 "." 是需要被替换的子字符串，第三个参数 "[.]" 是用来替换子字符串的新字符串。

示例代码如下：


```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	address := "192.168.1.1"
	newAddress := strings.ReplaceAll(address, ".", "[.]")
	fmt.Println(newAddress)
}
```

运行以上示例代码，输出将是 192[.]168[.]1[.]1。可以看到，原始字符串中所有的 "." 都被替换成了 "[.]"。