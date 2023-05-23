
---
title: leetcode 144. 二叉树的前序遍历
date: 2023-05-23 22:49:08
modificationDate: 2023 五月 23日 星期二 22:49:08
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---
[144. 二叉树的前序遍历 - 力扣（Leetcode）](https://leetcode.cn/problems/binary-tree-preorder-traversal/description/)


![](../../imgs/Pasted%20image%2020230523224940.png)

记得提前判断是否为空，否则会报找不到内存指针的错误
![](../../imgs/Pasted%20image%2020230523225147.png)

注意：这里和层序遍历不一样，这里不用使用中间变量lens := stack.len() 来遍历每层，虽然增加了每层遍历依然可以通过，但是没有必要。只有在层序遍历的时候才需要记录每层的信息。[leetcode 102. 二叉树的层序遍历](leetcode%20102.%20二叉树的层序遍历.md)
```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func preorderTraversal(root *TreeNode) []int {
	stack := list.New()
	res :=  []int{}
	
	if root == nil{//防止为空
			return res
	}
	stack.PushBack(root)
	for stack.Len() > 0 {
		top := stack.Remove(stack.Back()).(*TreeNode)
		res = append(res,top.Val)
		if top.Right !=nil {
			stack.PushBack(top.Right)
		}
		if top.Left !=nil {
			stack.PushBack(top.Left)
		}
	}
	return  res 
}
```
