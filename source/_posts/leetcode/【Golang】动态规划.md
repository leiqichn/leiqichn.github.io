---
title: 【Golang】动态规划
date: 2025-06-18 00:35:57
modificationDate: 2025 六月 18日 星期三 00:35:57
categories: 
	- leetcode
tags: []
sticky: []
published: true
category_bar: true
---

动态规划（Dynamic Programming, DP）是算法中的经典题型，LeetCode 上有许多高频题目。以下是常见的 DP 分类、经典题目及 Golang 实现模板总结：

---

### **一、经典题目分类与 Golang 实现**
#### 1. **线性 DP**
- **题目**：[70. 爬楼梯](https://leetcode.com/problems/climbing-stairs/)
  ```go
  func climbStairs(n int) int {
      if n <= 2 { return n }
      dp := make([]int, n+1)
      dp[1], dp[2] = 1, 2
      for i := 3; i <= n; i++ {
          dp[i] = dp[i-1] + dp[i-2]
      }
      return dp[n]
  }
  ```
  **优化空间**（滚动数组）：
  ```go
  func climbStairs(n int) int {
      if n <= 2 { return n }
      a, b := 1, 2
      for i := 3; i <= n; i++ {
          a, b = b, a+b
      }
      return b
  }
  ```

- **模板总结**：
  - 状态定义：`dp[i]` 表示第 `i` 阶的方案数。
  - 转移方程：`dp[i] = dp[i-1] + dp[i-2]`。
  - 初始化：`dp[1] = 1`, `dp[2] = 2`。

#### 2. **背包问题**
- **题目**：[416. 分割等和子集](https://leetcode.com/problems/partition-equal-subset-sum/)
  ```go
  func canPartition(nums []int) bool {
      sum := 0
      for _, num := range nums {
          sum += num
      }
      if sum%2 != 0 { return false }
      target := sum / 2
      dp := make([]bool, target+1)
      dp[0] = true
      for _, num := range nums {
          for j := target; j >= num; j-- {
              dp[j] = dp[j] || dp[j-num]
          }
      }
      return dp[target]
  }
  ```
  **模板总结**：
  - 状态定义：`dp[j]` 表示能否凑出和为 `j`。
  - 转移方程：`dp[j] = dp[j] || dp[j-num]`。
  - 初始化：`dp[0] = true`（和为 0 不需要选任何数）。

#### 3. **字符串 DP**
- **题目**：[1143. 最长公共子序列](https://leetcode.com/problems/longest-common-subsequence/)
  ```go
  func longestCommonSubsequence(text1 string, text2 string) int {
      m, n := len(text1), len(text2)
      dp := make([][]int, m+1)
      for i := range dp {
          dp[i] = make([]int, n+1)
      }
      for i := 1; i <= m; i++ {
          for j := 1; j <= n; j++ {
              if text1[i-1] == text2[j-1] {
                  dp[i][j] = dp[i-1][j-1] + 1
              } else {
                  dp[i][j] = max(dp[i-1][j], dp[i][j-1])
              }
          }
      }
      return dp[m][n]
  }
  ```
  **模板总结**：
  - 状态定义：`dp[i][j]` 表示 `text1[0..i-1]` 和 `text2[0..j-1]` 的 LCS 长度。
  - 转移方程：
    - 字符匹配：`dp[i][j] = dp[i-1][j-1] + 1`。
    - 不匹配：`dp[i][j] = max(dp[i-1][j], dp[i][j-1])`。

#### 4. **股票买卖问题**
- **题目**：[121. 买卖股票的最佳时机](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
  ```go
  func maxProfit(prices []int) int {
      minPrice, maxProfit := math.MaxInt32, 0
      for _, price := range prices {
          if price < minPrice {
              minPrice = price
          } else if profit := price - minPrice; profit > maxProfit {
              maxProfit = profit
          }
      }
      return maxProfit
  }
  ```
  **模板总结**：
  - 状态定义：`dp[i][0]` 表示第 `i` 天不持股的最大利润，`dp[i][1]` 表示持股的最大利润。
  - 转移方程：
    - `dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])`
    - `dp[i][1] = max(dp[i-1][1], -prices[i])`

#### 5. **区间 DP**
- **题目**：[5. 最长回文子串](https://leetcode.com/problems/longest-palindromic-substring/)
  ```go
  func longestPalindrome(s string) string {
      n := len(s)
      dp := make([][]bool, n)
      for i := range dp {
          dp[i] = make([]bool, n)
      }
      start, maxLen := 0, 1
      for i := 0; i < n; i++ {
          dp[i][i] = true
      }
      for l := 2; l <= n; l++ {
          for i := 0; i <= n-l; i++ {
              j := i + l - 1
              if s[i] == s[j] {
                  if l == 2 || dp[i+1][j-1] {
                      dp[i][j] = true
                      if l > maxLen {
                          start, maxLen = i, l
                      }
                  }
              }
          }
      }
      return s[start : start+maxLen]
  }
  ```
  **模板总结**：
  - 状态定义：`dp[i][j]` 表示 `s[i..j]` 是否为回文。
  - 转移方程：`dp[i][j] = (s[i] == s[j]) && (j-i <= 2 || dp[i+1][j-1])`。

---

### **二、动态规划通用解题模板（Golang）**
```go
func dpProblem(input) int {
    // 1. 初始化 DP 数组
    dp := make([][]int, m)
    for i := range dp {
        dp[i] = make([]int, n)
    }

    // 2. 边界条件
    dp[0][0] = baseCase

    // 3. 状态转移
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + value
        }
    }

    // 4. 返回结果
    return dp[m-1][n-1]
}
```

---

### **三、高频题目推荐**
1. 简单：70（爬楼梯）、198（打家劫舍）、53（最大子数组和）
2. 中等：322（零钱兑换）、300（最长递增子序列）、139（单词拆分）
3. 困难：72（编辑距离）、312（戳气球）、10（正则表达式匹配）

---

### **四、注意事项**
1. **状态定义**：明确 `dp[i]` 或 `dp[i][j]` 的含义。
2. **转移方程**：分析问题如何分解为子问题。
3. **空间优化**：滚动数组或逆序更新（如背包问题）。
4. **边界条件**：如 `dp[0]` 或 `dp[0][0]` 的初始化。

通过练习这些题目并总结模板，可以快速掌握动态规划的核心思想！