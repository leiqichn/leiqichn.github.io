
---
title: 代码随想录 day 22 回溯算法 part01
date: 2025-01-05 22:36:08
modificationDate: 2025 一月 5日 星期日 22:36:08
categories: 
	- carl
tags: []
sticky: []
hide: true
category_bar: true
---


# 第七章 回溯算法part01

### 理论基础

其实在讲解二叉树的时候，就给大家介绍过回溯，这次正式开启回溯算法，大家可以先看视频，对回溯算法有一个整体的了解。

题目链接/文章讲解：[https://programmercarl.com/%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html](https://programmercarl.com/%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)

视频讲解：[https://www.bilibili.com/video/BV1cy4y167mM](https://www.bilibili.com/video/BV1cy4y167mM)

### 77. 组合

对着 在 回溯算法理论基础 给出的 代码模板，来做本题组合问题，大家就会发现 写回溯算法套路。

在回溯算法解决实际问题的过程中，大家会有各种疑问，先看视频介绍，基本可以解决大家的疑惑。

本题关于剪枝操作是大家要理解的重点，因为后面很多回溯算法解决的题目，都是这个剪枝套路。

题目链接/文章讲解：[https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html](https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html)

视频讲解：[https://www.bilibili.com/video/BV1ti4y1L7cv](https://www.bilibili.com/video/BV1ti4y1L7cv)

剪枝操作：[https://www.bilibili.com/video/BV1wi4y157er](https://www.bilibili.com/video/BV1wi4y157er)



```go

var (
    path []int
    res  [][]int
)

func combine(n int, k int) [][]int {
    path, res = make([]int, 0, k), make([][]int, 0)
    dfs(n, k, 1)
    return res
}

func dfs(n int, k int, start int) {
    if len(path) == k {  // 说明已经满足了k个数的要求
        tmp := make([]int, k)
        copy(tmp, path)
        res = append(res, tmp)
        return
    }
    for i := start; i <= n; i++ {  // 从start开始，不往回走，避免出现重复组合
        if n - i + 1 < k - len(path) {  // 剪枝
            break
        }
        path = append(path, i)
        dfs(n, k, i+1)
        path = path[:len(path)-1]
    }
}

```


### 216.组合总和III

如果把 组合问题理解了，本题就容易一些了。

题目链接/文章讲解：[https://programmercarl.com/0216.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CIII.html](https://programmercarl.com/0216.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CIII.html)

视频讲解：[https://www.bilibili.com/video/BV1wg411873x](https://www.bilibili.com/video/BV1wg411873x)



```go
var (
    res [][]int
    path  []int
)
func combinationSum3(k int, n int) [][]int {
    res, path = make([][]int, 0), make([]int, 0, k)
    dfs(k, n, 1, 0)
    return res
}

func dfs(k, n int, start int, sum int) {
    if len(path) == k {
        if sum == n {
            tmp := make([]int, k)
            copy(tmp, path)
            res = append(res, tmp)
        }
        return
    }
    for i := start; i <= 9; i++ {
        if sum + i > n || 9-i+1 < k-len(path) {
            break
        }
        path = append(path, i)
        dfs(k, n, i+1, sum+i)
        path = path[:len(path)-1]
    }
}
```

### 17.电话号码的字母组合

本题大家刚开始做会有点难度，先自己思考20min，没思路就直接看题解。

题目链接/文章讲解：[https://programmercarl.com/0017.%E7%94%B5%E8%AF%9D%E5%8F%B7%E7%A0%81%E7%9A%84%E5%AD%97%E6%AF%8D%E7%BB%84%E5%90%88.html](https://programmercarl.com/0017.%E7%94%B5%E8%AF%9D%E5%8F%B7%E7%A0%81%E7%9A%84%E5%AD%97%E6%AF%8D%E7%BB%84%E5%90%88.html)

视频讲解：[https://www.bilibili.com/video/BV1yV4y1V7Ug](https://www.bilibili.com/video/BV1yV4y1V7Ug)



```go


var (
    m []string
    path []byte
    res []string
)
func letterCombinations(digits string) []string {
    m = []string{"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"}
    path, res = make([]byte, 0), make([]string, 0)
    if digits == "" {
        return res
    }
    dfs(digits, 0)
    return res
}
func dfs(digits string, start int) {
    if len(path) == len(digits) {  //终止条件，字符串长度等于digits的长度
        tmp := string(path)
        res = append(res, tmp)
        return
    }
    digit := int(digits[start] - '0')  // 将index指向的数字转为int（确定下一个数字）
    str := m[digit-2]   // 取数字对应的字符集（注意和map中的对应）
    for j := 0; j < len(str); j++ {
        path = append(path, str[j])
        dfs(digits, start+1)
        path = path[:len(path)-1]
    }
}

```
