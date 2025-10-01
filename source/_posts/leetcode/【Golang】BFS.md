---
title: 【Golang】BFS
date: 2025-06-18 00:12:10
modificationDate: 2025 六月 18日 星期三 00:12:10
categories: 
	- leetcode
tags: []
sticky: []
published: true
category_bar: true
---

# LeetCode BFS 练习题单与模板总结 (Golang 实现)

BFS（广度优先搜索）是一种重要的图遍历算法，特别适合解决最短路径、层次遍历等问题。以下是 Golang 实现的 BFS 模板和分类练习题单。

## BFS 通用模板 (Golang)

### 1. 树的 BFS 模板

```go
type TreeNode struct {
    Val   int
    Left  *TreeNode
    Right *TreeNode
}

func levelOrder(root *TreeNode) [][]int {
    if root == nil {
        return [][]int{}
    }
    
    var result [][]int
    queue := []*TreeNode{root}
    
    for len(queue) > 0 {
        levelSize := len(queue)
        currentLevel := make([]int, 0, levelSize)
        
        for i := 0; i < levelSize; i++ {
            node := queue[0]
            queue = queue[1:]
            currentLevel = append(currentLevel, node.Val)
            
            if node.Left != nil {
                queue = append(queue, node.Left)
            }
            if node.Right != nil {
                queue = append(queue, node.Right)
            }
        }
        
        result = append(result, currentLevel)
    }
    
    return result
}
```

### 2. 图的 BFS 模板

```go
func bfsGraph(start Node) []Node {
    visited := make(map[Node]bool)
    visited[start] = true
    queue := []Node{start}
    result := []Node{}
    
    for len(queue) > 0 {
        node := queue[0]
        queue = queue[1:]
        result = append(result, node)
        
        for _, neighbor := range getNeighbors(node) {
            if !visited[neighbor] {
                visited[neighbor] = true
                queue = append(queue, neighbor)
            }
        }
    }
    
    return result
}
```

## LeetCode BFS 练习题单 (Golang)

### 基础练习

1. **二叉树的层次遍历**
   - [102. 二叉树的层序遍历](https://leetcode.com/problems/binary-tree-level-order-traversal/)
   - [107. 二叉树的层次遍历 II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)
   - [637. 二叉树的层平均值](https://leetcode.com/problems/average-of-levels-in-binary-tree/)
   - [429. N叉树的层序遍历](https://leetcode.com/problems/n-ary-tree-level-order-traversal/)

2. **简单图/BFS应用**
   - [200. 岛屿数量](https://leetcode.com/problems/number-of-islands/)
   - [733. 图像渲染](https://leetcode.com/problems/flood-fill/)
   - [559. N叉树的最大深度](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)

### 进阶练习

1. **最短路径问题**
   - [111. 二叉树的最小深度](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
   - [752. 打开转盘锁](https://leetcode.com/problems/open-the-lock/)
   - [1091. 二进制矩阵中的最短路径](https://leetcode.com/problems/shortest-path-in-binary-matrix/)
   - [542. 01 矩阵](https://leetcode.com/problems/01-matrix/)

2. **复杂图/BFS应用**
   - [127. 单词接龙](https://leetcode.com/problems/word-ladder/)
   - [133. 克隆图](https://leetcode.com/problems/clone-graph/)
   - [310. 最小高度树](https://leetcode.com/problems/minimum-height-trees/)

3. **多源BFS**
   - [994. 腐烂的橘子](https://leetcode.com/problems/rotting-oranges/)
   - [286. 墙与门](https://leetcode.com/problems/walls-and-gates/) (付费题)

### 困难级别挑战

1. [815. 公交路线](https://leetcode.com/problems/bus-routes/)
2. [864. 获取所有钥匙的最短路径](https://leetcode.com/problems/shortest-path-to-get-all-keys/)
3. [1293. 网格中的最短路径](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/)

## Golang BFS 实现技巧

1. **队列实现**：Golang 中可以用 slice 实现队列，但要注意 dequeue 操作是 O(n)
   ```go
   // 入队
   queue = append(queue, node)
   
   // 出队
   node := queue[0]
   queue = queue[1:] // 这会创建新的 slice，可能影响性能
   ```

2. **性能优化**：对于大型队列，可以使用链表或固定大小的循环队列
   ```go
   type Queue struct {
       nodes []*TreeNode
       head  int
       tail  int
       count int
   }
   ```

3. **visited 记录**：对于图问题，使用 map 记录已访问节点
   ```go
   visited := make(map[*Node]bool)
   ```

4. **方向数组**：处理网格问题时很有用
   ```go
   dirs := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
   ```

## 示例题解：200. 岛屿数量 (Golang)

```go
func numIslands(grid [][]byte) int {
    if len(grid) == 0 {
        return 0
    }
    
    m, n := len(grid), len(grid[0])
    count := 0
    dirs := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
    
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == '1' {
                count++
                grid[i][j] = '0'
                queue := [][]int{{i, j}}
                
                for len(queue) > 0 {
                    cell := queue[0]
                    queue = queue[1:]
                    
                    for _, dir := range dirs {
                        x, y := cell[0]+dir[0], cell[1]+dir[1]
                        if x >= 0 && x < m && y >= 0 && y < n && grid[x][y] == '1' {
                            grid[x][y] = '0'
                            queue = append(queue, []int{x, y})
                        }
                    }
                }
            }
        }
    }
    
    return count
}
```