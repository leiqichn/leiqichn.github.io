---
title: leetcode 1091.二进制矩阵中的最短路径
date: 2023-05-26 23:35:54
modificationDate: 2023 五月 26日 星期五 23:35:54
categories: 
	- leetcode
tags: [二维数组最短路径]
sticky: []
hide: false
category_bar: true
---

[1091. 二进制矩阵中的最短路径 - 力扣（Leetcode）](https://leetcode.cn/problems/shortest-path-in-binary-matrix/description/)
![](../../imgs/Pasted%20image%2020230526235236.png)
DFS 超时版本：
```go
type point struct {
	x int
	y int
}

func shortestPathBinaryMatrix(grid [][]int) int {
	n := len(grid)
	if grid[0][0] == 1 || grid[n-1][n-1] == 1 {
		return -1
	}

	res := 0
	dirs := [][]int{{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}}

	var help func(i, j, tmp int)

	help = func(i, j, tmp int) {
		// 判断是否越界或已经访问过当前节点
		if i < 0 || i >= n || j < 0 || j >= n || grid[i][j] == 1 {
			return
		}

		if i == n-1 && j == n-1 {
			// 当到达终点时，更新res
			if tmp+1 < res || res == 0 {
				res = tmp + 1
			}
			return
		}

		// 将当前点标记为已访问
		grid[i][j] = 1
		tmp++
		for _, item := range dirs {
			x := i + item[0]
			y := j + item[1]
			help(x, y, tmp)
		}
		// 回溯操作，将当前点复原为未访问状态
		grid[i][j] = 0
	}

	help(0, 0, 0)

	if res == 0 {
		return -1
	}
	return res
}

```


BFS，最短路径使用BFS 

```go
type point struct {
	x,y int
}
func shortestPathBinaryMatrix(grid [][]int) int {
	// queue 维护
	m,n := len(grid),len(grid[0])
	visited := make(map[point]int)
	queue := make([]point,0)
	step := 1
	start := point{0,0}
	end := point{m-1,n-1}
	dirs := []point{{-1,0},{1,0},{0,-1},{0,1},{-1,1},{1,1},{-1,-1},{1,-1}}
	// 起点为1 则直接返回
    if grid[0][0] == 1 {
		return -1
	}
	queue = append(queue,start)
	visited[start] = 1

	for len(queue) > 0 {
		size := len(queue)
		// 将当前队列中的所有节点向四周扩散
		for i:=0; i < size; i++{
			cur := queue[0] // 当前cur
			queue = queue[1:] // 切掉当前点
			// 判断是否是终点
			if cur == end {
				return step
			}
			// 遍历八个方向 判断是否符合边界条件
			for _, dir :=range dirs{
				newX := cur.x + dir.x
				newY := cur.y + dir.y
				newPoint := point{newX,newY}
				if newX >=0 && newX < n&& newY >=0 && newY < m && visited[newPoint]==0 && grid[newX][newY]==0 {
					visited[point{newX,newY}] = 1
					queue =append(queue,newPoint)
				}
			}
			
		}
		step++
	}
	// 只能为0 的路径才可以更新到queue  边界控制
	return -1
}

```


**> [1091. 二进制矩阵中的最短路径 - 力扣（Leetcode）](https://leetcode.cn/problems/shortest-path-in-binary-matrix/solutions/1076268/bfszui-duan-lu-jing-wen-ti-bfsdfsde-si-k-ngc5/)### 解题思路**
> 
> 典型的BFS最短路径问题，用DFS也可以求解，但是容易超时。
> 
**> ### 在二维矩阵中搜索，什么时候用BFS，什么时候用DFS？**
> 
> 1.如果只是要找到某一个结果是否存在，那么DFS会更高效。因为DFS会首先把一种可能的情况尝试到底，才会回溯去尝试下一种情况，只要找到一种情况，就可以返回了。但是BFS必须所有可能的情况同时尝试，在找到一种满足条件的结果的同时，也尝试了很多不必要的路径； 2.如果是要找所有可能结果中最短的，那么BFS回更高效。因为DFS是一种一种的尝试，在把所有可能情况尝试完之前，无法确定哪个是最短，所以DFS必须把所有情况都找一遍，才能确定最终答案（DFS的优化就是剪枝，不剪枝很容易超时）。而BFS从一开始就是尝试所有情况，所以只要找到第一个达到的那个点，那就是最短的路径，可以直接返回了，其他情况都可以省略了，所以这种情况下，BFS更高效。
> 
**> ### BFS解法中的visited为什么可以全局使用？**
> 
> BFS是在尝试所有的可能路径，哪个最快到达终点，哪个就是最短。那么每一条路径走过的路不同，visited（也就是这条路径上走过的点）也应该不同，那么为什么visited可以全局使用呢？ 因为我们要找的是最短路径，那么如果在此之前某个点已经在visited中，也就是说有其他路径在小于或等于当前步数的情况下，到达过这个点，证明到达这个点的最短路径已经被找到。那么显然这个点没必要再尝试了，因为即便去尝试了，最终的结果也不会是最短路径了，所以直接放弃这个点即可。