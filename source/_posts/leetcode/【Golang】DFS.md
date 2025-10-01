
---
title: 【Golang】DFS
date: 2025-06-18 00:21:34
modificationDate: 2025 六月 18日 星期三 00:21:34
categories: 
	- leetcode
tags: []
sticky: []
published: true
category_bar: true
---

# LeetCode 上经典的 DFS 题目及 Golang 实现与模板总结

DFS（深度优先搜索）是算法面试中的常见题型，下面我将总结 LeetCode 上一些经典的 DFS 题目，并用 Golang 实现，最后提炼出通用的 DFS 解题模板。

## 经典 DFS 题目分类及 Golang 实现

### 1. 二叉树遍历类

#### 题目 94. 二叉树的中序遍历

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func inorderTraversal(root *TreeNode) []int {
    var res []int
    var dfs func(node *TreeNode)
    dfs = func(node *TreeNode) {
        if node == nil {
            return
        }
        dfs(node.Left)
        res = append(res, node.Val)
        dfs(node.Right)
    }
    dfs(root)
    return res
}
```

### 2. 排列组合类

#### 题目 46. 全排列

```go
func permute(nums []int) [][]int {
    var res [][]int
    visited := make([]bool, len(nums))
    
    var dfs func(path []int)
    dfs = func(path []int) {
        if len(path) == len(nums) {
            tmp := make([]int, len(path))
            copy(tmp, path)
            res = append(res, tmp)
            return
        }
        
        for i := 0; i < len(nums); i++ {
            if visited[i] {
                continue
            }
            visited[i] = true
            path = append(path, nums[i])
            dfs(path)
            path = path[:len(path)-1]
            visited[i] = false
        }
    }
    
    dfs([]int{})
    return res
}
```

### 3. 岛屿问题类

#### 题目 200. 岛屿数量

```go
func numIslands(grid [][]byte) int {
    if len(grid) == 0 {
        return 0
    }
    
    count := 0
    m, n := len(grid), len(grid[0])
    
    var dfs func(i, j int)
    dfs = func(i, j int) {
        if i < 0 || j < 0 || i >= m || j >= n || grid[i][j] != '1' {
            return
        }
        grid[i][j] = '0'
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    }
    
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == '1' {
                count++
                dfs(i, j)
            }
        }
    }
    
    return count
}
```

### 4. 回溯类问题

#### 题目 39. 组合总和

```go
func combinationSum(candidates []int, target int) [][]int {
    var res [][]int
    
    var dfs func(start int, path []int, sum int)
    dfs = func(start int, path []int, sum int) {
        if sum == target {
            tmp := make([]int, len(path))
            copy(tmp, path)
            res = append(res, tmp)
            return
        }
        if sum > target {
            return
        }
        
        for i := start; i < len(candidates); i++ {
            path = append(path, candidates[i])
            dfs(i, path, sum+candidates[i])
            path = path[:len(path)-1]
        }
    }
    
    dfs(0, []int{}, 0)
    return res
}
```

## Golang DFS 通用模板

根据以上题目，可以总结出 DFS 的通用模板：

### 递归回溯模板

```go
func problemFunction(params) [][]resultType {
    var res [][]resultType
    // 可能需要 visited 数组或其他辅助数据结构
    
    var dfs func(path []resultType, otherParams...)
    dfs = func(path []resultType, otherParams...) {
        // 终止条件
        if meetCondition {
            // 可能需要深拷贝 path
            tmp := make([]resultType, len(path))
            copy(tmp, path)
            res = append(res, tmp)
            return
        }
        
        // 遍历所有可能的选择
        for _, choice := range choices {
            // 剪枝：跳过不满足条件的选项
            if !isValid(choice) {
                continue
            }
            
            // 做选择
            path = append(path, choice)
            markAsVisited(choice)
            
            // 递归
            dfs(path, updatedParams...)
            
            // 撤销选择
            path = path[:len(path)-1]
            markAsUnvisited(choice)
        }
    }
    
    dfs(initialPath, initialParams...)
    return res
}
```

### 网格/矩阵DFS模板

```go
func gridProblem(grid [][]byte) int {
    if len(grid) == 0 {
        return 0
    }
    
    m, n := len(grid), len(grid[0])
    count := 0
    
    var dfs func(i, j int)
    dfs = func(i, j int) {
        // 边界条件
        if i < 0 || j < 0 || i >= m || j >= n || grid[i][j] != targetValue {
            return
        }
        
        // 标记已访问
        grid[i][j] = markedValue
        
        // 向四个方向扩散
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
        
        // 如果需要8个方向，可以加上对角线方向
    }
    
    // 遍历整个网格
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == targetValue {
                count++
                dfs(i, j)
            }
        }
    }
    
    return count
}
```

## 其他经典DFS题目推荐

1. 78. 子集
2. 17. 电话号码的字母组合
3. 79. 单词搜索
4. 207. 课程表 (拓扑排序)
5. 437. 路径总和 III
6. 494. 目标和
7. 695. 岛屿的最大面积
8. 733. 图像渲染
9. 113. 路径总和 II
10. 129. 求根到叶子节点数字和

DFS的关键在于理解递归的思想，明确递归的终止条件，以及在递归前后做好状态的保存和恢复（回溯）。掌握这些模板后，可以解决大部分DFS相关问题。