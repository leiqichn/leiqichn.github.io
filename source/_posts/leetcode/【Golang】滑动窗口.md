---
title: 【Golang】滑动窗口
date: 2025-06-17 23:52:02
modificationDate: 2025 六月 17日 星期二 23:52:02
categories: 
	- leetcode
tags: []
sticky: []
published: true
category_bar: true
---

# Golang 滑动窗口模板与套路详解

针对 LeetCode 1004（最大连续1的个数 III）这类问题，以下是专门为 Golang 开发者准备的滑动窗口实现模板、适用场景和常见变种：

## Golang 滑动窗口模板（1004 类型）

```go
func longestOnes(nums []int, k int) int {
    left, maxLen, zeroCount := 0, 0, 0

    for right := 0; right < len(nums); right++ {
        // 1. 右指针移动：更新窗口状态
        if nums[right] == 0 {
            zeroCount++
        }
        
        // 2. 左指针移动：当窗口不合法时收缩
        for zeroCount > k {
            if nums[left] == 0 {
                zeroCount--
            }
            left++
        }
        
        // 3. 更新结果（此时窗口合法）
        if windowSize := right - left + 1; windowSize > maxLen {
            maxLen = windowSize
        }
    }
    
    return maxLen
}
```

## 核心套路与技巧（Golang 实现）

1. **双指针初始化**：
   ```go
   left := 0
   maxLen := 0
   counter := 0 // 根据问题定义计数器
   ```

2. **右指针移动逻辑**：
   ```go
   for right := 0; right < len(nums); right++ {
       // 更新计数器
       if condition(nums[right]) {
           counter++
       }
   ```

3. **窗口收缩条件**：
   ```go
   for counter > k { // k 是允许的阈值
       if condition(nums[left]) {
           counter--
       }
       left++
   }
   ```

4. **结果更新**：
   ```go
   if windowSize := right - left + 1; windowSize > maxLen {
       maxLen = windowSize
   }
   ```

## Golang 常见变种实现

### 1. 替换后的最长重复字符（LeetCode 424）
```go
func characterReplacement(s string, k int) int {
    count := make([]int, 26)
    left, maxCount, maxLen := 0, 0, 0
    
    for right, ch := range s {
        count[ch-'A']++
        if count[ch-'A'] > maxCount {
            maxCount = count[ch-'A']
        }
        
        // 收缩条件：窗口大小 - 最大计数 > k
        if (right-left+1)-maxCount > k {
            count[s[left]-'A']--
            left++
        }
        
        if windowSize := right-left+1; windowSize > maxLen {
            maxLen = windowSize
        }
    }
    return maxLen
}
```

### 2. 水果成篮（LeetCode 904）
```go
func totalFruit(fruits []int) int {
    basket := make(map[int]int)
    left, maxFruits := 0, 0
    
    for right, fruit := range fruits {
        basket[fruit]++
        
        // 收缩条件：水果种类超过2种
        for len(basket) > 2 {
            basket[fruits[left]]--
            if basket[fruits[left]] == 0 {
                delete(basket, fruits[left])
            }
            left++
        }
        
        if windowSize := right-left+1; windowSize > maxFruits {
            maxFruits = windowSize
        }
    }
    return maxFruits
}
```

### 3. 最小覆盖子串（LeetCode 76）
```go
func minWindow(s string, t string) string {
    need := make(map[byte]int)
    window := make(map[byte]int)
    
    for i := range t {
        need[t[i]]++
    }
    
    left, valid := 0, 0
    start, length := 0, math.MaxInt32
    
    for right := 0; right < len(s); right++ {
        c := s[right]
        if _, exists := need[c]; exists {
            window[c]++
            if window[c] == need[c] {
                valid++
            }
        }
        
        // 当窗口满足条件时尝试收缩
        for valid == len(need) {
            // 更新最小覆盖子串
            if right-left+1 < length {
                start = left
                length = right - left + 1
            }
            
            // 收缩窗口
            d := s[left]
            if _, exists := need[d]; exists {
                if window[d] == need[d] {
                    valid--
                }
                window[d]--
            }
            left++
        }
    }
    
    if length == math.MaxInt32 {
        return ""
    }
    return s[start : start+length]
}
```

## 滑动窗口适用场景总结

| 问题特征 | 示例题目 | Golang 实现要点 |
|---------|---------|----------------|
| **有限修改连续序列** | 1004, 424, 2024 | 使用计数器跟踪修改需求 |
| **不同元素数量限制** | 904, 340 | 使用 map 跟踪元素种类 |
| **最短满足条件子串** | 209, 76 | 收缩时更新最小值 |
| **固定窗口大小** | 643, 1343 | 维护固定大小的窗口 |
| **无重复字符** | 3, 159 | 使用 map 或 set 检测重复 |

## Golang 实现技巧

1. **计数器选择**：
   - 简单计数：`int` 变量
   - 字符频率：`[26]int` 或 `[128]int`
   - 通用元素：`map[type]int`

2. **边界处理**：
   ```go
   // 处理空输入情况
   if len(nums) == 0 {
       return 0
   }
   ```

3. **性能优化**：
   - 避免不必要的内存分配（预分配 map 大小）
   - 使用数组代替 map 当键范围有限时
   - 减少循环内部的计算

4. **复杂条件处理**：
   ```go
   // 使用辅助函数判断窗口合法性
   for !isValid(window, condition) {
       // 收缩窗口
   }
   ```

掌握这些 Golang 实现的滑动窗口模式和变种，能高效解决 LeetCode 上大部分滑动窗口问题。关键是根据问题特征选择合适的计数器类型和窗口收缩条件。