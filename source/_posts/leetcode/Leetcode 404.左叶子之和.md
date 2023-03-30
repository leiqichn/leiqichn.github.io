---
title: Leetcode 404.左叶子之和
date: 2023-03-29 22:44:37
modificationDate: 2023 三月 29日 星期三 22:45:05
categories: 
	- leetcode
tags: []
sticky: []
hide: true
category_bar: true
---

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func sumOfLeftLeaves(root *TreeNode) int {
	// 递归
	res := 0
	// 终止条件
	if root == nil {
		return 0
	}
    leftNode := root.Left
	leftNodeVal := sumOfLeftLeaves(root.Left) // 左
    rightNodeVal := sumOfLeftLeaves(root.Right)// 右
	if leftNode != nil && leftNode.Left == nil && leftNode.Right == nil { // 中
		leftNodeVal = leftNode.Val
	}
	// 单次循环
    res = leftNodeVal + rightNodeVal // 中，左边+右边
	return res 
}

```
