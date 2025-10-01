
---
title: 【Golang】 switch使用
date: 2025-06-16 23:23:08
modificationDate: 2025 六月 16日 星期一 23:23:21
categories: 
	- Golang
tags: []
sticky: []
published: true
category_bar: true
---

在 Go 语言中，`switch` 语句提供了灵活的条件分支控制，相比其他语言有更多特性。以下是详细用法和示例：

---

### 1. **基础值匹配**
```go
day := 3
switch day {
case 1:
    fmt.Println("Monday")
case 2:
    fmt.Println("Tuesday")
case 3:
    fmt.Println("Wednesday") // 输出
case 4:
    fmt.Println("Thursday")
default:
    fmt.Println("Weekend")
}
```

---

### 2. **多值匹配（逗号分隔）**
```go
char := 'a'
switch char {
case 'a', 'e', 'i', 'o', 'u':
    fmt.Println("Vowel") // 输出
case 'y':
    fmt.Println("Sometimes vowel")
default:
    fmt.Println("Consonant")
}
```

---

### 3. **无表达式（替代 if-else）**
```go
score := 85
switch {
case score >= 90:
    fmt.Println("A")
case score >= 80: // 满足条件
    fmt.Println("B") // 输出
case score >= 70:
    fmt.Println("C")
default:
    fmt.Println("D")
}
```

---

### 4. **类型判断（Type Switch）**
```go
var data interface{} = "hello"
switch v := data.(type) {
case int:
    fmt.Println("Integer:", v)
case string:
    fmt.Println("String:", v) // 输出: String: hello
default:
    fmt.Println("Unknown type")
}
```

---

### 5. **穿透执行（fallthrough）**
```go
n := 2
switch n {
case 1:
    fmt.Println("One")
case 2:
    fmt.Println("Two") // 输出
    fallthrough        // 强制执行下一个 case
case 3:
    fmt.Println("Three") // 输出
}
// 输出: Two\nThree
```

---

### 6. **初始化语句**
```go
switch lang := "Go"; lang {
case "Java":
    fmt.Println("Enterprise")
case "Go":
    fmt.Println("Efficient") // 输出
default:
    fmt.Println("Other")
}
```

---

### 关键特性总结：
| 特性             | 说明                                                                 |
|------------------|----------------------------------------------------------------------|
| **自动终止**     | 无需 `break`，执行完 case 后自动退出 switch                          |
| **多值匹配**     | 用逗号分隔多个值（如 `case 1, 2, 3`）                               |
| **无表达式模式** | 类似 `if-else` 链，更简洁的条件分支                                 |
| **类型判断**     | 通过 `data.(type)` 检测接口值的实际类型                              |
| **fallthrough**  | 显式声明继续执行下一个 case（**不判断条件**）                        |
| **作用域隔离**   | 支持在 `switch` 后初始化局部变量（如 `switch x := 10; { ... }`）     |

---

### 示例：
```go
switch hour := time.Now().Hour(); {
case hour < 12:
    fmt.Println("Morning")
case hour < 18:
    fmt.Println("Afternoon")
default:
    fmt.Println("Night")
}
```

> Go 的 `switch` 设计强调简洁和安全，避免 C/C++ 中因忘记 `break` 导致的错误。根据场景选择合适用法可大幅提升代码可读性。