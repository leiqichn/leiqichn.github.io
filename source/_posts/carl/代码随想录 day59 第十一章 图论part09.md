---
title: 代码随想录 day59 第十一章 图论part09
date: 2025-01-05 22:02:10
modificationDate: 2025 一月 5日 星期日 22:02:10
categories: 
	- carl
tags: []
sticky: []
published: false
category_bar: true
---

# 第十一章：图论part09

今天的建议依然是，一刷的时候，能了解 原理，照着代码随想录能抄下来代码就好，就算达标。

二刷的时候自己尝试独立去写，三刷的时候 才能有一定深度理解各个最短路算法。

### dijkstra（堆优化版）精讲

https://www.programmercarl.com/kamacoder/0047.%E5%8F%82%E4%BC%9Adijkstra%E5%A0%86.html

```go

package main

import (
    "container/heap"
    "fmt"
    "math"
)

// Edge 表示带权重的边
type Edge struct {
    to, val int
}

// PriorityQueue 实现一个小顶堆
type Item struct {
    node, dist int
}

type PriorityQueue []*Item

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
    return pq[i].dist < pq[j].dist
}

func (pq PriorityQueue) Swap(i, j int) {
    pq[i], pq[j] = pq[j], pq[i]
}

func (pq *PriorityQueue) Push(x interface{}) {
    *pq = append(*pq, x.(*Item))
}

func (pq *PriorityQueue) Pop() interface{} {
    old := *pq
    n := len(old)
    item := old[n-1]
    *pq = old[0 : n-1]
    return item
}

func dijkstra(n, m int, edges [][]int, start, end int) int {
    grid := make([][]Edge, n+1)
    for _, edge := range edges {
        p1, p2, val := edge[0], edge[1], edge[2]
        grid[p1] = append(grid[p1], Edge{to: p2, val: val})
    }

    minDist := make([]int, n+1)
    for i := range minDist {
        minDist[i] = math.MaxInt64
    }
    visited := make([]bool, n+1)

    pq := &PriorityQueue{}
    heap.Init(pq)
    heap.Push(pq, &Item{node: start, dist: 0})
    minDist[start] = 0

    for pq.Len() > 0 {
        cur := heap.Pop(pq).(*Item)

        if visited[cur.node] {
            continue
        }

        visited[cur.node] = true

        for _, edge := range grid[cur.node] {
            if !visited[edge.to] && minDist[cur.node]+edge.val < minDist[edge.to] {
                minDist[edge.to] = minDist[cur.node] + edge.val
                heap.Push(pq, &Item{node: edge.to, dist: minDist[edge.to]})
            }
        }
    }

    if minDist[end] == math.MaxInt64 {
        return -1
    }
    return minDist[end]
}

func main() {
    var n, m int
    fmt.Scan(&n, &m)

    edges := make([][]int, m)
    for i := 0; i < m; i++ {
        var p1, p2, val int
        fmt.Scan(&p1, &p2, &val)
        edges[i] = []int{p1, p2, val}
    }

    start := 1  // 起点
    end := n    // 终点

    result := dijkstra(n, m, edges, start, end)
    fmt.Println(result)
}


```

### Bellman_ford 算法精讲

https://www.programmercarl.com/kamacoder/0094.%E5%9F%8E%E5%B8%82%E9%97%B4%E8%B4%A7%E7%89%A9%E8%BF%90%E8%BE%93I.html



```python

def main():
    n, m = map(int, input().strip().split())
    edges = []
    for _ in range(m):
        src, dest, weight = map(int, input().strip().split())
        edges.append([src, dest, weight])
    
    minDist = [float("inf")] * (n + 1)
    minDist[1] = 0  # 起点处距离为0
    
    for i in range(1, n):
        updated = False
        for src, dest, weight in edges:
            if minDist[src] != float("inf") and minDist[src] + weight < minDist[dest]:
                minDist[dest] = minDist[src] + weight
                updated = True
        if not updated:  # 若边不再更新，即停止回圈
            break
    
    if minDist[-1] == float("inf"):  # 返还终点权重
        return "unconnected"
    return minDist[-1]
    
if __name__ == "__main__":
    print(main())

```
