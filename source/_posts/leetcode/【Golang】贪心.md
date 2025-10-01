
---
title: 【Golang】贪心
date: 2025-06-18 00:33:41
modificationDate: 2025 六月 18日 星期三 00:33:44
categories: 
	- leetcode
tags: []
sticky: []
published: true
category_bar: true
---

# 贪心算法经典题目及Golang实现

贪心算法是一种在每一步选择中都采取当前状态下最优的选择，从而希望导致全局最优解的算法策略。以下是一些LeetCode上经典的贪心算法题目及其Golang实现，并总结一个通用的解题模板。

## 经典贪心题目及Golang实现

### 1. 分发饼干 (455. Assign Cookies)

```go
func findContentChildren(g []int, s []int) int {
    sort.Ints(g)
    sort.Ints(s)
    
    child, cookie := 0, 0
    for child < len(g) && cookie < len(s) {
        if s[cookie] >= g[child] {
            child++
        }
        cookie++
    }
    return child
}
```

### 2. 无重叠区间 (435. Non-overlapping Intervals)

```go
func eraseOverlapIntervals(intervals [][]int) int {
    if len(intervals) == 0 {
        return 0
    }
    
    // 按结束时间排序
    sort.Slice(intervals, func(i, j int) bool {
        return intervals[i][1] < intervals[j][1]
    })
    
    count := 1
    end := intervals[0][1]
    for i := 1; i < len(intervals); i++ {
        if intervals[i][0] >= end {
            count++
            end = intervals[i][1]
        }
    }
    return len(intervals) - count
}
```

### 3. 用最少数量的箭引爆气球 (452. Minimum Number of Arrows to Burst Balloons)

```go
func findMinArrowShots(points [][]int) int {
    if len(points) == 0 {
        return 0
    }
    
    sort.Slice(points, func(i, j int) bool {
        return points[i][1] < points[j][1]
    })
    
    arrows := 1
    pos := points[0][1]
    for i := 1; i < len(points); i++ {
        if points[i][0] > pos {
            arrows++
            pos = points[i][1]
        }
    }
    return arrows
}
```

### 4. 买卖股票的最佳时机 II (122. Best Time to Buy and Sell Stock II)

```go
func maxProfit(prices []int) int {
    profit := 0
    for i := 1; i < len(prices); i++ {
        if prices[i] > prices[i-1] {
            profit += prices[i] - prices[i-1]
        }
    }
    return profit
}
```

### 5. 跳跃游戏 (55. Jump Game)

```go
func canJump(nums []int) bool {
    farthest := 0
    for i := 0; i < len(nums); i++ {
        if i > farthest {
            return false
        }
        farthest = max(farthest, i+nums[i])
    }
    return true
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```

### 6. 跳跃游戏 II (45. Jump Game II)

```go
func jump(nums []int) int {
    jumps, curEnd, farthest := 0, 0, 0
    for i := 0; i < len(nums)-1; i++ {
        farthest = max(farthest, i+nums[i])
        if i == curEnd {
            jumps++
            curEnd = farthest
        }
    }
    return jumps
}
```

### 7. 加油站 (134. Gas Station)

```go
func canCompleteCircuit(gas []int, cost []int) int {
    total, curr, start := 0, 0, 0
    for i := 0; i < len(gas); i++ {
        total += gas[i] - cost[i]
        curr += gas[i] - cost[i]
        if curr < 0 {
            start = i + 1
            curr = 0
        }
    }
    if total >= 0 {
        return start
    }
    return -1
}
```

### 8. 任务调度器 (621. Task Scheduler)

```go
func leastInterval(tasks []byte, n int) int {
    freq := make([]int, 26)
    for _, t := range tasks {
        freq[t-'A']++
    }
    sort.Ints(freq)
    
    maxFreq := freq[25]
    idleSlots := (maxFreq - 1) * n
    
    for i := 24; i >= 0 && freq[i] > 0; i-- {
        idleSlots -= min(freq[i], maxFreq-1)
    }
    
    if idleSlots > 0 {
        return idleSlots + len(tasks)
    }
    return len(tasks)
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
```

## 贪心算法通用模板

虽然贪心算法没有固定的模板，但通常可以遵循以下步骤：

1. **排序**：很多贪心问题需要对输入数据进行排序
2. **初始化**：设置必要的变量（如计数器、指针等）
3. **遍历处理**：遍历排序后的数据，做出贪心选择
4. **验证结果**：检查是否满足题目要求

```go
func greedyAlgorithm(input []Type) ResultType {
    // 1. 排序（如果需要）
    sort.Slice(input, func(i, j int) bool {
        return compare(input[i], input[j])
    })
    
    // 2. 初始化变量
    result := 0
    current := initialValue
    
    // 3. 遍历处理
    for _, item := range input {
        if canMakeGreedyChoice(current, item) {
            // 做出贪心选择
            update(current, item)
            result++
        }
    }
    
    // 4. 返回结果
    return result
}
```

## 贪心算法适用场景

贪心算法通常适用于以下类型的问题：
- 可以分解为子问题的问题
- 子问题的最优解能递推到最终问题的最优解
- 无后效性，即某个状态以后的过程不会影响以前的状态

常见应用场景包括：
- 分配问题（如分发饼干）
- 区间问题（如无重叠区间）
- 调度问题（如任务调度器）
- 股票买卖问题
- 跳跃游戏类问题

贪心算法的关键在于证明贪心策略的正确性，这通常需要数学证明或直观理解。在实际应用中，如果无法确定贪心策略是否正确，可以先尝试，然后验证是否能够得到全局最优解。