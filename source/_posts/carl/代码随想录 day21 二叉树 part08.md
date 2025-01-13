---
title: 代码随想录 day21 二叉树 part08
date: 2024-11-20 00:31:50
modificationDate: 2024 十一月 20日 星期三 00:31:50
categories: 
	- carl
tags: []
sticky: []
hide: true
category_bar: true
---
# 第六章 二叉树part08

### 669. 修剪二叉搜索树

这道题目比较难，比 添加增加和删除节点难的多，建议先看视频理解。

题目链接/文章讲解： [https://programmercarl.com/0669.%E4%BF%AE%E5%89%AA%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.html](https://programmercarl.com/0669.%E4%BF%AE%E5%89%AA%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.html)

视频讲解： [https://www.bilibili.com/video/BV17P41177ud](https://www.bilibili.com/video/BV17P41177ud)

```go

// 递归
func trimBST(root *TreeNode, low int, high int) *TreeNode {
    if root == nil {
        return nil
    }
    if root.Val < low {     //如果该节点值小于最小值，则该节点更换为该节点的右节点值，继续遍历
        right := trimBST(root.Right, low, high)
        return right
    }
    if root.Val > high {    //如果该节点的值大于最大值，则该节点更换为该节点的左节点值，继续遍历
        left := trimBST(root.Left, low, high)
        return left
    }
    root.Left = trimBST(root.Left, low, high)
    root.Right = trimBST(root.Right, low, high)
    return root
}

```

### 108.将有序数组转换为二叉搜索树

本题就简单一些，可以尝试先自己做做。

[https://programmercarl.com/0108.%E5%B0%86%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84%E8%BD%AC%E6%8D%A2%E4%B8%BA%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.html](https://programmercarl.com/0108.%E5%B0%86%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84%E8%BD%AC%E6%8D%A2%E4%B8%BA%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.html)

视频讲解：[https://www.bilibili.com/video/BV1uR4y1X7qL](https://www.bilibili.com/video/BV1uR4y1X7qL)

思路：二分法：

```go

func sortedArrayToBST(nums []int) *TreeNode {
    if len(nums) == 0 {    //终止条件，最后数组为空则可以返回
        return nil
    }
    idx := len(nums)/2
    root := &TreeNode{Val: nums[idx]} 
     
    root.Left = sortedArrayToBST(nums[:idx])
    root.Right = sortedArrayToBST(nums[idx+1:])

    return root
}
```

### 538.把二叉搜索树转换为累加树

本题也不难，在 求二叉搜索树的最小绝对差 和 众数 那两道题目 都讲过了 双指针法，思路是一样的。

[https://programmercarl.com/0538.%E6%8A%8A%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E8%BD%AC%E6%8D%A2%E4%B8%BA%E7%B4%AF%E5%8A%A0%E6%A0%91.html](https://programmercarl.com/0538.%E6%8A%8A%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E8%BD%AC%E6%8D%A2%E4%B8%BA%E7%B4%AF%E5%8A%A0%E6%A0%91.html)

视频讲解：[https://www.bilibili.com/video/BV1d44y1f7wP](https://www.bilibili.com/video/BV1d44y1f7wP)

```go
var pre int
func convertBST(root *TreeNode) *TreeNode {
    pre = 0
    traversal(root)
    return root
}

func traversal(cur *TreeNode) {
    if cur == nil {
        return
    }
    traversal(cur.Right)
    cur.Val += pre
    pre = cur.Val
    traversal(cur.Left)
}

```

### 总结篇

好了，二叉树大家就这样刷完了，做一个总结吧

[https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E6%80%BB%E7%BB%93%E7%AF%87.html](https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E6%80%BB%E7%BB%93%E7%AF%87.html)
