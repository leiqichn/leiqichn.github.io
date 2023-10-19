---
title: 本地运行LeetCode的Python代码 调试
date: 2023-10-20 00:57:22
modificationDate: 2023 十月 20日 星期五 00:57:50
categories: 
	- Python
tags: []
sticky: []
hide: false
category_bar: true
---

最近打算开始捡起来python, 同时使用多种语言进行leetcode 训练，需要本地的调试环境，恰巧之前记录过如何在本地运行leetcode python。 大家一起来看看吧！看完就可以愉快的在本地coding啦

要在本地运行LeetCode的Python代码，你可以按照以下步骤创建一个Solution类：

创建一个Python文件（例如，leetcode_solution.py）来存放你的解决方案。

导入必要的模块。通常，你需要导入typing中的List，以及可能的其他模块，具体取决于问题的要求。

```python
from typing import List
```

创建Solution类并在其中定义问题的解决方案。例如：

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 实现你的解决方案
        # 例如，找到两个数的和等于目标，并返回它们的索引
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
        return []
```

创建一个main函数来测试你的解决方案。

```python
def main():
    solution = Solution()
    # 调用Solution类的方法进行测试
    result = solution.twoSum([2, 7, 11, 15], 9)
    print(result)
```


```python
if __name__ == "__main__":
    main()
```

执行你的Python脚本，可以使用命令行或你喜欢的Python集成开发环境（IDE）来运行。例如，使用命令行：

```sh
python leetcode_solution.py
```

这将运行你的解决方案并输出结果。你可以根据具体问题的要求来定义Solution类中的方法和逻辑，然后在main函数中进行测试。确保将问题的输入参数和返回值类型与LeetCode上的问题描述匹配。