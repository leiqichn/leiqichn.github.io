---
title: leetcode  1.两数之和
date: 2024-08-21 23:53:21
modificationDate: 2024 八月 21日 星期三 23:53:21
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---


有两种思路：
1. 使用暴力遍历， 复杂度的是 O(n ^2)

```go

func twoSum(nums []int, target int) []int {
    for i := 0; i < len(nums); i++ {
        for j:= i+1; j < len(nums); j++ {
            if nums[i] + nums[j] == target {
                return []int{i, j}
            }
        }
    }
    return []int{}
}

```

2. 使用哈希表，是O(n)
  使用哈希表需要注意的是， 这里需要判断idx 和idx2 不相同，因为是要找两个位置，不能取同一个位置
```go

func twoSum(nums []int, target int) []int {
	maps := make(map[int]int, len(nums))

	for idx, num := range nums {
		maps[num] = idx
	}

	for idx, num := range nums {
		if idx2, ok := maps[target-num]; ok && idx != idx2 { // 00 : 04 : 10 使用哈希表，需要注意的是，有可能使用了同一个idx 这里需要注意
			return []int{idx, idx2}
		}
	}
	return []int{}
}


```
