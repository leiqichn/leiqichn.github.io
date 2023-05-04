---
title: leetcode 108.将有序数组转换为二叉搜索树
date: 2023-05-04 23:23:48
modificationDate: 2023 五月 4日 星期四 23:23:48
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---

[108. 将有序数组转换为二叉搜索树 - 力扣（Leetcode）](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/description/)

![](../../imgs/Pasted%20image%2020230504232459.png)
### 递归解法
注意递归函数的返回值和输入值，确定终止条件，确定单层递归逻辑
注意递归函数定义，严格按照定义调用递归
使用前序遍历 中左右
```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sortedArrayToBST(nums []int) *TreeNode {
    return traversal(nums,0,len(nums)-1)
}

// 定义：返回nums root 节点
func traversal(nums []int,left int , right int) *TreeNode{
    if left > right {
        return nil
    }
    mid := (left + right)/2
    root := &TreeNode{nums[mid],nil,nil}
    root.Left =  traversal(nums,left,mid-1) // 把后边 root 节点添加到当前root left 左节点上
    root.Right = traversal(nums,mid+1,right) // 把后边 root 节点添加到当前root right 左节点上
    return root
}

```
