---
title: leetcode 104.二叉树的深度
date: 2023-05-30 23:33:48
modificationDate: 2023 五月 30日 星期二 23:33:48
categories: 
	- leetcode
tags: [DFS,BFS,层序遍历]
sticky: []
hide: false
category_bar: true
---
个人网站：https://leiqicn.gitee.io/categories/leetcode/
[104. 二叉树的最大深度 - 力扣（Leetcode）](https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/)
![](../../imgs/Pasted%20image%2020230531000419.png)

二叉树节点的深度指的是该节点到根节点的距离，也就是从根节点到该节点的路径长度。而二叉树节点的高度指的是该节点到其子树中最远叶子节点的距离，也就是该节点为根的子树的高度。

所以，可以将整个二叉树的高度定义为根节点的高度，也就是从根节点到最远叶子节点的距离。而整个二叉树的深度则没有固定的定义，通常是指二叉树中节点深度的最大值。
## 递归

```go
func max (a, b int) int {
    if a > b {
        return a;
    }
    return b;
}
// 递归
func maxdepth(root *treenode) int {
    if root == nil {
        return 0;
    }
    return max(maxdepth(root.left), maxdepth(root.right)) + 1;
}


```


## 迭代法
可以使用模板层序遍历

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
import "container/list"

func maxDepth(root *TreeNode) int {
	depth := 0
	if root == nil {
		return 0
	}
	queue := list.New()
	queue.PushBack(root)

	for queue.Len() > 0 {
		size := queue.Len()
		for i := 0; i < size; i++ {
			// 切掉第一个元素
			first := queue.Remove(queue.Front()).(*TreeNode) //注意层序遍历是切掉前边一个
			if first.Left != nil {
				queue.PushBack(first.Left)
			}
			if first.Right != nil {
				queue.PushBack(first.Right)
			}
		}
		depth++
	}
	return depth
}
```

## 切片实现

```go
// 定义：输入根节点，返回这棵二叉树的最大深度
func maxDepth(root *TreeNode) int {
	depth := 0;
	
    if root == nil {
        return 0
    }
	queue := []*TreeNode{}
	
	queue = append(queue,root)
	for len(queue) > 0 { // queue 不为空的时候
		size := len(queue)
		for i:=0;i <size ;i++ {// 遍历一层
			top := queue[0]
			queue = queue[1:] // 取最上层元素，并切掉该元素
			if top.Right != nil {
				queue = append(queue,top.Right)
			}
			if top.Left != nil {
				queue = append(queue,top.Left)
			}
			
		}
        depth++
	}
	return depth
}

```

## 使用一个临时切片来存储当前层所有节点的子节点

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}

	// 使用切片实现队列
	var queue []*TreeNode
	queue = append(queue, root)
	depth := 0

	for len(queue) > 0 {


		// 当前层的节点数量
		size := len(queue)

		// 使用一个临时切片来存储当前层所有节点的子节点
		var nextLevel []*TreeNode

		for i := 0; i < size; i++ {
			// 从队列头部移除节点
			node := queue[0]
			queue = queue[1:] // 移除队列的第一个元素

			// 将左子树和右子树添加到下一层的队列
			if node.Left != nil {
				nextLevel = append(nextLevel, node.Left)
			}
			if node.Right != nil {
				nextLevel = append(nextLevel, node.Right)
			}
		}

		// 将下一层的节点赋值给当前层的队列
		queue = nextLevel
		// 每次循环处理一层的节点
		depth++
	}

	return depth
}

```

