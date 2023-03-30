---
title: Leetcode 257.二叉树的所有路径
date: 2023-03-28 23:47:29
modificationDate: 2023 三月 29日 星期三 22:46:12
categories: 
	- leetcode
tags: []
sticky: []
hide: false
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

var res []string
var path []string

func binaryTreePaths(root *TreeNode) []string {
    res = make([]string,0)
    path = make([]string,0)
    if (root == nil) {
        return res
    }
	backTracking(root)
	return res
}
func backTracking(root *TreeNode){
	// 终点 左右子节点都为nil
	if isLeafNode(root) {
        NodeValStr := strconv.Itoa(root.Val)
	    path = append(path, NodeValStr)
		pathStr := strings.Join(path, "->")
		res = append(res, pathStr)
		return
	}
	// 前序遍历 中左右
	// 遍历 每次递归的操作
	NodeVal:= strconv.Itoa(root.Val)// 中
	path = append(path, NodeVal)
	if root.Left != nil { // 左
		backTracking(root.Left)
        path = path[:len(path)-1]
	}
	if root.Right != nil { // 右
		backTracking(root.Right)
        path = path[:len(path)-1]
	}
}

func isLeafNode(node *TreeNode) bool{
	if node.Right==nil && node.Left== nil && node!= nil{
		return true
	}
	return false
}
```
