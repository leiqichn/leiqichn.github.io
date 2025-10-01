
---
title: golang 中格式化打印单个字符
date: 2024-05-03 16:58:56
modificationDate: 2024 May 3rd Friday 16:59:24
categories: 
	- Golang
tags: []
sticky: []
hide: false
category_bar: true
---

在Go语言中，`fmt.Printf` 函数是用来格式化输出的，它接受一个格式化字符串作为第一个参数，后面跟着相应的参数。格式化字符串中可以包含一些格式化动词（也称为转换说明符），它们定义了如何将相应的参数值转换为字符串并输出。

`%c` 是一个格式化动词，它指定了对应的参数应该被转换为一个单一的Unicode字符并输出。当你在 `fmt.Printf` 中使用 `%c`，并且传入一个整数（`int` 类型）时，它会将该整数值转换为该整数值对应的Unicode码点的字符。

例如：

```go
package main

import "fmt"

func main() {
    var codePoint int = 65 // ASCII码中A的码点
    fmt.Printf("%c\n", codePoint) // 输出: A
}
```

在这个例子中，变量 `codePoint` 的值为 `65`，它是大写字母 "A" 在ASCII编码中的码点。`fmt.Printf("%c\n", codePoint)` 将这个整数值格式化为字符 "A" 并输出。

在处理字节数组 `[]byte` 并想要将每个字节转换为对应的字符时，`%c` 非常有用，因为Go的 `string` 类型是UTF-8编码的，每个字节可以是一个字符的一部分。例如：

```go
package main

import "fmt"

func main() {
    s := "hello"
    bytes := []byte(s)

    for i, b := range bytes {
        fmt.Printf("Byte %d: %c\n", i, b)
    }
    // 输出:
    // Byte 0: h
    // Byte 1: e
    // Byte 2: l
    // Byte 3: l
    // Byte 4: o
}
```

在这个例子中，我们遍历字符串 `"hello"` 的字节表示，并使用 `%c` 格式化每个字节为字符。由于 "hello" 由纯ASCII字符组成，每个字节都是一个完整的字符。如果处理包含多字节UTF-8字符的字符串，单独的字节可能不会形成有效的字符。