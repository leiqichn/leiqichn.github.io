---
title: 代码随想录 day28 贪心算法part02
date: 2024-11-27 23:39:10
modificationDate: 2024 十一月 27日 星期三 23:39:10
categories: 
	- carl
tags: []
sticky: []
hide: false
category_bar: true
---

# 第八章 贪心算法 part02

### 122.买卖股票的最佳时机II

本题解法很巧妙，本题大家可以先自己思考一下然后再看题解，会有惊喜！

https://programmercarl.com/0122.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAII.html

因为买卖可以是不连续的，所以和之前的题目还是有区别的。只要选后一天相对前一天是正数即可。

```go
func maxProfit(prices []int) int {
    var sum int
    for i := 1; i < len(prices); i++ {
        // 累加每次大于0的交易
        if prices[i] - prices[i-1] > 0 {
            sum += prices[i] - prices[i-1]
        }
    }
    return sum
}
```
### 55. 跳跃游戏

本题如果没接触过，很难想到，所以不要自己憋时间太久，读题思考一会，没思路立刻看题解

https://programmercarl.com/0055.%E8%B7%B3%E8%B7%83%E6%B8%B8%E6%88%8F.html
```go
// 贪心
func canJump(nums []int) bool {
    cover := 0
    n := len(nums)-1
    for i := 0; i <= cover; i++ { // 每次与覆盖值比较
        cover = max(i+nums[i], cover) //每走一步都将 cover 更新为最大值
        if cover >= n {
            return true
        }
    }
    return false
}
func max(a, b int ) int {
    if a > b {
        return a
    }
    return b
}
```


### 45.跳跃游戏II

本题同样不容易想出来。贪心就是这样，有的时候 会感觉简单到离谱，有时候，难的不行，主要是不容易想到。

https://programmercarl.com/0045.%E8%B7%B3%E8%B7%83%E6%B8%B8%E6%88%8FII.html
需要重新看TODO
```go

func jump(nums []int) int {
	// 根据题目规则，初始位置为nums[0]
	lastDistance := 0 // 上一次覆盖范围
	curDistance := 0  // 当前覆盖范围（可达最大范围）
	minStep := 0      // 记录最少跳跃次数

	for i := 0; i < len(nums); i++ {
		if i == lastDistance+1 { // 在上一次可达范围+1的位置，记录步骤
			minStep++                  // 跳跃次数+1
			lastDistance = curDistance // 记录时才可以更新
		}
		curDistance = max(nums[i]+i, curDistance) // 更新当前可达的最大范围
	}
	return minStep
}
```
### 1005.K次取反后最大化的数组和

本题简单一些，估计大家不用想着贪心 ，用自己直觉也会有思路。

https://programmercarl.com/1005.K%E6%AC%A1%E5%8F%96%E5%8F%8D%E5%90%8E%E6%9C%80%E5%A4%A7%E5%8C%96%E7%9A%84%E6%95%B0%E7%BB%84%E5%92%8C.html

需要重新看TODO


```go
func largestSumAfterKNegations(nums []int, K int) int {
	sort.Slice(nums, func(i, j int) bool {
		return math.Abs(float64(nums[i])) > math.Abs(float64(nums[j]))
	})
  
	for i := 0; i < len(nums); i++ {
		if K > 0 && nums[i] < 0 {
			nums[i] = -nums[i]
			K--
		}
	}

	if K%2 == 1 {
		nums[len(nums)-1] = -nums[len(nums)-1]
	}

	result := 0
	for i := 0; i < len(nums); i++ {
		result += nums[i]
	}
	return result
}

```
