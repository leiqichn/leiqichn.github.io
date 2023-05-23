

---
title: leetcode 226. 翻转二叉树
date: 2023-05-23 23:06:25
modificationDate: 2023 五月 23日 星期二 23:06:25
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---
[226. 翻转二叉树 - 力扣（Leetcode）](https://leetcode.cn/problems/invert-binary-tree/description/)
![](../../imgs/Pasted%20image%2020230523230644.png)


```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 // 定义将二叉树翻转
func invertTree(root *TreeNode) *TreeNode {
    // 递归终止条件
    if root == nil {
        return nil
    }
    // 单个任务逻辑 交换root 下的两个节点，然后在严格按照定义递归调用左右节点
    root.Right,root.Left = root.Left,root.Right 
    // 将右子树翻转
    invertTree(root.Right)
    // 将左子树翻转
    invertTree(root.Left)
    return root
}

```
