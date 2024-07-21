
---
title: Golang 使用new创建slice
date: 2024-07-21 14:14:35
modificationDate: 2024 July 21st Sunday 14:15:40
categories: 
	- Golang
tags: []
sticky: []
hide: false
category_bar: true
---
在 Go 语言中，new 关键字用于分配类型为 T 的零值并返回其地址，即类型为 *T 的值。对于 slice 来说，可以使用 new 来分配一个指向 slice 的指针，但是通常我们不这样做，因为 slice 是引用类型，我们更倾向于直接使用 make 函数来创建 slice。

然而，如果确实需要使用 new 来创建一个 slice 的指针，可以这样做：


```go
var s *[]int // 声明一个指向int类型slice的指针
s = new([]int) // 分配一个int类型的slice，并将其地址赋给s
```

但是，这样创建的 slice 是一个空的 slice，它没有任何底层数组（即 nil 的数组），并且长度和容量都是 0。如果需要一个具有特定长度和容量的 slice，应该使用 make 函数：


```go
s := make([]int, length, capacity) // 创建一个长度为 length，容量为 capacity 的int类型slice
```

如果使用 new 创建了一个 slice 指针，并且想要初始化它，可以这样做：


```go
s := new([]int)
*s = make([]int, length, capacity) // 通过解引用指针并使用make来初始化slice
```

在大多数情况下，直接使用 make 函数来创建 slice 是更常见和更简单的方法。使用 new 创建 slice 指针通常不是必要的，除非你有特定的需求，比如在函数中返回一个 slice 的指针，或者你需要在多个地方共享同一个 slice 的引用。
