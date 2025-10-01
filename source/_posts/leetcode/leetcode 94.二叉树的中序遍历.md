---
title: leetcode 94.二叉树的中序遍历
date: 2024-01-22 23:01:59
modificationDate: 2024 一月 22日 星期一 23:04:02
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---

# 递归方法

```go

func inorderTraversal(root *TreeNode) (res []int) {
    var traversal func(node *TreeNode)
    traversal = func(node *TreeNode) {
	if node == nil {
	    return
	}
	traversal(node.Left)
	res = append(res,node.Val)
	traversal(node.Right)
    }
    traversal(root)
    return res
}

```


# 非递归方法


```go
func inorderTraversal(root *TreeNode) []int {
    ans := []int{}
    if root == nil {
        return ans
    }

    st := list.New()
    cur := root

    for cur != nil || st.Len() > 0 {
        if cur != nil {
            st.PushBack(cur)
            cur = cur.Left
        } else {
            cur = st.Remove(st.Back()).(*TreeNode)
            ans = append(ans, cur.Val)
            cur = cur.Right
        }
    }

    return ans
}

```

下面是对代码的解释：

1. `ans := []int{}`: 创建一个空的整数切片，用于存储最终的中序遍历结果。
    
2. `if root == nil { return ans }`: 检查树的根节点是否为空，如果为空则返回空切片，避免对空树进行遍历。
    
3. `st := list.New()`: 创建一个新的链表（list），用作栈。这里使用标准库中的`list`包，实现了一个双向链表作为栈。
    
4. `cur := root`: 初始化当前节点为根节点。
    
5. `for cur != nil || st.Len() > 0 {`: 进入循环，只要当前节点不为空或栈不为空就继续遍历。
    
6. `if cur != nil {`: 如果当前节点不为空，将当前节点入栈，并将当前节点移动到左子树。
    
    - `st.PushBack(cur)`: 将当前节点入栈。
        
    - `cur = cur.Left`: 移动到左子树。
        
7. `} else {`: 如果当前节点为空，表示左子树已经遍历完毕，需要处理栈顶节点。
    
    - `cur = st.Remove(st.Back()).(*TreeNode)`: 弹出栈顶节点，即当前待处理的节点。
        
    - `ans = append(ans, cur.Val)`: 将当前节点的值加入结果切片。
        
    - `cur = cur.Right`: 移动到右子树。
        
8. 循环回到第5步，直到栈为空。
    

这种非递归中序遍历的实现使用了栈来辅助遍历，通过不断地将左子树的节点入栈，并在处理栈顶节点时将其值加入结果切片，最后移动到右子树，以达到中序遍历的顺序。
  
其中 进入循环的条件 `for cur != nil || st.Len() > 0` 是为了确保在树的所有节点都被遍历到之前，循环能够继续执行。让我们逐步解释这个条件：

- `cur != nil`: 如果当前节点不为空，表示还有左子树可以遍历，因此继续循环。
    
- `st.Len() > 0`: 如果当前节点为空，但栈不为空，说明还有节点需要处理（回溯到上一层的右子树），也继续循环。
    

这个条件的目的是确保在左子树和右子树都被遍历完之前，循环一直执行。当所有节点都被遍历过，且栈为空时，循环条件不再满足，退出循环，完成中序遍历。

在这个中序遍历的非递归实现中，通过栈来模拟递归调用的过程，确保每个节点都按照中序遍历的顺序被访问。