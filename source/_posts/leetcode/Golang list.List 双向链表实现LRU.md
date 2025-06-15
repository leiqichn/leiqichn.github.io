---
title: Golang list.List 双向链表实现LRU
date: 2025-06-16 00:36:57
modificationDate: 2025 六月 16日 星期一 00:36:57
categories: 
	- leetcode
tags: []
sticky: []
published: true
category_bar: true
---

# Go语言中使用双向链表(list.List)实现LRU缓存

LeetCode第146题"LRU缓存"来演示如何在Go语言中使用`container/list`包中的双向链表。

## LRU缓存题目要求

设计一个LRU (Least Recently Used) 缓存机制，它应该支持以下操作：
- `Get(key)`: 如果密钥存在则获取值，否则返回-1
- `Put(key, value)`: 如果密钥不存在，则写入数据；当缓存容量达到上限时，删除最久未使用的数据

## 实现方案

我们将使用`container/list`包中的双向链表来跟踪访问顺序，同时使用map来实现快速查找。

```go
import (
	"container/list"
)

// LRUCache 结构体
type LRUCache struct {
	capacity int                      // 缓存容量
	list     *list.List               // 双向链表用于维护访问顺序
	cache    map[int]*list.Element    // 哈希表用于快速查找
}

// entry 用于存储键值对
type entry struct {
	key   int
	value int
}

// Constructor 初始化LRU缓存
func Constructor(capacity int) LRUCache {
	return LRUCache{
		capacity: capacity,
		list:     list.New(),
		cache:    make(map[int]*list.Element),
	}
}

// Get 获取键对应的值
func (l *LRUCache) Get(key int) int {
	if elem, ok := l.cache[key]; ok {
		// 将访问的元素移动到链表头部表示最近使用
		l.list.MoveToFront(elem)
		return elem.Value.(*entry).value
	}
	return -1
}

// Put 插入或更新键值对
func (l *LRUCache) Put(key int, value int) {
	// 如果键已存在，更新值并移动到头部
	if elem, ok := l.cache[key]; ok {
		l.list.MoveToFront(elem)
		elem.Value.(*entry).value = value
		return
	}
	
	// 如果缓存已满，删除最近最少使用的元素（链表尾部）
	if l.list.Len() == l.capacity {
		tail := l.list.Back()
		if tail != nil {
			delete(l.cache, tail.Value.(*entry).key)
			l.list.Remove(tail)
		}
	}
	
	// 添加新元素到链表头部
	elem := l.list.PushFront(&entry{key, value})
	l.cache[key] = elem
}
```

## 关键点解析

1. **双向链表的使用**:
   - `list.New()` 创建一个新的双向链表
   - `PushFront()` 在链表头部插入元素
   - `MoveToFront()` 将元素移动到链表头部
   - `Back()` 获取链表尾部元素
   - `Remove()` 从链表中删除元素

2. **LRU策略实现**:
   - 最近访问的元素总是放在链表头部
   - 当需要淘汰元素时，删除链表尾部的元素
   - 使用map实现O(1)时间的查找

3. **性能分析**:
   - Get操作时间复杂度: O(1)
   - Put操作时间复杂度: O(1)
   - 空间复杂度: O(capacity)

