---
title: go语言实现优先队列
date: 2024-05-19 00:39:54
modificationDate: 2024 五月 19日 星期日 00:39:54
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---

Go 语言中实现优先队列，最大堆和最小堆通常可以通过使用容器/heap包来完成。Go 语言的heap包提供了一个堆操作的接口，它允许用户实现任意类型的堆，包括最大堆和最小堆。

### 1. 优先队列
优先队列是一种特殊的队列，元素出队顺序是根据优先级来决定的，而不是按照元素入队顺序。在Go语言中，优先队列可以通过heap包来实现。

### 2. 最大堆
最大堆是一种特殊的完全二叉树，其中每个父节点的值都大于或等于其子节点的值。在Go语言中，可以通过实现heap.Interface接口来创建最大堆。

### 3. 最小堆
最小堆与最大堆相反，其中每个父节点的值都小于或等于其子节点的值。最小堆也可以通过实现heap.Interface接口来创建。

### 实现步骤

#### 定义堆的元素类型
首先，你需要定义一个元素类型，这个类型将用于存储在堆中的元素。

```go
type IntHeap []int
```

#### 实现heap.Interface接口
要使用heap包的功能，你需要实现heap.Interface接口。这个接口包括三个方法：Push, Pop, 和 Less。

```go

type IntHeap []int
func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] } // 对于最小堆
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}
```


#### 使用heap.Init初始化堆
在使用堆之前，你需要调用heap.Init来初始化它。

```go
var h IntHeap // 先声明h

heap.Init(&h) // 再使用heap.Init(&h) 初始化h指针
```

#### 添加元素
使用heap.Push来添加元素。

```go
heap.Push(&h, 10)
heap.Push(&&h, 20)
```

#### 移除元素
使用heap.Pop来移除并获取堆顶元素。

```go
top := heap.Pop(&h)
fmt.Printf("top element: %v\n", top)
```

#### 修改元素
如果你需要修改堆中的元素，你需要自己处理，因为heap包不提供修改元素的接口。

### 转换为最大堆
如果你需要实现最大堆，只需要修改Less方法，让它返回父节点大于子节点。

```go
func (h IntHeap) Less(i, j int) bool { return h[i] > h[j] } // 对于最大堆
```

以上就是在Go语言中实现优先队列，最大堆和最小堆的基本步骤。通过实现heap.Interface接口，可以轻松地创建和管理各种类型的堆。

# 结构体 优先队列



```go

type Item struct {
    Value    string
    Priority int
    Index    int // 堆中的索引
}

type PriorityQueue []*Item

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
    // 优先值大的先出（最大堆）
    return pq[i].Priority > pq[j].Priority
}

func (pq PriorityQueue) Swap(i, j int) {
    pq[i], pq[j] = pq[j], pq[i]
    pq[i].Index = i
    pq[j].Index = j
}

func (pq *PriorityQueue) Push(x any) {
    n := len(*pq)
    item := x.(*Item)
    item.Index = n
    *pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() any {
    old := *pq
    n := len(old)
    item := old[n-1]
    old[n-1] = nil  // 避免内存泄漏
    item.Index = -1 // 标记已移除
    *pq = old[0 : n-1]
    return item
}

// 更新元素的优先级
func (pq *PriorityQueue) Update(item *Item, value string, priority int) {
    item.Value = value
    item.Priority = priority
    heap.Fix(pq, item.Index)
}

```


# 例题
[215. 数组中的第K个最大元素 - 力扣（LeetCode）](https://leetcode.cn/problems/kth-largest-element-in-an-array/description/?envType=problem-list-v2&envId=IAmiWIlN)

![](../../imgs/Pasted%20image%2020240520000338.png)

```go

/*
 * Copyright (c) 2024 Lei Qi. All rights reserved.
 * Author: Lei Qi
 * Description:
 * Date: 2024/5/20 上午12:00
 */

package leetcode215

import "container/heap"

func findKthLargest(nums []int, k int) int {
	h := heapify(nums) // 转化为heap 类型
	var res any
	for i := 0; i < k; i++ {
		res = heap.Pop(&h)
	}
	return res.(int)
}

type BigHeap []int

func (h BigHeap) Len() int { return len(h) }
func (h BigHeap) Less(i, j int) bool {
	// 大根堆
	return h[i] > h[j]
}

func (h BigHeap) Swap(i, j int) {
	tmp := h[i]
	h[i] = h[j]
	h[j] = tmp
}
func (h *BigHeap) Push(x any) { // 使用any 或者interface
	*h = append(*h, x.(int))
}

// 删除元素待定
func (h *BigHeap) Pop() any {
	x := (*h)[h.Len()-1]
	*h = (*h)[:h.Len()-1]
	return x
}

// 将 nums 转换成 BigHeap
func heapify(nums []int) BigHeap {

    h := BigHeap(nums) // bigHeap 本身就是slice 的别名，所以可以转换
    // 或者使用下边两行
	h := make(BigHeap, len(nums)) // 新建BigHeap，长度为lenNums
	copy(h, nums)                 // 将num copy 到 BigHeap 中去
	heap.Init(&h)                 // 需要输入指针
	return h
}


```

# [347. 前 K 个高频元素](https://leetcode.cn/problems/top-k-frequent-elements/)
![](../../imgs/Pasted%20image%2020240521004343.png)


涉及到两个元素，先构建一个长度为2的数组，然后对其value 进行优先队列的排序
```go

//方法一：小顶堆
func topKFrequent(nums []int, k int) []int {
    map_num:=map[int]int{}
    //记录每个元素出现的次数
    for _,item:=range nums{
        map_num[item]++
    }
    h:=&IHeap{}
    heap.Init(h)
    //所有元素入堆，堆的长度为k
    for key,value:=range map_num{
        heap.Push(h,[2]int{key,value})
        if h.Len()>k{
            heap.Pop(h)
        }
    }
    res:=make([]int,k)

    //按顺序返回堆中的元素
    for i:=0;i<k;i++{
        res[k-i-1]=heap.Pop(h).([2]int)[0]
    }
    return res
}

//构建小顶堆
type IHeap [][2]int

func (h IHeap) Len()int {
    return len(h)
}

func (h IHeap) Less (i,j int) bool {
    return h[i][1]<h[j][1]
}

func (h IHeap) Swap(i,j int) {
    h[i],h[j]=h[j],h[i]
}

func (h *IHeap) Push(x interface{}){
    *h=append(*h,x.([2]int))
}
func (h *IHeap) Pop() interface{}{
    old:=*h
    n:=len(old)
    x:=old[n-1]
    *h=old[0:n-1]
    return x
}



```
