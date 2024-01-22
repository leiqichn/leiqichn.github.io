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


```
