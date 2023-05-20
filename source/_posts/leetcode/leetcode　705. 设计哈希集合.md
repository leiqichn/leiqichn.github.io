
---
title: leetcode　705. 设计哈希集合
date: 2023-05-19 23:06:26
modificationDate: 2023 五月 20日 星期六 22:56:55
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---

[705. 设计哈希集合 - 力扣（Leetcode）](https://leetcode.cn/problems/design-hashset/description/)

![](../../imgs/Pasted%20image%2020230520225749.png)
```go
const base = 769 // 哈希表的长度 质数

type MyHashSet struct {
    data []list.List // 使用链表储存冲突元素
}

func Constructor() MyHashSet { // 构造函数，返回一个空的哈希集合
    return MyHashSet{make([]list.List, base)}
}

// 哈希函数：对键值取模得到哈希值
func (s *MyHashSet) hash(key int) int {
    return key % base
}

func (s *MyHashSet) Add(key int) { // 向哈希集合中添加元素
    if !s.Contains(key) { // 如果元素不在集合中
        h := s.hash(key) // 计算哈希值
        s.data[h].PushBack(key) // 将元素加入到链表中
    }
}

func (s *MyHashSet) Remove(key int) { // 从哈希集合中删除元素
    h := s.hash(key) // 计算哈希值
    for e := s.data[h].Front(); e != nil; e = e.Next() { // 遍历链表
        if e.Value.(int) == key { // 如果元素等于要删除的元素
            s.data[h].Remove(e) // 从链表中删除元素
        }
    }
}

func (s *MyHashSet) Contains(key int) bool { // 判断某个元素是否在哈希集合中
    h := s.hash(key) // 计算哈希值
    for e := s.data[h].Front(); e != nil; e = e.Next() { // 遍历链表
        if e.Value.(int) == key { // 如果元素等于要查找的元素
            return true // 返回 true
        }
    }
    return false // 没有找到元素，返回 false
}

```
