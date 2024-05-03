---
title: leetcode 208. 实现 Trie (前缀树)
date: 2024-04-17 00:34:47
modificationDate: 2024 四月 17日 星期三 00:34:47
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---
Trie [traɪ] 读音和 try 相同，它的另一些名字有：字典树，前缀树，单词查找树等。

[208. 实现 Trie (前缀树) - 力扣（LeetCode）](https://leetcode.cn/problems/implement-trie-prefix-tree/)

![](../../imgs/Pasted%20image%2020240417003637.png)

Trie 是一颗非典型的多叉树模型，多叉好理解，即每个结点的分支数量可能为多个。

为什么说非典型呢？因为它和一般的多叉树不一样，尤其在结点的数据结构设计上，比如一般的多叉树的结点是这样的：

```go
type TrieNode struct {

    Value int

    Next  *TrieNode

}

```
而 Trie 的结点是这样的(假设只包含'a'~'z'中的字符)：
```go
type TrieNode struct {

    children [26]*TrieNode

    isEnd    bool

}

```


```go
package main

  

import "fmt"

  

// TrieNode 代表Trie中的每个节点

type TrieNode struct {

    children [26]*TrieNode

    isEnd    bool

}

  

// Trie 代表整个前缀树

type Trie struct {

    root *TrieNode

}

  

// Constructor 初始化一个Trie对象

func Constructor() Trie {

    return Trie{root: &TrieNode{}}

}

  

// Insert 将word插入到trie中

func (this *Trie) Insert(word string) {

    node := this.root

    for _, ch := range word {

        index := ch - 'a'

        if node.children[index] == nil {

            node.children[index] = &TrieNode{}

        }

        node = node.children[index]

    }

    node.isEnd = true // 标记单词结束的节点

}

  

// Search 在trie中搜索word

func (this *Trie) Search(word string) bool {

    node := this.root

    for _, ch := range word {

        index := ch - 'a'

        if node.children[index] == nil {

            return false // 如果路径中的节点不存在，说明word不在trie中

        }

        node = node.children[index]

    }

    return node.isEnd // 检查最后一个节点是否标记为单词结尾

}

  

// StartsWith 返回trie中是否有任何单词以prefix为前缀

func (this *Trie) StartsWith(prefix string) bool {

    node := this.root

    for _, ch := range prefix {

        index := ch - 'a'

        if node.children[index] == nil {

            return false // 如果路径中的节点不存在，说明没有以prefix为前缀的word

        }

        node = node.children[index]

    }

    return true // 所有的char都在路径中，说明trie有以prefix为前缀的word

}

  

/**

 * Your Trie object will be instantiated and called as such:

 * obj := Constructor();

 * obj.Insert(word);

 * param_2 := obj.Search(word);

 * param_3 := obj.StartsWith(prefix);

 */

```
