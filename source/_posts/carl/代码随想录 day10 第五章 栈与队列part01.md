---
title: 代码随想录 day10 第五章 栈与队列part01
date: 2024-11-08 00:25:14
modificationDate: 2024 November 8th Friday 00:25:40
categories: 
	- carl
tags: []
sticky: []
published: false
category_bar: true
---
### 理论基础

了解一下 栈与队列的内部实现机制，文中是以C++为例讲解的。

文章讲解：[https://programmercarl.com/%E6%A0%88%E4%B8%8E%E9%98%9F%E5%88%97%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html](https://programmercarl.com/%E6%A0%88%E4%B8%8E%E9%98%9F%E5%88%97%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)

### 232.用栈实现队列

![](../../imgs/Pasted%20image%2020241110220524.png)
[232. 用栈实现队列 - 力扣（LeetCode）](https://leetcode.cn/problems/implement-queue-using-stacks/)
大家可以先看视频，了解一下模拟的过程，然后写代码会轻松很多。

题目链接/文章讲解/视频讲解：[https://programmercarl.com/0232.%E7%94%A8%E6%A0%88%E5%AE%9E%E7%8E%B0%E9%98%9F%E5%88%97.html](https://programmercarl.com/0232.%E7%94%A8%E6%A0%88%E5%AE%9E%E7%8E%B0%E9%98%9F%E5%88%97.html)


思路：使用两个辅助栈实现队列，一个作为in 栈，一个作为out 栈。in 先进后出，然后入out栈。 in: [1,2,3] -> out: [3,2,1]。 队列先出，即等于out栈的后出了。其实通过两个栈的反转就可以实现原先的先进后出，变为先进先出。同时每次操作的时候都要判断out 是否有元素，必须out 为空的时候，才能将in中元素添加到out.

```go
type MyQueue struct {

    inputStack  []int
    outputStack []int

}

  

func Constructor() MyQueue {

    return MyQueue{

        inputStack:  make([]int, 0),

        outputStack: make([]int, 0),

    }

}

  

func (this *MyQueue) Push(x int) {

    this.inputStack = append(this.inputStack, x)

}

  

func (this *MyQueue) Pop() int {

    if len(this.outputStack) != 0 {

  

        topTmp := this.outputStack[len(this.outputStack)-1] //

        this.outputStack = this.outputStack[:len(this.outputStack)-1]

        return topTmp

    } else {

        for len(this.inputStack) != 0 {

            this.outputStack = append(this.outputStack, this.inputStack[len(this.inputStack)-1])

            this.inputStack = this.inputStack[:len(this.inputStack)-1]

        }

    }

  

    top := this.outputStack[len(this.outputStack)-1] //

    this.outputStack = this.outputStack[:len(this.outputStack)-1]

    return top

}

  

func (this *MyQueue) Peek() int {

    if len(this.outputStack) != 0 {

  

        topTmp := this.outputStack[len(this.outputStack)-1] //

        return topTmp

    } else {

        for len(this.inputStack) != 0 {

            this.outputStack = append(this.outputStack, this.inputStack[len(this.inputStack)-1])

            this.inputStack = this.inputStack[:len(this.inputStack)-1]

        }

    }

  

    top := this.outputStack[len(this.outputStack)-1] //

    return top

}

  

func (this *MyQueue) Empty() bool {

    if len(this.inputStack) == 0 && len(this.outputStack) == 0 {

        return true

    }

    return false

}

  
  

/**

 * Your MyQueue object will be instantiated and called as such:

 * obj := Constructor();

 * obj.Push(x);

 * param_2 := obj.Pop();

 * param_3 := obj.Peek();

 * param_4 := obj.Empty();

 */
```

### 225. 用队列实现栈

可能大家惯性思维，以为还要两个队列来模拟栈，其实只用一个队列就可以模拟栈了。

建议大家掌握一个队列的方法，更简单一些，可以先看视频讲解

题目链接/文章讲解/视频讲解：[https://programmercarl.com/0225.%E7%94%A8%E9%98%9F%E5%88%97%E5%AE%9E%E7%8E%B0%E6%A0%88.html](https://programmercarl.com/0225.%E7%94%A8%E9%98%9F%E5%88%97%E5%AE%9E%E7%8E%B0%E6%A0%88.html)
思路:
![](../../imgs/Pasted%20image%2020241110221855.png)

![](../../imgs/Pasted%20image%2020241110222207.png)
思路：
栈是最后一元素出来；所以input 需要遍历到添加元素到output, 到剩余最后一个元素。这个元素就是要出栈的。出完栈再将output 重新赋值给input;output 重置为空；


```go

type MyStack struct {
	inputQueue  []int
	outputQueue []int
}

func Constructor() MyStack {
	return MyStack{
		inputQueue:  make([]int, 0),
		outputQueue: make([]int, 0),
	}

}

func (this *MyStack) Push(x int) {
	this.inputQueue = append(this.inputQueue, x)

}

func (this *MyStack) Pop() int {
	for len(this.inputQueue) != 1 {
		this.outputQueue = append(this.outputQueue, this.inputQueue[0])
		this.inputQueue = this.inputQueue[1:]
	}
	top := this.inputQueue[0]
	this.inputQueue = this.outputQueue
    this.outputQueue = []int{}
	return top

}

func (this *MyStack) Top() int {
	for len(this.inputQueue) != 1 {
		this.outputQueue = append(this.outputQueue, this.inputQueue[0])
		this.inputQueue = this.inputQueue[1:]
	}
	top := this.inputQueue[0]
	// 不删除元素，需要将inputqueue 添加上去。
	this.inputQueue = append(this.outputQueue, this.inputQueue...)
    this.outputQueue = []int{}
	return top
}

func (this *MyStack) Empty() bool {
	// 两个队列都为空才为空
	if (len(this.inputQueue) == 0) && (len(this.outputQueue) == 0) {
		return true
	}
	return false
}

```


### 20. 有效的括号

讲完了栈实现队列，队列实现栈，接下来就是栈的经典应用了。

大家先自己思考一下 有哪些不匹配的场景，在看视频 我讲的都有哪些场景，落实到代码其实就容易很多了。

题目链接/文章讲解/视频讲解：[https://programmercarl.com/0020.%E6%9C%89%E6%95%88%E7%9A%84%E6%8B%AC%E5%8F%B7.html](https://programmercarl.com/0020.%E6%9C%89%E6%95%88%E7%9A%84%E6%8B%AC%E5%8F%B7.html)

思路： 不要上来就写代码，这样容易越写越乱。需要分析好有多少种情况，然后开始写代码就比较清晰了。如果不在动手之前分析好，写出的代码会有很多问题。


![](../../imgs/Pasted%20image%2020241110223549.png)
第一种情况：已经遍历完了字符串，但是栈不为空，说明有相应的左括号没有右括号来匹配，所以return false

第二种情况：遍历字符串匹配的过程中，发现栈里没有要匹配的字符。所以return false

第三种情况：遍历字符串匹配的过程中，栈已经为空了，没有匹配的字符了，说明右括号没有找到对应的左括号return false


左括号直接入栈。
```go
/ 思路： 使用栈来进行括号的匹配
// 时间复杂度 O(n)
// 空间复杂度 O(n)
func isValid(s string) bool {
	// 使用切片模拟栈的行为
	stack := make([]rune, 0)

	// m 用于记录某个右括号对应的左括号
	m := make(map[rune]rune)
	m[')'] = '('
	m[']'] = '['
	m['}'] = '{'

	// 遍历字符串中的 rune
	for _, c := range s {
		// 左括号直接入栈
		if c == '(' || c == '[' || c == '{' {
			stack = append(stack, c)
		} else {
			// 如果是右括号，先判断栈内是否还有元素
			if len(stack) == 0 {
				return false
			}
			// 再判断栈顶元素是否能够匹配
			peek := stack[len(stack)-1]
			if peek != m[c] {
				return false
			}
			// 模拟栈顶弹出
			stack = stack[:len(stack)-1]
		}
	}

	// 若栈中不再包含元素，则能完全匹配
	return len(stack) == 0
}

```


### 1047. 删除字符串中的所有相邻重复项

栈的经典应用。

要知道栈为什么适合做这种类似于**爱消除的操作**，因为**栈帮助我们记录了 遍历数组当前元素时候，前一个元素是什么**。

题目链接/文章讲解/视频讲解：[https://programmercarl.com/1047.%E5%88%A0%E9%99%A4%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD%E7%9A%84%E6%89%80%E6%9C%89%E7%9B%B8%E9%82%BB%E9%87%8D%E5%A4%8D%E9%A1%B9.html](https://programmercarl.com/1047.%E5%88%A0%E9%99%A4%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD%E7%9A%84%E6%89%80%E6%9C%89%E7%9B%B8%E9%82%BB%E9%87%8D%E5%A4%8D%E9%A1%B9.html)

思路：
通过栈的先入后出，或者说后入先出的能力，可以韩浩的记录当前元素的前一个元素是什么。从而判断是否是相邻的重复项。最终将栈中的元素反转即可。

![](../../imgs/Pasted%20image%2020241110224626.png)

```go

func removeDuplicates(s string) string {
    stack := make([]rune, 0)
    for _, val := range s {
        if len(stack) == 0 || val != stack[len(stack)-1] {
            stack = append(stack, val)
        } else {
            stack = stack[:len(stack)-1]
        }
    }

    // 这里是遵守stack 是个栈，所以需要弹出，并反转。如果不遵守实际可以直接返回 return string(stack)
    var res []rune
    for len(stack) != 0 { // 将栈中元素放到result字符串汇总
        res = append(res, stack[len(stack)-1])
        stack = stack[:len(stack)-1]
    }
    // 此时字符串需要反转一下
    l, r := 0, len(res)-1
    for l < r {
        res[l], res[r] = res[r], res[l]
        l++
        r--
    }
    return string(res)
}
```


这里是遵守stack 是个栈，所以需要弹出，并反转。如果不遵守实际可以直接返回 return string(stack)
可以修改为：

```go
func removeDuplicates(s string) string {
    stack := make([]rune, 0)
    for _, val := range s {
        if len(stack) == 0 || val != stack[len(stack)-1] {
            stack = append(stack, val)
        } else {
            stack = stack[:len(stack)-1]
        }
    }

    return string(stack)
}


```


