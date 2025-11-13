---
title: 【Golang】滑动窗口总结
date: 2025-11-13 23:04:26
modificationDate: 2025 十一月 13日 星期四 23:04:26
categories: 
	- leetcode
tags: []
sticky: []
published: true
category_bar: true
---

# 双指针与滑动窗口算法总结

## 一、核心思想

### 双指针 (Two Pointers)
- **思想**：使用两个指针在序列中按特定规则移动，避免暴力枚举
- **特点**：通常时间复杂度从 O(n²) 优化到 O(n)

### 滑动窗口 (Sliding Window)
- **思想**：维护一个动态的窗口，通过移动左右边界来寻找最优解
- **特点**：窗口大小可能固定或可变

## 二、通用模板

### 1. 滑动窗口通用模板
```go
func slidingWindow(nums []int, k int) int {
    left := 0
    count := 0 // 或使用map记录窗口内元素
    result := 0
    
    for right := 0; right < len(nums); right++ {
        // 右指针扩张，更新窗口状态
        count = updateCount(count, nums[right], +1)
        
        // 收缩窗口条件
        for windowNeedShrink(left, right, count, k) {
            // 左指针收缩，更新窗口状态
            count = updateCount(count, nums[left], -1)
            left++
        }
        
        // 更新结果（注意边界处理）
        if windowValid(left, right, count, k) {
            result = updateResult(result, left, right)
        }
    }
    return result
}
```

### 2. 双指针通用模板
```go
func twoPointers(nums []int, target int) int {
    left, right := 0, len(nums)-1
    result := 0
    
    for left < right {
        sum := nums[left] + nums[right]
        
        if sum == target {
            // 找到解
            result = updateResult(result, left, right)
            left++ // 或 right-- 根据具体情况
        } else if sum < target {
            left++
        } else {
            right--
        }
    }
    return result
}
```

## 三、常见题型分类

### 1. 固定长度窗口
**特点**：窗口大小固定
```go
// 示例：大小为k的子数组最大和
func fixedWindow(nums []int, k int) int {
    sum := 0
    for i := 0; i < k; i++ {
        sum += nums[i]
    }
    maxSum := sum
    
    for i := k; i < len(nums); i++ {
        sum = sum - nums[i-k] + nums[i]
        maxSum = max(maxSum, sum)
    }
    return maxSum
}
```

### 2. 可变长度窗口（最常用）
**特点**：窗口大小根据条件动态变化

#### A. 最多包含K个某类元素
```go
// 最长包含最多K个0的子数组
func atMostK(nums []int, k int) int {
    left, zeroCount, maxLen := 0, 0, 0
    
    for right := 0; right < len(nums); right++ {
        if nums[right] == 0 {
            zeroCount++
        }
        
        for zeroCount > k {
            if nums[left] == 0 {
                zeroCount--
            }
            left++
        }
        
        maxLen = max(maxLen, right-left+1)
    }
    return maxLen
}
```

#### B. 恰好包含K个某类元素
```go
func exactlyK(nums []int, k int) int {
    return atMostK(nums, k) - atMostK(nums, k-1)
}
```

### 3. 快慢指针
**特点**：处理环形数组、链表环检测等
```go
func slowFastPointer(nums []int) bool {
    slow, fast := 0, 0
    for fast < len(nums) && nums[fast] != 0 {
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast {
            return true // 有环
        }
    }
    return false
}
```

## 四、关键细节与技巧

### 1. 结果计算时机
- **窗口扩张后**：立即计算（如求最大值）
- **窗口收缩后**：满足条件时计算（如求最小值）

### 2. 边界处理
```go
// 注意：是否需要 +1 取决于问题定义
res = max(res, right-left)    // 区间长度 = right - left
res = max(res, right-left+1)  // 区间长度 = right - left + 1
```

### 3. 收缩条件
- `while` vs `if`：通常用 `while` 确保窗口始终有效
- 收缩时机：根据问题要求决定何时收缩

## 五、经典问题映射

| 问题类型 | 窗口条件 | 结果计算 |
|---------|---------|----------|
| 无重复字符的最长子串 | 字符计数 ≤ 1 | right-left+1 |
| 最小覆盖子串 | 包含所有目标字符 | right-left+1 |
| 最大连续1的个数III | 0的个数 ≤ K | right-left+1 |
| 长度最小的子数组 | 和 ≥ target | right-left+1 |
| 删除一个元素后全1数组 | 0的个数 ≤ 1 | right-left |

## 六、复杂度分析

- **时间复杂度**：O(n)，每个元素最多被左右指针各访问一次
- **空间复杂度**：O(1) 或 O(k)，取决于使用的数据结构

## 七、实战技巧

1. **先确定窗口维护什么**：计数、和、唯一性等
2. **明确收缩条件**：什么情况下需要移动左指针
3. **注意结果更新时机**：在收缩前、收缩后还是循环外
4. **处理边界情况**：空数组、全符合条件、全不符合条件

掌握这些模板和思路，就能应对大多数双指针和滑动窗口问题, 欢迎交流