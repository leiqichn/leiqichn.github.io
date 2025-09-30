---
title: leetcode 102. 二叉树的层序遍历
date: 2023-05-23 22:46:19
modificationDate: 2023 五月 23日 星期二 22:46:19
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---
[102. 二叉树的层序遍历 - 力扣（Leetcode）](https://leetcode.cn/problems/binary-tree-level-order-traversal/description/)
![](../../imgs/Pasted%20image%2020230523224632.png)

```go
func levelOrder(root *TreeNode) [][]int {
    res := [][]int{}
    if root == nil{//防止为空
        return res
    }
    queue := &list.List{}
    queue.PushBack(root)

    for queue.Len() > 0 {
        length := queue.Len()               //保存当前层的长度，然后处理当前层（十分重要，防止添加下层元素影响判断层中元素的个数）     
        var levelQueue []int
        fmt.Println(length)
        for i := 0; i < length; i++ {
            node := queue.Remove(queue.Front()).(*TreeNode)    //出队列
            if node.Left != nil {
                queue.PushBack(node.Left)
            }
            if node.Right != nil {
                queue.PushBack(node.Right)
            }
            levelQueue = append(levelQueue, node.Val)    //将值加入本层切片中
        }
        res = append(res, levelQueue)          //放入结果集
    }

    return res
}
```

