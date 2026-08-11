---
title: Go 递归与回溯：为什么 int 参数不需要手动"恢复"？
date: 2026-08-11 08:35:00
modificationDate: 2026 八月 11日 星期二 08:35:00
categories:
  - [算法, LeetCode]
tags: [Go, 递归, 回溯, DFS]
sticky: []
published: true
category_bar: true
---

这是一个非常好的问题，触及了递归和回溯的核心概念。

**简短回答：不需要手动恢复，你的代码是完全正确的。**

为什么不需要恢复？这涉及到编程语言中参数传递的机制。

## 1. 值传递机制

在 Go 语言中，`int` 类型是基本类型，函数参数是**值传递**的。

当你在函数内部执行 `targetSum -= root.Val` 时，你修改的只是当前函数栈帧中 `targetSum` 这个局部变量的**副本**。

当你调用下一层递归 `hasPathSum(root.Left, targetSum)` 时：

- Go 会把当前的 `targetSum` 值复制一份传给新的函数
- 新的函数拿到的是一个全新的副本，它的修改不会影响到上一层函数里的 `targetSum`

举个例子，假设当前节点值是 5，`targetSum` 是 22：

1. 进入函数，`targetSum` 是 22
2. 执行 `targetSum -= 5`，当前层级的 `targetSum` 变成了 17
3. 调用左子树：`hasPathSum(left, 17)`。左子树函数内部怎么折腾这个 17，都不会改变当前层级的 17，更不会变回 22
4. **关键点**：当左子树调用结束，程序回到当前层级，准备执行右子树 `hasPathSum(right, targetSum)` 时，这里的 `targetSum` 依然是刚才算出来的 17

所以，对于这道题，这种写法天然就是"正确"的——每一层都拿着自己的一份"账单副本"在计算。

## 2. 什么时候需要"恢复"？

你可能在其他的回溯算法（如全排列、组合总和）中见过需要"恢复状态"的代码，通常长这样：

```go
// 典型的回溯模板
path = append(path, root.Val)     // 做选择
dfs(root.Left, targetSum-root.Val)
path = path[:len(path)-1]         // 撤销选择（恢复状态）
```

为什么这里需要恢复，而上面的 `targetSum` 不需要？

**区别在于数据结构：**

- `targetSum`（int）：**值类型**。函数调用时自动复制，天然的隔离保护了每一层的数据，所以不需要手动恢复
- `path`（切片/slice）：**引用类型**（或者理解为它传递的是内存地址）。所有递归层级**共享同一个 `path` 数组**。如果递归左子树时往里面加了东西，递归完不拿出来，遍历右子树时 `path` 里就会带着左子树的数据，导致结果错误

## 3. 如果是指针传递呢？

如果你的函数参数不是 `int`，而是一个指针（比如 `*int`），那么你就**需要**恢复：

```go
func hasPathSum(root *TreeNode, targetSum *int) bool {
    // ...
    *targetSum -= root.Val   // 修改了内存中真实的值
    // ...
    hasPathSum(root.Left, targetSum)
    *targetSum += root.Val   // 这里就必须加回来（恢复），否则右子树的判断会出错
    // ...
}
```

## 总结

代码逻辑图解如下：

```
进入节点 A (targetSum = 22)
|
+-- 执行 targetSum -= A.Val (当前层 targetSum = 17)
|
+-- 调用左子树 B (传入值 17)
|   |
|   +-- 进入 B (targetSum = 17 的副本)
|   +-- B 内部不管怎么改，不影响 A 层的 17
|   +-- 返回
|
+-- 左子树结束，回到 A 层 (targetSum 还是 17)
|
+-- 调用右子树 C (传入值 17)
|   ...
```

因为 `targetSum` 是通过值传递的，每一层递归都有自己独立的变量副本，互不干扰，所以**不需要也不存在"恢复"一说**。你的写法是标准的 DFS 写法。

> **核心结论：值类型天然隔离，引用类型需要手动恢复。** 判断是否需要"撤销选择"，看参数是值传递还是引用传递即可。
