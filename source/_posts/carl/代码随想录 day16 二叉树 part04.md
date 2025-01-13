---
title: 代码随想录 day16
date: 2024-11-15 00:52:00
modificationDate: 2024 November 15th Friday 00:52:00
categories: 
	- carl
tags: []
sticky: []
hide: false
category_bar: true
---


# 第六章 二叉树 part04

### 找树左下角的值

本题递归偏难，反而迭代简单属于模板题， 两种方法掌握一下

题目链接/文章讲解/视频讲解：[https://programmercarl.com/0513.%E6%89%BE%E6%A0%91%E5%B7%A6%E4%B8%8B%E8%A7%92%E7%9A%84%E5%80%BC.html](https://programmercarl.com/0513.%E6%89%BE%E6%A0%91%E5%B7%A6%E4%B8%8B%E8%A7%92%E7%9A%84%E5%80%BC.html)

TODO： 迭代法

迭代法，找到记录最后一层中i = 0 的value 即可。

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func findBottomLeftValue(root *TreeNode) int {

    if root == nil {
        return 0
    }
    var result int
    queue := make([]*TreeNode, 0)

    queue = append(queue, root)

    for len(queue) > 0 {
        size := len(queue)
        for i := 0; i< size; i++ {
            top := queue[0] // 取最顶上的元素
            queue = queue[1:]
            if i == 0 {
                result = top.Val
            }
            if top.Left != nil {
                queue = append(queue, top.Left)
            }

            if top.Right != nil {
                queue = append(queue, top.Right)
            }
        }
    }
    return result
}


```

### 路径总和           

本题 又一次涉及到回溯的过程，而且回溯的过程隐藏的还挺深，建议先看视频来理解

112. 路径总和，和 113. 路径总和ii 一起做了。 优先掌握递归法。

题目链接/文章讲解/视频讲解：[https://programmercarl.com/0112.%E8%B7%AF%E5%BE%84%E6%80%BB%E5%92%8C.html](https://programmercarl.com/0112.%E8%B7%AF%E5%BE%84%E6%80%BB%E5%92%8C.html)

```go
func hasPathSum(root *TreeNode, targetSum int) bool {
    if root == nil {
        return false
    }
    return traversal(root, targetSum - root.Val)
}

func traversal(cur *TreeNode, count int) bool {
    if cur.Left == nil && cur.Right == nil && count == 0 {
        return true
    }
    if cur.Left == nil && cur.Right == nil {
        return false
    }
    if cur.Left != nil {
        count -= cur.Left.Val
        if traversal(cur.Left, count) {
            return true
        }
        count += cur.Left.Val
    }
    if cur.Right != nil {
        count -= cur.Right.Val
        if traversal(cur.Right, count) {
            return true
        }
        count += cur.Right.Val
    }
    return false
}

```

### 从中序与后序遍历序列构造二叉树

本题算是比较难的二叉树题目了，大家先看视频来理解。

106.从中序与后序遍历序列构造二叉树，105.从前序与中序遍历序列构造二叉树 一起做，思路一样的

题目链接/文章讲解/视频讲解：[https://programmercarl.com/0106.%E4%BB%8E%E4%B8%AD%E5%BA%8F%E4%B8%8E%E5%90%8E%E5%BA%8F%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97%E6%9E%84%E9%80%A0%E4%BA%8C%E5%8F%89%E6%A0%91.html](https://programmercarl.com/0106.%E4%BB%8E%E4%B8%AD%E5%BA%8F%E4%B8%8E%E5%90%8E%E5%BA%8F%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97%E6%9E%84%E9%80%A0%E4%BA%8C%E5%8F%89%E6%A0%91.html)

本题是构造二叉树。是一个比较不容考到的点。需要知道如何构造二叉树。



```go

func buildTree(inorder []int, postorder []int) *TreeNode {
    if len(postorder) == 0 {
        return nil
    }
    
    // 后序遍历数组最后一个元素，就是当前的中间节点
    rootValue := postorder[len(postorder)-1]
    root := &TreeNode{Val:rootValue}
    
    // 叶子结点
    if len(postorder) == 1 {
        return root
    }
    
    // 找到中序遍历的切割点
    var delimiterIndex int
    for delimiterIndex = 0; delimiterIndex < len(inorder); delimiterIndex++ {
        if inorder[delimiterIndex] == rootValue {
            break;
        }
    }
    
    // 切割中序数组
    // 左闭右开区间：[0, delimiterIndex)
    leftInorder := inorder[:delimiterIndex]
    // [delimiterIndex + 1, end)
    rightInorder := inorder[delimiterIndex+1:]
    
    // postorder 舍弃末尾元素
    postorder = postorder[:len(postorder)-1]
    
    // 切割后序数组
    // 依然左闭右开，注意这里使用了左中序数组大小作为切割点
    // [0, len(leftInorder))
    leftPostorder := postorder[:len(leftInorder)]
    // [len(leftInorder), end)
    rightPostorder := postorder[len(leftInorder):]
    
    root.Left = buildTree(leftInorder, leftPostorder)
    root.Right = buildTree(rightInorder, rightPostorder)
    
    return root
}

```


