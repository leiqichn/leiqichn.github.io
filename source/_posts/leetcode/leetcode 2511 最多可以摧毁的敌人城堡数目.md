---
title: leetcode 2511 最多可以摧毁的敌人城堡数目
date: 2023-09-02 20:51:41
modificationDate: 2023 九月 2日 星期六 20:51:41
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---

[2511. 最多可以摧毁的敌人城堡数目 - 力扣（LeetCode）](https://leetcode.cn/problems/maximum-enemy-forts-that-can-be-captured/description/?envType=daily-question&envId=2023-09-02)


![](../../imgs/Pasted%20image%2020230902205220.png)


# 思路

抽象出来就是求1和-1间最大连续0 的数量。

有两种情况，开始是1 结尾是-1，中间都是0；第二种情况开始是-1结尾是1，中间都是0；上边怎么保证终点和起点不一样呢？

1.当然可以分类讨论，代码会很复杂，判断很多，容易出错

2.  使用 一个变量pre记录开始节点，变更当1或者-1 进来的时候，pre 更新为index，判断当前节点是否和pre 不相等,符合条件则更新res

```go
func captureForts(forts []int) int {

    ans, pre := 0, -1

    //pre 记录的是 1 或 -1 的位置 

    for i, fort := range forts {

        if fort == -1 || fort == 1 {

            if pre >= 0 && forts[pre] != fort {

                ans = max(ans, i - pre - 1)

            }

            pre = i

        }

    }

    return ans

}

  

func max(a int, b int) int {

    if a > b {

        return a

    }

    return b

}

```

