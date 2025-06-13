---
title: Golang LeetCode 刷题必备基础和常用模板
date: 2025-06-14 00:03:18
modificationDate: 2025 六月 14日 星期六 00:03:18
categories: 
	- Golang
tags: []
sticky: []
published: true
category_bar: true
---
# Golang LeetCode 刷题必备基础备忘录

## 1. 基础数据结构用法

### 数组/切片 (Slice)
```go
// 初始化
arr := []int{1, 2, 3}
slice := make([]int, 5) // 长度5
slice2 := make([]int, 0, 10) // 长度0，容量10

// 操作
slice = append(slice, 4) // 追加
len(slice) // 长度
copy(dest, src) // 复制
sort.Ints(slice) // 排序
```

### 字符串 (String)
```go
// 基本操作
s := "hello"
len(s) // 字节长度(非字符数)
utf8.RuneCountInString(s) // 字符数
strings.Contains(s, "ell") // true
strings.Split("a,b,c", ",") // ["a","b","c"]
strings.Join([]string{"a","b"}, "-") // "a-b"
strconv.Itoa(123) // "123"
strconv.Atoi("123") // 123, error

// 遍历字符
for i, r := range s { // r是rune类型(Unicode码点)
    fmt.Printf("%d: %c\n", i, r)
}
```

### 映射 (Map)
```go
m := make(map[string]int)
m["key"] = 1
val, exists := m["key"] // exists为bool表示是否存在
delete(m, "key") // 删除键
```

### 链表 (List)
```go
import "container/list"
l := list.New()
l.PushBack(1)
l.PushFront(2)
for e := l.Front(); e != nil; e = e.Next() {
    fmt.Println(e.Value)
}
```

## 2. 常用算法模板

### 二分查找
```go
func binarySearch(nums []int, target int) int {
    left, right := 0, len(nums)-1
    for left <= right {
        mid := left + (right-left)/2
        if nums[mid] == target {
            return mid
        } else if nums[mid] < target {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
    return -1
}
```

### 快速排序
```go
func quickSort(nums []int) {
    if len(nums) <= 1 {
        return
    }
    pivot := nums[0]
    left, right := 0, len(nums)-1
    for i := 1; i <= right; {
        if nums[i] < pivot {
            nums[i], nums[left] = nums[left], nums[i]
            left++
            i++
        } else if nums[i] > pivot {
            nums[i], nums[right] = nums[right], nums[i]
            right--
        } else {
            i++
        }
    }
    quickSort(nums[:left])
    quickSort(nums[right+1:])
}
```

## 3. 标准库重要包

### `sort` 排序包
```go
import "sort"

// 基本类型排序
sort.Ints(arr)
sort.Strings(arr)
sort.Float64s(arr)

// 自定义排序
sort.Slice(people, func(i, j int) bool {
    return people[i].Age < people[j].Age
})
```

### `container/heap` 堆实现
```go
import "container/heap"

// 最小堆示例
type MinHeap []int
func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *MinHeap) Push(x any)        { *h = append(*h, x.(int)) }
func (h *MinHeap) Pop() any {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[:n-1]
    return x
}

// 使用
h := &MinHeap{2, 1, 5}
heap.Init(h)
heap.Push(h, 3)
smallest := heap.Pop(h)
```

### `math` 数学包
```go
import "math"

math.Max(float64, float64)
math.Min(float64, float64)
math.Abs(float64)
math.Pow(x, y float64)
math.Sqrt(float64)
math.Ceil(float64)
math.Floor(float64)
math.MaxInt32 // 常量
math.MinInt32
```

## 4. 并发编程基础

### Goroutine
```go
go func() {
    // 并发执行的代码
}()
```

### Channel
```go
ch := make(chan int, 10) // 缓冲通道
ch <- 1 // 发送
val := <-ch // 接收
close(ch) // 关闭通道

// select多路复用
select {
case v := <-ch1:
    fmt.Println(v)
case ch2 <- 1:
    fmt.Println("sent")
default:
    fmt.Println("default")
}
```

## 5. 常用技巧

### 位运算
```go
n & 1 // 判断奇偶
n >> 1 // 除以2
n << 1 // 乘以2
a ^ b // 异或
a &^ b // 位清除
```

### 常用常量
```go
const INT_MAX = int(^uint(0) >> 1
const INT_MIN = ^INT_MAX
```

### 快速输入输出 (竞赛用)
```go
import (
    "bufio"
    "fmt"
    "os"
)

reader := bufio.NewReader(os.Stdin)
writer := bufio.NewWriter(os.Stdout)
defer writer.Flush()
fmt.Fscan(reader, &a, &b)
fmt.Fprintln(writer, a+b)
```

## 6. 测试用例写法

```go
import "testing"

func TestFunc(t *testing.T) {
    tests := []struct {
        name string
        input int
        want int
    }{
        {"case1", 1, 2},
        {"case2", 2, 4},
    }
    
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            if got := Func(tt.input); got != tt.want {
                t.Errorf("Func() = %v, want %v", got, tt.want)
            }
        })
    }
}
```

## 7. 常见题型解题要点

1. **双指针**：数组/链表问题，滑动窗口
2. **DFS/BFS**：树/图遍历，回溯问题
3. **动态规划**：状态转移方程，备忘录
4. **贪心算法**：局部最优解
5. **并查集**：连通性问题
6. **前缀和/差分数组**：区间查询/更新
7. **单调栈**：下一个更大/小元素问题


## 1. 双指针技巧

### 数组/链表问题模板
```go
// 快慢指针找链表中点
func middleNode(head *ListNode) *ListNode {
    slow, fast := head, head
    for fast != nil && fast.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next
    }
    return slow
}

// 有序数组两数之和
func twoSum(nums []int, target int) []int {
    left, right := 0, len(nums)-1
    for left < right {
        sum := nums[left] + nums[right]
        if sum == target {
            return []int{left, right}
        } else if sum < target {
            left++
        } else {
            right--
        }
    }
    return nil
}
```

### 滑动窗口模板
```go
func slidingWindow(s string) int {
    freq := make(map[byte]int)
    left, maxLen := 0, 0
    
    for right := 0; right < len(s); right++ {
        freq[s[right]]++
        // 窗口收缩条件
        for freq[s[right]] > 1 {
            freq[s[left]]--
            left++
        }
        maxLen = max(maxLen, right-left+1)
    }
    return maxLen
}
```

## 2. DFS/BFS 算法

### 树遍历模板
```go
// DFS 递归遍历
func dfs(root *TreeNode) {
    if root == nil {
        return
    }
    // 前序位置
    dfs(root.Left)
    // 中序位置
    dfs(root.Right)
    // 后序位置
}

// BFS 层序遍历
func bfs(root *TreeNode) [][]int {
    var res [][]int
    if root == nil {
        return res
    }
    queue := []*TreeNode{root}
    for len(queue) > 0 {
        levelSize := len(queue)
        var level []int
        for i := 0; i < levelSize; i++ {
            node := queue[0]
            queue = queue[1:]
            level = append(level, node.Val)
            if node.Left != nil {
                queue = append(queue, node.Left)
            }
            if node.Right != nil {
                queue = append(queue, node.Right)
            }
        }
        res = append(res, level)
    }
    return res
}
```

### 回溯算法模板
```go
func backtrack(nums []int) [][]int {
    var res [][]int
    var path []int
    used := make([]bool, len(nums))
    
    var dfs func()
    dfs = func() {
        if len(path) == len(nums) {
            res = append(res, append([]int{}, path...))
            return
        }
        for i := 0; i < len(nums); i++ {
            if used[i] {
                continue
            }
            used[i] = true
            path = append(path, nums[i])
            dfs()
            path = path[:len(path)-1]
            used[i] = false
        }
    }
    dfs()
    return res
}
```

## 3. 动态规划

### 经典DP模板
```go
// 斐波那契数列 (备忘录)
func fib(n int) int {
    if n <= 1 {
        return n
    }
    dp := make([]int, n+1)
    dp[0], dp[1] = 0, 1
    for i := 2; i <= n; i++ {
        dp[i] = dp[i-1] + dp[i-2]
    }
    return dp[n]
}

// 0-1背包问题
func knapsack(weights []int, values []int, W int) int {
    n := len(weights)
    dp := make([][]int, n+1)
    for i := range dp {
        dp[i] = make([]int, W+1)
    }
    
    for i := 1; i <= n; i++ {
        for w := 1; w <= W; w++ {
            if weights[i-1] > w {
                dp[i][w] = dp[i-1][w]
            } else {
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]]+values[i-1])
            }
        }
    }
    return dp[n][W]
}
```

## 4. 贪心算法

### 区间调度问题
```go
func intervalSchedule(intervals [][]int) int {
    // 按结束时间排序
    sort.Slice(intervals, func(i, j int) bool {
        return intervals[i][1] < intervals[j][1]
    })
    
    count := 1
    end := intervals[0][1]
    for _, interval := range intervals {
        start := interval[0]
        if start >= end {
            count++
            end = interval[1]
        }
    }
    return count
}
```

## 5. 并查集

### 标准实现
```go
type UnionFind struct {
    parent []int
    count  int
}

func NewUnionFind(n int) *UnionFind {
    parent := make([]int, n)
    for i := range parent {
        parent[i] = i
    }
    return &UnionFind{parent, n}
}

func (uf *UnionFind) Find(x int) int {
    for uf.parent[x] != x {
        uf.parent[x] = uf.parent[uf.parent[x]] // 路径压缩
        x = uf.parent[x]
    }
    return x
}

func (uf *UnionFind) Union(x, y int) {
    rootX := uf.Find(x)
    rootY := uf.Find(y)
    if rootX == rootY {
        return
    }
    uf.parent[rootX] = rootY
    uf.count--
}
```

## 6. 前缀和与差分数组

### 前缀和模板
```go
// 一维前缀和
type PrefixSum struct {
    prefix []int
}

func NewPrefixSum(nums []int) *PrefixSum {
    n := len(nums)
    prefix := make([]int, n+1)
    for i := 1; i <= n; i++ {
        prefix[i] = prefix[i-1] + nums[i-1]
    }
    return &PrefixSum{prefix}
}

func (ps *PrefixSum) Query(i, j int) int {
    return ps.prefix[j+1] - ps.prefix[i]
}

// 二维前缀和
type NumMatrix struct {
    prefix [][]int
}

func Constructor(matrix [][]int) NumMatrix {
    if len(matrix) == 0 {
        return NumMatrix{}
    }
    m, n := len(matrix), len(matrix[0])
    prefix := make([][]int, m+1)
    for i := range prefix {
        prefix[i] = make([]int, n+1)
    }
    for i := 1; i <= m; i++ {
        for j := 1; j <= n; j++ {
            prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + matrix[i-1][j-1]
        }
    }
    return NumMatrix{prefix}
}

func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
    return this.prefix[row2+1][col2+1] - this.prefix[row1][col2+1] - this.prefix[row2+1][col1] + this.prefix[row1][col1]
}
```

## 7. 单调栈

### 下一个更大元素
```go
func nextGreaterElements(nums []int) []int {
    n := len(nums)
    res := make([]int, n)
    for i := range res {
        res[i] = -1
    }
    stack := []int{} // 存储索引
    
    for i := 0; i < 2*n; i++ {
        num := nums[i%n]
        for len(stack) > 0 && num > nums[stack[len(stack)-1]] {
            top := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            res[top] = num
        }
        if i < n {
            stack = append(stack, i)
        }
    }
    return res
}
```

### 柱状图中最大矩形
```go
func largestRectangleArea(heights []int) int {
    heights = append(heights, 0) // 哨兵
    stack := []int{-1}           // 哨兵
    maxArea := 0
    
    for i := 0; i < len(heights); i++ {
        for len(stack) > 1 && heights[i] < heights[stack[len(stack)-1]] {
            h := heights[stack[len(stack)-1]]
            stack = stack[:len(stack)-1]
            w := i - stack[len(stack)-1] - 1
            maxArea = max(maxArea, h*w)
        }
        stack = append(stack, i)
    }
    return maxArea
}
```

## 各题型解题要点总结

1. **双指针**：
   - 数组问题：注意有序数组的特殊性质
   - 滑动窗口：明确窗口收缩条件，维护窗口状态

2. **DFS/BFS**：
   - 树遍历：前中后序选择取决于问题需求
   - 回溯：注意状态恢复，剪枝优化

3. **动态规划**：
   - 明确状态定义和转移方程
   - 考虑空间优化（滚动数组）

4. **贪心算法**：
   - 证明贪心选择的正确性
   - 通常需要先排序

5. **并查集**：
   - 路径压缩和按秩合并优化
   - 处理连通分量问题

6. **前缀和/差分**：
   - 前缀和用于快速区间查询
   - 差分数组用于快速区间更新

7. **单调栈**：
   - 维护栈内元素的单调性
   - 用于解决"下一个更大/小元素"类问题
