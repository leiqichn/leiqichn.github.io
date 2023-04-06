  
[513. 找树左下角的值 - 力扣（Leetcode）](https://leetcode.cn/problems/find-bottom-left-tree-value/)

给定一个二叉树的 **根节点** `root`，请找出该二叉树的 **最底层 最左边** 节点的值。

假设二叉树中至少有一个节点。

**示例 1:**

![](https://assets.leetcode.com/uploads/2020/12/14/tree1.jpg)

**输入:** root = [2,1,3]
**输出:** 1

**示例 2:**

![](https://assets.leetcode.com/uploads/2020/12/14/tree2.jpg)

**输入:** [1,2,3,4,null,5,6,null,null,7]
**输出:** 7

**提示:**

-   二叉树的节点个数的范围是 `[1,104]`
-   `-2^31 <= Node.val <= 2^31 - 1`

## 思考

本题可以转化为什么呢？
> 1.最后一层的最左边的数值，递归的话需要记录最后一层，并且记录最左边的值
> 2.如果是迭代呢？这个就更适合了，只要记录每层迭代中的第一个值，并且不断更新更大的值就好。

## 代码实现
1.递归

```go
var depth int   // 全局变量 最大深度
var res int     // 记录最终结果
func findBottomLeftValue(root *TreeNode) int {
    depth, res = 0, 0   
    dfs(root, 1)
    return res
}

func dfs(root *TreeNode, d int) {
    //这里判断nil ,后边左右节点就不用判断了
    if root == nil {
        return
    }
    // 因为先遍历左边，所以左边如果有值，右边的同层不会更新结果
    if root.Left == nil && root.Right == nil && depth < d { 
        depth = d
        res = root.Val
    }
    dfs(root.Left, d+1)   
    dfs(root.Right, d+1)
}

```



2.迭代

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
	res := -1
	queue := []*TreeNode{}

	if root == nil {
		return -1
	}
	
	queue = append(queue, root)
	//res 在哪里更新呢？
	for len(queue) > 0 {
		size := len(queue)
		// 遍历每一层
		for i := 0; i < size; i++ {
			top := queue[0]
			queue = queue[1:]
			// 获取每一层的最左边的位置，更新res
			if i == 0 {
				res = top.Val
			}
			if top.Left != nil {
				queue = append(queue, top.Left)
			}
			if top.Right != nil {
				queue = append(queue, top.Right)
			}
		}

	}
	return res
}


// 迭代2 每层用一个切片

func findBottomLeftValue(root *TreeNode) int {
	res := -1
	queue := []*TreeNode{}

	if root == nil {
		return -1
	}
	// 通过另外一个切片来添加的解法也要尝试学习一下
	queue = append(queue, root)
	//res 在哪里更新呢？
	for len(queue) > 0 {
		size := len(queue)
		// 使用nextqueue 保存每一层，然后追加到queue
		nextqueue := []*TreeNode{}
		for i := 0; i < size; i++ {
			top := queue[0]
			queue = queue[1:]
		    res = nextqueue[0]
			if top.Left != nil {
				nextqueue = append(nextqueue, top.Left)
			}

			if top.Right != nil {
				nextqueue = append(nextqueue, top.Right)
			}
		}
		queue = append(queue,nextqueue...)

	}
	return res
}
```

## 拓展思考

如果要求最右边的值呢？这里该怎么求呢？

只需要将 遍历左右的顺序颠倒一下即可


```go
func findBottomLeftValue(root *TreeNode) int {
	res := -1
	queue := []*TreeNode{}

	if root == nil {
		return -1
	}
	
	queue = append(queue, root)
	//res 在哪里更新呢？
	for len(queue) > 0 {
		size := len(queue)
		// 遍历每一层
		for i := 0; i < size; i++ {
			top := queue[0]
			queue = queue[1:]
			// 获取每一层的最左边的位置，更新res
			if i == 0 {
				res = top.Val
			}
			
			if top.Right != nil {
				queue = append(queue, top.Right)
			}
			
			if top.Left != nil {
				queue = append(queue, top.Left)
			}

		}

	}
	return res
}


```


