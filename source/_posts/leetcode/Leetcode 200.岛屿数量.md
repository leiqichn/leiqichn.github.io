---
title: Leetcode 200.岛屿数量
date: 2023-05-11 01:02:51
modificationDate: 2023 五月 11日 星期四 01:03:17
categories: 
	- leetcode
tags: [图遍历，岛屿问题]
sticky: []
hide: false
category_bar: true
---

[200. 岛屿数量 - 力扣（Leetcode）](https://leetcode.cn/problems/number-of-islands/description/)
![](../../imgs/Pasted%20image%2020230511010424.png)

```go

// 1 岛屿，0 海水， 见到岛屿则使用dfs 淹了这个所有1相连的岛屿，res++
func numIslands(grid [][]byte) int {
	res := 0
	r := len(grid)
	c := len(grid[0])
	visited := make([][]byte, r)
	for i := 0; i < r; i++ {
		visited[i] = make([]byte, c)
	}

	// 遍历二维slice
	for i := 0; i < r; i++ {
		for j := 0; j < c; j++ {
			// 每个位置
            if grid[i][j] == '1' {
                dfs(grid, i, j, visited)
                res++
            }
		}
	}
    return res
}

func dfs(grid [][]byte, i int, j int, visited [][]byte) {
	r := len(grid)
	c := len(grid[0])

	// 边界判断
	if i < 0 || j < 0 || i >= r || j >= c {
		return
	}

	// 判断值，是海水直接返回
	if grid[i][j] == '0' {
		return
	}
    // 判断是否走过
	if visited[i][j] == '1' {
		return
	}

	// 改变状态为海水,并修改为走过
	grid[i][j] = '0'
    visited[i][j] = '1'
	//单层递归逻辑，四面八方递归
	dfs(grid, i+1, j, visited)
	dfs(grid, i, j+1, visited)
	dfs(grid, i-1, j, visited)
	dfs(grid, i, j-1, visited)
}
```


也可以使用方向二维数组来遍历

可以使用二维切片dirs表示方向变化值，将每个递归调用拆分为多个方向，并在循环中使用方向切片来更新i和j的值。示例如下：


```go
func dfs(grid [][]byte, i int, j int, visited [][]byte) {
    r := len(grid)
    c := len(grid[0])

    // 定义方向变化值dirs
    dirs := [][]int{{1,0}, {-1,0}, {0,1}, {0,-1}}

    // 边界判断
    if i < 0 || j < 0 || i >= r || j >= c {
        return
    }

    // 判断值，是海水直接返回
    if grid[i][j] == '0' {
        return
    }

    // 判断是否走过
    if visited[i][j] == '1' {
        return
    }

    // 改变状态为海水,并修改为走过
    grid[i][j] = '0'
    visited[i][j] = '1'

    // 循环遍历dirs，对四个方向进行递归
    for _, d := range dirs {
        new_i, new_j := i + d[0], j + d[1]
        dfs(grid, new_i, new_j, visited)
    }
}
```

在上述示例代码中，我们定义了二维切片dirs，它保存了四个元素，分别代表四个方向的横向(x方向)和纵向(y方向)跨度。在dfs函数内部，我们遍历了dirs，并使用d[0]和d[1]来更新当前的i和j值。这样就可以对每个方向进行递归了。

需要注意的是，如上所述，使用dirs表示方向变化会稍微增加代码的复杂性，但它还可以使函数更灵活，并在处理其他需要迭代解决问题时提供帮助。