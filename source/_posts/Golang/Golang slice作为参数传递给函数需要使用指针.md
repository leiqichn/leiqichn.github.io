---
title: Golang slice作为参数传递给函数需要使用指针
date: 2024-04-12 00:35:04
modificationDate: 2024 四月 12日 星期五 00:35:52
categories: 
	- Golang
tags: []
sticky: []
hide: false
category_bar: true
---

```go
func combine(n int, k int) [][]int {
    res := [][]int{}
    dfs(1,n,k,&res,&[]int{})
    return res
}

func dfs(s, n, k int, res *[][]int, item *[]int) {
    if len(*item) == k {
        *res = append(*res, append([]int{}, *item...))
        return
    }
    for i := s; i <= n-(k-len(*item))+1; i++{
        *item = append(*item, i)
        dfs(i+1, n, k, res, item)
        *item = (*item)[:len(*item)-1]
    }
} 

```


在 Go 语言中，虽然 slice 是引用类型，但是当它作为参数传递给函数时，传递的实际上是 slice 的引用副本，而不是指向底层数组的指针。这意味着函数接收到的是一个指向原始 slice 的指针的副本。对于 slice 的修改操作，如果是改变 slice 内部的元素，那么在函数内外都是同步的，因为它们指向同一个底层数组。 然而，如果操作涉及到改变 slice 的长度或者容量，比如通过 append 函数或者直接索引赋值的方式，那么在函数内部对 slice 进行这样的操作不会影响到原始 slice，因为这些操作会创建一个新的底层数组来存储新的 slice 元素，而原始 slice 仍然指向原来的底层数组。

这就是为什么在需要修改 slice 的长度或容量的情况下，我们需要传递指向 slice 的指针（即指针的指针），因为只有这样，函数内部对 slice 的修改才能反映到原始 slice 上。

例如，在 `combine` 函数中，如果想要 `dfs` 函数能够修改 `res` slice 的长度（即添加新的组合到 `res` 中），那么需要传递 `res` 的指针的指针。这样，当 `dfs` 函数执行 `*res = append(*res, newCombination...)` 时，它会修改原始的 `res` slice 而不是它的副本。

传递指针的原因是为了：

1. **避免不必要的副本创建**：传递指针可以避免在每次函数调用时创建 slice 的副本，从而减少内存的使用和垃圾回收的压力。
    
2. **确保函数内部的修改能够反映到原始数据上**：当需要在函数内部修改 slice 的长度或容量时，传递指针是必要的，因为只有通过指针，函数才能访问并修改原始 slice 的底层数组。
    
3. **提高代码的效率和性能**：使用指针可以提高代码的执行效率，尤其是在处理大量数据或者递归算法时，可以显著减少内存分配和复制操作，从而提高程序的整体性能。


还可以转化为全局变量；需要注意的是
go 中引用类型（如切片、map、channel等会自动初始化为nil, 需要手动初始化
```go
var res [][]int // go 中引用类型（如切片、map、channel等会自动初始化为nil, 需要手动初始化
var path []int

func combine(n int, k int) [][]int {

    res = make([][]int, 0) // 需要进行初始化
    path = make([]int, 0)
	// 结束条件
	var backtracking func(n, k ,startIdx int)
	backtracking = func(n, k ,startIdx int) {
        // 提前返回需要return
		if len(path) == k {
            pathTmp := make([]int,len(path))
			copy(pathTmp, path)
			res = append(res, pathTmp)
            return
		}

		for i := startIdx;i<= n ;i++ {
			path = append(path,i)
			backtracking(n,k,i+1)
			path = path[:(len(path) -1)]
		}
	}
	backtracking(n,k,1)
	return res
}
```


tempPath := make([]int, k) // **tempPath := []int{}**,copy(tempPath, path) 将会失败，因为 copy 函数需要目标切片有足够的容量来接收源切片的元素。
copy(tempPath, path)
```go
var res [][]int // go 中引用类型（如切片、map、channel等会自动初始化为nil, 需要手动初始化
var path []int

func combine(n int, k int) [][]int {

    res = make([][]int, 0)
    path = make([]int, 0)
	// 结束条件
	var backtracking func(n int, k int, startIndex int)
    backtracking = func(n int, k int, startIndex int) {
        if len(path) == k {
            tempPath := make([]int, k) // tempPath := []int{},copy(tempPath, path) 将会失败，因为 copy 函数需要目标切片有足够的容量来接收源切片的元素。
            copy(tempPath, path)
            res = append(res, tempPath)
        }

        for i:= startIndex; i <= n; i++ {
            if (n -i +1 ) < (k -len(path)) {
                return
            }

            path = append(path, i)
            backtracking(n, k, i+1)
            path = path[:len(path)-1]
        }
    }

	backtracking(n,k,1)
	return res
}
```
