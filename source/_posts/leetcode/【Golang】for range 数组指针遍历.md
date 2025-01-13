---
title: 【Golang】for range 数组指针遍历
date: 2024-12-04 00:55:24
modificationDate: 2024 十二月 4日 星期三 00:55:24
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---

在Go语言中，使用`for range`遍历数组或切片时，确实会对每个元素进行值拷贝。但是，当你遍历的是指针数组（如`[]*Student`）时，虽然指针本身是被拷贝的，但拷贝的指针仍然指向原始的内存地址。因此，通过这个拷贝的指针修改指向的值会影响到原始数据。

这意味着，即使`for range`对指针进行了拷贝，你仍然可以通过这个拷贝的指针修改原始结构体的内容。下面是一个例子来说明这一点：

```go
package main

import "fmt"

type Student struct {
    Name string
    Age  int
}

func main() {
    students := []*Student{
        {Name: "Alice", Age: 20},
        {Name: "Bob", Age: 22},
    }

    // 使用for range遍历指针数组
    for _, student := range students {
        // 修改指向的结构体的内容
        student.Age += 1 // 给每个学生的年龄加1
    }

    // 打印修改后的students数组
    for _, student := range students {
        fmt.Printf("Name: %s, Age: %d\n", student.Name, student.Age)
    }
}
```

在这个例子中，尽管`for range`对每个`*Student`指针进行了拷贝，但通过这个拷贝的指针修改`Age`字段时，修改的是原始`Student`结构体的内容。因此，当再次遍历`students`数组时，你会看到每个学生的年龄都已经增加了。

总结来说，当你使用`for range`遍历指针数组并修改指向的值时，这些修改会反映在原始数组上，因为指针拷贝仍然指向原始的内存地址。
