---
title: 【基础知识】Golang  sort.Slice 复杂排序
date: 2024-11-24 12:47:52
modificationDate: 2024 十一月 24日 星期日 12:47:52
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---


在 Go 语言中，你可以使用 `sort.Slice` 对 `slice` 按照复杂条件进行排序。 `sort.Slice` 函数接受一个 `slice` 和一个比较函数，该比较函数定义了两个元素之间的排序关系。

以下是实现复杂条件排序的步骤和示例：

### 1. 基本语法

```go
sort.Slice(slice, func(i, j int) bool {
    // 比较 slice[i] 和 slice[j]
    return 条件
})
```

### 2. 示例：对结构体切片进行多条件排序

假设有一个包含多个 `Person` 的切片，我们希望按以下规则排序：

1. 年龄从小到大排序。
2. 如果年龄相同，则按名字的字母顺序排序。

```go
package main

import (
	"fmt"
	"sort"
)

type Person struct {
	Name string
	Age  int
}

func main() {
	people := []Person{
		{"Alice", 30},
		{"Bob", 25},
		{"Charlie", 30},
		{"Dave", 25},
	}

	// 使用 sort.Slice 按多个条件排序
	sort.Slice(people, func(i, j int) bool {
		// 优先按年龄排序
		if people[i].Age != people[j].Age {
			return people[i].Age < people[j].Age
		}
		// 如果年龄相同，则按名字排序
		return people[i].Name < people[j].Name
	})

	fmt.Println(people)
}
```

### 3. 更复杂条件：按多个字段权重排序

如果排序条件较为复杂，可以通过一个辅助函数生成比较结果。例如：

```go
package main

import (
	"fmt"
	"sort"
)

type Product struct {
	Name  string
	Price float64
	Rating int
}

func main() {
	products := []Product{
		{"Laptop", 1000, 5},
		{"Phone", 800, 4},
		{"Tablet", 800, 5},
		{"Watch", 400, 4},
	}

	// 按价格降序 -> 评分降序 -> 名称升序排序
	sort.Slice(products, func(i, j int) bool {
		// 按价格降序
		if products[i].Price != products[j].Price {
			return products[i].Price > products[j].Price
		}
		// 如果价格相同，按评分降序
		if products[i].Rating != products[j].Rating {
			return products[i].Rating > products[j].Rating
		}
		// 如果评分也相同，按名称升序
		return products[i].Name < products[j].Name
	})

	fmt.Println(products)
}
```

### 4. 注意事项

- 如果需要对不同的维度进行排序，可以考虑在比较函数中依次判断。
- `sort.Slice` 是不稳定的。如果需要稳定排序，可以使用 `sort.SliceStable`。
- 对于大数据排序，可以先构造权重或转换为单一排序值，减少比较复杂度。

通过 `sort.Slice` 的灵活性，可以轻松实现各种复杂条件的排序逻辑。