---
title: 代码随想录 day62 第十一章 图论part11
date: 2025-01-05 22:08:53
modificationDate: 2025 一月 5日 星期日 22:08:53
categories: 
	- carl
tags: []
sticky: []
published: false
category_bar: true
---


# 第十一章：图论part11

### Floyd 算法精讲

Floyd 算法代码很简单，但真正理解起原理 还是需要花点功夫，大家在看代码的时候，会发现 Floyd 的代码很简单，甚至看一眼就背下来了，但我为了讲清楚原理，本篇还是花了大篇幅来讲解。

[https://www.programmercarl.com/kamacoder/0097.%E5%B0%8F%E6%98%8E%E9%80%9B%E5%85%AC%E5%9B%AD.html](https://www.programmercarl.com/kamacoder/0097.%E5%B0%8F%E6%98%8E%E9%80%9B%E5%85%AC%E5%9B%AD.html)


```python
if __name__ == '__main__':
    max_int = 10005  # 设置最大路径，因为边最大距离为10^4

    n, m = map(int, input().split())

    grid = [[[max_int] * (n+1) for _ in range(n+1)] for _ in range(n+1)]  # 初始化三维dp数组

    for _ in range(m):
        p1, p2, w = map(int, input().split())
        grid[p1][p2][0] = w
        grid[p2][p1][0] = w

    # 开始floyd
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                grid[i][j][k] = min(grid[i][j][k-1], grid[i][k][k-1] + grid[k][j][k-1])

    # 输出结果
    z = int(input())
    for _ in range(z):
        start, end = map(int, input().split())
        if grid[start][end][n] == max_int:
            print(-1)
        else:
            print(grid[start][end][n])

```


### A * 算法精讲 （A star算法）

一般 笔试或者 面试的时候，不会考察A*， 都是会结合具体业务场景问 A*算法，例如：地图导航，游戏开发 等等。

其实基础版的A* 并不难，所以大家不要畏惧，理解本篇内容，甚至独立写出代码，大家可以做到，加油

[https://www.programmercarl.com/kamacoder/0126.%E9%AA%91%E5%A3%AB%E7%9A%84%E6%94%BB%E5%87%BBastar.html](https://www.programmercarl.com/kamacoder/0126.%E9%AA%91%E5%A3%AB%E7%9A%84%E6%94%BB%E5%87%BBastar.html)


```python

import heapq
 
n = int(input())
 
moves = [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]
 
def distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
 
def bfs(start, end):
    q = [(distance(start, end), start)]
    step = {start: 0}
     
    while q:
        d, cur = heapq.heappop(q)
        if cur == end:
            return step[cur]
        for move in moves:
            new = (move[0] + cur[0], move[1] + cur[1])
            if 1 <= new[0] <= 1000 and 1 <= new[1] <= 1000:
                step_new = step[cur] + 1
                if step_new < step.get(new, float('inf')):
                    step[new] = step_new
                    heapq.heappush(q, (distance(new, end) + step_new, new))
    return False
                     
for _ in range(n):
    a1, a2, b1, b2 = map(int, input().split())
    print(bfs((a1, a2), (b1, b2)))
```


### 最短路算法总结篇

最各个最短路算法有个全面的了解

[https://www.programmercarl.com/kamacoder/%E6%9C%80%E7%9F%AD%E8%B7%AF%E9%97%AE%E9%A2%98%E6%80%BB%E7%BB%93%E7%AF%87.html](https://www.programmercarl.com/kamacoder/%E6%9C%80%E7%9F%AD%E8%B7%AF%E9%97%AE%E9%A2%98%E6%80%BB%E7%BB%93%E7%AF%87.html)

**如果遇到单源且边为正数，直接Dijkstra**。

至于 **使用朴素版还是 堆优化版 还是取决于图的稠密度**， 多少节点多少边算是稠密图，多少算是稀疏图，这个没有量化，如果想量化只能写出两个版本然后做实验去测试，不同的判题机得出的结果还不太一样。

一般情况下，可以直接用堆优化版本。

**如果遇到单源边可为负数，直接 Bellman-Ford**，同样 SPFA 还是 Bellman-Ford 取决于图的稠密度。

一般情况下，直接用 SPFA。

**如果有负权回路，优先 Bellman-Ford**， 如果是有限节点最短路 也优先 Bellman-Ford，理由是写代码比较方便。

**如果是遇到多源点求最短路，直接 Floyd**。
### 图论总结

[https://www.programmercarl.com/kamacoder/%E5%9B%BE%E8%AE%BA%E6%80%BB%E7%BB%93%E7%AF%87.html](https://www.programmercarl.com/kamacoder/%E5%9B%BE%E8%AE%BA%E6%80%BB%E7%BB%93%E7%AF%87.html)