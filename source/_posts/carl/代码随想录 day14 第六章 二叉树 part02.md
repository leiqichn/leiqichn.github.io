---
title: 代码随想录 day14 第六章 二叉树 part02
date: 2024-11-12 23:48:36
modificationDate: 2024 November 12th Tuesday 23:48:36
categories: 
	- carl
tags: []
sticky: []
hide: true
category_bar: true
---

# 第六章 二叉树 part02

### 226.翻转二叉树 （优先掌握递归）

这道题目 一些做过的同学 理解的也不够深入，建议大家先看我的视频讲解，无论做过没做过，都会有很大收获。

题目链接/文章讲解/视频讲解：[https://programmercarl.com/0226.%E7%BF%BB%E8%BD%AC%E4%BA%8C%E5%8F%89%E6%A0%91.html](https://programmercarl.com/0226.%E7%BF%BB%E8%BD%AC%E4%BA%8C%E5%8F%89%E6%A0%91.html)

思路： 使用递归。分治，递归只要想好边界条件和需要重复执行的最小单元操作即可。
```go

func invertTree(root *TreeNode) *TreeNode {
    if root == nil {
        return nil
    }
    root.Left, root.Right = root.Right, root.Left    //交换
    
    invertTree(root.Left)
    invertTree(root.Right)

    return root
}

```

### 101. 对称二叉树 （优先掌握递归）

先看视频讲解，会更容易一些。

题目链接/文章讲解/视频讲解：[https://programmercarl.com/0101.%E5%AF%B9%E7%A7%B0%E4%BA%8C%E5%8F%89%E6%A0%91.html](https://programmercarl.com/0101.%E5%AF%B9%E7%A7%B0%E4%BA%8C%E5%8F%89%E6%A0%91.html)

思路： 使用递归的方式。在二叉树的外边对比，在二叉树的里边对比。
```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSymmetric(root *TreeNode) bool {
    return check(root, root)
}

func check(p, q *TreeNode) bool {
    // 边界场景判断，都为nil的时候为true
    if p == nil && q == nil {
        return true
    }
    // 其中有一个为nil, 另一个不为nil, 返回false
    if p == nil || q == nil {
        return false
    }
    // 考虑值不相等，为false
    if p.Val != q.Val {
        return false
    }
    // 判断外部的节点是否对称
    out := check(p.Left, q.Right)
    // 判断内部的边界是否对称
    in := check(p.Right, q.Left)
    isSame := out && in
    return isSame
}

```


### 104.二叉树的最大深度 （优先掌握递归）

什么是深度，什么是高度，如何求深度，如何求高度，这里有关系到二叉树的遍历方式。

大家 要先看视频讲解，就知道以上我说的内容了，很多录友刷过这道题，但理解的还不够。

题目链接/文章讲解/视频讲解： [https://programmercarl.com/0104.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E5%A4%A7%E6%B7%B1%E5%BA%A6.html](https://programmercarl.com/0104.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E5%A4%A7%E6%B7%B1%E5%BA%A6.html)

思路：可以层序遍历或者使用递归到叶子节点上。

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


// 遍历1 直接使用queue
func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	queue := []*TreeNode{}

	queue = append(queue, root)
	deeps := 0
	for len(queue) > 0 {
		size := len(queue)

		for i := 0; i < size; i++ {
            top := queue[0]
            queue = queue[1:]
            
			if top.Left != nil {
				queue = append(queue, top.Left)

			}
			if top.Right != nil {
				queue = append(queue, top.Right)
			}
		}

        deeps++
	}
	return deeps
}

// 遍历2 使用中间slice
func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	queue := []*TreeNode{}

	queue = append(queue, root)
	deeps := 0
	for len(queue) > 0 {
		size := len(queue)
		nextLevel := []*TreeNode{}

		for i := 0; i < size; i++ {
            top := queue[0]
            queue = queue[1:]
            
			if top.Left != nil {
                nextLevel = append(nextLevel, top.Left)
			}
			if top.Right != nil {
                nextLevel = append(nextLevel, top.Right)
			}
		}
        queue = nextLevel
        deeps++
	}
	return deeps
}

```


### 111.二叉树的最小深度 （优先掌握递归）

先看视频讲解，和最大深度 看似差不多，其实 差距还挺大，有坑。

题目链接/文章讲解/视频讲解：[https://programmercarl.com/0111.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E5%B0%8F%E6%B7%B1%E5%BA%A6.html](https://programmercarl.com/0111.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E5%B0%8F%E6%B7%B1%E5%BA%A6.html)


递归三步曲：
1. 确定递归函数的参数和返回值
2. 确定终止条件
3. 确定单层递归的逻辑

```go


func minDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	queue := []*TreeNode{}

	queue = append(queue, root)
	deeps := 0
	for len(queue) > 0 {
		size := len(queue)

		for i := 0; i < size; i++ {
            top := queue[0]
			if top.Left != nil {
				queue = append(queue, top.Left)

			}
			if top.Right != nil {
				queue = append(queue, top.Right)
			}
            if top.Left == nil && top.Right == nil {
                return deeps + 1
            }
            queue = queue[1:]
		}

        deeps++
	}
	return deeps
}


```
