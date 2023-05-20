---
title: leetcode 705. 设计哈希集合
date: 2023-05-20 22:58:30
modificationDate: 2023 五月 20日 星期六 22:58:30
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---
[706. 设计哈希映射 - 力扣（Leetcode）](https://leetcode.cn/problems/design-hashmap/description/)
![](../../imgs/Pasted%20image%2020230520230121.png)
使用了go 语言的list.List (双向列表)，具体如何使用请看文章：Go语言-list.List
## 使用结构体（非指针）
```go
// 链地址法
var base = 769

// base := 769
type entry struct {
	k int
	v int
}

type MyHashMap struct {
	hashMaps []list.List
}

// hash集合可以使用数组链表；
func Constructor() MyHashMap {
	return MyHashMap{make([]list.List, base)}
}

// func　(this *MyHashMap) hash(key int, value int){

// }

func (this *MyHashMap) Put(key int, value int) {
	hash := key % base
	for e := this.hashMaps[hash].Front(); e != nil; e = e.Next() {
		if et := e.Value.(entry); et.k == key {
			e.Value = entry{key, value} // 注意这里et 是拷贝，需要是使用e.Value 而不是其拷贝
			return
		}
	}
	this.hashMaps[hash].PushBack(entry{key, value})
}

func (this *MyHashMap) Get(key int) int {
	hash := key % base
	for e := this.hashMaps[hash].Front(); e != nil; e = e.Next() {
		if et, ok := e.Value.(entry); ok&& et.k == key{
			return et.v
		}
	}
	return -1
}

func (this *MyHashMap) Remove(key int) {
	hash := key % base
	for e := this.hashMaps[hash].Front(); e != nil; e = e.Next() {
		if et, ok := e.Value.(entry); ok && et.k == key {
			this.hashMaps[hash].Remove(e)
			return
		}
	}
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Put(key,value);
 * param_2 := obj.Get(key);
 * obj.Remove(key);
 */
```
## 使用结构体指针
```go
// 链地址法
var base = 769

// base := 769
type entry struct {
	k int
	v int
}

type MyHashMap struct {
	hashMaps []list.List
}

// hash集合可以使用数组链表；
func Constructor() MyHashMap {
	return MyHashMap{make([]list.List, base)}
}

func (this *MyHashMap) Put(key int, value int) {
	hash := key % base
	for e := this.hashMaps[hash].Front(); e != nil; e = e.Next() {
		if et := e.Value.(*entry); et.k == key { // 注意list 的元素类型是空接口，需要断言类型
			et.v = value  // 注意这里et 是拷贝，需要是使用e.Value 而不是其拷贝,可以使用其指针
			return
		}
	}
	this.hashMaps[hash].PushBack(&entry{key, value})
}


func (this *MyHashMap) Get(key int) int {
	hash := key % base
	for e := this.hashMaps[hash].Front(); e != nil; e = e.Next() {
		if et, ok := e.Value.(*entry); ok&& et.k == key{ // 可以缩写为if et := e.Value.(entry); et.k == key  用于断言，并找key
			return et.v
		}
	}
	return -1
}

func (this *MyHashMap) Remove(key int) {
	hash := key % base
	for e := this.hashMaps[hash].Front(); e != nil; e = e.Next() {
		if et, ok := e.Value.(*entry); ok && et.k == key {
			this.hashMaps[hash].Remove(e)
			return
		}
	}
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Put(key,value);
 * param_2 := obj.Get(key);
 * obj.Remove(key);
 */

```
