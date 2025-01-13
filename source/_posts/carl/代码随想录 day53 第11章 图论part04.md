---
title: 代码随想录 day53 第11章 图论part04
date: 2024-12-22 23:48:48
modificationDate: 2024 十二月 22日 星期日 23:48:48
categories: 
	- carl
tags: []
sticky: []
hide: false
category_bar: true
---

  

# **第十一章：图论part04**

  

  

经过上面的练习，大家可能会感觉 广搜不过如此，都刷出自信了，本题让大家初步感受一下，广搜难不在广搜本身，而是如何应用广搜。

https://www.programmercarl.com/kamacoder/0110.%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%8E%A5%E9%BE%99.html



```go
// ladderLength 实现 BFS 查找最短路径长度
func ladderLength(beginWord, endWord string, wordList []string) int {
	wordSet := make(map[string]struct{})
	for _, word := range wordList {
		wordSet[word] = struct{}{}
	}

	if _, exists := wordSet[endWord]; !exists {
		return 0
	}

	queue := []string{beginWord}
	visitMap := make(map[string]int)
	visitMap[beginWord] = 1

	for len(queue) > 0 {
		currentWord := queue[0]
		queue = queue[1:]
		path := visitMap[currentWord]

		for i := 0; i < len(currentWord); i++ {
			chars := []rune(currentWord)
			for ch := 'a'; ch <= 'z'; ch++ {
				chars[i] = ch
				newWord := string(chars)

				if newWord == endWord {
					return path + 1
				}

				if _, exists := wordSet[newWord]; exists {
					if _, visited := visitMap[newWord]; !visited {
						visitMap[newWord] = path + 1
						queue = append(queue, newWord)
					}
				}
			}
		}
	}

	return 0
}


```



深搜有细节，同样是深搜两种写法的区别，以及什么时候需要回溯操作呢？

https://www.programmercarl.com/kamacoder/0105.%E6%9C%89%E5%90%91%E5%9B%BE%E7%9A%84%E5%AE%8C%E5%85%A8%E5%8F%AF%E8%BE%BE%E6%80%A7.html


```python
import collections

path = set()  # 纪录 BFS 所经过之节点

def bfs(root, graph):
    global path
    
    que = collections.deque([root])
    while que:
        cur = que.popleft()
        path.add(cur)
        
        for nei in graph[cur]:
            que.append(nei)
        graph[cur] = []
    return

def main():
    N, K = map(int, input().strip().split())
    graph = collections.defaultdict(list)
    for _ in range(K):
        src, dest = map(int, input().strip().split())
        graph[src].append(dest)
    
    bfs(1, graph)
    if path == {i for i in range(1, N + 1)}:
        return 1
    return -1
        

if __name__ == "__main__":
    print(main())
```
  
# 106. 岛屿的周长

[卡码网题目链接（ACM模式）(opens new window)](https://kamacoder.com/problempage.php?pid=1178)


简单题，避免大家惯性思维，建议大家先独立做题。

https://www.programmercarl.com/kamacoder/0106.%E5%B2%9B%E5%B1%BF%E7%9A%84%E5%91%A8%E9%95%BF.html

思路： 计算出总的岛屿数，并计算相邻岛屿数目。

```python


def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # 读取 n 和 m
    n = int(data[0])
    m = int(data[1])
    
    # 初始化 grid
    grid = []
    index = 2
    for i in range(n):
        grid.append([int(data[index + j]) for j in range(m)])
        index += m
    
    sum_land = 0    # 陆地数量
    cover = 0       # 相邻数量

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                sum_land += 1
                # 统计上边相邻陆地
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    cover += 1
                # 统计左边相邻陆地
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    cover += 1
                # 不统计下边和右边，避免重复计算
    
    result = sum_land * 4 - cover * 2
    print(result)

if __name__ == "__main__":
    main()

```
