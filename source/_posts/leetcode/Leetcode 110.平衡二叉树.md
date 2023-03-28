---
title: Leetcode 110.平衡二叉树
date: 2023-03-28 11:18:47
modificationDate: 2023 三月 28日 星期二 23:18:47
categories: 
	- leetcode
tags: []
sticky: []
hide: true
category_bar: true
---

[110. 平衡二叉树 - 力扣（Leetcode）](https://leetcode.cn/problems/balanced-binary-tree/)

<font color="#2DC26B">简单 </font>
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

> 一个二叉树_每个节点_ 的左右两个子树的高度差的绝对值不超过 1 。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg)

**输入：**root = [3,9,20,null,null,15,7]
**输出：**true

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg)

**输入：**root = [1,2,2,3,3,null,null,4,4]
**输出：**false

**示例 3：**

**输入：**root = []
**输出：**true

**提示：**

-   树中的节点数在范围 `[0, 5000]` 内
-   `-104 <= Node.val <= 104`

## 思路

这里是求**高度**： 节点到叶子节点的最长距离，使用**后序遍历**
**深度**是root 到该节点的最长距离（距离☞节点数），使用**前序遍历**

因此只要分别计算左右子树的高度，并且做差不大于1就行

## 代码实现

使用-1 记录 res 不是平衡二叉树
每次执行，都需要判断是不是等于-1，直接返回-1