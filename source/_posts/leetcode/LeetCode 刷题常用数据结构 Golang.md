---
title: LeetCode 刷题常用数据结构（Golang）
date: 2023-03-14
categories: 
	- leetcode
tags: []
sticky: []
published: false
category_bar: ["关于我","leetcode","about"]
---
## 前言

工作需要，最近使用Go 来刷算法题


## 数据结构

### 数组

#### 初始化

```go
// 初始化一个大小为10，默认值为0的数组
nums := make([10]int)

// 初始化一个二位boolean数组
visited := make([5][10]int)
```

#### 常用方法

```go
for i := 0; i < len(nums); i++ {
    // 访问num[i]
}
```

### 字符串 String

#### 初始化

```go
s1 := "hello world"

// 创建多行字符串
s2 := `This is a
multiline
string.`
```

#### 访问字符串

```go
// 可直接用索引访问字节（非字符）
s1 := "hello world"
first := s[0]

s2 := []byte(s1)
first := s2[0]
```

#### 修改字符串

```go
// 字符串的值是不可变的，可以分配一个新字符串值
s := "hello"
t := s

// 将字符串转为[]byte或[]rune可以进行修改
s1 := "hello world"
s2 := []byte(s1)   // s2 := []byte(s1) 转化为byte 之后可以对指定的index 进行修改
s2[0] = 'H' // s2[0] = 'H'
s3 := string(s2) // 通过string 转化元素。
```
[【Golang】 byte和rune 有什么区别](【Golang】%20byte和rune%20有什么区别.md)

#### 查询字符是否属于特定字符集

```go
    // 判断字符串s的i索引位置字符是否是元音，前边是字符串集合
    if strings.Contains("aeiouAEIOU", string(s[i])) {
        // ...
    }

package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "Hello, world!"
	substr := "world"

	// 检查str是否包含substr
	if strings.Contains(str, substr) {
		fmt.Println("The string contains the substring.")
	} else {
		fmt.Println("The string does not contain the substring.")
	}
}
```

#### 判断字符串大小

```go
if s1 == s2 {
    // 相等
} else {
    // 不相等
}
// Compare 函数可以用于比较，1大于，0相等，-1小于
// EqualFold 函数忽略大小写后比较
```

#### 拼接字符串

```go
// 支持直接用+进行连接，但是效率不高 字符串拼接使用+相连
s1 := "hello "
s2 := s1 + "world"
```

#### 高效拼接字符串

```go
// bytes.Buffer可以一次性连接
var b bytes.Buffer
b.WriteString("Hello")
b.WriteString("World")
b1 := b.String()

// 多个字符串拼接
var strs []string
strings.Join(strs, "World")
```

这段Go语言代码使用了`bytes.Buffer`类型，这是一个可变大小的字节缓冲区，常用于构建或获取字符串数据。下面是代码的逐行解释：

1. `var b bytes.Buffer` 这行代码声明了一个名为`b`的变量，类型为`bytes.Buffer`。`bytes.Buffer`是`bytes`包中的一个类型，它实现了`io.Writer`和`io.Reader`接口，允许你向缓冲区写入数据，也可以从缓冲区读取数据。
    
2. `b.WriteString("Hello")` 这行代码调用`bytes.Buffer`的`WriteString`方法，将字符串`"Hello"`写入到缓冲区`b`中。`WriteString`方法接受一个字符串参数，并将该字符串的字节表示形式追加到缓冲区的末尾。
    
3. `b.WriteString("World")` 这行代码再次调用`WriteString`方法，这次是将字符串`"World"`追加到缓冲区`b`的末尾。由于`WriteString`方法只是简单地追加数据，所以`"Hello"`和`"World"`会连续地存储在缓冲区中，中间没有空格或其他分隔符。
    
4. `b1 := b.String()` 这行代码调用`bytes.Buffer`的`String`方法，将缓冲区`b`中的内容转换为一个字符串，并赋值给变量`b1`。`String`方法返回缓冲区中所有字节的字符串表示形式，即`"HelloWorld"`。
    

这段代码创建了一个`bytes.Buffer`对象，向其中连续写入了两个字符串，然后提取了缓冲区中的全部内容作为一个字符串。最终，`b1`变量包含了字符串`"HelloWorld"`。这种方法可以用于高效地拼接大量字符串，因为它避免了多次内存分配和复制，特别是在处理大量数据时，使用`bytes.Buffer`通常比直接使用字符串连接操作更高效。
#### 整型 (或任意数据类型) 转为字符串

```go
// Itoa转换
i := 123
t := strconv.Itoa(i)

// Sprintf将数字转化为字符串
i := 123
t := fmt.Sprintf("%d", i)
```



### 切片 slice

#### 初始化

```go
// 初始化一个存储String类型的切片
slice := make([]string, 0)
slice := []string

// 初始化一个存储int类型的切片
slice := make([]int, 0)
slice := []int
```

#### 常用方法

```go
// 判断是否为空
if len(slice) == 0 {
    // 为空
}

// 返回元素个数
len()

// 访问索引元素
slice[i]

// 在尾部添加元素
slice = append(slice, 1)
```

### 通过切片模拟栈和队列

#### 栈
先进后出， 使用pop,在尾部弹出，需要将尾部元素删除

```go
// 创建栈
stack := make([]int, 0)
// push压入
stack = append(stack, 10)
// pop弹出
v := stack[len(stack) - 1]
stack = stack[:len(stack) - 1] // 左闭右开，需要将尾部元素删除 len(stack) -1 
// 检查栈空
len(stack) == 0 // 检查栈是否为空
```

#### 队列
先入先出

```go
// 创建队列
queue := make([]int, 0)
// enqueue入队
queue = append(queue, 10)
// dequeue出队
v := queue[0]
queue = queue[1:]
// 长度0为空
len(queue) == 0
```

### Map

```go
// 创建
m := make(map[string]int, 10)
// 设置kv
m["hello"] = 1
// 删除k
delete(m,"hello") // delete(map, "key")
// 遍历
for k, v := range m{
    // 操作
}

判断键 是否存在

if value, ok := dict["key1"]; ok {
        fmt.Printf(value)
    }
if value,ok := dict["key1]; ok {
		fmt.Printf(value)
}

// map键需要可比较，不能为slice、map、function
// map值都有默认值，可以直接操作默认值，如：m[age]++ 值由0变为1
// 比较两个map需要遍历，其中的kv是否相同，因为有默认值关系，所以需要检查val和ok两个值
```

### 标准库

#### SORT

```go
// int排序
sort.Ints([]int{})
// 字符串排序
sort.Strings([]string{})
```

#### MATH

```go
// int32 最大最小值
math.MaxInt32 
math.MinInt32
// int64 最大最小值（int默认是int64）
math.MaxInt64
math.MinInt64
```
![](../../imgs/Pasted%20image%2020241123132930.png)
#### COPY

删除指定index 的 
```go
// 删除a[i]，可以用 copy 将i+1到末尾的值覆盖到i（i 位置的地址上的值就被覆盖了）,然后末尾-1
copy(a[i:], a[i+1:])
a = a[:len(a)-1]

// make创建长度，则通过索引赋值
a := make([]int, n)
a[n] = x

// make长度为0，则通过append()赋值
a := make([]int, 0)
a = append(a, x)
```

#### 插入slice 元素

#### 删除slice 元素
### 类型转换

```go
// byte转数字 
// byte 和rune 都会转化为阿斯克吗，不同的是rune 遇到汉字是一个字符，byte 是三个
// byte 和int 转换需要 + '0'
// int 转byte 需要  int(s[0] - '0') 
// 单个byte 或 rune 可以前面直接加string 进行转换。[]byte{} []rune{} 也可以使用string 转换。
s = "12345"  // s[0] 类型是byte
num := int(s[0] - '0') // 1
str := string(s[0]) // "1"
b := byte(num + '0') // '1'
fmt.Printf("%d%s%c\n", num, str, b) // 111

// 字符串转数字
num, _ := strconv.Atoi()
str := strconv.Itoa()
```

`strconv.FormatInt` 和 `strconv.ParseInt` 是 Go 语言中用于进制转换的两个非常有用的函数。下面是如何使用这两个函数的示例：

### 使用 `strconv.FormatInt`

`strconv.FormatInt` 函数用于将一个整数（`int64` 类型）转换为指定进制的字符串。函数签名如下：

```go
func FormatInt(i int64, base int) string
```

- `i` 是要转换的整数。
- `base` 是目标进制，可以是 2（二进制）、8（八进制）、10（十进制）、16（十六进制）等。

#### 示例代码：

```go
package main

import (
    "fmt"
    "strconv"
)

func main() {
    num := int64(255)

    // 转换为二进制
    binaryStr := strconv.FormatInt(num, 2)
    fmt.Println("Binary:", binaryStr)

    // 转换为八进制
    octalStr := strconv.FormatInt(num, 8)
    fmt.Println("Octal:", octalStr)

    // 转换为十六进制
    hexStr := strconv.FormatInt(num, 16)
    fmt.Println("Hexadecimal:", hexStr)
}
```

### 使用 `strconv.ParseInt`

`strconv.ParseInt` 函数用于将一个字符串形式的数字转换为十进制整数。函数签名如下：

```go
func ParseInt(s string, base int, bitSize int) (i int64, err error)
```

- `s` 是要解析的字符串。
- `base` 是字符串的进制，可以是 0（自动检测进制）、2（二进制）、8（八进制）、16（十六进制）等。
- `bitSize` 是结果的位大小，通常为 0、8、16、32、64。如果为 0，则根据 `base` 自动选择合适的位大小。

#### 示例代码：

```go
package main

import (
    "fmt"
    "strconv"
)

func main() {
    // 二进制字符串
    binaryStr := "11111111"
    num, err := strconv.ParseInt(binaryStr, 2, 64)
    if err != nil {
        fmt.Println("Error:", err)
    } else {
        fmt.Println("Binary to Int:", num)
    }

    // 八进制字符串
    octalStr := "377"
    num, err = strconv.ParseInt(octalStr, 8, 64)
    if err != nil {
        fmt.Println("Error:", err)
    } else {
        fmt.Println("Octal to Int:", num)
    }

    // 十六进制字符串
    hexStr := "ff"
    num, err = strconv.ParseInt(hexStr, 16, 64)
    if err != nil {
        fmt.Println("Error:", err)
    } else {
        fmt.Println("Hexadecimal to Int:", num)
    }
}
```

这两个函数提供了强大的进制转换功能，使得在 Go 语言中处理不同进制的数字变得非常方便。


# 反转切片

```go
func reverseSlice(s []int) []int {
    for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
        s[i], s[j] = s[j], s[i]
    }
    return s
}

```

# 反转字符串

```go

func reverseString(s string) string {
    // 将字符串转换为 rune 切片
    runes := []rune(s)

    // 使用双指针法反转切片
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }

    // 将 rune 切片转换回字符串
    reversedString := string(runes)
    return reversedString
}
```

## 总结

以上是“术”的内容，算法之“道” 需要经过大量练习和思考才能习得，加油


参考：
[LeetCode 刷题常用数据结构（Go 篇） · Pseudoyu](https://www.pseudoyu.com/zh/2021/05/29/algorithm_data_structure_go/)
