---
title: 代码随想录 day56 第十一章 图论part056
date: 2025-01-05 21:47:28
modificationDate: 2025 一月 5日 星期日 21:47:28
categories: 
	- carl
tags: []
sticky: []
hide: true
category_bar: true
---




# 第十一章：图论part06

### 108.  冗余连接

并查集应用类题目，关键是如何把题意转化成并查集问题

[https://www.programmercarl.com/kamacoder/0108.%E5%86%97%E4%BD%99%E8%BF%9E%E6%8E%A5.html](https://www.programmercarl.com/kamacoder/0108.%E5%86%97%E4%BD%99%E8%BF%9E%E6%8E%A5.html)


```python

father = list()

def find(u):
    if u == father[u]:
        return u
    else:
        father[u] = find(father[u])
        return father[u]
        
def is_same(u, v):
    u = find(u)
    v = find(v)
    return u == v
    
def join(u, v):
    u = find(u)
    v = find(v)
    if u != v:
        father[u] = v
        
if __name__ == "__main__":
    # 輸入
    n = int(input())
    for i in range(n + 1):
        father.append(i)
    # 尋找冗余邊    
    result = None
    for i in range(n):
        s, t = map(int, input().split())
        if is_same(s, t):
            result = str(s) + ' ' + str(t)
        else:
            join(s, t)
        
    # 輸出
    print(result)

```


### 109.  冗余连接II

上面两道题目是不是感觉做出自信了，感觉并查集不过如此？

来这道题目 给大家适当一些打击， 难度上来了。

[https://www.programmercarl.com/kamacoder/0109.%E5%86%97%E4%BD%99%E8%BF%9E%E6%8E%A5II.html](https://www.programmercarl.com/kamacoder/0109.%E5%86%97%E4%BD%99%E8%BF%9E%E6%8E%A5II.html)

```python
from collections import defaultdict

father = list()


def find(u):
    if u == father[u]:
        return u
    else:
        father[u] = find(father[u])
        return father[u]
        
        
def is_same(u, v):
    u = find(u)
    v = find(v)
    return u == v
    
    
def join(u, v):
    u = find(u)
    v = find(v)
    if u != v:
        father[u] = v
    
    
def is_tree_after_remove_edge(edges, edge, n):
    # 初始化并查集
    global father 
    father = [i for i in range(n + 1)]
    
    for i in range(len(edges)):
        if i == edge:
            continue
        s, t = edges[i]
        if is_same(s, t): # 成環，即不是有向樹
            return False
        else: # 將s,t放入集合中
            join(s, t)
    return True
    

def get_remove_edge(edges):
    # 初始化并查集
    global father
    father = [i for i in range(n + 1)]
    
    for s, t in edges:
        if is_same(s, t):
            print(s, t)
            return
        else:
            join(s, t)
        

if __name__ == "__main__":
    # 輸入
    n = int(input())
    edges = list()
    in_degree = defaultdict(int)
    
    for i in range(n):
        s, t = map(int, input().split())
        in_degree[t] += 1
        edges.append([s, t])
        
    # 尋找入度為2的邊，並紀錄其下標(index)
    vec = list()
    for i in range(n - 1, -1, -1):
        if in_degree[edges[i][1]] == 2:
            vec.append(i)
            
    # 輸出
    if len(vec) > 0:
        # 情況一：刪除輸出順序靠後的邊 
        if is_tree_after_remove_edge(edges, vec[0], n):
            print(edges[vec[0]][0], edges[vec[0]][1])
        # 情況二：只能刪除特定的邊
        else:
            print(edges[vec[1]][0], edges[vec[1]][1])
    else:
        # 情況三： 原圖有環
        get_remove_edge(edges)

```
