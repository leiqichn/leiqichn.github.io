---
title: 【Golang】sort.Search二分包
date: 2025-06-18 00:26:45
modificationDate: 2025 六月 18日 星期三 00:26:45
categories: 
	- leetcode
tags: []
sticky: []
published: true
category_bar: true
---

# Golang 中二分查找包的使用方法

Go 标准库中的 `sort` 包提供了二分查找的功能，主要通过 `sort.Search` 函数实现。下面详细介绍如何使用这个功能。


### 二分法通用模板


```go

func binarySearch(nums []int, target int) int {
    left, right := 0, len(nums)-1 // 初始化边界
    
    for left <= right { // 终止条件
        mid := left + (right-left)/2 // 防止溢出
        
        if nums[mid] == target {
            return mid // 找到目标
        } else if nums[mid] < target {
            left = mid + 1 // 调整左边界
        } else {
            right = mid - 1 // 调整右边界
        }
    }
    
    return -1 // 未找到
}

// 寻找左边界变体
func findLeftBound(nums []int, target int) int {
    left, right := 0, len(nums)-1
    res := -1
    
    for left <= right {
        mid := left + (right-left)/2
        if nums[mid] >= target {
            right = mid - 1
        } else {
            left = mid + 1
        }
        
        if nums[mid] == target {
            res = mid
        }
    }
    
    return res
}

// 寻找右边界变体
func findRightBound(nums []int, target int) int {
    left, right := 0, len(nums)-1
    res := -1
    
    for left <= right {
        mid := left + (right-left)/2
        if nums[mid] <= target {
            left = mid + 1
        } else {
            right = mid - 1
        }
        
        if nums[mid] == target {
            res = mid
        }
    }
    
    return res
}

```

## 1. `sort.Search` 基本用法

`sort.Search` 函数的签名如下：

```go
func Search(n int, f func(int) bool) int
```

它会在 `[0, n)` 范围内查找满足 `f(i)` 为 `true` 的最小索引 `i`。如果不存在这样的索引，则返回 `n`。

### 基本示例：在有序切片中查找元素

```go
package main

import (
	"fmt"
	"sort"
)

func main() {
	nums := []int{1, 3, 5, 7, 9}
	target := 5

	// 查找目标值的索引
	index := sort.Search(len(nums), func(i int) bool {
		return nums[i] >= target
	})

	if index < len(nums) && nums[index] == target {
		fmt.Printf("找到 %d，索引为 %d\n", target, index)
	} else {
		fmt.Printf("未找到 %d\n", target)
	}
}
```

## 2. 查找特定条件的元素

`sort.Search` 的强大之处在于可以查找满足任意条件的第一个元素。

### 示例：查找第一个大于等于目标值的元素

```go
nums := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
target := 5

index := sort.Search(len(nums), func(i int) bool {
    return nums[i] >= target
})

fmt.Printf("第一个大于等于 %d 的元素是 %d，索引为 %d\n", target, nums[index], index)
```

### 示例：查找第一个满足条件的偶数

```go
nums := []int{1, 3, 5, 6, 7, 9, 10, 11}

index := sort.Search(len(nums), func(i int) bool {
    return nums[i]%2 == 0
})

if index < len(nums) {
    fmt.Printf("第一个偶数是 %d，索引为 %d\n", nums[index], index)
} else {
    fmt.Println("没有找到偶数")
}
```

## 3. 自定义类型的二分查找

对于自定义类型，需要先实现 `sort.Interface` 接口，然后才能使用 `sort.Search`。

### 示例：自定义结构体切片查找

```go
type Person struct {
    Name string
    Age  int
}

type ByAge []Person

func (a ByAge) Len() int           { return len(a) }
func (a ByAge) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a ByAge) Less(i, j int) bool { return a[i].Age < a[j].Age }

func main() {
    people := ByAge{
        {"Alice", 25},
        {"Bob", 30},
        {"Charlie", 35},
        {"Dave", 40},
    }

    // 必须先排序
    sort.Sort(people)

    // 查找年龄大于等于 33 的第一个人
    targetAge := 33
    index := sort.Search(len(people), func(i int) bool {
        return people[i].Age >= targetAge
    })

    if index < len(people) {
        fmt.Printf("找到 %+v，索引为 %d\n", people[index], index)
    } else {
        fmt.Println("没有找到满足条件的人")
    }
}
```

## 4. 查找浮点数近似值

`sort.Search` 也可以用于浮点数近似查找。

### 示例：查找平方根近似值

```go
func sqrt(x float64) float64 {
    // 设置精度
    precision := 1e-6
    low, high := 0.0, x
    
    // 使用二分查找逼近平方根
    for high-low > precision {
        mid := (low + high) / 2
        if mid*mid < x {
            low = mid
        } else {
            high = mid
        }
    }
    
    return (low + high) / 2
}

func main() {
    fmt.Println("√2 ≈", sqrt(2))
}
```

## 5. 查找切片中的插入位置

`sort.Search` 非常适合用来查找元素应该插入的位置。

### 示例：查找插入位置

```go
nums := []int{1, 3, 5, 7, 9}
target := 6

index := sort.Search(len(nums), func(i int) bool {
    return nums[i] >= target
})

fmt.Printf("%d 应该插入到索引 %d 的位置\n", target, index)
// 输出: 6 应该插入到索引 3 的位置
```

## 6. 标准库中的其他相关函数

除了 `sort.Search`，标准库还提供了：

- `sort.SearchInts(a []int, x int) int` - 在已排序的 int 切片中查找 x
- `sort.SearchFloat64s(a []float64, x float64) int` - 在已排序的 float64 切片中查找 x
- `sort.SearchStrings(a []string, x string) int` - 在已排序的 string 切片中查找 x

### 示例：使用 `sort.SearchInts`

```go
nums := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
target := 5

index := sort.SearchInts(nums, target)

if index < len(nums) && nums[index] == target {
    fmt.Printf("找到 %d，索引为 %d\n", target, index)
} else {
    fmt.Printf("未找到 %d\n", target)
}
```

## 7. 性能考虑

`sort.Search` 的时间复杂度是 O(log n)，因为它使用的是二分查找算法。但需要注意：

1. 切片必须是已排序的，否则结果不可靠
2. 比较函数 `f` 应该尽可能简单高效
3. 对于非常大的数据集，考虑内存局部性和缓存效应

## 8. 实际应用示例

### 示例：实现类似 C++ 的 lower_bound 和 upper_bound

```go
// lowerBound 返回第一个 >= target 的元素的索引
func lowerBound(nums []int, target int) int {
    return sort.Search(len(nums), func(i int) bool {
        return nums[i] >= target
    })
}

// upperBound 返回第一个 > target 的元素的索引
func upperBound(nums []int, target int) int {
    return sort.Search(len(nums), func(i int) bool {
        return nums[i] > target
    })
}

func main() {
    nums := []int{1, 2, 2, 2, 3, 4, 5}
    target := 2
    
    lb := lowerBound(nums, target)
    ub := upperBound(nums, target)
    
    fmt.Printf("lowerBound: %d, upperBound: %d\n", lb, ub)
    fmt.Printf("元素 %d 的出现次数: %d\n", target, ub-lb)
}
```

