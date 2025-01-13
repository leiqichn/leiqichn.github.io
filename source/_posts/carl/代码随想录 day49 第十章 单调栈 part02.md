---
title: 代码随想录 day49 第十章 单调栈 part02
date: 2024-12-23 00:25:11
modificationDate: 2024 十二月 23日 星期一 00:25:11
categories: 
	- carl
tags: []
sticky: []
hide: false
category_bar: true
---


# 第十章 单调栈part02

### 42. 接雨水

接雨水这道题目是 面试中特别高频的一道题，也是单调栈 应用的题目，大家好好做做。

建议是掌握 双指针 和单调栈，因为在面试中 写出单调栈可能 有点难度，但双指针思路更直接一些。

在时间紧张的情况有，能写出双指针法也是不错的，然后可以和面试官在慢慢讨论如何优化。

https://programmercarl.com/0042.%E6%8E%A5%E9%9B%A8%E6%B0%B4.html

![42.接雨水3](https://code-thinking-1253855093.file.myqcloud.com/pics/20210223092732301.png)

列4 左侧最高的柱子是列3，高度为2（以下用lHeight表示）。

列4 右侧最高的柱子是列7，高度为3（以下用rHeight表示）。

列4 柱子的高度为1（以下用height表示）

那么列4的雨水高度为 列3和列7的高度最小值减列4高度，即： min(lHeight, rHeight) - height。

列4的雨水高度求出来了，宽度为1，相乘就是列4的雨水体积了。

此时求出了列4的雨水体积。


需要注意的是第一个柱子和最后一个柱子不接水


单调栈就是保持栈内元素有序。和[栈与队列：单调队列 (opens new window)](https://programmercarl.com/0239.%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E6%9C%80%E5%A4%A7%E5%80%BC.html)一样，需要我们自己维持顺序，没有现成的容器可以用。

通常是一维数组，要寻找任一个元素的右边或者左边第一个比自己大或者小的元素的位置，此时我们就要想到可以用单调栈了。

而接雨水这道题目，我们正需要寻找一个元素，右边最大元素以及左边最大元素，来计算雨水面积。

取栈顶元素，将栈顶元素弹出，这个就是凹槽的底部，也就是中间位置，下标记为mid，对应的高度为height[mid]（就是图中的高度1）。

此时的栈顶元素st.top()，就是凹槽的左边位置，下标为st.top()，对应的高度为height[st.top()]（就是图中的高度2）。

当前遍历的元素i，就是凹槽右边的位置，下标为i，对应的高度为height[i]（就是图中的高度3）。

此时大家应该可以发现其实就是**栈顶和栈顶的下一个元素以及要入栈的元素，三个元素来接水！**

那么雨水高度是 min(凹槽左边高度, 凹槽右边高度) - 凹槽底部高度，代码为：`int h = min(height[st.top()], height[i]) - height[mid];`

雨水的宽度是 凹槽右边的下标 - 凹槽左边的下标 - 1（因为只求中间宽度），代码为：`int w = i - st.top() - 1 ;`

当前凹槽雨水的体积就是：`h * w`。

求当前凹槽雨水的体积代码如下：





```go

func trap(height []int) int {
	var left, right, leftMax, rightMax, res int
	right = len(height) - 1
	for left < right {
		if height[left] < height[right] {
			if height[left] >= leftMax {
				leftMax = height[left]  // 设置左边最高柱子
			} else {
				res += leftMax - height[left]  // //右边必定有柱子挡水，所以遇到所有值小于等于leftMax的，全部加入水池中
			}
			left++
		} else {
			if height[right] > rightMax {
				rightMax = height[right]  // //设置右边最高柱子
			} else {
				res += rightMax - height[right]  // //左边必定有柱子挡水，所以，遇到所有值小于等于rightMax的，全部加入水池
			}
			right--
		}
	}
	return res
}

```


### 84.  柱状图中最大的矩形

有了之前单调栈的铺垫，这道题目就不难了。

https://programmercarl.com/0084.%E6%9F%B1%E7%8A%B6%E5%9B%BE%E4%B8%AD%E6%9C%80%E5%A4%A7%E7%9A%84%E7%9F%A9%E5%BD%A2.html


```go

func largestRectangleArea(heights []int) int {
    max := 0
    // 使用切片实现栈
    stack := make([]int, 0)
    // 数组头部加入0
    heights = append([]int{0}, heights...)
    // 数组尾部加入0
    heights = append(heights, 0)
    // 初始化栈，序号从0开始
    stack = append(stack, 0)
    for i := 1; i < len(heights); i ++ {
        // 结束循环条件为：当即将入栈元素>top元素，也就是形成非单调递增的趋势
        for heights[stack[len(stack) - 1]] > heights[i] {
            // mid 是top
            mid := stack[len(stack) - 1]
            // 出栈
            stack = stack[0 : len(stack) - 1]
            // left是top的下一位元素，i是将要入栈的元素
            left := stack[len(stack) - 1]
            // 高度x宽度
            tmp := heights[mid] * (i - left - 1)
            if tmp > max {
                max = tmp
            }
        }
        stack = append(stack, i)
    }
    return max
}

```
