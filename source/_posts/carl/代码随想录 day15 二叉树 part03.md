---
title: 代码随想录 day15 二叉树 part03
date: 2024-11-15 00:45:49
modificationDate: 2024 November 15th Friday 00:45:49
categories: 
	- carl
tags: []
sticky: []
hide: true
category_bar: true
---

# 第六章 二叉树part03

迭代法，大家可以直接过，二刷有精力的时候 再去掌握迭代法。

### 110.平衡二叉树 （优先掌握递归）

再一次涉及到，什么是高度，什么是深度，可以巩固一下。

题目链接/文章讲解/视频讲解：[https://programmercarl.com/0110.%E5%B9%B3%E8%A1%A1%E4%BA%8C%E5%8F%89%E6%A0%91.html](https://programmercarl.com/0110.%E5%B9%B3%E8%A1%A1%E4%BA%8C%E5%8F%89%E6%A0%91.html)



```go

func isBalanced(root *TreeNode) bool {
    h := getHeight(root)
    if h == -1 {
        return false
    }
    return true
}
// 返回以该节点为根节点的二叉树的高度，如果不是平衡二叉树了则返回-1
func getHeight(root *TreeNode) int {
    if root == nil {
        return 0
    }
    l, r := getHeight(root.Left), getHeight(root.Right)
    if l == -1 || r == -1 {
        return -1
    }
    if l - r > 1 || r - l > 1 {
        return -1
    }
    return max(l, r) + 1
}
func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

```

### 257. 二叉树的所有路径 （优先掌握递归）

这是大家第一次接触到回溯的过程， 我在视频里重点讲解了 本题为什么要有回溯，已经回溯的过程。

如果对回溯 似懂非懂，没关系， 可以先有个印象。

题目链接/文章讲解/视频讲解：[https://programmercarl.com/0257.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%89%80%E6%9C%89%E8%B7%AF%E5%BE%84.html](https://programmercarl.com/0257.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%89%80%E6%9C%89%E8%B7%AF%E5%BE%84.html)



```go
func binaryTreePaths(root *TreeNode) []string {
    res := make([]string, 0)
    var travel func(node *TreeNode, s string)
    travel = func(node *TreeNode, s string) {
        if node.Left == nil && node.Right == nil {
            v := s + strconv.Itoa(node.Val)
            res = append(res, v)
            return
        }
        s = s + strconv.Itoa(node.Val) + "->"
        if node.Left != nil {
            travel(node.Left, s)
        }
        if node.Right != nil {
            travel(node.Right, s)
        }
    }
    travel(root, "")
    return res
}
```

### 404.左叶子之和 （优先掌握递归）

其实本题有点文字游戏，搞清楚什么是左叶子，剩下的就是二叉树的基本操作。

题目链接/文章讲解/视频讲解：[https://programmercarl.com/0404.%E5%B7%A6%E5%8F%B6%E5%AD%90%E4%B9%8B%E5%92%8C.html](https://programmercarl.com/0404.%E5%B7%A6%E5%8F%B6%E5%AD%90%E4%B9%8B%E5%92%8C.html)


```go
func sumOfLeftLeaves(root *TreeNode) int {
    if root == nil {
        return 0
    }
    leftValue := sumOfLeftLeaves(root.Left)   // 左

    if root.Left != nil && root.Left.Left == nil && root.Left.Right == nil {
        leftValue = root.Left.Val             // 中
    }

    rightValue := sumOfLeftLeaves(root.Right) // 右

    return leftValue + rightValue
}


```


### 222.完全二叉树的节点个数（优先掌握递归）

需要了解，普通二叉树 怎么求，完全二叉树又怎么求

题目链接/文章讲解/视频讲解：[https://programmercarl.com/0222.%E5%AE%8C%E5%85%A8%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E8%8A%82%E7%82%B9%E4%B8%AA%E6%95%B0.html](https://programmercarl.com/0222.%E5%AE%8C%E5%85%A8%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E8%8A%82%E7%82%B9%E4%B8%AA%E6%95%B0.html)


```go
var depth int   // 全局变量 最大深度
var res int     // 记录最终结果
func findBottomLeftValue(root *TreeNode) int {
    depth, res = 0, 0   // 初始化
    dfs(root, 1)
    return res
}

func dfs(root *TreeNode, d int) {
    if root == nil {
        return
    }
    // 因为先遍历左边，所以左边如果有值，右边的同层不会更新结果
    if root.Left == nil && root.Right == nil && depth < d { 
        depth = d
        res = root.Val
    }
    dfs(root.Left, d+1)   // 隐藏回溯
    dfs(root.Right, d+1)
}
```
