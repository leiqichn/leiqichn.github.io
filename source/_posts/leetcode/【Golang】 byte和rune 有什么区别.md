---
title: 【Golang】 byte和rune 有什么区别
date: 2024-11-23 12:38:13
modificationDate: 2024 十一月 23日 星期六 12:38:13
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---

byte 和rune 有什么区别？
	在Go语言（Golang）中，byte和rune是两种不同的数据类型，它们在处理文本数据时有不同的用途和含义：

byte：

byte是uint8的别名，即一个无符号的8位整数。
在Go语言中，byte通常用于表示字节（byte），即数据的基本单位。
byte可以存储任何0到255之间的值，因为一个字节有8位，每位可以是0或1，所以总共有256种可能的值（从0到255）。
rune：

rune是int32的别名，即一个有符号的32位整数。
rune在Go语言中用于表示一个Unicode码点（Unicode scalar value），可以表示任何Unicode字符。
rune类型用于处理字符串中的单个字符，特别是对于需要表示多字节字符（如中文、日文、韩文等）的Unicode字符非常有用。
由于rune是一个32位整数，它可以表示从0到0x10FFFF（即Unicode的最大值）的任何值。
区别：

大小：byte是8位的，而rune是32位的。
用途：byte用于处理字节数据，rune用于处理Unicode字符。
范围：byte的范围是0到255，而rune的范围是0到0x10FFFF。
编码：在字符串中，byte类型表示的是UTF-8编码的字节序列，而rune类型表示的是Unicode码点。例如，一个包含中文字符的字符串在byte切片中可能包含多个字节，但在rune切片中，每个rune值对应一个Unicode字符。
在处理文本数据时，选择byte还是rune取决于你的具体需求，如果你需要处理原始字节数据，比如文件I/O或者网络传输，可能会使用byte。而如果你需要处理文本数据，特别是涉及到多字节字符集的文本，使用rune会更加方便。