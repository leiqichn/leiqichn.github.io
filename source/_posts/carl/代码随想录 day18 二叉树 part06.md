---
title: 代码
date: 2024-11-16 13:32:31
modificationDate: 2024 十一月 16日 星期六 13:32:31
categories: 
	- carl
tags: []
sticky: []
hide: true
category_bar: true
---

# 第六章 二叉树part06

## 详细布置

### 530.二叉搜索树的最小绝对差
[530. 二叉搜索树的最小绝对差](https://leetcode.cn/problems/minimum-absolute-difference-in-bst/)
需要领悟一下二叉树遍历上双指针操作，优先掌握递归

题目链接/文章讲解：[https://programmercarl.com/0530.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E6%9C%80%E5%B0%8F%E7%BB%9D%E5%AF%B9%E5%B7%AE.html](https://programmercarl.com/0530.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E6%9C%80%E5%B0%8F%E7%BB%9D%E5%AF%B9%E5%B7%AE.html)

视频讲解：[https://www.bilibili.com/video/BV1DD4y11779](https://www.bilibili.com/video/BV1DD4y11779)
一些同学不知道在递归中如何记录前一个节点的指针，其实实现起来是很简单的，大家只要看过一次，写过一次，就掌握了。

代码如下：


```
class Solution {
private:
int result = INT_MAX;
TreeNode* pre = NULL;
void traversal(TreeNode* cur) {
    if (cur == NULL) return;
    traversal(cur->left);   // 左
    if (pre != NULL){       // 中
        result = min(result, cur->val - pre->val);
    }
    pre = cur; // 记录前一个
    traversal(cur->right);  // 右
}
public:
    int getMinimumDifference(TreeNode* root) {
        traversal(root);
        return result;
    }
};
```

```go
// 中序遍历的同时计算最小值
func getMinimumDifference(root *TreeNode) int {
    // 保留前一个节点的指针
    var prev *TreeNode
    // 定义一个比较大的值
    min := math.MaxInt64
    var travel func(node *TreeNode)
    travel = func(node *TreeNode) {
        if node == nil {
            return 
        }
        travel(node.Left)
        // 在中间操作
        if prev != nil && node.Val - prev.Val < min {
            min = node.Val - prev.Val
        }
        prev = node
        travel(node.Right)
    }
    travel(root)
    return min
}
```
### 501.二叉搜索树中的众数

和 530差不多双指针思路，不过 这里涉及到一个很巧妙的代码技巧。

可以先自己做做看，然后看我的视频讲解。

[https://programmercarl.com/0501.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E4%BC%97%E6%95%B0.html](https://programmercarl.com/0501.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E4%BC%97%E6%95%B0.html)

视频讲解：[https://www.bilibili.com/video/BV1fD4y117gp](https://www.bilibili.com/video/BV1fD4y117gp)



```go
func findMode(root *TreeNode) []int {
    res := make([]int, 0)
    count := 1
    max := 1
    var prev *TreeNode
    var travel func(node *TreeNode) 
    travel = func(node *TreeNode) {
        if node == nil {
            return
        }
        travel(node.Left)
        if prev != nil && prev.Val == node.Val {
            count++
        } else {
            count = 1
        }
        if count >= max {
            if count > max && len(res) > 0 {
                res = []int{node.Val}
            } else {
                res = append(res, node.Val)
            }
            max = count
        }
        prev = node
        travel(node.Right)
    }
    travel(root)
    return res
}

```

### 236. 二叉树的最近公共祖先

本题其实是比较难的，可以先看我的视频讲解

[https://programmercarl.com/0236.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88.html](https://programmercarl.com/0236.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88.html)

视频讲解：[https://www.bilibili.com/video/BV1jd4y1B7E2](https://www.bilibili.com/video/BV1jd4y1B7E2)

```go

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
    // check
    if root == nil {
        return root
    }
    // 相等 直接返回root节点即可
    if root == p || root == q {
        return root
    }
    // Divide
    left := lowestCommonAncestor(root.Left, p, q)
    right := lowestCommonAncestor(root.Right, p, q)

    // Conquer
    // 左右两边都不为空，则根节点为祖先
    if left != nil && right != nil {
        return root
    }
    if left != nil {
        return left
    }
    if right != nil {
        return right
    }
    return nil
}
```
