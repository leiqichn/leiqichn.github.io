---
title: 代码随想录 day50 第十一章 图论part01
date: 2024-12-23 00:56:29
modificationDate: 2024 十二月 23日 星期一 00:56:29
categories: 
	- carl
tags: []
sticky: []
hide: false
category_bar: true
---



# 第十一章：图论part01

### 图论理论基础

大家可以在看图论理论基础的时候，很多内容 看不懂，例如也不知道 看完之后 还是不知道 邻接矩阵，邻接表怎么用， 别着急。

理论基础大家先对各个概念有个印象就好，后面在刷题的过程中，每个知识点都会得到巩固。

https://www.programmercarl.com/kamacoder/%E5%9B%BE%E8%AE%BA%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html

### 深搜理论基础

了解一下深搜的原理和过程

https://www.programmercarl.com/kamacoder/%E5%9B%BE%E8%AE%BA%E6%B7%B1%E6%90%9C%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html


## 可以使用邻接矩阵来表示图

邻接矩阵 使用 二维数组来表示图结构。 邻接矩阵是从节点的角度来表示图，有多少节点就申请多大的二维数组。

例如： grid[2][5] = 6，表示 节点 2 连接 节点5 为有向图，节点2 指向 节点5，边的权值为6。

如果想表示无向图，即：grid[2][5] = 6，grid[5][2] = 6，表示节点2 与 节点5 相互连通，权值为6。

如图：

![](https://code-thinking-1253855093.file.myqcloud.com/pics/20240222110025.png)

在一个 n （节点数）为8 的图中，就需要申请 8 * 8 这么大的空间。
### 98. 所有可达路径

https://www.programmercarl.com/kamacoder/0098.%E6%89%80%E6%9C%89%E5%8F%AF%E8%BE%BE%E8%B7%AF%E5%BE%84.html


```go

package main

import (
	"fmt"
)

var result [][]int // 收集符合条件的路径
var path []int     // 1节点到终点的路径

func dfs(graph [][]int, x, n int) {
	// 当前遍历的节点x 到达节点n
	if x == n { // 找到符合条件的一条路径
		temp := make([]int, len(path))
		copy(temp, path)
		result = append(result, temp)
		return
	}
	for i := 1; i <= n; i++ { // 遍历节点x链接的所有节点
		if graph[x][i] == 1 { // 找到 x链接的节点
			path = append(path, i)    // 遍历到的节点加入到路径中来
			dfs(graph, i, n)          // 进入下一层递归
			path = path[:len(path)-1] // 回溯，撤销本节点
		}
	}
}

func main() {
	var n, m int
	fmt.Scanf("%d %d", &n, &m)

	// 节点编号从1到n，所以申请 n+1 这么大的数组
	graph := make([][]int, n+1)
	for i := range graph {
		graph[i] = make([]int, n+1)
	}

	for i := 0; i < m; i++ {
		var s, t int
		fmt.Scanf("%d %d", &s, &t)
		// 使用邻接矩阵表示无向图，1 表示 s 与 t 是相连的
		graph[s][t] = 1
	}

	path = append(path, 1) // 无论什么路径已经是从1节点出发
	dfs(graph, 1, n)       // 开始遍历

	// 输出结果
	if len(result) == 0 {
		fmt.Println(-1)
	} else {
		for _, pa := range result {
			for i := 0; i < len(pa)-1; i++ {
				fmt.Print(pa[i], " ")
			}
			fmt.Println(pa[len(pa)-1])
		}
	}
}
```


### 广搜理论基础

https://www.programmercarl.com/kamacoder/%E5%9B%BE%E8%AE%BA%E5%B9%BF%E6%90%9C%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html

广搜（bfs）是一圈一圈的搜索过程，和深搜（dfs）是一条路跑到黑然后再回溯。

广搜的搜索方式就适合于解决两个点之间的**最短路径**问题。

因为广搜是从起点出发，以起始点为中心一圈一圈进行搜索，一旦遇到终点，记录之前走过的节点就是一条最短路。

当然，也有一些问题是广搜 和 深搜都可以解决的，例如岛屿问题，**这类问题的特征就是不涉及具体的遍历方式，只要能把相邻且相同属性的节点标记上就行**




