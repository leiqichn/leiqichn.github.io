---
title: 【go】初始化双向列表List
date: 2024-01-22 22:39:01
modificationDate: 2024 一月 22日 星期一 22:39:06
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---

在Go语言中，两种方法都可以用于初始化一个`list.List`。

1. `queue := &list.List{}`: 这是使用结构体字面量的方式，创建一个 `list.List` 类型的结构体变量，并返回该结构体的指针。这种方式创建了一个空的链表。
    
2. `queue := list.New()`: 这是使用 `list` 包中的 `New` 函数来创建一个新的 `list.List`。`New` 函数返回一个指向新创建的 `list.List` 实例的指针。同样，这种方式也创建了一个空的链表。
    

两种方式都是有效的