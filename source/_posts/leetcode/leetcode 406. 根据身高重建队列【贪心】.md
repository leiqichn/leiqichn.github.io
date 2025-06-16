---
title: leetcode 406. 根据身高重建队列【贪心】
date: 2024-01-24 00:13:30
modificationDate: 2024 一月 24日 星期三 00:13:30
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---

[406. 根据身高重建队列 - 力扣（LeetCode）](https://leetcode.cn/problems/queue-reconstruction-by-height/description/)

![](../../imgs/Pasted%20image%2020240124001349.png)


```go
func reconstructQueue(people [][]int) [][]int {
	sort.Slice(people, func(i, j int) bool {
		if people[i][0] == people[j][0]{
			return people[i][1] < people[j][1]
		}
		return people[i][0] > people[j][0] // 身高由大到小排列

	})i
	// 再按照K进行插入排序，优先插入K小的
	for i, p := range people {
		copy(people[p[1]+1 :i+1], people[p[1] :i+1])  // 腾空出一个位置
        people[p[1]] = pi
	}
	return people
}

```

1. `sort.Slice(people, func(i, j int) bool { ... })`: 使用 `sort.Slice` 对 `people` 进行排序，按照身高从大到小排列，如果身高相同则按照 `k` 从小到大排列。
    
2. `for i, p := range people { ... }`: 遍历排序后的数组，按照每个人的 `k` 值进行插入排序。
    
3. `copy(people[p[1]+1:i+1], people[p[1]:i+1])`: 在插入位置 `p[1]` 之后的位置腾出一个空位，为新的元素插入做准备。
    
4. `people[p[1]] = p`: 将当前人物 `p` 插入到正确的位置。
    

最终，返回重新排列后的队列 `people`。

在 `copy(people[p[1]+1:i+1], people[p[1]:i+1])` 中，使用 `i+1` 而不是 `len(people)` 的原因是为了确保只复制有效的元素范围。这里的目标是将 `people[p[1]:i+1]` 复制到 `people[p[1]+1:i+1]`，而不是复制整个切片。

让我们考虑一下为什么使用 `i+1`：

1. `i` 表示当前元素的索引，而我们想要复制的范围是从 `p[1]` 到 `i`。
2. 使用 `i+1` 作为结束索引可以确保包含 `i` 在内的元素，而不会超出有效的范围。
3. 如果使用 `len(people)` 作为结束索引，那么将会复制从 `p[1]` 到 `len(people)-1` 的所有元素，这超出了实际有效的范围。
