---
title: 【BFS DFS通用模板】
date: 2024-01-23 00:05:29
modificationDate: 2024 一月 23日 星期二 00:05:29
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---

# 深度优先搜索（DFS）通用模板


```go

// 通用的深度优先搜索函数
func dfs(node int, visited []bool, graph [][]int) {
	// 边界终止条件 
	if m n {
	}
    // 终止条件
    if visited[node] {
        return
    }

    // 处理当前节点
    // ...

    // 标记当前节点为已访问
    visited[node] = true

    // 递归处理相邻节点
    for _, neighbor := range graph[node] {
        dfs(neighbor, visited, graph)
    }
}

// 在主函数中调用
func main() {
    // 初始化节点、访问数组等
    // ...

    // 遍历所有节点
    for node := 0; node < len(graph); node++ {
        if !visited[node] {
            dfs(node, visited, graph)
        }
    }
}

```

# 广度优先搜索（BFS）通用模板


```go
// 通用的广度优先搜索函数
func bfs(start int, graph [][]int) {
    queue := []int{start}
    visited := make([]bool, len(graph))

    for len(queue) > 0 {
        // 出队列
        node := queue[0]
        queue = queue[1:]

        // 处理当前节点
        // ...

        // 标记当前节点为已访问
        visited[node] = true

        // 将相邻节点入队列
        for _, neighbor := range graph[node] {
            if !visited[neighbor] {
                queue = append(queue, neighbor)
            }
        }
    }
}

// 在主函数中调用
func main() {
    // 初始化起始节点、图等
    // ...

    // 调用BFS函数
    bfs(start, graph)
}


// 计算从起点 start 到终点 target 的最近距离
func BFS(start Node, target Node) int {
    // 核心数据结构
    q := make([]Node, 0)
    // 避免走回头路
    visited := make(map[Node]bool)
    
    // 将起点加入队列
    q = append(q, start)
    visited[start] = true

    for len(q) > 0 {
        sz := len(q)
        // 将当前队列中的所有节点向四周扩散
        for i := 0; i < sz; i++ {
            cur := q[0]
            q = q[1:]
            // 划重点：这里判断是否到达终点
            if cur == target {
                return step
            }
            // 将 cur 的相邻节点加入队列
            for _, x := range cur.adj() {
                if _, ok := visited[x]; !ok {
                    q = append(q, x)
                    visited[x] = true
                }
            }
        }
    }
    // 如果走到这里，说明在图中没有找到目标节点
}


```
