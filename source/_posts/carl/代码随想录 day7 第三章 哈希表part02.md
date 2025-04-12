
---
title: 代码随想录 day6 第三章 哈希表part02
date: 2024-11-04 23:04:17
modificationDate: 2024 November 4th Monday 23:04:17
categories: 
	- carl
tags: []
sticky: []
published: false
category_bar: true
---

# 第三章 哈希表part02

## 今日任务

●  454.四数相加II

●  383. 赎金信

●  15. 三数之和

●  18. 四数之和

●  总结

## 详细布置

### 454.四数相加II

建议：本题是 使用map 巧妙解决的问题，好好体会一下 哈希法 如何提高程序执行效率，降低时间复杂度，当然使用哈希法 会提高空间复杂度，但一般来说我们都是舍空间 换时间， 工业开发也是这样。

题目链接/文章讲解/视频讲解：[https://programmercarl.com/0454.%E5%9B%9B%E6%95%B0%E7%9B%B8%E5%8A%A0II.html](https://programmercarl.com/0454.%E5%9B%9B%E6%95%B0%E7%9B%B8%E5%8A%A0II.html)

思路： 
题目条件中说明了不去重。 暴力做法：需要遍历四个数值。分治，先算两个数组中的和，然后在求对应两个列表的数值之和。

需要注意的点：
去哈希表中招对应的-key 是否存在，存在需要加val, 而不是加一
code 
```go
func fourSumCount(nums1 []int, nums2 []int, nums3 []int, nums4 []int) int {
	maps := make(map[int]int, len(nums1))
	// 不去重， 暴力做法：需要遍历四个数值。分治，先算两个数组中的和，然后在求对应两个列表的数值之和。
	for _, v := range nums1 {
		for _, v2 := range nums2 {
			maps[v+v2] += 1
		}
	}
	count := 0
	for _, v3 := range nums3 {
		for _, v4 := range nums4 {
            // 去哈希表中招对应的-key 是否存在，存在需要加val, 而不是加一
			if val, ok := maps[-v3-v4]; ok {
				count += val
			}
		}
	}
	return count
}

```

### 383. 赎金信

建议：本题 和 242.有效的字母异位词 是一个思路 ，算是拓展题

题目链接/文章讲解：[https://programmercarl.com/0383.%E8%B5%8E%E9%87%91%E4%BF%A1.html](https://programmercarl.com/0383.%E8%B5%8E%E9%87%91%E4%BF%A1.html)


思路： 
抽象出来就是字符a， 看能否使用b来组成。
1. 判断赎金中各个字符串出现的次数，是否小于等于杂志中出现的次数
2. 只有小写字母

使用两个map 记录，然后遍历ransomNote 需要凑成的单词数量，判断对应杂志中是否有足够的数量字母出现。需要注意的是使用卫语句可以实现提前返回。
```go
func canConstruct(ransomNote string, magazine string) bool {
    ransomNoteMap := make(map[rune]int, len(ransomNote))
    magazineMap := make(map[rune]int, len(magazine))


    for _, v1 := range magazine {
        magazineMap[v1] += 1 
    }

    for _, v := range ransomNote {
        ransomNoteMap[v] += 1
    }

    for k, v := range ransomNoteMap {
        if v > magazineMap[k]{
            return false
        }   
    }
    return true
}

```


### 15. 三数之和

建议：本题虽然和 两数之和 很像，也能用哈希法，但用哈希法会很麻烦，双指针法才是正解，可以先看视频理解一下 双指针法的思路，文章中讲解的，没问题 哈希法很麻烦。

题目链接/文章讲解/视频讲解：[https://programmercarl.com/0015.%E4%B8%89%E6%95%B0%E4%B9%8B%E5%92%8C.html](https://programmercarl.com/0015.%E4%B8%89%E6%95%B0%E4%B9%8B%E5%92%8C.html)

思路:
		先排序，然后使用双指针，然后分别对相邻数据进行排序。
TODO:**待二刷**

```go

func threeSum(nums []int) [][]int {
	sort.Ints(nums)
	res := [][]int{}
	// 找出a + b + c = 0
	// a = nums[i], b = nums[left], c = nums[right]
	for i := 0; i < len(nums)-2; i++ {
		// 排序之后如果第一个元素已经大于零，那么无论如何组合都不可能凑成三元组，直接返回结果就可以了
		n1 := nums[i]
		if n1 > 0 {
			break
		}
		// 去重a
		if i > 0 && n1 == nums[i-1] {
			continue
		}
		l, r := i+1, len(nums)-1
		for l < r {
			n2, n3 := nums[l], nums[r]
			if n1+n2+n3 == 0 {
				res = append(res, []int{n1, n2, n3})
				// 去重逻辑应该放在找到一个三元组之后，对b 和 c去重
				for l < r && nums[l] == n2 {
					l++
				}
				for l < r && nums[r] == n3 {
					r--
				}
			} else if n1+n2+n3 < 0 {
				l++
			} else {
				r--
			}
		}
	}
	return res
}
```


### 18. 四数之和

建议： 要比较一下，本题和 454.四数相加II 的区别，为什么 454.四数相加II 会简单很多，这个想明白了，对本题理解就深刻了。 本题 思路整体和 三数之和一样的，都是双指针，但写的时候 有很多小细节，需要注意，建议先看视频。

题目链接/文章讲解/视频讲解：[https://programmercarl.com/0018.%E5%9B%9B%E6%95%B0%E4%B9%8B%E5%92%8C.html](https://programmercarl.com/0018.%E5%9B%9B%E6%95%B0%E4%B9%8B%E5%92%8C.html)

要求也不能重复，需要去重，返回布尔值。


思路：将四数之和转化为三数之和
需要注意的点，四数之和返回的是任意值。可能为附属

**TODO: 待二刷**
```go

func fourSum(nums []int, target int) [][]int {
	if len(nums) < 4 {
		return nil
	}
	sort.Ints(nums)
	var res [][]int
	for i := 0; i < len(nums)-3; i++ {
		n1 := nums[i]
		// if n1 > target { // 不能这样写,因为可能是负数
		// 	break
		// }
		if i > 0 && n1 == nums[i-1] {  // 对nums[i]去重
			continue
		}
		for j := i + 1; j < len(nums)-2; j++ {
			n2 := nums[j]
			if j > i+1 && n2 == nums[j-1] {  // 对nums[j]去重
				continue
			}
			l := j + 1
			r := len(nums) - 1
			for l < r {
				n3 := nums[l]
				n4 := nums[r]
				sum := n1 + n2 + n3 + n4
				if sum < target {
					l++
				} else if sum > target {
					r--
				} else {
					res = append(res, []int{n1, n2, n3, n4})
					for l < r && n3 == nums[l+1] { // 去重
						l++
					}
					for l < r && n4 == nums[r-1] { // 去重
						r--
					}
					// 找到答案时,双指针同时靠近
					r--
					l++
				}
			}
		}
	}
	return res
}

```
