---
title: leetcode 每日温度 单调栈
date: 2024-05-21 00:16:04
modificationDate: 2024 五月 21日 星期二 00:16:04
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---


[739. 每日温度 - 力扣（LeetCode）](https://leetcode.cn/problems/daily-temperatures/description/?envType=study-plan-v2&envId=top-100-liked)


![](../../imgs/Pasted%20image%2020240521001833.png)
栈里边存放的是还没有找到后边更大值的元素
```go
func dailyTemperatures(temperatures []int) []int {
    length := len(temperatures)  // 长度 
    ans := make([]int, length)   // 返回的数组
    stack := []int{}            // 单调栈
    for i := 0; i < length; i ++ {
        temperature := temperatures[i] 
        fmt.Println("temperature:", temperature)
        fmt.Println("stack:", stack)
        for len(stack) > 0 && temperature > temperatures[stack[len(stack) -1]] {
            fmt.Println("temperature now:", temperature, temperatures[stack[len(stack) -1]], stack[len(stack) -1])
            preindex := stack[len(stack)-1] // 上一个位置的index
            stack = stack[:len(stack) -1] // 栈顶找到了当前更大的数，
            ans[preindex] = i -preindex // 记录位置
        }
        stack = append(stack, i) // 如果不满足要求，则说明是小的数，需要添加到栈中
    }
    return ans
}



```


这段代码是一个Go语言编写的函数，名为`dailyTemperatures`，它使用单调栈的数据结构来解决一个特定问题：给定一个每日温度列表`temperatures`，返回一个新列表，其中第i个元素是温度列表中第i天之后第一个比第i天温度更高的温度的天数。

### 代码思想解释：

1. **问题定义**：我们想要找到一个序列中每个元素之后的第一个更大元素，并记录它们之间的索引差。

2. **单调栈的应用**：单调栈是一种特殊的栈结构，它保证栈内的元素是单调递增或单调递减的。在这个场景中，我们使用单调栈来维护一个<font color="#ff0000">**索引栈**，**栈内元素代表尚未找到更大温度的天的索引**</font>。

3. **初始化**：
   - `n`：记录输入温度数组的长度。
   - `ans`：初始化一个长度为`n`的数组，用于存储结果，初始值设为0。
   - `st`：初始化一个空的切片，用作单调栈。

4. **遍历温度数组**：
   - 通过`range`关键字遍历`temperatures`数组，同时获取索引`i`和对应的温度值`t`。

5. **维护单调栈**：
   - 当前温度`t`大于栈顶元素对应的温度时，说明栈顶元素之后的第一个更高温度就是当前温度。此时，执行以下操作：
     - 弹出栈顶元素`j`，即`st[len(st)-1]`。
     - 计算索引差`i - j`，并将这个差值赋给`ans[j]`。
     - 更新栈`st`，移除栈顶元素。

6. **压栈操作**：
   - 将当前索引`i`压入栈`st`中。这表示当前索引的天还没有找到之后的第一个更高温度。

7. **返回结果**：
   - 遍历结束后，返回`ans`数组，其中每个元素表示对应天之后第一个更高温度的天数。
