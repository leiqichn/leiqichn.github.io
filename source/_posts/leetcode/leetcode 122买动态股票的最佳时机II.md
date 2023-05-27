---
title: leetcode 122买动态股票的最佳时机II
date: 2023-05-27 23:51:57
modificationDate: 2023 五月 27日 星期六 23:51:57
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---
[122. 买卖股票的最佳时机 II - 力扣（Leetcode）](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/description/)
![](../../imgs/Pasted%20image%2020230527235217.png)

每次只允许在一天买入一支股票，在之后某个时间卖出它。同时，你也可以选择不进行任何交易。

相比于第一题买卖股票的最佳时机（只能进行一次交易），这道题没有限制交易次数，因此我们应该从一个更灵活的角度去考虑如何进行交易。

下面是代码解释：

首先定义变量 sum 记录当前总利润。
然后从第二个价格开始遍历，计算当日价格与前一天价格之差。
如果价格上涨了，则将当前利润加上买卖差价，否则不进行操作。
最后返回累计的总利润。
这样做的原理在于，如果在 i 天买入，在 j 天卖出（j > i），我们可以等价于在 i+1、i+2……j-1、j 这些连续的日子里都进行了购入和卖出，而我们所需获得的利润即为这些差价的总和。因此，代码中只统计了所有价格差大于 0 的部分，而将其他价格差为负值的日子抛弃掉了。

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



