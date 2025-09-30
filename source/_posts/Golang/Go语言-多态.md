---
title: Go语言-多态
date: 2023-04-21 00:32:20
modificationDate: 2023 四月 21日 星期五 00:52:51
categories: 
	- Golang
tags: []
sticky: []
hide: false
category_bar: true
---
Go语言中没有类，我们可以使用结构体作为对象，来绑定对应的方法。而接口是功能的抽象，是方法的集合。

我们来实现这样一个例子：
- 实现猫和狗**两个对象**，并且他们都有动作：叫，**但叫声不同**。再实现一个**对象鸟**，他除了叫，还会**飞**。

下面是基于Go语言，实现题目要求的代码：

```go
package main

import "fmt"

type Animal interface {
    Cry()
}

type Cat struct{}

func (c Cat) Cry() {
    fmt.Println("喵喵喵")
}

type Dog struct{}

func (d Dog) Cry() {
    fmt.Println("汪汪汪")
}

type Bird struct{}

func (b Bird) Cry() {
    fmt.Println("叽叽喳喳")
}

func (b Bird) Fly() {
    fmt.Println("我会飞")
}

func main() {
    var animal Animal

    // 创建一只猫
    animal = Cat{}
    animal.Cry()

    // 创建一只狗
    animal = Dog{}
    animal.Cry()

    // 创建一只鸟
    bird := Bird{}
    animal = bird
    animal.Cry()
    bird.Fly()
}
```

在上述代码中，定义了一个Animal接口和三个结构体Cat、Dog、Bird分别实现了这个接口。其中，Cat和Dog只能叫，而Bird除了叫外还可以飞行。在main函数中创建相应的对象并调用相应的方法。

运行上述代码，输出如下：

```
喵喵喵
汪汪汪
叽叽喳喳
我会飞
```

在这段代码中，我们使用了**接口的多态特性**，通过定义**Animal接口**，实现了**不同类型的对象之间的通用性**，并且在**Bird中新增了Fly() 方法**，符合面向对象的**开放封闭原则**。

