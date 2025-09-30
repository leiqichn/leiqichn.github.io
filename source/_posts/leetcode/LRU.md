---
title: LRU
date: 2023-08-07 23:29:00
modificationDate: 2023 八月 7日 星期一 23:29:00
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---
[146. LRU 缓存 - 力扣（LeetCode）](https://leetcode.cn/problems/lru-cache/description/)
![](../../imgs/Pasted%20image%2020230807233035.png)

list Elemet 双向列表；
![](../../imgs/Pasted%20image%2020230807233013.png)
```go
import "container/list"

type LRUCache struct {
    cap  int                    // 缓存容量
    cache map[int]*list.Element//!!! 双向链表 使用Element // 双向链表节点 指向的map
    list *list.List             // 双向链表
}

type keyVal struct {
    key, val int // 节点的Key和Value
}

func Constructor(capacity int) LRUCache {
    return LRUCache{
        cap:   capacity,                            // 初始化缓存容量
        cache: make(map[int]*list.Element),          // 初始化map映射
        list:  list.New(),                           // 初始化双向链表
    }
}

func (this *LRUCache) Get(key int) int {
    if elem, ok := this.cache[key]; ok {             // 如果map里有key对应的双向链表节点
        this.list.MoveToFront(elem)                  // 把节点移动到链表头
        return elem.Value.(*keyVal).val              // 返回节点的value值
    }
    return -1                                        // 没有找到的情况下，返回-1
}

func (this *LRUCache) Put(key int, value int) {
    if elem, ok := this.cache[key]; ok {             // 如果map里有key对应的双向链表节点
        this.list.MoveToFront(elem)                  // 把节点移动到链表头
        //!!! elem.Value 是接口，需要将其转为对应结构体，然后再取值；
        elem.Value.(*keyVal).val = value             // 更新节点的value值 
        return
    }
    if this.list.Len() >= this.cap {                 // 如果超过了缓存容量
        tail := this.list.Back()                     // 获取链表的尾节点
        k := tail.Value.(*keyVal).key                // 获取节点的key
        this.list.Remove(tail)                       // 从链表中删除尾节点
        delete(this.cache, k)                        // 从map中删除尾节点
    }
    elem := this.list.PushFront(&keyVal{key, value}) // 将节点添加到链表头
    this.cache[key] = elem                           // 将节点映射到map中
}

```
