---
title: 代码随想录 day 3  链表 part01
date: 2025-01-05 22:16:31
modificationDate: 2025 一月 5日 星期日 22:16:31
categories: 
	- carl
tags: []
sticky: []
hide: false
category_bar: true
---


# 第二章 链表part01

day1 任务以及具体安排：[https://docs.qq.com/doc/DUG9UR2ZUc3BjRUdY](https://docs.qq.com/doc/DUG9UR2ZUc3BjRUdY)

day 2 任务以及具体安排：[https://docs.qq.com/doc/DUGRwWXNOVEpyaVpG](https://docs.qq.com/doc/DUGRwWXNOVEpyaVpG)

## 今日任务

●  链表理论基础

●  203.移除链表元素

●  707.设计链表

●  206.反转链表

## 详细布置

### 链表理论基础

建议：了解一下链表基础，以及链表和数组的区别

文章链接：[https://programmercarl.com/%E9%93%BE%E8%A1%A8%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html](https://programmercarl.com/%E9%93%BE%E8%A1%A8%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)

### 203.移除链表元素

建议： 本题最关键是要理解 虚拟头结点的使用技巧，这个对链表题目很重要。

题目链接/文章讲解/视频讲解：：[https://programmercarl.com/0203.%E7%A7%BB%E9%99%A4%E9%93%BE%E8%A1%A8%E5%85%83%E7%B4%A0.html](https://programmercarl.com/0203.%E7%A7%BB%E9%99%A4%E9%93%BE%E8%A1%A8%E5%85%83%E7%B4%A0.html)

```go

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeElements(head *ListNode, val int) *ListNode {
    dummyHead := &ListNode{}
    dummyHead.Next = head
    cur := dummyHead
    for cur != nil && cur.Next != nil {
        if cur.Next.Val == val {
            cur.Next = cur.Next.Next
        } else {
            cur = cur.Next
        }
    }
    return dummyHead.Next
}

```

### 707.设计链表

建议： 这是一道考察 链表综合操作的题目，不算容易，可以练一练 使用虚拟头结点

题目链接/文章讲解/视频讲解：[https://programmercarl.com/0707.%E8%AE%BE%E8%AE%A1%E9%93%BE%E8%A1%A8.html](https://programmercarl.com/0707.%E8%AE%BE%E8%AE%A1%E9%93%BE%E8%A1%A8.html)
```go

//单链表实现
package main

import (
	"fmt"
)

type SingleNode struct {
	Val  int         // 节点的值
	Next *SingleNode // 下一个节点的指针
}

type MyLinkedList struct {
	dummyHead *SingleNode // 虚拟头节点
	Size      int         // 链表大小
}

func main() {
	list := Constructor()     // 初始化链表
	list.AddAtHead(100)       // 在头部添加元素
	list.AddAtTail(242)       // 在尾部添加元素
	list.AddAtTail(777)       // 在尾部添加元素
	list.AddAtIndex(1, 99999) // 在指定位置添加元素
	list.printLinkedList()    // 打印链表
}

/** Initialize your data structure here. */
func Constructor() MyLinkedList {
	newNode := &SingleNode{ // 创建新节点
		-999,
		nil,
	}
	return MyLinkedList{ // 返回链表
		dummyHead: newNode,
		Size:      0,
	}

}

/** Get the value of the index-th node in the linked list. If the index is
  invalid, return -1. */
func (this *MyLinkedList) Get(index int) int {
	/*if this != nil || index < 0 || index > this.Size {
		return -1
	}*/
	if this == nil || index < 0 || index >= this.Size { // 如果索引无效则返回-1
		return -1
	}
	// 让cur等于真正头节点
	cur := this.dummyHead.Next   // 设置当前节点为真实头节点
	for i := 0; i < index; i++ { // 遍历到索引所在的节点
		cur = cur.Next
	}
	return cur.Val // 返回节点值
}

/** Add a node of value val before the first element of the linked list. After
  the insertion, the new node will be the first node of the linked list. */
func (this *MyLinkedList) AddAtHead(val int) {
	// 以下两行代码可用一行代替
	// newNode := new(SingleNode)
	// newNode.Val = val
	newNode := &SingleNode{Val: val}   // 创建新节点
	newNode.Next = this.dummyHead.Next // 新节点指向当前头节点
	this.dummyHead.Next = newNode      // 新节点变为头节点
	this.Size++                        // 链表大小增加1
}

/** Append a node of value val to the last element of the linked list. */
func (this *MyLinkedList) AddAtTail(val int) {
	newNode := &SingleNode{Val: val} // 创建新节点
	cur := this.dummyHead            // 设置当前节点为虚拟头节点
	for cur.Next != nil {            // 遍历到最后一个节点
		cur = cur.Next
	}
	cur.Next = newNode // 在尾部添加新节点
	this.Size++        // 链表大小增加1
}

/** Add a node of value val before the index-th node in the linked list. If
  index equals to the length of linked list, the node will be appended to the
  end of linked list. If index is greater than the length, the node will not be
  inserted. */
func (this *MyLinkedList) AddAtIndex(index int, val int) {
	if index < 0 { // 如果索引小于0，设置为0
		index = 0
	} else if index > this.Size { // 如果索引大于链表长度，直接返回
		return
	}

	newNode := &SingleNode{Val: val} // 创建新节点
	cur := this.dummyHead            // 设置当前节点为虚拟头节点
	for i := 0; i < index; i++ {     // 遍历到指定索引的前一个节点
		cur = cur.Next
	}
	newNode.Next = cur.Next // 新节点指向原索引节点
	cur.Next = newNode      // 原索引的前一个节点指向新节点
	this.Size++             // 链表大小增加1
}

/** Delete the index-th node in the linked list, if the index is valid. */
func (this *MyLinkedList) DeleteAtIndex(index int) {
	if index < 0 || index >= this.Size { // 如果索引无效则直接返回
		return
	}
	cur := this.dummyHead        // 设置当前节点为虚拟头节点
	for i := 0; i < index; i++ { // 遍历到要删除节点的前一个节点
		cur = cur.Next
	}
	if cur.Next != nil {
		cur.Next = cur.Next.Next // 当前节点直接指向下下个节点，即删除了下一个节点
	}
	this.Size-- // 注意删除节点后应将链表大小减一
}

// 打印链表
func (list *MyLinkedList) printLinkedList() {
	cur := list.dummyHead // 设置当前节点为虚拟头节点
	for cur.Next != nil { // 遍历链表
		fmt.Println(cur.Next.Val) // 打印节点值
		cur = cur.Next            // 切换到下一个节点
	}
}


```


### 206.反转链表

建议先看我的视频讲解，视频讲解中对 反转链表需要注意的点讲的很清晰了，看完之后大家的疑惑基本都解决了。

题目链接/文章讲解/视频讲解：[https://programmercarl.com/0206.%E7%BF%BB%E8%BD%AC%E9%93%BE%E8%A1%A8.html](https://programmercarl.com/0206.%E7%BF%BB%E8%BD%AC%E9%93%BE%E8%A1%A8.html)

```go

//双指针
func reverseList(head *ListNode) *ListNode {
    var pre *ListNode
    cur := head
    for cur != nil {
        next := cur.Next
        cur.Next = pre
        pre = cur
        cur = next
    }
    return pre
}

//递归
func reverseList(head *ListNode) *ListNode {
    return help(nil, head)
}

func help(pre, head *ListNode)*ListNode{
    if head == nil {
        return pre
    }
    next := head.Next
    head.Next = pre
    return help(head, next)
}

```