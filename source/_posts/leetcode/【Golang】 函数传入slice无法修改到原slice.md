---
title: 【Golang】 函数传入slice无法修改到原slice
date: 2025-06-15 13:53:49
modificationDate: 2025 六月 15日 星期日 13:53:49
categories: 
	- leetcode
tags: []
sticky: []
published: true
category_bar: true
---

[46. 全排列 - 力扣（LeetCode）](https://leetcode.cn/problems/permutations/description/)

```go

func permute(nums []int) [][]int {
    res := [][]int{}
    track := []int{}
    used := make([]bool, len(nums))
    
    backtrack(nums, track, used, &res)
    return res
}

// 回溯函数
func backtrack(nums []int, track []int, used []bool, res *[][]int) {
    // 触发结束条件
    if len(track) == len(nums) {
        // 因为 track 是全局变量，因此需要新建一个数组来存储一份全排列
        temp := make([]int, len(track))
        copy(temp, track)
        *res = append(*res, temp)
        return
    }
    
    for i := range nums {
        // 排除不合法的选择
        if used[i] {
            // 剪枝，避免重复使用同一个数字
            continue
        }
        // 做选择
        track = append(track, nums[i])
        used[i] = true
        // 进入下一层决策树
        backtrack(nums, track, used, res)
        // 取消选择
        track = track[:len(track)-1]
        used[i] = false
    }
}

```

上边的res 代码slice中需要使用指针 我去掉指针不行。

使用闭包函数可以。


```go
func permute(nums []int) [][]int {
    res := [][]int{}
    track := []int{}
    used := make([]bool, len(nums))
    var backtrack func()
    backtrack = func() {
    // 触发结束条件
    if len(track) == len(nums) {
        // 因为 track 是全局变量，因此需要新建一个数组来存储一份全排列
        temp := make([]int, len(track))
        copy(temp, track)
        res = append(res, temp)
        return
    }
    
    for i := range nums {
        // 排除不合法的选择
        if used[i] {
            // 剪枝，避免重复使用同一个数字
            continue
        }
        // 做选择
        track = append(track, nums[i])
        used[i] = true
        // 进入下一层决策树
        backtrack()
        // 取消选择
        track = track[:len(track)-1]
        used[i] = false
    }
}

    backtrack()
    return res
}

// 回溯函数

```

# 切片与指针的区别

Go 中的切片是引用类型，但它们与指针在行为上还是有一些关键区别，这正是为什么在这个回溯算法中需要使用指针的原因。

## 切片作为引用类型的局限

虽然切片是引用类型（底层数组的指针+长度+容量），但切片头（slice header）本身是按值传递的。这意味着：

1. **可以修改底层数组元素**：函数内部可以修改切片指向的数组元素，这些修改会反映到外部
2. **不能修改切片头**：<font color="#ff0000">对切片本身的修改（如追加元素导致重新分配）不会反映到外部</font>

## 具体到代码

回溯算法中：

```go
*res = append(*res, temp)  // 使用指针可以修改外部的res
```

如果改为不使用指针：

```go
res = append(res, temp)  // 这只修改了函数内部的切片头副本
```

## 为什么需要指针的详细解释

1. **追加操作的特殊性**：
   - `append` 可能会返回一个新的切片头（当容量不足时）
   - 不使用指针时，新切片头只存在于函数内部

2. **递归调用的累积效果**：
   - 每次递归调用都需要累积结果
   - 不使用指针时，每次递归的修改都会丢失

## 验证示例

简单例子验证：

```go
func modifySlice(s []int) {
    s = append(s, 100) // 不会影响外部
    s[0] = 99          // 会影响外部（修改底层数组）
}

func modifySliceByPtr(s *[]int) {
    *s = append(*s, 100) // 会影响外部
}

func main() {
    a := []int{1, 2, 3}
    modifySlice(a)
    fmt.Println(a) // 输出: [99 2 3]
    
    modifySliceByPtr(&a)
    fmt.Println(a) // 输出: [99 2 3 100]
}
```

## 结论

在需要修改切片本身<font color="#ff0000">（如追加元素）</font>并且希望这些修改在函数外部可见时，必须使用指针。这正是你的回溯算法中需要使用 `*[][]int` 的原因。