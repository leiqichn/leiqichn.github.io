---
title: 代码随想录 day 4  链表 part02
date: 2025-01-05 22:19:48
modificationDate: 2025 一月 5日 星期日 22:19:48
categories: 
	- carl
tags: []
sticky: []
hide: false
category_bar: true
---


# 第二章 链表part02

## 今日任务

## 详细布置

### 24. 两两交换链表中的节点

用虚拟头结点，这样会方便很多。

本题链表操作就比较复杂了，建议大家先看视频，视频里我讲解了注意事项，为什么需要temp保存临时节点。

题目链接/文章讲解/视频讲解： https://programmercarl.com/0024.%E4%B8%A4%E4%B8%A4%E4%BA%A4%E6%8D%A2%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B9.html


```go

func swapPairs(head *ListNode) *ListNode {
    dummy := &ListNode{
        Next: head,
    }
    //head=list[i]
    //pre=list[i-1]
    pre := dummy 
    for head != nil && head.Next != nil {
        pre.Next = head.Next
        next := head.Next.Next
        head.Next.Next = head
        head.Next = next
        //pre=list[(i+2)-1]
        pre = head 
        //head=list[(i+2)]
        head = next
    }
    return dummy.Next
}

```

### 19.删除链表的倒数第N个节点

双指针的操作，要注意，删除第N个节点，那么我们当前遍历的指针一定要指向 第N个节点的前一个节点，建议先看视频。

题目链接/文章讲解/视频讲解：https://programmercarl.com/0019.%E5%88%A0%E9%99%A4%E9%93%BE%E8%A1%A8%E7%9A%84%E5%80%92%E6%95%B0%E7%AC%ACN%E4%B8%AA%E8%8A%82%E7%82%B9.html

```go

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	dummyNode := &ListNode{0, head}
	fast, slow := dummyNode, dummyNode
	for i := 0; i <= n; i++ { // 注意<=，否则快指针为空时，慢指针正好在倒数第n个上面
		fast = fast.Next
	}
	for fast != nil {
		fast = fast.Next
		slow = slow.Next
	}
	slow.Next = slow.Next.Next
	return dummyNode.Next
}

```

### 面试题 02.07. 链表相交

本题没有视频讲解，大家注意 数值相同，不代表指针相同。

题目链接/文章讲解：https://programmercarl.com/%E9%9D%A2%E8%AF%95%E9%A2%9802.07.%E9%93%BE%E8%A1%A8%E7%9B%B8%E4%BA%A4.html


```go
func getIntersectionNode(headA, headB *ListNode) *ListNode {
    l1,l2 := headA, headB
    for l1 != l2 {
        if l1 != nil {
            l1 = l1.Next
        } else {
            l1 = headB
        }

        if l2 != nil {
            l2 = l2.Next
        } else {
            l2 = headA
        }
    }

    return l1
}

```


### 142.环形链表II

算是链表比较有难度的题目，需要多花点时间理解 确定环和找环入口，建议先看视频。

题目链接/文章讲解/视频讲解：https://programmercarl.com/0142.%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8II.html

```go
func detectCycle(head *ListNode) *ListNode {
    slow, fast := head, head
    for fast != nil && fast.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next
        if slow == fast {
            for slow != head {
                slow = slow.Next
                head = head.Next
            }
            return head
        }
    }
    return nil
}

```

### 总结

对于链表的题目，大家最大的困惑可能就是 什么使用用虚拟头结点，什么时候不用虚拟头结点？

一般涉及到 增删改操作，用虚拟头结点都会方便很多， 如果只能查的话，用不用虚拟头结点都差不多。

当然大家也可以为了方便记忆，统一都用虚拟头结点。

https://www.programmercarl.com/%E9%93%BE%E8%A1%A8%E6%80%BB%E7%BB%93%E7%AF%87.html