---
title: 代码随想录 day52 第十一章 图论part03
date: 2024-12-23 01:35:07
modificationDate: 2024 十二月 23日 星期一 01:35:07
categories: 
	- carl
tags: []
sticky: []
hide: true
category_bar: true
---

# 第十一章：图论part03

### 101.  孤岛的总面积

基础题目 可以自己尝试做一做 。

[https://www.programmercarl.com/kamacoder/0101.%E5%AD%A4%E5%B2%9B%E7%9A%84%E6%80%BB%E9%9D%A2%E7%A7%AF.html](https://www.programmercarl.com/kamacoder/0101.%E5%AD%A4%E5%B2%9B%E7%9A%84%E6%80%BB%E9%9D%A2%E7%A7%AF.html)

```go

package main

import (
    "fmt"
)

var count int
var dir = [4][2]int{{0, 1}, {1, 0}, {-1, 0}, {0, -1}} // 四个方向

func bfs(grid [][]int, x, y int) {
    queue := [][2]int{{x, y}}
    grid[x][y] = 0 // 只要加入队列，立刻标记
    count++
    
    for len(queue) > 0 {
        cur := queue[0]
        queue = queue[1:]
        curx, cury := cur[0], cur[1]
        
        for i := 0; i < 4; i++ {
            nextx := curx + dir[i][0]
            nexty := cury + dir[i][1]
            
            if nextx < 0 || nextx >= len(grid) || nexty < 0 || nexty >= len(grid[0]) {
                continue // 越界了，直接跳过
            }
            
            if grid[nextx][nexty] == 1 {
                queue = append(queue, [2]int{nextx, nexty})
                count++
                grid[nextx][nexty] = 0 // 只要加入队列立刻标记
            }
        }
    }
}

func main() {
    var n, m int
    fmt.Scan(&n, &m)
    
    grid := make([][]int, n)
    for i := range grid {
        grid[i] = make([]int, m)
    }
    
    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            fmt.Scan(&grid[i][j])
        }
    }
    
    // 从左侧边，和右侧边向中间遍历
    for i := 0; i < n; i++ {
        if grid[i][0] == 1 {
            bfs(grid, i, 0)
        }
        if grid[i][m-1] == 1 {
            bfs(grid, i, m-1)
        }
    }
    
    // 从上边和下边向中间遍历
    for j := 0; j < m; j++ {
        if grid[0][j] == 1 {
            bfs(grid, 0, j)
        }
        if grid[n-1][j] == 1 {
            bfs(grid, n-1, j)
        }
    }
    
    // 清空之前的计数
    count = 0
    
    // 遍历所有位置
    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            if grid[i][j] == 1 {
                bfs(grid, i, j)
            }
        }
    }
    
    fmt.Println(count)
}



```

### 102.  沉没孤岛

和上一题差不多，尝试自己做做

[https://www.programmercarl.com/kamacoder/0102.%E6%B2%89%E6%B2%A1%E5%AD%A4%E5%B2%9B.html](https://www.programmercarl.com/kamacoder/0102.%E6%B2%89%E6%B2%A1%E5%AD%A4%E5%B2%9B.html)

### 103.  水流问题

需要点优化思路，建议先自己读题，相处一个解题方法，有时间就自己写代码，没时间就直接看题解，优化方式 会让你 耳目一新。

[https://www.programmercarl.com/kamacoder/0103.%E6%B0%B4%E6%B5%81%E9%97%AE%E9%A2%98.html](https://www.programmercarl.com/kamacoder/0103.%E6%B0%B4%E6%B5%81%E9%97%AE%E9%A2%98.html)

### 104.建造最大岛屿

同样优化思路也会让你耳目一新，自己想比较难想出来。

[https://www.programmercarl.com/kamacoder/0104.%E5%BB%BA%E9%80%A0%E6%9C%80%E5%A4%A7%E5%B2%9B%E5%B1%BF.html](https://www.programmercarl.com/kamacoder/0104.%E5%BB%BA%E9%80%A0%E6%9C%80%E5%A4%A7%E5%B2%9B%E5%B1%BF.html)