---
title: 代码随想录 day51 第十一章 图论part02
date: 2024-12-23 01:34:38
modificationDate: 2024 十二月 23日 星期一 01:34:38
categories: 
	- carl
tags: []
sticky: []
hide: true
category_bar: true
---

# 第十一章：图论part02

# 99.  岛屿数量 深搜

注意深搜的两种写法，熟练掌握这两种写法 以及 知道区别在哪里，才算掌握的深搜。

[https://www.programmercarl.com/kamacoder/0099.%E5%B2%9B%E5%B1%BF%E7%9A%84%E6%95%B0%E9%87%8F%E6%B7%B1%E6%90%9C.html](https://www.programmercarl.com/kamacoder/0099.%E5%B2%9B%E5%B1%BF%E7%9A%84%E6%95%B0%E9%87%8F%E6%B7%B1%E6%90%9C.html)

# 99.  岛屿数量 广搜

注意广搜的两种写法，第一种写法为什么会超时， 如果自己做的录友，题目通过了，也要仔细看第一种写法的超时版本，弄清楚为什么会超时，因为你第一次 幸运 没那么想，第二次可就不一定了。

[https://www.programmercarl.com/kamacoder/0099.%E5%B2%9B%E5%B1%BF%E7%9A%84%E6%95%B0%E9%87%8F%E5%B9%BF%E6%90%9C.html](https://www.programmercarl.com/kamacoder/0099.%E5%B2%9B%E5%B1%BF%E7%9A%84%E6%95%B0%E9%87%8F%E5%B9%BF%E6%90%9C.html)

```go

package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
    "strings"
)

var dir = [4][2]int{{0, 1}, {1, 0}, {-1, 0}, {0, -1}} // 四个方向

func dfs(grid [][]int, visited [][]bool, x, y int) {
    for i := 0; i < 4; i++ {
        nextx := x + dir[i][0]
        nexty := y + dir[i][1]
        if nextx < 0 || nextx >= len(grid) || nexty < 0 || nexty >= len(grid[0]) {
            continue // 越界了，直接跳过
        }
        if !visited[nextx][nexty] && grid[nextx][nexty] == 1 { // 没有访问过的 同时 是陆地的
            visited[nextx][nexty] = true
            dfs(grid, visited, nextx, nexty)
        }
    }
}

func main() {
    reader := bufio.NewReader(os.Stdin)
    var n, m int
    fmt.Scanf("%d %d", &n, &m)

    grid := make([][]int, n)
    for i := 0; i < n; i++ {
        grid[i] = make([]int, m)
        line, _ := reader.ReadString('\n')
        line = strings.TrimSpace(line)
        elements := strings.Split(line, " ")
        for j := 0; j < m; j++ {
            grid[i][j], _ = strconv.Atoi(elements[j])
        }
    }

    visited := make([][]bool, n)
    for i := 0; i < n; i++ {
        visited[i] = make([]bool, m)
    }

    result := 0
    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            if !visited[i][j] && grid[i][j] == 1 {
                visited[i][j] = true
                result++ // 遇到没访问过的陆地，+1
                dfs(grid, visited, i, j) // 将与其链接的陆地都标记上 true
            }
        }
    }

    fmt.Println(result)
}

```

# 100.  岛屿的最大面积

本题就是基础题了，做过上面的题目，本题很快。

[https://www.programmercarl.com/kamacoder/0100.%E5%B2%9B%E5%B1%BF%E7%9A%84%E6%9C%80%E5%A4%A7%E9%9D%A2%E7%A7%AF.html](https://www.programmercarl.com/kamacoder/0100.%E5%B2%9B%E5%B1%BF%E7%9A%84%E6%9C%80%E5%A4%A7%E9%9D%A2%E7%A7%AF.html)



```go

package main

import (
	"fmt"
)

var count int
var dir = [][]int{{0, 1}, {1, 0}, {-1, 0}, {0, -1}} // 四个方向

func dfs(grid [][]int, visited [][]bool, x, y int) {
	for i := 0; i < 4; i++ {
		nextx := x + dir[i][0]
		nexty := y + dir[i][1]
		if nextx < 0 || nextx >= len(grid) || nexty < 0 || nexty >= len(grid[0]) {
			continue // 越界了，直接跳过
		}
		if !visited[nextx][nexty] && grid[nextx][nexty] == 1 { // 没有访问过的 同时 是陆地的
			visited[nextx][nexty] = true
			count++
			dfs(grid, visited, nextx, nexty)
		}
	}
}

func main() {
	var n, m int
	fmt.Scan(&n, &m)

	grid := make([][]int, n)
	for i := 0; i < n; i++ {
		grid[i] = make([]int, m)
		for j := 0; j < m; j++ {
			fmt.Scan(&grid[i][j])
		}
	}

	visited := make([][]bool, n)
	for i := 0; i < n; i++ {
		visited[i] = make([]bool, m)
	}

	result := 0
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if !visited[i][j] && grid[i][j] == 1 {
				count = 1 // 因为dfs处理下一个节点，所以这里遇到陆地了就先计数，dfs处理接下来的相邻陆地
				visited[i][j] = true
				dfs(grid, visited, i, j)
				if count > result {
					result = count
				}
			}
		}
	}

	fmt.Println(result)
}

```
