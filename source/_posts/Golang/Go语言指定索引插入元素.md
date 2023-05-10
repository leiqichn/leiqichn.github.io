---
title: Go语言指定索引插入元素
date: 2023-05-10 23:42:50
modificationDate: 2023 五月 10日 星期三 23:42:50
categories: 
	- Golang
tags: [golang]
sticky: []
hide: false
category_bar: true
---

在Go语言中，可以使用切片（slice）的 append 函数和切片的切割（slice expression）操作来在指定索引位置插入元素。

下面是一个示例代码，它插入一个元素到切片的第二个位置：


```go
package main

import "fmt"

func main() {
    a := []int{1, 2, 3, 4}
    i := 1 // 要插入的位置
    b := append(a[:i], append([]int{5}, a[i:]...)...) // 在切片的第二个位置插入数字5
    fmt.Println(b) // 输出 [1 5 2 3 4]
}
```

在上面的代码中，我们首先定义了切片 a，包含整数 1、2、3、4。然后我们定义要插入的位置 i 为第二个元素（也就是索引值为 1）。

接着，在 append 函数中，我们将原始切片 a 切割成两部分：从起始位置到插入位置的子切片 a[:i]，和从插入位置到末尾的子切片 a[i:]。我们在这两个子切片之间插入了元素 5，然后使用两个 append 函数将它们拼接回去。

最后，我们将结果赋值给变量 b 并打印输出它。