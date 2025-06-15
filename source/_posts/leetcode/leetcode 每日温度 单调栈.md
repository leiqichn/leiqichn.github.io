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
![](../../imgs/Pasted%20image%2020250615183912.png)

[739. 每日温度 - 力扣（LeetCode）](https://leetcode.cn/problems/daily-temperatures/description/?envType=study-plan-v2&envId=top-100-liked)


![](../../imgs/Pasted%20image%2020240521001833.png)

![](../../imgs/Pasted%20image%2020250615171658.png)
栈里边存放的是还没有找到后边更大值的元素
```go
// 从左向右，
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


// 从右向左

func dailyTemperatures(temperatures []int) []int {
    lens := len(temperatures)
    ans := make([]int, lens)
    stack := []int{}  // 单调递增栈（从栈底到栈顶）
    
    for i := lens-1; i >= 0; i-- {
        temperature := temperatures[i]
        // 弹出所有小于等于当前温度的索引
        for len(stack) > 0 && temperature >= temperatures[stack[len(stack)-1]] {
            stack = stack[:len(stack)-1]
        }
        // 如果栈不为空，栈顶就是第一个比当前大的温度
        if len(stack) > 0 {
            ans[i] = stack[len(stack)-1] - i
        }
        stack = append(stack, i)
    }
    return ans
}


```
![](../../imgs/Pasted%20image%2020250615183212.png)
![](../../imgs/Pasted%20image%2020250615183915.png)
单调栈 适用于 上一个更大(更小)元素，或者下一个更大（小）元素

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

# 接雨水
  [42. 接雨水 - 力扣（LeetCode）](https://leetcode.cn/problems/trapping-rain-water/description/)
![](../../imgs/Pasted%20image%2020250615200522.png)
![](../../imgs/Pasted%20image%2020250615200607.png)

```go

func trap(height []int) (ans int) {
    st := []int{}
    for i, h := range height {
        for len(st) > 0 && h >= height[st[len(st)-1]] { // 1. **处理相等高度的情况**：
%%     
    - 当遇到相等高度的柱子时，后面的柱子才是有效的右边界
        
    - 使用`>=`可以正确处理这种情况，确保弹出所有小于等于当前高度的柱子
        
    - 如果只用`>`，相等高度的柱子会留在栈中，导致计算错误 %%
            bottomH := height[st[len(st)-1]]
            st = st[:len(st)-1]
            if len(st) == 0 {
                break
            }
            left := st[len(st)-1]
            dh := min(height[left], h) - bottomH // 面积的高
            ans += dh * (i - left - 1)// 面积高*宽
        }
        st = append(st, i)
    }
    return
}

## 示例分析

以高度数组`[0,1,0,2,1,0,1,3,2,1,2,1]`为例：

1. 遇到第二个高度为1的柱子时：
    
    - 弹出之前高度为0的柱子
        
    - 计算它与左边高度1的柱子之间的雨水
        
2. 遇到高度为2的柱子时：
    
    - 弹出高度为1的柱子（因为2 >= 1）
        
    - 计算它与左边更高柱子之间的雨水
        
3. 遇到相等高度1的柱子时：
    
    - 前面的1被弹出（因为1 >= 1）
        
    - 确保新的1作为右边界参与后续计算
```
