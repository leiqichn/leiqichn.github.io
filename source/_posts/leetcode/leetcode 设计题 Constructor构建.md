---
title: leetcode 设计题 Constructor构建
date: 2023-05-14 22:13:21
modificationDate: 2023 五月 14日 星期日 22:13:21
categories: 
	- leetcode
tags: [设计题]
sticky: []
hide: false
category_bar: true
---


在面向对象编程中，构造函数通常用于创建新对象并初始化其属性。对于 LeetCode 样例题目 "Design Parking System" 中的 ParkingSystem 结构体，可以这样编写 Constructor 方法：


```go
type ParkingSystem struct {
    carNums map[int]int // 记录每种停车位的数量
}

func Constructor(big int, medium int, small int) ParkingSystem {
    return ParkingSystem{
        carNums: map[int]int{1: big, 2: medium, 3: small}, // 初始化 carNums 映射
    }
}
```

在这个实现中，我们使用传递给 Constructor 方法的三个整数参数来初始化 ParkingSystem 结构体的属性。具体而言，我们使用 map[int]int 类型的 carNums 映射保持每种车位类型的可用数量。在初始化结构体时，我们使用字面量映射来启用 1、2 和 3 的停车位类型，并将它们的值与输入参数big、medium 和 small 相关联。

请注意，当声明类似 structA map[int]structB 的嵌套 map 时，只需要在创建 A 实例时初始化外部映射即可。此时内部的 structB 映射会默认为 nil，但可以在需要使用时通过相应的方法或直接进行初始化以此。例如，当需要在内部映射中添加元素时，可以先检查是否为 nil，然后在需要时进行初始化。

具体来说，如果需要创建一个名为 A 的 map[int]B 类型的 map 以及名为 B 的 map[int]int 类型的嵌套 map，则可以按以下方式实现：


```go
type B struct {
    m map[int]int
}

type A struct {
    m map[int]B
}

func main() {
    a := &A{
        m: make(map[int]B),
    }
    b := &B{
        m: make(map[int]int),
    }
    a.m[1] = *b // 给 A 中的第一个元素分配一个新的 B 结构体实例
}
```

在这个示例中，我们首先定义了类型 B 和 A。在 A 中，我们使用包含 int 键和 B 值的映射来保持所有项目的索引和子结构体指针。请注意，为了确保不会出现 **nil 引用错误**，我们还在代码中使用了 make 函数创建了一个空映射。

例如, 下边结构体中map 嵌套了另外一个结构体的map,
可以通过使用 make 函数和伪造的 Res 结构体实例定义方式来初始化一个新的 ParkingSystem 实例，然后在之后的代码中修改 carNums 映射对象。以下是一个示例：


```go
type Res struct {
    big map[int]int
}

type ParkingSystem struct {map
    carNums map[int]*Res // map 嵌套map
}

func NewParkingSystem() *ParkingSystem {
    return &ParkingSystem{carNums: make(map[int]*Res)} // 只用先make 一个空map,指向Res
}

func main() {
    ps := NewParkingSystem()
    ps.carNums[1] = &Res{big: make(map[int]int)}
}
```

在这个示例中，我们定义了一个名为 NewParkingSystem 的函数，它返回指向新的 ParkingSystem 实例的指针，并在函数体中使用 make 函数创建一个新的空指针映射。

然后在主函数的其他位置，我们通过传入适当的值来修改 carNums 中的每个停车场位置类型。请注意，与之前相同，我们在此处使用 & 参考运算符来提供指向新声明的 Res 结构体实例的指针。

总之，可以分别声明 ParkingSystem 和 Res 结构体，并通过调用适当的函数或编写正确的初始化代码，在以后的程序执行期间引用并修改它们。