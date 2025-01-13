
---
title: 代码随想录 day 24
date: 2025-01-05 22:40:19
modificationDate: 2025 一月 5日 星期日 22:40:19
categories: 
	- carl
tags: []
sticky: []
hide: false
category_bar: true
---

# 第七章 回溯算法part03

### 93.复原IP地址

本期本来是很有难度的，不过 大家做完 分割回文串 之后，本题就容易很多了

题目链接/文章讲解：https://programmercarl.com/0093.%E5%A4%8D%E5%8E%9FIP%E5%9C%B0%E5%9D%80.html

视频讲解：https://www.bilibili.com/video/BV1XP4y1U73i/


```go
var (
    path []string
    res  []string
)
func restoreIpAddresses(s string) []string {
    path, res = make([]string, 0, len(s)), make([]string, 0)
    dfs(s, 0)
    return res
}
func dfs(s string, start int) {  
    if len(path) == 4 {    // 够四段后就不再继续往下递归
        if start == len(s) {      
            str := strings.Join(path, ".")
            res = append(res, str)
        }
        return 
    }
    for i := start; i < len(s); i++ {
        if i != start && s[start] == '0' { // 含有前导 0，无效
            break
        }
        str := s[start : i+1]
        num, _ := strconv.Atoi(str)
        if num >= 0 && num <= 255 {
            path = append(path, str)  // 符合条件的就进入下一层
            dfs(s, i+1)
            path = path[:len(path) - 1]
        } else {   // 如果不满足条件，再往后也不可能满足条件，直接退出
            break
        }
    }
}
```

### 78.子集

子集问题，就是收集树形结构中，每一个节点的结果。 整体代码其实和 回溯模板都是差不多的。

题目链接/文章讲解：https://programmercarl.com/0078.%E5%AD%90%E9%9B%86.html

视频讲解：https://www.bilibili.com/video/BV1U84y1q7Ci


```go

var (
    path   []int
    res  [][]int
)
func subsets(nums []int) [][]int {
    res, path = make([][]int, 0), make([]int, 0, len(nums))
    dfs(nums, 0)
    return res
}
func dfs(nums []int, start int) {
    tmp := make([]int, len(path))
    copy(tmp, path)
    res = append(res, tmp)

    for i := start; i < len(nums); i++ {
        path = append(path, nums[i])
        dfs(nums, i+1)
        path = path[:len(path)-1]
    }
}

```


### 90.子集II

大家之前做了 40.组合总和II 和 78.子集 ，本题就是这两道题目的结合，建议自己独立做一做，本题涉及的知识，之前都讲过，没有新内容。

题目链接/文章讲解：https://programmercarl.com/0090.%E5%AD%90%E9%9B%86II.html

视频讲解：https://www.bilibili.com/video/BV1vm4y1F71J

```go

var (
    result [][]int
    path []int
)

func subsetsWithDup(nums []int) [][]int {
    result = make([][]int, 0)
    path = make([]int, 0)
    used := make([]bool, len(nums))
    sort.Ints(nums) // 去重需要排序
    backtracing(nums, 0, used)
    return result
}

func backtracing(nums []int, startIndex int, used []bool) {
    tmp := make([]int, len(path))
    copy(tmp, path)
    result = append(result, tmp)
    for i := startIndex; i < len(nums); i++ {
        // used[i - 1] == true，说明同一树枝candidates[i - 1]使用过
        // used[i - 1] == false，说明同一树层candidates[i - 1]使用过
        // 而我们要对同一树层使用过的元素进行跳过
        if i > 0 && nums[i] == nums[i-1] && used[i-1] == false {
            continue
        }
        path = append(path, nums[i])
        used[i] = true
        backtracing(nums, i + 1, used)
        path = path[:len(path)-1]
        used[i] = false
    }
}
```