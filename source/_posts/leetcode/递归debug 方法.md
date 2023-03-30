
---
title: 递归debug 方法
date: 2023-03-30 00:38:35
modificationDate: 2023 三月 30日 星期四 00:38:39
categories: 
	- leetcode
tags: []
sticky: []
hide: true
category_bar: true
---

使用tab 
参考
[递归函数的Debug技巧 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/369464796)
[分享一个小技巧，提高刷题幸福感 (qq.com)](https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247490945&idx=1&sn=03da23d366ad4577d2a22328f3ba04f9)
![](../../imgs/a96e8e7a2780c45a863303b03c2a068.jpg)


![](../../imgs/3f0c31123f22ff3aa51312dc4d9a726.jpg)


![](../../imgs/b4ef89bfab7f211d72486980e53d7b0.jpg)

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
import "fmt"
var count int = 0
func printIndent(n int) {
    for i:=0;i <n; i++ {
        fmt.Print("|    ")
    }
}


func sumOfLeftLeaves(root *TreeNode) int {
	// 递归的输入和返回值是对的了

	res := 0
    count++
    printIndent(count)
    fmt.Println("res:",res)
	// 终止条件
	if root == nil {
        count--
        printIndent(count)
        fmt.Println("return:",0)
		return 0
	}
    leftNodeVal := 0 
    rightNodeVal := 0
	leftNode := root.Left
    rightNode := root.Right
	if leftNode != nil && leftNode.Left == nil && leftNode.Right == nil {
		leftNodeVal = leftNode.Val
	}
    if rightNode !=nil && rightNode.Left != nil {
        rightNodeVal = sumOfLeftLeaves(rightNode.Left)
    } 
	// 单次循环
    res  = leftNodeVal +  rightNodeVal
    count--
    printIndent(count)
    fmt.Println("return:",res)
	return res 
}

```

添加以下部分是可以缩进 递归debug 的。
```go
import "fmt"
var count int = 0
func printIndent(n int) {
    for i:=0;i <n; i++ {
        fmt.Print("|    ")
    }
}

```