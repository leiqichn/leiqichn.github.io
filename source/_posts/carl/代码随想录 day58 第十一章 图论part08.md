---
title: 代码随想录 day58 第十一章 图论part08
date: 2025-01-05 22:00:15
modificationDate: 2025 一月 5日 星期日 22:00:15
categories: 
	- carl
tags: []
sticky: []
hide: true
category_bar: true
---

# 第十一章：图论part08

### 拓扑排序精讲

拓扑排序看上去很复杂，其实了解其原理之后，代码不难

[https://www.programmercarl.com/kamacoder/0117.%E8%BD%AF%E4%BB%B6%E6%9E%84%E5%BB%BA.html](https://www.programmercarl.com/kamacoder/0117.%E8%BD%AF%E4%BB%B6%E6%9E%84%E5%BB%BA.html)


```python

from collections import deque, defaultdict

def topological_sort(n, edges):
    inDegree = [0] * n # inDegree 记录每个文件的入度
    umap = defaultdict(list) # 记录文件依赖关系

    # 构建图和入度表
    for s, t in edges:
        inDegree[t] += 1
        umap[s].append(t)

    # 初始化队列，加入所有入度为0的节点
    queue = deque([i for i in range(n) if inDegree[i] == 0])
    result = []

    while queue:
        cur = queue.popleft()  # 当前选中的文件
        result.append(cur)
        for file in umap[cur]:  # 获取该文件指向的文件
            inDegree[file] -= 1  # cur的指向的文件入度-1
            if inDegree[file] == 0:
                queue.append(file)

    if len(result) == n:
        print(" ".join(map(str, result)))
    else:
        print(-1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    topological_sort(n, edges)

```


### dijkstra（朴素版）精讲

后面几天都是最短路系列了，对于最短路系列，我的建议是，如果第一次接触最短路算法的话，能看懂原理，能照着代码随想录把代码抄下来就可以了，二刷的时候 再尝试自己去写出来。 三刷的时候，差不多才能把最短路吃透。

对于一刷的录友们，不要强行去逼迫自己去学透，很难刚接触到最短路算法就学透。

[https://www.programmercarl.com/kamacoder/0047.%E5%8F%82%E4%BC%9Adijkstra%E6%9C%B4%E7%B4%A0.html](https://www.programmercarl.com/kamacoder/0047.%E5%8F%82%E4%BC%9Adijkstra%E6%9C%B4%E7%B4%A0.html)



```python 
import sys

def dijkstra(n, m, edges, start, end):
    # 初始化邻接矩阵
    grid = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for p1, p2, val in edges:
        grid[p1][p2] = val

    # 初始化距离数组和访问数组
    minDist = [float('inf')] * (n + 1)
    visited = [False] * (n + 1)

    minDist[start] = 0  # 起始点到自身的距离为0

    for _ in range(1, n + 1):  # 遍历所有节点
        minVal = float('inf')
        cur = -1

        # 选择距离源点最近且未访问过的节点
        for v in range(1, n + 1):
            if not visited[v] and minDist[v] < minVal:
                minVal = minDist[v]
                cur = v

        if cur == -1:  # 如果找不到未访问过的节点，提前结束
            break

        visited[cur] = True  # 标记该节点已被访问

        # 更新未访问节点到源点的距离
        for v in range(1, n + 1):
            if not visited[v] and grid[cur][v] != float('inf') and minDist[cur] + grid[cur][v] < minDist[v]:
                minDist[v] = minDist[cur] + grid[cur][v]

    return -1 if minDist[end] == float('inf') else minDist[end]

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    n, m = int(data[0]), int(data[1])
    edges = []
    index = 2
    for _ in range(m):
        p1 = int(data[index])
        p2 = int(data[index + 1])
        val = int(data[index + 2])
        edges.append((p1, p2, val))
        index += 3
    start = 1  # 起点
    end = n    # 终点

    result = dijkstra(n, m, edges, start, end)
    print(result)


```
