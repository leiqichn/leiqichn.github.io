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
