---
title: Go语言-接口
date: 2023-04-21 00:42:26
modificationDate: 2023 四月 21日 星期五 00:42:26
categories: 
	- Golang
tags: []
sticky: []
hide: false
category_bar: true
---


在 Go 语言中，接口(interface)是一种类型，它定义了对象的行为规范，即定义了一组方法签名，而不需要指定具体的实现。接口使得不同的类型可以通过实现相同的方法集合来进行互换使用。

以一个简单的例子来说明接口的作用，在下面这段代码中，接口Printer定义了一个打印的方法Print()：


```go
type Printer interface {
    Print()
}

type User struct {
    name string
}

func (u User) Print() {
    fmt.Println(u.name,"我爱加班")
} 

func printAll(ps []Printer) {
    for _, p := range ps {
        p.Print()
    }
}

func main() {
    var ps []Printer
    ps = append(ps, User{"Alice"})
    ps = append(ps, User{"Bob"})
    printAll(ps)
}
```

在main函数中，我们创建了一个ps的切片，里面放了两个User类型的元素。然后调用printAll打印所有的元素，因为User类型实现了Printer接口中定义的Print() 方法，所以可以将User类型的变量赋值给Print()参数中的表达式，并且调用p.Print() 方法。最终的输出结果为：

```go
Alice 我爱加班
Bob 我爱加班
```

在这段代码中，我们通过接口将**User类型**与PrintAll() 函数解耦，这样当我们需要添加**新的类型时，只需要实现Print()方法**即可，而不需要修改**PrintAll()函数实现**。

比如现在需要有个老板类型，也要打印，我们只要实现老板对应的Print 方法即可，而不用修改**PrintAll()函数实现**。这样我们应该会更好理解接口的使用场景：适用于数量比较多的多个对象，**有相同的特征**，我们将其抽象出来，降低代码耦合性。


```go
type Boss struct {
    name string
}

func (b Boss) Print() {
    fmt.Println("你明天不用来了")
} 
```


其实我们可以将其类比于现实生活中的“合同”或“协议”等，接口定义了一组规则和方法集合，当你实现接口时，就像在签署一个合同，你同意遵守这个合同的规定，将这个合同上的对应部分填上具体的内容，这样就可以按照**合同的规定**进行处理。

同时，接口的使用，使得代码更加灵活、可扩展和相互独立，降低了耦合性，提高了代码的可维护性和重复利用性。