---
title: 代码随想录 day27 贪心算法part01
date: 2024-11-27 23:37:36
modificationDate: 2024 十一月 27日 星期三 23:37:36
categories: 
	- carl
tags: []
sticky: []
hide: true
category_bar: true
---


# 第八章 贪心算法 part01

贪心算法其实就是没有什么规律可言，所以大家了解贪心算法 就了解它没有规律的本质就够了。

不用花心思去研究其规律， 没有思路就立刻看题解。

基本贪心的题目 有两个极端，要不就是特简单，要不就是死活想不出来。

学完贪心之后再去看动态规划，就会了解贪心和动规的区别。

# 详细布置

## 理论基础

[https://programmercarl.com/%E8%B4%AA%E5%BF%83%E7%AE%97%E6%B3%95%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html](https://programmercarl.com/%E8%B4%AA%E5%BF%83%E7%AE%97%E6%B3%95%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)

贪心算法不要想着数学证明，只要举不出来反例就行。

## 455.分发饼干

[https://programmercarl.com/0455.%E5%88%86%E5%8F%91%E9%A5%BC%E5%B9%B2.html](https://programmercarl.com/0455.%E5%88%86%E5%8F%91%E9%A5%BC%E5%B9%B2.html)
思路就是小的饼干满足最小的胃口。需要注意的是，数组需要排序。并且遍历的时候需要保证index 不要越界。


```go
func findContentChildren(g []int, s []int) int {
	// 使用大的饼干gIndex 来满足孩子 sIndex
	// 都排序
    sort.Ints(g)
	sort.Ints(s)
	// 遍历饼干s  遍历孩子胃口g
	res := 0
	sIndex := 0
	for i := 0; i < len(s); i++ {
		if sIndex < len(g) && s[i] >= g[sIndex] {
			res++
			sIndex++
		} 
	}
	return res
}


```


## 376. 摆动序列

[https://programmercarl.com/0376.%E6%91%86%E5%8A%A8%E5%BA%8F%E5%88%97.html](https://programmercarl.com/0376.%E6%91%86%E5%8A%A8%E5%BA%8F%E5%88%97.html)
使用prediff 和curDiff nums[i] - nums[i-1] 来判断是否有斜率变化。

```go
func wiggleMaxLength(nums []int) int {
	n := len(nums)
	if n < 2 { // 小于2 场景
		return n
	}
	ans := 1
	prevDiff := nums[1] - nums[0]
	if prevDiff != 0 { // 两个数不同场景
		ans = 2
	}
	for i := 2; i < n; i++ {
		diff := nums[i] - nums[i-1]
		if diff > 0 && prevDiff <= 0 || diff < 0 && prevDiff >= 0 {
			ans++
			prevDiff = diff
		}
	}
	return ans
}

```

## 53. 最大子序和

[https://programmercarl.com/0053.%E6%9C%80%E5%A4%A7%E5%AD%90%E5%BA%8F%E5%92%8C.html](https://programmercarl.com/0053.%E6%9C%80%E5%A4%A7%E5%AD%90%E5%BA%8F%E5%92%8C.html)

误区二：

大家在使用贪心算法求解本题，经常陷入的误区，就是分不清，是遇到 负数就选择起始位置，还是连续和为负选择起始位置。

在动画演示用，大家可以发现， 4，遇到 -1 的时候，我们依然累加了，为什么呢？

因为和为 3，只要连续和还是正数就会 对后面的元素 起到增大总和的作用。 所以只要连续和为正数我们就保留。
```go
func maxSubArray(nums []int) int {
    max := nums[0]
    count := 0

    for i := 0; i < len(nums); i++{
        count += nums[i]
        if count > max{
            max = count
        }
        // 小于0 重新开始
        if count < 0 {
            count = 0
        }
    } 
    return max
}
```
