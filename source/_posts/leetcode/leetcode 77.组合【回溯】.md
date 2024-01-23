---
title: leetcode 77.组合【回溯】
date: 2024-01-23 23:17:11
modificationDate: 2024 一月 23日 星期二 23:17:11
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---

[77. 组合 - 力扣（LeetCode）](https://leetcode.cn/problems/combinations/description/)
![](../../imgs/Pasted%20image%2020240123231742.png)


使用回溯的模板
```cpp
void backtracking(参数) {
    if (终止条件) {
        存放结果;
        return;
    }

    for (选择：本层集合中元素（树中节点孩子的数量就是集合的大小）) {
        处理节点;
        backtracking(路径，选择列表); // 递归
        回溯，撤销处理结果
    }
}
```

```go
func combine(n int, k int) [][]int {
	res := [][]int{}
	path := []int{}

	// 结束条件
	var backtracking func(n, k ,startIdx int)
	backtracking = func(n, k ,startIdx int) {
        // 提前返回需要return
		if len(path) == k {
            pathTmp := make([]int,len(path))
			copy(pathTmp, path)
			res = append(res, pathTmp)
            return // return 
		}

		for i := startIdx;i <= n ;i++ {
			path = append(path,i)
			backtracking(n,k,i+1) // i+1 进行下一轮
			path = path[:(len(path) -1)]
		}
	}
	backtracking(n,k,1)
	return res
}

```


1. 创建一个二维切片 `res` 用于存储最终结果，以及一个一维切片 `path` 用于存储当前路径。
    
2. 定义回溯函数 `backtracking`，它接收三个参数：`n` 表示数字范围，`k` 表示组合长度，`startIdx` 表示当前起始数字的索引。
    
3. 在回溯函数中，如果当前路径的长度等于 k，将当前路径添加到结果中。
    
4. 使用循环遍历数字范围，将当前数字加入路径，并递归调用回溯函数。
    
5. 在递归结束后，进行回溯，将当前数字从路径中移除，继续遍历下一个数字。
    
6. 在主函数中初始调用回溯函数，然后返回最终结果。