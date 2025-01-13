---
title: 代码随想录 day55 第十一章 图论part05
date: 2025-01-05 21:26:28
modificationDate: 2025 一月 5日 星期日 21:26:28
categories: 
	- carl
tags: []
sticky: []
hide: true
category_bar: true
---



### 并查集理论基础

并查集理论基础很重要，明确并查集解决什么问题，代码如何写，对后面做并查集类题目很有帮助。

[https://www.programmercarl.com/kamacoder/%E5%9B%BE%E8%AE%BA%E5%B9%B6%E6%9F%A5%E9%9B%86%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html](https://www.programmercarl.com/kamacoder/%E5%9B%BE%E8%AE%BA%E5%B9%B6%E6%9F%A5%E9%9B%86%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)

并查集 可以解决什么问题呢？
主要有两个功能：
1. 将两个元素添加到一个集合中
2. 判断两个元素在不在同一个集合中
![](../../imgs/Pasted%20image%2020250105213812.png)


![](../../imgs/Pasted%20image%2020250105213834.png)

##   
代码模板

那么此时并查集的模板就出来了， 整体模板C++代码如下：

```
int n = 1005; // n根据题目中节点数量而定，一般比节点数量大一点就好
vector<int> father = vector<int> (n, 0); // C++里的一种数组结构

// 并查集初始化
void init() {
    for (int i = 0; i < n; ++i) {
        father[i] = i;
    }
}
// 并查集里寻根的过程
int find(int u) {
    return u == father[u] ? u : father[u] = find(father[u]); // 路径压缩
}

// 判断 u 和 v是否找到同一个根
bool isSame(int u, int v) {
    u = find(u);
    v = find(v);
    return u == v;
}

// 将v->u 这条边加入并查集
void join(int u, int v) {
    u = find(u); // 寻找u的根
    v = find(v); // 寻找v的根
    if (u == v) return ; // 如果发现根相同，则说明在一个集合，不用两个节点相连直接返回
    father[v] = u;
}
```

### 寻找存在的路径

并查集裸题，学会理论基础后，本题直接可以直接刷过

[https://www.programmercarl.com/kamacoder/0107.%E5%AF%BB%E6%89%BE%E5%AD%98%E5%9C%A8%E7%9A%84%E8%B7%AF%E5%BE%84.html](https://www.programmercarl.com/kamacoder/0107.%E5%AF%BB%E6%89%BE%E5%AD%98%E5%9C%A8%E7%9A%84%E8%B7%AF%E5%BE%84.html)



```go

package main

import (
    "fmt"
)

const MaxNodes = 101

var n int
var father [MaxNodes]int

// 初始化并查集
func initialize() {
    for i := 1; i <= n; i++ {
        father[i] = i
    }
}

// 并查集里寻根的过程
func find(u int) int {
    if u == father[u] {
        return u
    }
    father[u] = find(father[u])
    return father[u]
}

// 判断 u 和 v 是否找到同一个根
func isSame(u, v int) bool {
    return find(u) == find(v)
}

// 将 v->u 这条边加入并查集
func join(u, v int) {
    rootU := find(u)
    rootV := find(v)
    if rootU != rootV {
        father[rootV] = rootU
    }
}

func main() {
    var m, s, t, source, destination int
    fmt.Scan(&n, &m)
    initialize()
    for i := 0; i < m; i++ {
        fmt.Scan(&s, &t)
        join(s, t)
    }
    fmt.Scan(&source, &destination)
    if isSame(source, destination) {
        fmt.Println(1)
    } else {
        fmt.Println(0)
    }
}


```
