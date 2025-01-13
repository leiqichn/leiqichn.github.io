
---
title: TODO 代码随想录 day11 第五章 栈与队列part02
date: 2024-11-10 21:43:44
modificationDate: 2024 November 10th Sunday 21:43:44
categories: 
	- carl
tags: []
sticky: []
hide: true
category_bar: true
---


### 150. 逆波兰表达式求值

本题不难，但第一次做的话，会很难想到，所以先看视频，了解思路再去做题

题目链接/文章讲解/视频讲解：[https://programmercarl.com/0150.%E9%80%86%E6%B3%A2%E5%85%B0%E8%A1%A8%E8%BE%BE%E5%BC%8F%E6%B1%82%E5%80%BC.html](https://programmercarl.com/0150.%E9%80%86%E6%B3%A2%E5%85%B0%E8%A1%A8%E8%BE%BE%E5%BC%8F%E6%B1%82%E5%80%BC.html)


思路：
不从后序表达式来考虑。从栈的角度，消消乐游戏的角度来考虑也是可以的。


```go
func evalRPN(tokens []string) int {
	stack := []int{}
	for _, token := range tokens {
		val, err := strconv.Atoi(token)
		if err == nil {
			stack = append(stack, val)
		} else {   // 如果err不为nil说明不是数字
			num1, num2 := stack[len(stack)-2], stack[(len(stack))-1]
			stack = stack[:len(stack)-2]
			switch token {
			case "+":
				stack = append(stack, num1+num2)
			case "-":
				stack = append(stack, num1-num2)
			case "*":
				stack = append(stack, num1*num2)
			case "/":
				stack = append(stack, num1/num2)
			}
		}
	}
	return stack[0]
}

```

### 239. 滑动窗口最大值 （有点难度，可能代码写不出来，但一刷至少需要理解思路）

之前讲的都是栈的应用，这次该是队列的应用了。

本题算比较有难度的，需要自己去构造单调队列，建议先看视频来理解。

题目链接/文章讲解/视频讲解：[https://programmercarl.com/0239.%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E6%9C%80%E5%A4%A7%E5%80%BC.html](https://programmercarl.com/0239.%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E6%9C%80%E5%A4%A7%E5%80%BC.html)

思路： 需要构造单调队列。比较难。

这这题想到需要如何使用大顶堆和小顶堆。

```go
// 封装单调队列的方式解题
type MyQueue struct {
    queue []int
}

func NewMyQueue() *MyQueue {
    return &MyQueue{
        queue: make([]int, 0),
    }
}

func (m *MyQueue) Front() int {
    return m.queue[0]
}

func (m *MyQueue) Back() int {
    return m.queue[len(m.queue)-1]
}

func (m *MyQueue) Empty() bool {
    return len(m.queue) == 0
}

func (m *MyQueue) Push(val int) {
    for !m.Empty() && val > m.Back() {
        m.queue = m.queue[:len(m.queue)-1]
    }
    m.queue = append(m.queue, val)
}

func (m *MyQueue) Pop(val int) {
    if !m.Empty() && val == m.Front() {
        m.queue = m.queue[1:]
    }
}

func maxSlidingWindow(nums []int, k int) []int {
    queue := NewMyQueue()
    length := len(nums)
    res := make([]int, 0)
    // 先将前k个元素放入队列
    for i := 0; i < k; i++ {
        queue.Push(nums[i])
    }
    // 记录前k个元素的最大值
    res = append(res, queue.Front())

    for i := k; i < length; i++ {
        // 滑动窗口移除最前面的元素
        queue.Pop(nums[i-k])
        // 滑动窗口添加最后面的元素
        queue.Push(nums[i])
        // 记录最大值
        res = append(res, queue.Front())
    }
    return res
}

```

### 347.前 K 个高频元素 （有点难度，可能代码写不出来，一刷至少需要理解思路）

大/小顶堆的应用， 在C++中就是优先级队列

本题是 大数据中取前k值 的经典思路，了解想法之后，不算难。

题目链接/文章讲解/视频讲解：[https://programmercarl.com/0347.%E5%89%8DK%E4%B8%AA%E9%AB%98%E9%A2%91%E5%85%83%E7%B4%A0.html](https://programmercarl.com/0347.%E5%89%8DK%E4%B8%AA%E9%AB%98%E9%A2%91%E5%85%83%E7%B4%A0.html)

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
type IHeap [][2]int // 这里是什么意思？

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

### 总结

栈与队列做一个总结吧，加油

[https://programmercarl.com/%E6%A0%88%E4%B8%8E%E9%98%9F%E5%88%97%E6%80%BB%E7%BB%93.html](https://programmercarl.com/%E6%A0%88%E4%B8%8E%E9%98%9F%E5%88%97%E6%80%BB%E7%BB%93.html)