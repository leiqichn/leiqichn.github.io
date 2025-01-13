---
title: 代码随想录 day20 二叉树 part07
date: 2024-11-19 23:08:59
modificationDate: 2024 十一月 19日 星期二 23:08:59
categories: 
	- carl
tags: []
sticky: []
hide: true
category_bar: true
---

### 235. 二叉搜索树的最近公共祖先

相对于 二叉树的最近公共祖先 本题就简单一些了，因为 可以利用二叉搜索树的特性。

题目链接/文章讲解：[https://programmercarl.com/0235.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88.html](https://programmercarl.com/0235.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88.html)

视频讲解：[https://www.bilibili.com/video/BV1Zt4y1F7ww](https://www.bilibili.com/video/BV1Zt4y1F7ww)

```go
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
    if root.Val > p.Val && root.Val > q.Val {
        return lowestCommonAncestor(root.Left, p, q)
    } else if root.Val < p.Val && root.Val < q.Val {
        return lowestCommonAncestor(root.Right, p, q)
    } else {
        return root
    }
}
```

### 701.二叉搜索树中的插入操作

本题比想象中的简单，大家可以先自己想一想应该怎么做，然后看视频讲解，就发现 本题为什么比较简单了。

题目链接/文章讲解：[https://programmercarl.com/0701.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E6%8F%92%E5%85%A5%E6%93%8D%E4%BD%9C.html](https://programmercarl.com/0701.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E6%8F%92%E5%85%A5%E6%93%8D%E4%BD%9C.html)

视频讲解：[https://www.bilibili.com/video/BV1Et4y1c78Y](https://www.bilibili.com/video/BV1Et4y1c78Y)

```go
func insertIntoBST(root *TreeNode, val int) *TreeNode {
    if root == nil {
        root = &TreeNode{Val: val}
        return root
    }
    if root.Val > val {
        root.Left = insertIntoBST(root.Left, val) // 接住新的节点 **有返回值的话，可以利用返回值完成新加入的节点与其父节点的赋值操作**
    } else {
        root.Right = insertIntoBST(root.Right, val)
    }
    return root
}
```

### 450.删除二叉搜索树中的节点

相对于 插入操作，本题就有难度了，涉及到改树的结构

题目链接/文章讲解：[https://programmercarl.com/0450.%E5%88%A0%E9%99%A4%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B9.html](https://programmercarl.com/0450.%E5%88%A0%E9%99%A4%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B9.html)

视频讲解：[https://www.bilibili.com/video/BV1tP41177us](https://www.bilibili.com/video/BV1tP41177us)



```go
// 递归版本
func deleteNode(root *TreeNode, key int) *TreeNode {
    if root == nil {
        return nil
    }
    if key < root.Val {
        root.Left = deleteNode(root.Left, key)
        return root
    }
    if key > root.Val {
        root.Right = deleteNode(root.Right, key)
        return root
    }
    if root.Right == nil {
        return root.Left
    }
    if root.Left == nil{
        return root.Right
    }
    minnode := root.Right
    for minnode.Left != nil {
        minnode = minnode.Left
    }
    root.Val = minnode.Val
    root.Right = deleteNode1(root.Right)
    return root
}

func deleteNode1(root *TreeNode)*TreeNode {
    if root.Left == nil {
        pRight := root.Right
        root.Right = nil
        return pRight
    }
    root.Left = deleteNode1(root.Left)
    return root
}
```
