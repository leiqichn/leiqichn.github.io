---
title: Go语言中的byte类型与Unicode码点与整数的转换
date: 2023-07-09 22:22:16
modificationDate: 2023 七月 9日 星期日 22:22:16
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---

# byte类型与Unicode码点的转换
在Go语言中，byte 类型是无符号的8位整数类型，而字符类型 rune 则用于表示Unicode码点。

当我们将一个 byte 类型的值转换为对应的 int 类型时，它实际上是将字节的数值直接转换为 int。这种转换通常用于将ASCII字符转换为对应的整数。


```go
package main

import (
	"fmt"
)

func main() {
	b := byte('A')
	i := int(b)

	fmt.Printf("Byte: %c, Unicode码点: %d, 转换后的整数: %d\n", b, b, i)
}
```

在上面的示例代码中，我们将字符 'A' 转换为 byte 类型并赋值给变量 b，然后再将 b 转换为 int 类型并赋值给变量 i。输出结果如下：

```go
Byte: A, Unicode码点: 65, 转换后的整数: 65
```

可以看到，转换后的整数值与字符 'A' 的ASCII码值相同。
# byte类型与整数的转换
之前一直容易搞混byte类型与整数的转换和之前unicode 码点转换。整数的转换意思是a = byte('0'); var b int =0; 将a 转换为b的整数0；
在Go语言中，我们可以将字符 '0' 转换为对应的整数 0。这种转换可以通过 byte('0') - '0' 的方式实现，利用了字符的ASCII码值之间的差异。


```go
package main  
  
import (  
   "fmt"  
)  
  
func main() {  
   ch := '0'  
   num := int(ch - '0')  
  
   fmt.Printf("字符: %c, unicode码点或者byte对应的数值: %d, 转换后的整数: %d\n", ch, ch, num)  
}
```

在上面的示例代码中，我们将字符 '0' 赋值给变量 ch，然后通过 ch - '0' 的操作将其转换为整数并赋值给变量 num。输出结果如下：

```go
字符: 0, unicode码点或者byte对应的数值: 48, 转换后的整数: 0
```

可以看到，字符 '0' 成功转换为整数 0。
其中需要注意的是：在Go语言中，格式化输出时 `%c` 是一个占位符，用于表示要输出的值是一个Unicode字符。
具体来说，`%c` 会将相应参数作为一个Unicode码点（或称为rune类型）来解释，并将其格式化为相应的字符表示。这允许你将一个整数值或字符类型的变量作为参数，并将其打印为对应的字符。例如上边就是直接打印编码后的字符0,而不是byte/rune 对应的值 48

这种转换方式可以用于将字符 '0' 到 '9' 范围内的数字字符转换为对应的整数值。

# 总结
byte/rune 转对应unicode 码点的话，直接使用int() 进行强转；
如果是要转成0-9 对应的整数，则需要使用 int(byte('XX') - '0' )进行转换 。