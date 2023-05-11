---
title: Go语言-byte和rune 有什么区别 byte rune 转为int
date: 2023-05-12 00:06:34
modificationDate: 2023 五月 12日 星期五 00:06:34
categories: 
	- Golang
tags: []
sticky: []
hide: false
category_bar: true
---


在 Go 语言中，byte 和 rune 都是用来表示字符类型的数据类型。

byte 是 uint8 的别名，在 Go 中通常用于表示 ASCII 字符集中的一个字节。
rune 是 int32 的别名，在 Go 中通常用于表示 Unicode 字符集中的一个代码点。
因此，对于 ASCII 字符来说，byte 和 rune 的值是相同的，但是对于大部分 Unicode 字符来说，它们是不同的。

将 byte 或 rune 转换为 int 可以使用类型转换操作符：


```go
b := byte('0')
i := int(b) - int('0') // 将 byte '0' 转换为 int 0
// 上边可以简写为
i := b - '0'
r := rune('中')
i := int(r)             // 将 rune '中' 转换为 int 类型（其实是它的 Unicode 码点）
```

将 int 转换为 byte 或 rune 可以使用类型断言或类型转换操作符，但是需要注意溢出的情况。例如：


```go
i := 10
b := byte(i)   // 溢出！编译器会忽略高位部分，直接取低位部分的字节
r := rune(i)
if r < 0xFFFF {
    r = rune(b) // 类型断言
}
```

可以通过判断 r 是否小于 0xFFFF 来检测转换是否正确，因为 Unicode 的码点范围在 0～0x10FFFF，超过该范围的值会被认为是无效码点。