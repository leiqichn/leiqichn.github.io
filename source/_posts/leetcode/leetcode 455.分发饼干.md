---
title: leetcode 455.分发饼干
date: 2023-05-21 23:10:15
modificationDate: 2023 五月 21日 星期日 23:10:15
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---

[455. 分发饼干 - 力扣（Leetcode）](https://leetcode.cn/problems/assign-cookies/description/)
![](../../imgs/Pasted%20image%2020230521231054.png)

https://leiqicn.gitee.io/ 欢迎关注我的博客，定时更新golang 刷题笔记

  

贪心的策略：
> 贪心算法一般分为如下四步：
>  将问题分解为若干个子问题
> 找出适合的贪心策略
> 求解每一个子问题的最优解
> 将局部最优解堆叠成全局最优解


排序，遍历饼干，child胃口初始化idx=0 ,res =0 ;
如果没有越界并且饼干大于等于胃口，则childIdx ++；res++

```go

func findContentChildren(g []int, s []int) int {
    // g 小孩胃口 s 饼干 从大到小排序 排序,并给胃口初始化赋值
    sort.Ints(g)
    sort.Ints(s)
    j := 0
    res := 0
    // 用小饼干 来满足最小的胃口
    for i := 0; i < len(s); i++ {
        // 判断越界 饼干大于胃口
        if j < len(g) && s[i] >= g[j]  { // len不越界的条件需要在前边

            res++
            j++
        }
    }
    return res
}

```