---
title: 字面值进行初始化和make初始化
date: 2023-07-03 22:23:44
modificationDate: 2023 七月 3日 星期一 22:23:44
categories: 
	- leetcode
tags: []
sticky: []
published: false
category_bar: true
---

可以给我举个例子 使用make 和使用字面值进行初始化的对比吗？


当需要创建动态大小的切片、映射或通道时，可以使用 make 函数进行初始化。以下是一个示例，比较了使用 make 和使用字面值进行初始化的对比：


```go
package main

import "fmt"

func main() {
	// 使用 make 初始化切片
	slice1 := make([]int, 0, 5)
	fmt.Println(slice1) // 输出: []

	// 使用字面值进行切片初始化
	slice2 := []int{1, 2, 3}
	fmt.Println(slice2) // 输出: [1 2 3]

	// 使用 make 初始化映射
	map1 := make(map[string]int)
	fmt.Println(map1) // 输出: map[]

	// 使用字面值进行映射初始化
	map2 := map[string]int{
		"one":   1		"two":   2,
		"three": 3,
	}
	fmt.Println(map2) // 输出: map[one:1 three:3 two:2]
}
```

在上述示例中，我们比较了使用 make 和使用字面值进行切和映射的初始化。

对于切片 slice1，我们使用 make 函数创建的切片是空的，长度为 0，但具有预分配的内部数组容量。
而对于切片 slice2，我们使用字面值直接提供了初始值 [1, 2, 3]。
对于映射 map1，我们使用 make 函数创建了一个空映射。
对于映射 map2，我们使用字面值直接提供了具有键和值的初始项。
通过比较这两种初始化方式，可以看到使用字面值进行初始化更简洁和直观，特别是在提供明确初值的情况下。而使用 make 主要用于需要动态大小的切片、映射或通道的初始化，因为它允许我们指定初始容量或其他选项。