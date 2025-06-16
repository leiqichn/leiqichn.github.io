---
title: 【Golang】slice append 和copy对比
date: 2025-06-16 23:53:12
modificationDate: 2025 六月 16日 星期一 23:53:12
categories: 
	- Golang
tags: []
sticky: []
published: true
category_bar: true
---

# 正确
```go
 func reconstructQueue(people [][]int) [][]int {
    //先将身高从大到小排序，确定最大个子的相对位置
    sort.Slice(people,func(i,j int)bool{
        if people[i][0]==people[j][0]{
            return people[i][1]<people[j][1]//这个才是当身高相同时，将K按照从小到大排序
        }
        return people[i][0]>people[j][0]//这个只是确保身高按照由大到小的顺序来排，并不确定K是按照从小到大排序的
    })
    //再按照K进行插入排序，优先插入K小的
    result := make([][]int, 0)
	for _, info := range people {
		result = append(result, info)
		copy(result[info[1] +1:], result[info[1]:])//将插入位置之后的元素后移动一位（意思是腾出空间）
		result[info[1]] = info//将插入元素位置插入元素
	}
	return result
}

```

# 错误


```go
unc reconstructQueue(people [][]int) [][]int {
    //先将身高从大到小排序，确定最大个子的相对位置
    sort.Slice(people,func(i,j int)bool{
        if people[i][0]==people[j][0]{
            return people[i][1]<people[j][1]//这个才是当身高相同时，将K按照从小到大排序
        }
        return people[i][0]>people[j][0]//这个只是确保身高按照由大到小的顺序来排，并不确定K是按照从小到大排序的
    })
    //再按照K进行插入排序，优先插入K小的
    result := make([][]int, 0)
	for _, info := range people {
		result = append(result, info)
		pos := info[1]
        result = append(result[:pos+1], result[pos:]...)  // 在 pos 处分割并拼接
        result[pos] = info      //将插入位置之后的元素后移动一位（意思是腾出空间）
	}
	return result
}
```

![](../../imgs/Pasted%20image%2020250616235439.png)
两个 `reconstructQueue` 函数的主要区别在于 **插入元素的方式**，而第二个版本能通过是因为它正确处理了 **切片的动态扩容和元素移动**

---

### **关键问题分析**
#### 1. **第一个版本的问题（Slice 操作）**
```go
result = append(result, info)          // 先追加元素（长度+1）
pos := info[1]
result = append(result[:pos+1], result[pos:]...)  // 尝试在 pos 处腾出位置
result[pos] = info                     // 插入元素
```
**问题原因**：
- **`append(result[:pos+1], result[pos:]...)` 会导致数据错乱**  
  当 `pos` 不是最后一个位置时，`result[pos:]` 会包含刚刚追加的 `info`（因为上一步 `append(result, info)` 已经增加了长度），导致切片拼接时重复复制元素，最终结果错误。

#### 2. **第二个版本的正确性（copy 操作）**
```go
result = append(result, info)          // 先追加元素（长度+1）
copy(result[info[1]+1:], result[info[1]:]) // 正确后移元素
result[info[1]] = info                 // 插入元素
```
**为什么正确**：
- `copy` **直接覆盖内存**，不会因 `append` 的嵌套调用引发数据错乱。
- 逻辑清晰：先扩展切片，再移动元素，最后插入新值。

---

### **修复第一个版本的方法**
如果仍想用 **Slice 操作**，需避免提前追加元素，改为直接插入：
```go
func reconstructQueue(people [][]int) [][]int {
    sort.Slice(people, func(i, j int) bool {
        if people[i][0] == people[j][0] {
            return people[i][1] < people[j][1]
        }
        return people[i][0] > people[j][0]
    })

    result := make([][]int, 0)
    for _, info := range people {
        pos := info[1]
        result = append(result[:pos], append([][]int{info}, result[pos:]...)...) // 直接插入
    }
    return result
}
```
**关键修改**：
- 使用 `append([][]int{info}, result[pos:]...)` 一次性完成插入，避免提前扩展切片。

---

### **两种方式的对比**
| 操作方式       | 代码示例                                | 优点                  | 缺点                  |
|----------------|----------------------------------------|-----------------------|-----------------------|
| **copy**       | `copy(result[pos+1:], result[pos:])`   | 内存操作直接，不易出错 | 代码稍显冗长          |
| **Slice 拼接** | `append(result[:pos], append([][]int{info}, result[pos:]...)...)` | 代码简洁              | 嵌套 `append` 可读性略低 |

---

### **为什么第二个版本更鲁棒？**
1. **`copy` 是底层内存复制**  
   不会受切片共享或嵌套 `append` 的影响，适合需要精确控制内存的场景。
2. **`append` 的嵌套可能导致临时切片**  
   在复杂逻辑中容易引入错误（如你的第一个版本）。

---

### **总结**
- **推荐使用 `copy` 的版本**：逻辑清晰，适合大多数场景。
- 如果追求代码简洁，可以用修复后的 **Slice 拼接**，但需注意 `append` 的副作用。

> **关键教训**：在操作切片时，**避免在同一个逻辑块中混合多次 `append`**，除非你能确保切片长度的变化不会影响后续操作。