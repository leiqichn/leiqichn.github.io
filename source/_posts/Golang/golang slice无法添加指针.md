---
title: golang slice无法添加指针
date: 2024-05-02 21:37:36
modificationDate: 2024 May 2nd Thursday 21:37:36
categories: 
	- Golang
tags: []
sticky: []
hide: false
category_bar: true
---

在Go语言中，指针是一种存储变量内存地址的数据类型。当你有一个指向`int`的指针，比如`timePtr *int`，你可以通过`*timePtr`来访问和修改指针指向的值。然而，指针本身是一个值类型，它存储的是变量的内存地址，而不是变量本身。

在你提供的`add`函数中：

```go
func add(timePtr *int) { *timePtr += 1 } // 增加一秒
```

`timePtr`是一个指向`int`的指针。虽然你可以通过`*timePtr`来间接修改它所指向的`int`值，但是你不能使用这个指针来创建一个关于`*int`的切片。原因如下：

1. **指针的值是地址**：`timePtr`变量存储的是`currentTime`变量的内存地址，而不是`currentTime`的值。切片是基于数组的，它们需要一个具体的数据集合来创建。

2. **切片的元素类型**：切片的元素类型是固定的，并且是在创建时确定的。你不能创建一个关于`*int`的切片，**因为切片的元素类型是**`int`，而不是`*int`（指向`int`的指针）。

3. **切片创建语法**：创建切片通常需要一个数组或另一个切片作为基础，或者使用`make`函数指定长度和容量。例如：
   ```go
   var arr [5]int
   slice1 := arr[:] // 基于数组的切片
   slice2 := make([]int, 5, 10) // 使用make创建切片
   ```

如果你的目的是创建一个记录时间变化历史的切片，你需要一个独立的切片来存储这些时间值。你可以在`main`函数中声明这样一个切片，并在CRUD操作中更新它：

```go
var currentTime int
var history []int // 用于记录历史时间

func add(timePtr *int, historyPtr *[]int) {
    *timePtr++
    historyPtr = append(*historyPtr, *timePtr)
}

func main() {
    currentTime = 0
    history = make([]int, 0) // 初始化历史切片

    add(&currentTime, &history)
    // 可以继续调用 add 并传入 &currentTime 和 &history 来记录更多时间点

    fmt.Println("History of times:", history)
}
```

在这个例子中，`history`是一个切片，用于存储时间点的历史记录。每次调用`add`函数时，我们不仅更新`currentTime`，还将新的时间点添加到`history`切片中。注意，由于切片是引用类型，我们传递`&history`来允许函数修改原始切片。