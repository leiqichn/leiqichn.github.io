> Problem: [1726. 同积元组](https://leetcode.cn/problems/tuple-with-same-product/description/)

# 思路
>使用排列组合的方法，开始使用三种语言同时写leetcode.

# 解题方法
![](../../imgs/Pasted%20image%2020231020003943.png)
# 复杂度
- 时间复杂度:
> 添加时间复杂度, 示例： $O(n)$

- 空间复杂度:
> 添加空间复杂度, 示例： $O(n)$
  
# Code

```Go []
func tupleSameProduct(nums []int) int {
    n := len(nums)
    cnt := make(map[int]int)
    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {// j +1 不要重复
            cnt[nums[i] * nums[j]]++ // 使用map 遍历每次乘积对应次数
        }
    }
    ans := 0
    for _, v := range cnt {
        ans += v * (v - 1) * 4
    }
   
```
```C++ []
class Solution {
public:
    int tupleSameProduct(vector<int>& nums) {
        int n = nums.size();
        int ans = 0;
        unordered_map<int, int> cnt;
        for (int i = 0; i < n; i++) {
            for(int j = i + 1; j < n; j++) {
                cnt[nums[i] * nums[j]]++;
            }
        }
        for (auto &[k, v] : cnt) {
            ans += v * (v - 1) * 4;
        }
        return ans;
    }
};
```
```Python3 []
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maps = dict()
        
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]*nums[j] in maps:
                    maps[nums[i] * nums[j]] += 1
                else:
                    maps[nums[i] * nums[j]] = 1

        ans = 0
        for _, v in maps.items():
            ans += v*(v-1) *4
        return ans
```
  