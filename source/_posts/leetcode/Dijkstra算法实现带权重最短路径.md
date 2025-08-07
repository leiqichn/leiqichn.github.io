
---
title: Dijkstra算法实现带权重最短路径
date: 2025-08-07 23:47:53
modificationDate: 2025 八月 7日 星期四 23:47:53
categories: 
	- leetcode
tags: []
sticky: []
published: true
category_bar: true
---

以下是使用 Dijkstra 算法解决带权重最短路径问题的 Golang 实现（以 LeetCode 743 "网络延迟时间" 为例）。该算法通过优先队列（最小堆）高效地寻找单源最短路径：

```go
import (
	"container/heap"
	"math"
)

// 优先队列元素结构
type Item struct {
	node     int // 节点编号
	distance int // 从起点到该节点的距离
	index    int // 在堆中的索引
}

// 优先队列（最小堆）
type PriorityQueue []*Item

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].distance < pq[j].distance
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *PriorityQueue) Push(x interface{}) {
	n := len(*pq)
	item := x.(*Item)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	old[n-1] = nil  // 避免内存泄漏
	item.index = -1 // 标记已移除
	*pq = old[0 : n-1]
	return item
}

// Dijkstra 算法主函数
func networkDelayTime(times [][]int, n int, k int) int {
	// 构建图的邻接表
	graph := make(map[int][][2]int)
	for _, time := range times {
		u, v, w := time[0], time[1], time[2]
		graph[u] = append(graph[u], [2]int{v, w})
	}

	// 初始化距离数组
	dist := make([]int, n+1)
	for i := range dist {
		dist[i] = math.MaxInt32
	}
	dist[k] = 0

	// 初始化优先队列
	pq := make(PriorityQueue, 0)
	heap.Push(&pq, &Item{node: k, distance: 0})

	// Dijkstra 算法核心
	for pq.Len() > 0 {
		item := heap.Pop(&pq).(*Item)
		u := item.node
		d := item.distance

		// 跳过已处理的节点
		if d > dist[u] {
			continue
		}

		// 遍历邻居节点
		for _, edge := range graph[u] {
			v, w := edge[0], edge[1]
			newDist := d + w
			// 发现更短路径
			if newDist < dist[v] {
				dist[v] = newDist
				heap.Push(&pq, &Item{node: v, distance: newDist})
			}
		}
	}

	// 寻找最大距离
	maxTime := 0
	for i := 1; i <= n; i++ {
		if dist[i] == math.MaxInt32 {
			return -1 // 存在不可达节点
		}
		if dist[i] > maxTime {
			maxTime = dist[i]
		}
	}
	return maxTime
}
```

### 算法说明：
1. **图表示**：使用邻接表 `map[int][][2]int` 存储图结构，键为源节点，值为目标节点和权重的二元组
2. **距离数组**：`dist` 数组记录起点到各节点的最短距离，初始化为最大值（除起点为0）
3. **优先队列**：
   - 实现最小堆，按距离排序
   - 初始将起点 (距离=0) 入队
4. **核心流程**：
   - 弹出当前距离最小的节点
   - 若该节点距离已过期则跳过（由于堆不支持修改，可能有多个版本）
   - 遍历邻居节点，若发现更短路径则更新距离并入队
5. **结果处理**：
   - 遍历 `dist` 数组，若有节点不可达（距离仍为最大值）则返回 -1
   - 否则返回最大距离值

### 复杂度分析：
- **时间复杂度**：O(E log V)，其中 E 是边数，V 是节点数（每个边最多入队一次，堆操作 O(log V)）
- **空间复杂度**：O(V + E)（存储图和距离数组）

此实现严格遵循 Dijkstra 算法，适用于解决带非负权重的有向图单源最短路径问题。在 LeetCode 743 中，函数返回使所有节点收到信号所需的时间（即最短路径的最大值），若有节点不可达则返回 -1。