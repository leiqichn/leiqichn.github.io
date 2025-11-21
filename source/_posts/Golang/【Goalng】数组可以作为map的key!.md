---
title: 【Goalng】数组可以作为map的key!
date: 2025-11-21 23:08:24
modificationDate: 2025 十一月 21日 星期五 23:08:24
categories: 
	- Golang
tags: []
sticky: []
published: true
category_bar: true
---

在Go语言中，**数组可以作为map的key**，这是Go语言的一个特性。

## 数组作为map key的特性

### 1. 数组是值类型，不是指针
```go
a := [3]int{1, 2, 3}
b := a  // 这里是值拷贝，不是引用
b[0] = 9
fmt.Println(a) // [1 2 3] - 原数组不变
fmt.Println(b) // [9 2 3]
```

### 2. 数组是可比较的（comparable）
Go语言中，数组支持 `==` 和 `!=` 操作符：
```go
a := [3]int{1, 2, 3}
b := [3]int{1, 2, 3}
c := [3]int{1, 2, 4}

fmt.Println(a == b) // true
fmt.Println(a == c) // false
```

### 3. 因此数组可以作为map key
```go
// 这是合法的
cnt := map[[3]int]int{}
key := [3]int{1, 2, 3}
cnt[key] = 1
```

## 与切片的对比

**切片不能作为map key**：
```go
// 这会编译错误
// cnt := map[[]int]int{} 

// 错误：invalid map key type []int
```

因为切片是引用类型，比较的是地址而不是内容。

## 在[2352. 相等行列对](https://leetcode.cn/problems/equal-row-and-column-pairs/)题目代码中的应用

```go
cnt := map[[200]int]int{}

// 统计行
for _, row := range grid {
    a := [200]int{}
    for j, v := range row {
        a[j] = v  // 复制值到数组
    }
    cnt[a]++  // 使用数组作为key
}

// 检查列
for j := range grid[0] {
    a := [200]int{}
    for i, row := range grid {
        a[i] = row[j]  // 复制列值到数组
    }
    ans += cnt[a]  // 查找匹配的行
}
```

## 为什么这样设计？

1. **值语义**：数组比较的是内容，不是地址
2. **确定性**：相同的数组内容总是产生相同的key
3. **性能**：数组长度固定，哈希计算更高效

## 注意事项

- 数组长度是类型的一部分，`[3]int` 和 `[4]int` 是不同的类型
- 大数组作为key可能会有性能开销（拷贝成本）
- 在这个题目中，由于n ≤ 200，使用固定长度数组是可行的

这种设计使得我们可以用数组的内容作为唯一标识，从而高效地统计和查找匹配的行列对。