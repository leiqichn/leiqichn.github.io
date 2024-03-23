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

