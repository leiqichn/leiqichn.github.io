---
title: 数据结构和操作的对比：Python vs. Go vs. C++
date: 2023-10-20 00:25:56
modificationDate: 2023 十月 20日 星期五 00:28:47
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---

# Python示例


```python
# 数组
my_list = [1, 2, 3, 4]

# 切片
sub_list = my_list[1:3]
reversed_list = my_list[::-1python]

# 字典
my_dict = {'name': 'Alice', 'age': 30}

# 双向链表（使用collections.deque）
from collections import deque
my_linked_list = deque()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

# 最大堆和最小堆（需要使用第三方库heapq）
import heapq
max_heap = []
min_heap = []

# 二叉树（使用类或结构体）

# 字符串操作
my_string = "Hello, World!"
substring = my_string[7:12]
my_int = 42
my_str = str(my_int)

# 深度拷贝和浅拷贝（使用copy模块）
import copy
original_list = [1, [2, 3], 4]
shallow_copy = copy.copy(original_list)
deep_copy = copy.deepcopy(original_list)

# 删除元素
my_list.pop(1)  # 删除第二个元素

# 查找小写字母
if my_string.islower():
    print("String contains only lowercase letters")

# 遍历数组
for item in my_list:
    print(item)

# 使用循环遍历字典
for key, value in my_dict.items():
    print(key, value)

# 判断字典是否包含键
if 'name' in my_dict:
    print("Dictionary contains 'name'")
```

# Go


```go
// Go示例

// 数组和切片
mySlice := []int{1, 2, 3, 4}
subSlice := mySlice[1:3]
reversedSlice := reverseSlice(mySlice)

// 字典
myMap := map[string]interface{}{
    "name": "Alice",
    "age": 30,
}

// 双向链表（使用container/list）
import "container/list"
myList := list.New()
myList.PushBack(1)
myList.PushBack(2)
myList.PushBack(3)

// 最大堆和最小堆（需要使用heap包）
import "container/heap"
maxHeap := &MaxHeap{}
minHeap := &MinHeap{}

// 二叉树（使用结构体或指针）

// 字符串操作
myString := "Hello, World!"
substring := myString[7:12]
myInt := 42
myStr := fmt.Sprintf("%d", myInt)

// 深度拷贝和浅拷贝（使用复制切片或递归）
originalSlice := []int{1, 2, 3, 4}
shallowCopy := make([]int, len(originalSlice))
copy(shallowCopy, originalSlice)
deepCopy := append([]int(nil), originalSlice...)

// 删除元素
index := 1
mySlice = append(mySlice[:index], mySlice[index+1:]...)

// 查找小写字母
containsLowercase := false
for _, char := range myString {
    if unicode.IsLower(char) {
        containsLowercase = true
        break
    }
}

// 遍历切片
for _, item := range mySlice {
    fmt.Println(item)
}

// 使用循环遍历字典
for key, value := range myMap {
    fmt.Println(key, value)
}

// 判断字典是否包含键
if _, exists := myMap["name"]; exists {
    fmt.Println("Map contains 'name'")
}
```

## C++


```cpp
// C++示例

// 数组和向量
#include <vector>
std::vector<int> myVector = {1, 2, 3, 4};
std::vector<int> subVector(myVector.begin() + 1, myVector.begin() + 3);
std::vector<int> reversedVector(myVector.rbegin(), myVector.rend());

// 字典（使用std::map）
#include <map>
std::map<std::string, int> myMap;
myMap["name"] = "Alice";
myMap["age"] = 30;

// 双向链表（使用std::list）
#include <list>
std::list<int> myList;
myList.push_back(1);
myList.push_back(2);
myList.push_back(3);

// 最大堆和最小堆（使用std::priority_queue）
#include <queue>
std::priority_queue<int> maxHeap;
std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;

// 二叉树（使用结构体或指针）

// 字符串操作
std::string myString = "Hello, World!";
std::string substring = myString.substr(7, 5);
int myInt = 42;
std::string myStr = std::to_string(myInt);

// 深度拷贝和浅拷贝
std::vector<int> originalVector = {1, 2, 3, 4};
std::vector<int> shallowCopy = originalVector;
std::vector<int> deepCopy(originalVector);

// 删除元素
int index = 1;
myVector.erase(myVector.begin() + index);

// 查找小写字母
bool containsLowercase = false;
for (char c : myString) {
    if (std::islower(c)) {
        containsLowercase = true;
        break;
    }
}

// 遍历向量
for (int item : myVector) {
    std::cout << item << std::endl;
}

// 使用循环遍历字典
for (const auto& pair : myMap) {
    std::cout << pair.first << " " << pair.second << std::endl;
}

// 判断字典是否包含键
if (myMap.find("name") != myMap.end()) {
    std::cout << "Map contains 'name'" << std::endl;
}
```
