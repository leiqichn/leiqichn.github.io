---
title: leetcode 双指针
date: 2024-03-23 22:51:46
modificationDate: 2024 March 23rd Saturday 22:51:46
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---


![](../../imgs/Pasted%20image%2020240323225412.png)



```go
// 删除有序数组中的重复元素
func removeDuplicates(nums []int) int {
    slow:=0
    for fast:=1;fast <len(nums);fast++ {
        if nums[fast] != nums[slow] {
            slow++// 跳到下个位置，保存slow

            nums[slow] = nums[fast]
            
        }
    }
    return slow +1
}

```

![](../../imgs/Pasted%20image%2020240323225326.png)

slow是指向当前已经处理好的序列的尾部，右指针指向待处理序列的头部。
右指针不断向右移动，每次右指针指向非零数，则将左右指针对应的数交换，同时左指针右移。

**注意到以下性质：**
- 左指针左边均为非零数；
- 右指针左边直到左指针处均为零。
因此每次交换，都是将slow指针的零与fast指针的非零数交换，且非零数的相对顺序并未改变。

```go

func moveZeroes(nums []int) {
	slow, n := 0, len(nums)
	for fast := 0; fast < n; fast++ { // 注意第一个是0的时候需要比较
		if nums[fast] != 0 { // 不是零的时候，才会交换，如果第一个是0，则fast 是会向后移动的，这样就会交换数值，保证的是slow是指向当前已经处理好的序列的尾部，右指针指向待处理序列的头部。
			nums[slow], nums[fast] = nums[fast], nums[slow]
			slow++
		}
	}
}
```


![](../../imgs/Pasted%20image%2020240324224049.png)
**思路：**
![](../../imgs/Pasted%20image%2020240324224214.png)


```go
func maxArea(height []int) int {
	ans := 0
	for i := 0; i < len(height); i++ {
		for j := i + 1; j < len(height); j++ {
			area := (j - i) * min(height[i], height[j])
			ans = max(area,ans)
		}
	}
	return ans
}

func min(a, b int) int { if a > b { return b }; return a }
func max(a, b int) int { if a < b { return b }; return a }

```

![](../../imgs/Pasted%20image%2020240324223922.png)



```go
func maxArea(height []int) (ans int) {
    left, right := 0, len(height)-1 // 初始化两边指针
    for left < right {
        area := (right - left) * min(height[left], height[right]) // 计算面积
        ans = max(ans, area) // 计算最大值
        if height[left] < height[right] { 
            left++ // 移动短的那个
        } else {
            right--
        }
    }
    return
}

func min(a, b int) int { if a > b { return b }; return a }
func max(a, b int) int { if a < b { return b }; return a }


```



![](../../imgs/Pasted%20image%2020240326011627.png)

前缀和，后缀和
木桶效应，当前能装的水，取决于两边最大值 的最小值。

```go

func trap(height []int) (ans int) {
    n := len(height)
    preMax := make([]int, n) // preMax[i] 表示从 height[0] 到 height[i] 的最大值
    preMax[0] = height[0]
    for i := 1; i < n; i++ {
        preMax[i] = max(preMax[i-1], height[i])
    }

    sufMax := make([]int, n) // sufMax[i] 表示从 height[i] 到 height[n-1] 的最大值
    sufMax[n-1] = height[n-1]
    for i := n - 2; i >= 0; i-- {
        sufMax[i] = max(sufMax[i+1], height[i])
    }

    for i, h := range height {
        ans += min(preMax[i], sufMax[i]) - h // 累加每个水桶能接多少水
    }
    return
}

func min(a, b int) int { if a > b { return b }; return a }
func max(a, b int) int { if a < b { return b }; return a }



```


双指针

```go
func trap(height []int) (ans int) {
    left, right, preMax, sufMax := 0, len(height)-1, 0, 0
    for left < right {
        preMax = max(preMax, height[left])
        sufMax = max(sufMax, height[right])
        if preMax < sufMax {
            ans += preMax - height[left]
            left++
        } else {
            ans += sufMax - height[right]
            right--
        }
    }
    return
}

func max(a, b int) int { if a < b { return b }; return a }

```
