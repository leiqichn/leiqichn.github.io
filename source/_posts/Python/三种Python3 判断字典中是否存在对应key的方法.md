---
title: 三种Python3 判断字典中是否存在对应key的方法
date: 2023-10-20 00:41:07
modificationDate: 2023 十月 20日 星期五 00:57:12
categories: 
	- Python
tags: []
sticky: []
hide: false
category_bar: true
---

# 第一种：使用get()方法
 **生成一个字典**

```
dict = {'name': '','age': '','sex': ''}
```

 **打印返回值**

```
print(dict.get('name'))  # 结果返回对应val
print(dict.get('id'))  # 结果返回None
```

第二种：使用keys()方法

 **生成一个字典**
dict = {'name': '','age': '','sex': ''}
 **判断是否存在，其中dict.keys()是列出字典所有的key**

```
print('name' in dict.keys())  # 结果返回True
print('id' in dict.keys())  # 结果返回False
```

除了使用in也可以使用not in，用于判定这个key不存在

第三种：使用 in 关键字

**生成一个字典**

```
dict = {'name': '','age': '','sex': ''}
```

**# 判断key是否存在于dict中**

```
print('name' in dict)  # 结果返回True
print('id' in dict)  # 结果返回False
```


# 补充：生成默认字典（`collections.defaultdict`）
使用`defaultdict(int)`来创建`maps`，它会自动初始化未存在的键为0，这样你无需手动检查键是否存在。普通的dict() 要判断key 不存在要赋初值。

```python
from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maps = defaultdict(int)
        
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                product = nums[i] * nums[j]
                ans += maps[product] * 4
                maps[product] += 1
                
        return ans
```
