---
title: 代码随想录 day17 二叉树 part05
date: 2024-11-15 22:46:40
modificationDate: 2024 November 15th Friday 22:46:40
categories: 
	- carl
tags: []
sticky: []
published: false
category_bar: true
---


# 第六章 二叉树 part05

## 详细布置
 
### 654.最大二叉树

又是构造二叉树，昨天大家刚刚做完 中序后序确定二叉树，今天做这个 应该会容易一些， 先看视频，好好体会一下 为什么构造二叉树都是 前序遍历

题目链接/文章讲解：[https://programmercarl.com/0654.%E6%9C%80%E5%A4%A7%E4%BA%8C%E5%8F%89%E6%A0%91.html](https://programmercarl.com/0654.%E6%9C%80%E5%A4%A7%E4%BA%8C%E5%8F%89%E6%A0%91.html)

视频讲解：[https://www.bilibili.com/video/BV1MG411G7ox](https://www.bilibili.com/video/BV1MG411G7ox)
思路： 构造树，一般采用前序遍历，因为先构造中间节点。然后构造左子树和右子树。
1. 确定递归函数的参数和返回值 `func constructMaximumBinaryTree(nums []int) *TreeNode` 返回头节点即可
2. 确定终止条件： 题目中说了输入的数组大小一定是大于等于1的，所以我们不用考虑小于1的情况，那么当递归遍历的时候，如果传入的数组大小为1，说明遍历到了叶子节点了。那么应该定义一个新的节点，并把这个数组的数值赋给新的节点，然后返回这个节点。 这表示一个数组大小是1的时候，构造了一个新的节点，并返回。**或者判断nums == 0的时候直接返回nil**
3. 确定三层递归的逻辑 3步操作：1. 先要找到数组中最大的值和对应的下标， 最大的值构造根节点，下标用来下一步分割数组。 2. 最大值所在的下标左区间 构造左子树 3. 最大值所在的下标右区间 构造右子树

```go
func constructMaximumBinaryTree(nums []int) *TreeNode {
    if len(nums) == 0 {
        return nil 
    }
    // 找到最大值
    index := findMax(nums)
    // 构造二叉树
    root := &TreeNode {
        Val: nums[index],
        Left: constructMaximumBinaryTree(nums[:index]),   //左半边
        Right: constructMaximumBinaryTree(nums[index+1:]),//右半边
        }
    return root
}
func findMax(nums []int) (index int) { // 获取最大元素的index
    for i, v := range nums {
        if nums[index] < v {
            index = i
        }
    }
    return 
}

```

### 617.合并二叉树

这次是一起操作两个二叉树了， 估计大家也没一起操作过两个二叉树，也不知道该如何一起操作，可以看视频先理解一下。 优先掌握递归。

题目链接/文章讲解：[https://programmercarl.com/0617.%E5%90%88%E5%B9%B6%E4%BA%8C%E5%8F%89%E6%A0%91.html](https://programmercarl.com/0617.%E5%90%88%E5%B9%B6%E4%BA%8C%E5%8F%89%E6%A0%91.html)

视频讲解：[https://www.bilibili.com/video/BV1m14y1Y7JK](https://www.bilibili.com/video/BV1m14y1Y7JK)

1. **确定递归函数的参数和返回值：**

首先要合入两个二叉树，那么参数至少是要传入两个二叉树的根节点，返回值就是合并之后二叉树的根节点。
2. **确定终止条件：**

因为是传入了两个树，那么就有两个树遍历的节点t1 和 t2，如果t1 == NULL 了，两个树合并就应该是 t2 了（如果t2也为NULL也无所谓，合并之后就是NULL）。

反过来如果t2 == NULL，那么两个数合并就是t1（如果t1也为NULL也无所谓，合并之后就是NULL）。

3. **确定单层递归的逻辑：**

单层递归的逻辑就比较好写了，这里我们重复利用一下t1这个树，t1就是合并之后树的根节点（就是修改了原来树的结构）。

那么单层递归中，就要把两棵树的元素加到一起。
```go
// 前序遍历
func mergeTrees(root1 *TreeNode, root2 *TreeNode) *TreeNode {
    if root1 == nil {
        return root2
    }
    if root2 == nil {
        return root1
    }
    root1.Val += root2.Val
    root1.Left = mergeTrees(root1.Left, root2.Left) // 同时遍历两个二叉树
    root1.Right = mergeTrees(root1.Right, root2.Right)
    return root1
}
```

**迭代法**
使用迭代法，如何同时处理两棵树呢？

思路我们在[二叉树：我对称么？ (opens new window)](https://programmercarl.com/0101.%E5%AF%B9%E7%A7%B0%E4%BA%8C%E5%8F%89%E6%A0%91.html)中的迭代法已经讲过一次了，求二叉树对称的时候就是把两个树的节点同时加入队列进行比较。


```go

func mergeTrees(root1 *TreeNode, root2 *TreeNode) *TreeNode {
    queue := make([]*TreeNode,0)
    if root1 == nil{
        return root2
    }
    if root2 == nil{
        return root1
    }
    queue = append(queue,root1)
    queue = append(queue,root2)

    for size := len(queue); size>0; size=len(queue) {
        node1 := queue[0]
        queue = queue[1:]
        node2 := queue[0]
        queue = queue[1:]
        node1.Val += node2.Val
        // 左子树都不为空
        if node1.Left != nil && node2.Left != nil {
            queue = append(queue,node1.Left)
            queue = append(queue,node2.Left)
        }
        // 右子树都不为空
        if node1.Right !=nil && node2.Right !=nil {
            queue = append(queue, node1.Right)
            queue = append(queue, node2.Right)
        }
        // 树 1 的左子树为 nil，直接接上树 2 的左子树
        if node1.Left == nil {
            node1.Left = node2.Left
        }
        // 树 1 的右子树为 nil，直接接上树 2 的右子树
        if node1.Right == nil {
            node1.Right = node2.Right
        }
    }
    return root1
}

```

### 700.二叉搜索树中的搜索
[700. 二叉搜索树中的搜索](https://leetcode.cn/problems/search-in-a-binary-search-tree/)


递归和迭代 都可以掌握以下，因为本题比较简单， 了解一下 二叉搜索树的特性

题目链接/文章讲解: [https://programmercarl.com/0700.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E6%90%9C%E7%B4%A2.html](https://programmercarl.com/0700.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E6%90%9C%E7%B4%A2.html)

视频讲解：[https://www.bilibili.com/video/BV1wG411g7sF](https://www.bilibili.com/video/BV1wG411g7sF)


思路：二叉搜索树是一个有序树：

若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
它的左、右子树也分别为二叉搜索树
##### 递归方法
1. 确定递归函数的参数和返回值

递归函数的参数传入的就是根节点和要搜索的数值，返回的就是以这个搜索数值所在的节点。

2. 确定终止条件

如果root为空，或者找到这个数值了，就返回root节点。
3. 确定单层递归的逻辑

看看二叉搜索树的单层递归逻辑有何不同。

因为二叉搜索树的节点是有序的，所以可以有方向的去搜索。

如果root->val > val，搜索左子树，如果root->val < val，就搜索右子树，最后如果都没有搜索到，就返回NULL。

```go
func searchBST(root *TreeNode, val int) *TreeNode {
    if root == nil || root.Val == val {
        return root
    }
    if root.Val > val {
        return searchBST(root.Left, val)
    }
    return searchBST(root.Right, val)
}

```

#### 迭代方法

对于二叉搜索树，不需要回溯的过程，因为节点的有序性就帮我们确定了搜索的方向。

例如要搜索元素为3的节点，我们不需要搜索其他节点，也不需要做回溯，查找的路径已经规划好了


```go

 //迭代法
func searchBST(root *TreeNode, val int) *TreeNode {
    for root != nil {
        if root.Val > val {
            root = root.Left
        } else if root.Val < val {
            root = root.Right
        } else {
            return root
        }
    }
    return nil
}

```


### 98.验证二叉搜索树
[98. 验证二叉搜索树](https://leetcode.cn/problems/validate-binary-search-tree/)
遇到 搜索树，一定想着中序遍历，这样才能利用上特性。

但本题是有陷阱的，可以自己先做一做，然后在看题解，看看自己是不是掉陷阱里了。这样理解的更深刻。

题目链接/文章讲解：[https://programmercarl.com/0098.%E9%AA%8C%E8%AF%81%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.html](https://programmercarl.com/0098.%E9%AA%8C%E8%AF%81%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.html)

视频讲解：[https://www.bilibili.com/video/BV18P411n7Q4](https://www.bilibili.com/video/BV18P411n7Q4)


思路
要知道中序遍历下，输出的二叉搜索树节点的数值是**有序序列**。

有了这个特性，验证二叉搜索树，就相当于变成了判断一个序列是不是递增的


```go


// 中序遍历解法
func isValidBST(root *TreeNode) bool {
    // 保存上一个指针
    var prev *TreeNode
    var travel func(node *TreeNode) bool
    travel = func(node *TreeNode) bool {
        if node == nil {
            return true
        }
        leftRes := travel(node.Left)
        // 当前值小于等于前一个节点的值，返回false
        if prev != nil && node.Val <= prev.Val {
            return false
        }
        prev = node
        rightRes := travel(node.Right)
        return leftRes && rightRes
    }
    return travel(root)
}

```

当然也可以中序遍历将值放入到对应的列表中。然后遍历列表中前一个值是否是小于等于后边一个值。