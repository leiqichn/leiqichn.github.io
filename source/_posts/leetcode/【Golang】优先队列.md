
---
title: 【Golang】优先队列
date: 2025-06-18 00:29:57
modificationDate: 2025 六月 18日 星期三 00:29:57
categories: 
	- leetcode
tags: []
sticky: []
published: true
category_bar: true
---

# 优先队列在LeetCode上的经典题目及Golang实现

优先队列（Priority Queue）是一种重要的数据结构，它在很多算法问题中都有广泛应用。以下是LeetCode上一些经典的优先队列题目，以及用Golang实现的解决方案和模板总结。

## 优先队列的Golang实现

在Golang中，我们可以使用`container/heap`包来实现优先队列。首先，我们需要定义一个实现heap.Interface的类型：

```go
import "container/heap"

// 定义一个最小堆
type MinHeap []int

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x interface{}) {
    *h = append(*h, x.(int))
}

func (h *MinHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[0 : n-1]
    return x
}

// 最大堆只需修改Less方法
type MaxHeap []int

func (h MaxHeap) Len() int           { return len(h) }
func (h MaxHeap) Less(i, j int) bool { return h[i] > h[j] } // 改为大于号
func (h MaxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MaxHeap) Push(x interface{}) {
    *h = append(*h, x.(int))
}

func (h *MaxHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[0 : n-1]
    return x
}
```

## 经典题目及实现

### 1. 合并K个升序链表 (LeetCode 23)

```go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

type NodeHeap []*ListNode

func (h NodeHeap) Len() int           { return len(h) }
func (h NodeHeap) Less(i, j int) bool { return h[i].Val < h[j].Val }
func (h NodeHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *NodeHeap) Push(x interface{}) {
    *h = append(*h, x.(*ListNode))
}

func (h *NodeHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[0 : n-1]
    return x
}

func mergeKLists(lists []*ListNode) *ListNode {
    h := &NodeHeap{}
    heap.Init(h)
    
    // 将所有链表的头节点加入堆
    for _, list := range lists {
        if list != nil {
            heap.Push(h, list)
        }
    }
    
    dummy := &ListNode{}
    current := dummy
    
    for h.Len() > 0 {
        node := heap.Pop(h).(*ListNode)
        current.Next = node
        current = current.Next
        
        if node.Next != nil {
            heap.Push(h, node.Next)
        }
    }
    
    return dummy.Next
}
```

### 2. 数组中的第K个最大元素 (LeetCode 215)

```go
func findKthLargest(nums []int, k int) int {
    h := &MinHeap{}
    heap.Init(h)
    
    for _, num := range nums {
        heap.Push(h, num)
        if h.Len() > k {
            heap.Pop(h)
        }
    }
    
    return heap.Pop(h).(int)
}
```

### 3. 前K个高频元素 (LeetCode 347)

```go
type Item struct {
    value int
    count int
}

type PriorityQueue []*Item

func (pq PriorityQueue) Len() int           { return len(pq) }
func (pq PriorityQueue) Less(i, j int) bool { return pq[i].count < pq[j].count } // 最小堆
func (pq PriorityQueue) Swap(i, j int)      { pq[i], pq[j] = pq[j], pq[i] }

func (pq *PriorityQueue) Push(x interface{}) {
    item := x.(*Item)
    *pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
    old := *pq
    n := len(old)
    item := old[n-1]
    *pq = old[0 : n-1]
    return item
}

func topKFrequent(nums []int, k int) []int {
    // 统计频率
    frequency := make(map[int]int)
    for _, num := range nums {
        frequency[num]++
    }
    
    // 创建优先队列
    pq := &PriorityQueue{}
    heap.Init(pq)
    
    // 将元素加入队列
    for value, count := range frequency {
        heap.Push(pq, &Item{value: value, count: count})
        if pq.Len() > k {
            heap.Pop(pq)
        }
    }
    
    // 收集结果
    result := make([]int, k)
    for i := k - 1; i >= 0; i-- {
        result[i] = heap.Pop(pq).(*Item).value
    }
    
    return result
}
```

### 4. 数据流的中位数 (LeetCode 295)

```go
type MedianFinder struct {
    maxHeap *MaxHeap // 存储较小的一半
    minHeap *MinHeap // 存储较大的一半
}

func Constructor() MedianFinder {
    return MedianFinder{
        maxHeap: &MaxHeap{},
        minHeap: &MinHeap{},
    }
}

func (this *MedianFinder) AddNum(num int) {
    // 先加入maxHeap
    heap.Push(this.maxHeap, num)
    
    // 平衡两个堆
    heap.Push(this.minHeap, heap.Pop(this.maxHeap))
    
    if this.maxHeap.Len() < this.minHeap.Len() {
        heap.Push(this.maxHeap, heap.Pop(this.minHeap))
    }
}

func (this *MedianFinder) FindMedian() float64 {
    if this.maxHeap.Len() > this.minHeap.Len() {
        return float64((*this.maxHeap)[0])
    }
    return float64((*this.maxHeap)[0]+(*this.minHeap)[0]) / 2
}
```

## 优先队列解题模板

基于以上题目，可以总结出优先队列的通用解题模板：

1. **定义堆类型**：
   - 实现heap.Interface接口（Len, Less, Swap, Push, Pop方法）
   - 根据需求决定是最小堆还是最大堆（通过Less方法控制）

2. **初始化堆**：
   ```go
   h := &CustomHeap{}
   heap.Init(h)
   ```

3. **使用堆**：
   - 添加元素：`heap.Push(h, element)`
   - 弹出元素：`heap.Pop(h)`
   - 访问堆顶元素（不弹出）：对于最小堆是`h[0]`，注意要先检查长度

4. **常见模式**：
   - 维护一个大小为K的堆（求前K大/小元素）
   - 使用两个堆维护动态数据流的中位数
   - 在贪心算法中使用优先队列选择最优解

## 其他经典优先队列题目

1. 滑动窗口最大值 (LeetCode 239)
2. 任务调度器 (LeetCode 621)
3. 最接近原点的K个点 (LeetCode 973)
4. 重构字符串 (LeetCode 767)
5. 网络延迟时间 (LeetCode 743)

优先队列是解决许多复杂问题的有力工具，特别是在需要动态获取最大/最小元素或前K个元素的场景中。掌握其实现和应用模式对算法面试非常有帮助。