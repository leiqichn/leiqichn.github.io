---
title: golang 设计题
date: 2025-02-28 00:12:49
modificationDate: 2025 February 28th Friday 00:12:49
categories:
  - [编程语言, Golang]
tags: []
sticky: []
published: false
category_bar: true
---

要高效解决 LeetCode 的设计题（如设计 LRU 缓存、设计数据结构等），需要抓住 **问题建模、数据结构选择、接口设计、边界处理** 四大核心环节。以下是系统化的方法论和 Golang 实现技巧：

[【强化练习】更多经典设计习题 | labuladong 的算法笔记](https://labuladong.online/algo/problem-set/ds-design/)


# 基础
![](../../imgs/Pasted%20image%2020250304232815.png)
![](../../imgs/Pasted%20image%2020250304232749.png)

# 速成目录的题目列表

#### [链表双指针技巧](https://labuladong.online/algo/intro/quick-learning-plan/#%E9%93%BE%E8%A1%A8%E5%8F%8C%E6%8C%87%E9%92%88%E6%8A%80%E5%B7%A7)

| LeetCode                                                                                                                      | 力扣                                                                                                 | 难度  |
| ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | --- |
| [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/?show=1)                                    | [21. 合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists/?show=1)                        | 🟢  |
| [86. Partition List](https://leetcode.com/problems/partition-list/?show=1)                                                    | [86. 分隔链表](https://leetcode.cn/problems/partition-list/?show=1)                                    | 🟠  |
| [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/?show=1)                                        | [23. 合并K个升序链表](https://leetcode.cn/problems/merge-k-sorted-lists/?show=1)                          | 🔴  |
| [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/?show=1)                                             | [141. 环形链表](https://leetcode.cn/problems/linked-list-cycle/?show=1)                                | 🟢  |
| [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/?show=1)                                       | [142. 环形链表 II](https://leetcode.cn/problems/linked-list-cycle-ii/?show=1)                          | 🟠  |
| [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/?show=1)                             | [876. 链表的中间结点](https://leetcode.cn/problems/middle-of-the-linked-list/?show=1)                     | 🟢  |
| [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/?show=1)                | [19. 删除链表的倒数第 N 个结点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/?show=1)        | 🟠  |
| [160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/?show=1)               | [160. 相交链表](https://leetcode.cn/problems/intersection-of-two-linked-lists/?show=1)                 | 🟢  |
| [264. Ugly Number II](https://leetcode.com/problems/ugly-number-ii/?show=1)                                                   | [264. 丑数 II](https://leetcode.cn/problems/ugly-number-ii/?show=1)                                  | 🟠  |
| [378. Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/?show=1) | [378. 有序矩阵中第 K 小的元素](https://leetcode.cn/problems/kth-smallest-element-in-a-sorted-matrix/?show=1) | 🟠  |
| [373. Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/?show=1)                 | [373. 查找和最小的 K 对数字](https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/?show=1)          | 🟠  |
| [82. Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/?show=1)      | [82. 删除排序链表中的重复元素 II](https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/?show=1)  | 🟠  |
| [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/?show=1)                                                   | [2. 两数相加](https://leetcode.cn/problems/add-two-numbers/?show=1)                                    | 🟠  |
| [445. Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/?show=1)                                           | [445. 两数相加 II](https://leetcode.cn/problems/add-two-numbers-ii/?show=1)                            | 🟠  |
|                                                                                                                               |                                                                                                    |     |

#### [递归操作链表](https://labuladong.online/algo/intro/quick-learning-plan/#%E9%80%92%E5%BD%92%E6%93%8D%E4%BD%9C%E9%93%BE%E8%A1%A8)

|LeetCode|力扣|难度|
|---|---|---|
|[234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/?show=1)|[234. 回文链表](https://leetcode.cn/problems/palindrome-linked-list/?show=1)|🟢|
|[206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/?show=1)|[206. 反转链表](https://leetcode.cn/problems/reverse-linked-list/?show=1)|🟢|
|[92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/?show=1)|[92. 反转链表 II](https://leetcode.cn/problems/reverse-linked-list-ii/?show=1)|🟠|
|[25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/?show=1)|[25. K 个一组翻转链表](https://leetcode.cn/problems/reverse-nodes-in-k-group/?show=1)|🔴|

#### [数组双指针技巧](https://labuladong.online/algo/intro/quick-learning-plan/#%E6%95%B0%E7%BB%84%E5%8F%8C%E6%8C%87%E9%92%88%E6%8A%80%E5%B7%A7)

|LeetCode|力扣|难度|
|---|---|---|
|[26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/?show=1)|[26. 删除有序数组中的重复项](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/?show=1)|🟢|
|[83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/?show=1)|[83. 删除排序链表中的重复元素](https://leetcode.cn/problems/remove-duplicates-from-sorted-list/?show=1)|🟢|
|[27. Remove Element](https://leetcode.com/problems/remove-element/?show=1)|[27. 移除元素](https://leetcode.cn/problems/remove-element/?show=1)|🟢|
|[283. Move Zeroes](https://leetcode.com/problems/move-zeroes/?show=1)|[283. 移动零](https://leetcode.cn/problems/move-zeroes/?show=1)|🟢|
|[167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?show=1)|[167. 两数之和 II - 输入有序数组](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/?show=1)|🟠|
|[344. Reverse String](https://leetcode.com/problems/reverse-string/?show=1)|[344. 反转字符串](https://leetcode.cn/problems/reverse-string/?show=1)|🟢|
|[5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/?show=1)|[5. 最长回文子串](https://leetcode.cn/problems/longest-palindromic-substring/?show=1)|🟠|
|[80. Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?show=1)|[80. 删除有序数组中的重复项 II](https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/?show=1)|🟠|
|[125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/?show=1)|[125. 验证回文串](https://leetcode.cn/problems/valid-palindrome/?show=1)|🟢|
|[75. Sort Colors](https://leetcode.com/problems/sort-colors/?show=1)|[75. 颜色分类](https://leetcode.cn/problems/sort-colors/?show=1)|🟠|
|[88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/?show=1)|[88. 合并两个有序数组](https://leetcode.cn/problems/merge-sorted-array/?show=1)|🟢|
|[977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/?show=1)|[977. 有序数组的平方](https://leetcode.cn/problems/squares-of-a-sorted-array/?show=1)|🟢|

#### [二维数组操作技巧](https://labuladong.online/algo/intro/quick-learning-plan/#%E4%BA%8C%E7%BB%B4%E6%95%B0%E7%BB%84%E6%93%8D%E4%BD%9C%E6%8A%80%E5%B7%A7)

|LeetCode|力扣|难度|
|---|---|---|
|[151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/?show=1)|[151. 反转字符串中的单词](https://leetcode.cn/problems/reverse-words-in-a-string/?show=1)|🟠|
|[48. Rotate Image](https://leetcode.com/problems/rotate-image/?show=1)|[48. 旋转图像](https://leetcode.cn/problems/rotate-image/?show=1)|🟠|
|[54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/?show=1)|[54. 螺旋矩阵](https://leetcode.cn/problems/spiral-matrix/?show=1)|🟠|
|[59. Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/?show=1)|[59. 螺旋矩阵 II](https://leetcode.cn/problems/spiral-matrix-ii/?show=1)|🟠|
|[1329. Sort the Matrix Diagonally](https://leetcode.com/problems/sort-the-matrix-diagonally/?show=1)|[1329. 将矩阵按对角线排序](https://leetcode.cn/problems/sort-the-matrix-diagonally/?show=1)|🟠|
|[1260. Shift 2D Grid](https://leetcode.com/problems/shift-2d-grid/?show=1)|[1260. 二维网格迁移](https://leetcode.cn/problems/shift-2d-grid/?show=1)|🟢|
|[867. Transpose Matrix](https://leetcode.com/problems/transpose-matrix/?show=1)|[867. 转置矩阵](https://leetcode.cn/problems/transpose-matrix/?show=1)|🟢|
|[14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/?show=1)|[14. 最长公共前缀](https://leetcode.cn/problems/longest-common-prefix/?show=1)|🟢|

#### [滑动窗口算法](https://labuladong.online/algo/intro/quick-learning-plan/#%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E7%AE%97%E6%B3%95)

|LeetCode|力扣|难度|
|---|---|---|
|[76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/?show=1)|[76. 最小覆盖子串](https://leetcode.cn/problems/minimum-window-substring/?show=1)|🔴|
|[567. Permutation in String](https://leetcode.com/problems/permutation-in-string/?show=1)|[567. 字符串的排列](https://leetcode.cn/problems/permutation-in-string/?show=1)|🟠|
|[438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/?show=1)|[438. 找到字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/?show=1)|🟠|
|[3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/?show=1)|[3. 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/?show=1)|🟠|
|[1658. Minimum Operations to Reduce X to Zero](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/?show=1)|[1658. 将 x 减到 0 的最小操作数](https://leetcode.cn/problems/minimum-operations-to-reduce-x-to-zero/?show=1)|🟠|
|[713. Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/?show=1)|[713. 乘积小于 K 的子数组](https://leetcode.cn/problems/subarray-product-less-than-k/?show=1)|🟠|
|[219. Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/?show=1)|[219. 存在重复元素 II](https://leetcode.cn/problems/contains-duplicate-ii/?show=1)|🟢|
|[220. Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/?show=1)|[220. 存在重复元素 III](https://leetcode.cn/problems/contains-duplicate-iii/?show=1)|🔴|
|[209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/?show=1)|[209. 长度最小的子数组](https://leetcode.cn/problems/minimum-size-subarray-sum/?show=1)|🟠|

#### [二分搜索算法](https://labuladong.online/algo/intro/quick-learning-plan/#%E4%BA%8C%E5%88%86%E6%90%9C%E7%B4%A2%E7%AE%97%E6%B3%95)

|LeetCode|力扣|难度|
|---|---|---|
|[704. Binary Search](https://leetcode.com/problems/binary-search/?show=1)|[704. 二分查找](https://leetcode.cn/problems/binary-search/?show=1)|🟢|
|[34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/?show=1)|[34. 在排序数组中查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/?show=1)|🟠|
|[875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/?show=1)|[875. 爱吃香蕉的珂珂](https://leetcode.cn/problems/koko-eating-bananas/?show=1)|🟠|
|[1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/?show=1)|[1011. 在 D 天内送达包裹的能力](https://leetcode.cn/problems/capacity-to-ship-packages-within-d-days/?show=1)|🟠|
|[410. Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/?show=1)|[410. 分割数组的最大值](https://leetcode.cn/problems/split-array-largest-sum/?show=1)|🔴|

#### [前缀和/差分技巧](https://labuladong.online/algo/intro/quick-learning-plan/#%E5%89%8D%E7%BC%80%E5%92%8C-%E5%B7%AE%E5%88%86%E6%8A%80%E5%B7%A7)

|LeetCode|力扣|难度|
|---|---|---|
|[303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/?show=1)|[303. 区域和检索 - 数组不可变](https://leetcode.cn/problems/range-sum-query-immutable/?show=1)|🟢|
|[304. Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/?show=1)|[304. 二维区域和检索 - 矩阵不可变](https://leetcode.cn/problems/range-sum-query-2d-immutable/?show=1)|🟠|
|[1109. Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/?show=1)|[1109. 航班预订统计](https://leetcode.cn/problems/corporate-flight-bookings/?show=1)|🟠|
|[1094. Car Pooling](https://leetcode.com/problems/car-pooling/?show=1)|[1094. 拼车](https://leetcode.cn/problems/car-pooling/?show=1)|🟠|

#### [栈](https://labuladong.online/algo/intro/quick-learning-plan/#%E6%A0%88)

|LeetCode|力扣|难度|
|---|---|---|
|[71. Simplify Path](https://leetcode.com/problems/simplify-path/?show=1)|[71. 简化路径](https://leetcode.cn/problems/simplify-path/?show=1)|🟠|
|[143. Reorder List](https://leetcode.com/problems/reorder-list/?show=1)|[143. 重排链表](https://leetcode.cn/problems/reorder-list/?show=1)|🟠|
|[20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/?show=1)|[20. 有效的括号](https://leetcode.cn/problems/valid-parentheses/?show=1)|🟢|
|[150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/?show=1)|[150. 逆波兰表达式求值](https://leetcode.cn/problems/evaluate-reverse-polish-notation/?show=1)|🟠|
|[225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/?show=1)|[225. 用队列实现栈](https://leetcode.cn/problems/implement-stack-using-queues/?show=1)|🟢|
|[388. Longest Absolute File Path](https://leetcode.com/problems/longest-absolute-file-path/?show=1)|[388. 文件的最长绝对路径](https://leetcode.cn/problems/longest-absolute-file-path/?show=1)|🟠|

#### [队列](https://labuladong.online/algo/intro/quick-learning-plan/#%E9%98%9F%E5%88%97)

|LeetCode|力扣|难度|
|---|---|---|
|[933. Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/?show=1)|[933. 最近的请求次数](https://leetcode.cn/problems/number-of-recent-calls/?show=1)|🟢|
|[622. Design Circular Queue](https://leetcode.com/problems/design-circular-queue/?show=1)|[622. 设计循环队列](https://leetcode.cn/problems/design-circular-queue/?show=1)|🟠|
|[641. Design Circular Deque](https://leetcode.com/problems/design-circular-deque/?show=1)|[641. 设计循环双端队列](https://leetcode.cn/problems/design-circular-deque/?show=1)|🟠|
|[1670. Design Front Middle Back Queue](https://leetcode.com/problems/design-front-middle-back-queue/?show=1)|[1670. 设计前中后队列](https://leetcode.cn/problems/design-front-middle-back-queue/?show=1)|🟠|
|[2073. Time Needed to Buy Tickets](https://leetcode.com/problems/time-needed-to-buy-tickets/?show=1)|[2073. 买票需要的时间](https://leetcode.cn/problems/time-needed-to-buy-tickets/?show=1)|🟢|

#### [单调栈技巧](https://labuladong.online/algo/intro/quick-learning-plan/#%E5%8D%95%E8%B0%83%E6%A0%88%E6%8A%80%E5%B7%A7)

|LeetCode|力扣|难度|
|---|---|---|
|[1019. Next Greater Node In Linked List](https://leetcode.com/problems/next-greater-node-in-linked-list/?show=1)|[1019. 链表中的下一个更大节点](https://leetcode.cn/problems/next-greater-node-in-linked-list/?show=1)|🟠|
|[1944. Number of Visible People in a Queue](https://leetcode.com/problems/number-of-visible-people-in-a-queue/?show=1)|[1944. 队列中可以看到的人数](https://leetcode.cn/problems/number-of-visible-people-in-a-queue/?show=1)|🔴|
|[1475. Final Prices With a Special Discount in a Shop](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/?show=1)|[1475. 商品折扣后的最终价格](https://leetcode.cn/problems/final-prices-with-a-special-discount-in-a-shop/?show=1)|🟢|
|[901. Online Stock Span](https://leetcode.com/problems/online-stock-span/?show=1)|[901. 股票价格跨度](https://leetcode.cn/problems/online-stock-span/?show=1)|🟠|
|[402. Remove K Digits](https://leetcode.com/problems/remove-k-digits/?show=1)|[402. 移掉 K 位数字](https://leetcode.cn/problems/remove-k-digits/?show=1)|🟠|
|[853. Car Fleet](https://leetcode.com/problems/car-fleet/?show=1)|[853. 车队](https://leetcode.cn/problems/car-fleet/?show=1)|🟠|
|[581. Shortest Unsorted Continuous Subarray](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/?show=1)|[581. 最短无序连续子数组](https://leetcode.cn/problems/shortest-unsorted-continuous-subarray/?show=1)|🟠|

#### [单调队列技巧](https://labuladong.online/algo/intro/quick-learning-plan/#%E5%8D%95%E8%B0%83%E9%98%9F%E5%88%97%E6%8A%80%E5%B7%A7)

|LeetCode|力扣|难度|
|---|---|---|
|[239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/?show=1)|[239. 滑动窗口最大值](https://leetcode.cn/problems/sliding-window-maximum/?show=1)|🔴|
|[1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/?show=1)|[1438. 绝对差不超过限制的最长连续子数组](https://leetcode.cn/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/?show=1)|🟠|
|[862. Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/?show=1)|[862. 和至少为 K 的最短子数组](https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k/?show=1)|🔴|
|[918. Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/?show=1)|[918. 环形子数组的最大和](https://leetcode.cn/problems/maximum-sum-circular-subarray/?show=1)|🟠|

#### [二叉树](https://labuladong.online/algo/intro/quick-learning-plan/#%E4%BA%8C%E5%8F%89%E6%A0%91)

|LeetCode|力扣|难度|
|---|---|---|
|[226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/?show=1)|[226. 翻转二叉树](https://leetcode.cn/problems/invert-binary-tree/?show=1)|🟢|
|[114. Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/?show=1)|[114. 二叉树展开为链表](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/?show=1)|🟠|
|[116. Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/?show=1)|[116. 填充每个节点的下一个右侧节点指针](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/?show=1)|🟠|
|[654. Maximum Binary Tree](https://leetcode.com/problems/maximum-binary-tree/?show=1)|[654. 最大二叉树](https://leetcode.cn/problems/maximum-binary-tree/?show=1)|🟠|
|[105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/?show=1)|[105. 从前序与中序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/?show=1)|🟠|
|[106. Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/?show=1)|[106. 从中序与后序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/?show=1)|🟠|
|[889. Construct Binary Tree from Preorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/?show=1)|[889. 根据前序和后序遍历构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-postorder-traversal/?show=1)|🟠|
|[297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/?show=1)|[297. 二叉树的序列化与反序列化](https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/?show=1)|🔴|
|[236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/?show=1)|[236. 二叉树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/?show=1)|🟠|
|[235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/?show=1)|[235. 二叉搜索树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/?show=1)|🟠|
|[222. Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/?show=1)|[222. 完全二叉树的节点个数](https://leetcode.cn/problems/count-complete-tree-nodes/?show=1)|🟠|

#### [二叉搜索树](https://labuladong.online/algo/intro/quick-learning-plan/#%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91)

|LeetCode|力扣|难度|
|---|---|---|
|[230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/?show=1)|[230. 二叉搜索树中第K小的元素](https://leetcode.cn/problems/kth-smallest-element-in-a-bst/?show=1)|🟠|
|[538. Convert BST to Greater Tree](https://leetcode.com/problems/convert-bst-to-greater-tree/?show=1)|[538. 把二叉搜索树转换为累加树](https://leetcode.cn/problems/convert-bst-to-greater-tree/?show=1)|🟠|
|[1038. Binary Search Tree to Greater Sum Tree](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/?show=1)|[1038. 从二叉搜索树到更大和树](https://leetcode.cn/problems/binary-search-tree-to-greater-sum-tree/?show=1)|🟠|
|[450. Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/?show=1)|[450. 删除二叉搜索树中的节点](https://leetcode.cn/problems/delete-node-in-a-bst/?show=1)|🟠|
|[701. Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/?show=1)|[701. 二叉搜索树中的插入操作](https://leetcode.cn/problems/insert-into-a-binary-search-tree/?show=1)|🟠|
|[700. Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/?show=1)|[700. 二叉搜索树中的搜索](https://leetcode.cn/problems/search-in-a-binary-search-tree/?show=1)|🟢|
|[98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/?show=1)|[98. 验证二叉搜索树](https://leetcode.cn/problems/validate-binary-search-tree/?show=1)|🟠|
|[96. Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/?show=1)|[96. 不同的二叉搜索树](https://leetcode.cn/problems/unique-binary-search-trees/?show=1)|🟠|
|[95. Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/?show=1)|[95. 不同的二叉搜索树 II](https://leetcode.cn/problems/unique-binary-search-trees-ii/?show=1)|🟠|

#### [数据结构设计](https://labuladong.online/algo/intro/quick-learning-plan/#%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E8%AE%BE%E8%AE%A1)

|LeetCode|力扣|难度|
|---|---|---|
|[146. LRU Cache](https://leetcode.com/problems/lru-cache/?show=1)|[146. LRU 缓存](https://leetcode.cn/problems/lru-cache/?show=1)|🟠|
|[460. LFU Cache](https://leetcode.com/problems/lfu-cache/?show=1)|[460. LFU 缓存](https://leetcode.cn/problems/lfu-cache/?show=1)|🔴|
|[729. My Calendar I](https://leetcode.com/problems/my-calendar-i/?show=1)|[729. 我的日程安排表 I](https://leetcode.cn/problems/my-calendar-i/?show=1)|🟠|
|[950. Reveal Cards In Increasing Order](https://leetcode.com/problems/reveal-cards-in-increasing-order/?show=1)|[950. 按递增顺序显示卡牌](https://leetcode.cn/problems/reveal-cards-in-increasing-order/?show=1)|🟠|
|[1700. Number of Students Unable to Eat Lunch](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/?show=1)|[1700. 无法吃午餐的学生数量](https://leetcode.cn/problems/number-of-students-unable-to-eat-lunch/?show=1)|🟢|
|[155. Min Stack](https://leetcode.com/problems/min-stack/?show=1)|[155. 最小栈](https://leetcode.cn/problems/min-stack/?show=1)|🟠|
|[1670. Design Front Middle Back Queue](https://leetcode.com/problems/design-front-middle-back-queue/?show=1)|[1670. 设计前中后队列](https://leetcode.cn/problems/design-front-middle-back-queue/?show=1)|🟠|
|[895. Maximum Frequency Stack](https://leetcode.com/problems/maximum-frequency-stack/?show=1)|[895. 最大频率栈](https://leetcode.cn/problems/maximum-frequency-stack/?show=1)|🔴|
|[224. Basic Calculator](https://leetcode.com/problems/basic-calculator/?show=1)|[224. 基本计算器](https://leetcode.cn/problems/basic-calculator/?show=1)|🔴|
|[227. Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/?show=1)|[227. 基本计算器 II](https://leetcode.cn/problems/basic-calculator-ii/?show=1)|🟠|

#### [图相关算法](https://labuladong.online/algo/intro/quick-learning-plan/#%E5%9B%BE%E7%9B%B8%E5%85%B3%E7%AE%97%E6%B3%95)

|LeetCode|力扣|难度|
|---|---|---|
|[207. Course Schedule](https://leetcode.com/problems/course-schedule/?show=1)|[207. 课程表](https://leetcode.cn/problems/course-schedule/?show=1)|🟠|
|[210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/?show=1)|[210. 课程表 II](https://leetcode.cn/problems/course-schedule-ii/?show=1)|🟠|
|[990. Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/?show=1)|[990. 等式方程的可满足性](https://leetcode.cn/problems/satisfiability-of-equality-equations/?show=1)|🟠|
|[684. Redundant Connection](https://leetcode.com/problems/redundant-connection/?show=1)|[684. 冗余连接](https://leetcode.cn/problems/redundant-connection/?show=1)|🟠|
|[1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/?show=1)|[1584. 连接所有点的最小费用](https://leetcode.cn/problems/min-cost-to-connect-all-points/?show=1)|🟠|
|[743. Network Delay Time](https://leetcode.com/problems/network-delay-time/?show=1)|[743. 网络延迟时间](https://leetcode.cn/problems/network-delay-time/?show=1)|🟠|
|[1631. Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/?show=1)|[1631. 最小体力消耗路径](https://leetcode.cn/problems/path-with-minimum-effort/?show=1)|🟠|
|[1514. Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/?show=1)|[1514. 概率最大的路径](https://leetcode.cn/problems/path-with-maximum-probability/?show=1)|🟠|

#### [DFS/回溯算法](https://labuladong.online/algo/intro/quick-learning-plan/#dfs-%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95)

|LeetCode|力扣|难度|
|---|---|---|
|[78. Subsets](https://leetcode.com/problems/subsets/?show=1)|[78. 子集](https://leetcode.cn/problems/subsets/?show=1)|🟠|
|[90. Subsets II](https://leetcode.com/problems/subsets-ii/?show=1)|[90. 子集 II](https://leetcode.cn/problems/subsets-ii/?show=1)|🟠|
|[77. Combinations](https://leetcode.com/problems/combinations/?show=1)|[77. 组合](https://leetcode.cn/problems/combinations/?show=1)|🟠|
|[39. Combination Sum](https://leetcode.com/problems/combination-sum/?show=1)|[39. 组合总和](https://leetcode.cn/problems/combination-sum/?show=1)|🟠|
|[40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/?show=1)|[40. 组合总和 II](https://leetcode.cn/problems/combination-sum-ii/?show=1)|🟠|
|[216. Combination Sum III](https://leetcode.com/problems/combination-sum-iii/?show=1)|[216. 组合总和 III](https://leetcode.cn/problems/combination-sum-iii/?show=1)|🟠|
|[46. Permutations](https://leetcode.com/problems/permutations/?show=1)|[46. 全排列](https://leetcode.cn/problems/permutations/?show=1)|🟠|
|[47. Permutations II](https://leetcode.com/problems/permutations-ii/?show=1)|[47. 全排列 II](https://leetcode.cn/problems/permutations-ii/?show=1)|🟠|
|[37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/?show=1)|[37. 解数独](https://leetcode.cn/problems/sudoku-solver/?show=1)|🔴|
|[51. N-Queens](https://leetcode.com/problems/n-queens/?show=1)|[51. N 皇后](https://leetcode.cn/problems/n-queens/?show=1)|🔴|
|[52. N-Queens II](https://leetcode.com/problems/n-queens-ii/?show=1)|[52. N皇后 II](https://leetcode.cn/problems/n-queens-ii/?show=1)|🔴|
|[200. Number of Islands](https://leetcode.com/problems/number-of-islands/?show=1)|[200. 岛屿数量](https://leetcode.cn/problems/number-of-islands/?show=1)|🟠|
|[1254. Number of Closed Islands](https://leetcode.com/problems/number-of-closed-islands/?show=1)|[1254. 统计封闭岛屿的数目](https://leetcode.cn/problems/number-of-closed-islands/?show=1)|🟠|
|[695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/?show=1)|[695. 岛屿的最大面积](https://leetcode.cn/problems/max-area-of-island/?show=1)|🟠|
|[1905. Count Sub Islands](https://leetcode.com/problems/count-sub-islands/?show=1)|[1905. 统计子岛屿](https://leetcode.cn/problems/count-sub-islands/?show=1)|🟠|
|[967. Numbers With Same Consecutive Differences](https://leetcode.com/problems/numbers-with-same-consecutive-differences/?show=1)|[967. 连续差相同的数字](https://leetcode.cn/problems/numbers-with-same-consecutive-differences/?show=1)|🟠|
|[491. Non-decreasing Subsequences](https://leetcode.com/problems/non-decreasing-subsequences/?show=1)|[491. 递增子序列](https://leetcode.cn/problems/non-decreasing-subsequences/?show=1)|🟠|
|[980. Unique Paths III](https://leetcode.com/problems/unique-paths-iii/?show=1)|[980. 不同路径 III](https://leetcode.cn/problems/unique-paths-iii/?show=1)|🔴|
|[131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/?show=1)|[131. 分割回文串](https://leetcode.cn/problems/palindrome-partitioning/?show=1)|🟠|
|[93. Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/?show=1)|[93. 复原 IP 地址](https://leetcode.cn/problems/restore-ip-addresses/?show=1)|🟠|
|[17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/?show=1)|[17. 电话号码的字母组合](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/?show=1)|🟠|
|[79. Word Search](https://leetcode.com/problems/word-search/?show=1)|[79. 单词搜索](https://leetcode.cn/problems/word-search/?show=1)|🟠|

#### [BFS 算法](https://labuladong.online/algo/intro/quick-learning-plan/#bfs-%E7%AE%97%E6%B3%95)

|LeetCode|力扣|难度|
|---|---|---|
|[752. Open the Lock](https://leetcode.com/problems/open-the-lock/?show=1)|[752. 打开转盘锁](https://leetcode.cn/problems/open-the-lock/?show=1)|🟠|
|[773. Sliding Puzzle](https://leetcode.com/problems/sliding-puzzle/?show=1)|[773. 滑动谜题](https://leetcode.cn/problems/sliding-puzzle/?show=1)|🔴|
|[919. Complete Binary Tree Inserter](https://leetcode.com/problems/complete-binary-tree-inserter/?show=1)|[919. 完全二叉树插入器](https://leetcode.cn/problems/complete-binary-tree-inserter/?show=1)|🟠|
|[841. Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/?show=1)|[841. 钥匙和房间](https://leetcode.cn/problems/keys-and-rooms/?show=1)|🟠|
|[433. Minimum Genetic Mutation](https://leetcode.com/problems/minimum-genetic-mutation/?show=1)|[433. 最小基因变化](https://leetcode.cn/problems/minimum-genetic-mutation/?show=1)|🟠|
|[1926. Nearest Exit from Entrance in Maze](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/?show=1)|[1926. 迷宫中离入口最近的出口](https://leetcode.cn/problems/nearest-exit-from-entrance-in-maze/?show=1)|🟠|
|[1091. Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/?show=1)|[1091. 二进制矩阵中的最短路径](https://leetcode.cn/problems/shortest-path-in-binary-matrix/?show=1)|🟠|
|[994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/?show=1)|[994. 腐烂的橘子](https://leetcode.cn/problems/rotting-oranges/?show=1)|🟠|
|[721. Accounts Merge](https://leetcode.com/problems/accounts-merge/?show=1)|[721. 账户合并](https://leetcode.cn/problems/accounts-merge/?show=1)|🟠|
|[127. Word Ladder](https://leetcode.com/problems/word-ladder/?show=1)|[127. 单词接龙](https://leetcode.cn/problems/word-ladder/?show=1)|🔴|
|[365. Water and Jug Problem](https://leetcode.com/problems/water-and-jug-problem/?show=1)|[365. 水壶问题](https://leetcode.cn/problems/water-and-jug-problem/?show=1)|🟠|

#### [动态规划](https://labuladong.online/algo/intro/quick-learning-plan/#%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92)

|LeetCode|力扣|难度|
|---|---|---|
|[509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/?show=1)|[509. 斐波那契数](https://leetcode.cn/problems/fibonacci-number/?show=1)|🟢|
|[322. Coin Change](https://leetcode.com/problems/coin-change/?show=1)|[322. 零钱兑换](https://leetcode.cn/problems/coin-change/?show=1)|🟠|
|[300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/?show=1)|[300. 最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/?show=1)|🟠|
|[354. Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/?show=1)|[354. 俄罗斯套娃信封问题](https://leetcode.cn/problems/russian-doll-envelopes/?show=1)|🔴|
|[72. Edit Distance](https://leetcode.com/problems/edit-distance/?show=1)|[72. 编辑距离](https://leetcode.cn/problems/edit-distance/?show=1)|🔴|
|[53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/?show=1)|[53. 最大子数组和](https://leetcode.cn/problems/maximum-subarray/?show=1)|🟠|
|[1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/?show=1)|[1143. 最长公共子序列](https://leetcode.cn/problems/longest-common-subsequence/?show=1)|🟠|
|[583. Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/?show=1)|[583. 两个字符串的删除操作](https://leetcode.cn/problems/delete-operation-for-two-strings/?show=1)|🟠|
|[712. Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/?show=1)|[712. 两个字符串的最小ASCII删除和](https://leetcode.cn/problems/minimum-ascii-delete-sum-for-two-strings/?show=1)|🟠|
|[416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/?show=1)|[416. 分割等和子集](https://leetcode.cn/problems/partition-equal-subset-sum/?show=1)|🟠|
|[518. Coin Change II](https://leetcode.com/problems/coin-change-ii/?show=1)|[518. 零钱兑换 II](https://leetcode.cn/problems/coin-change-ii/?show=1)|🟠|

#### [贪心算法](https://labuladong.online/algo/intro/quick-learning-plan/#%E8%B4%AA%E5%BF%83%E7%AE%97%E6%B3%95)

|LeetCode|力扣|难度|
|---|---|---|
|[55. Jump Game](https://leetcode.com/problems/jump-game/?show=1)|[55. 跳跃游戏](https://leetcode.cn/problems/jump-game/?show=1)|🟠|
|[45. Jump Game II](https://leetcode.com/problems/jump-game-ii/?show=1)|[45. 跳跃游戏 II](https://leetcode.cn/problems/jump-game-ii/?show=1)|🟠|
|[134. Gas Station](https://leetcode.com/problems/gas-station/?show=1)|[134. 加油站](https://leetcode.cn/problems/gas-station/?show=1)|🟠|

#### [分治算法](https://labuladong.online/algo/intro/quick-learning-plan/#%E5%88%86%E6%B2%BB%E7%AE%97%E6%B3%95)

|LeetCode|力扣|难度|
|---|---|---|
|[23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/?show=1)|[23. 合并K个升序链表](https://leetcode.cn/problems/merge-k-sorted-lists/?show=1)|🔴|
|[241. Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/?show=1)|[241. 为运算表达式设计优先级](https://leetcode.cn/problems/different-ways-to-add-parentheses/?show=1)|🟠|

#### [数学算法](https://labuladong.online/algo/intro/quick-learning-plan/#%E6%95%B0%E5%AD%A6%E7%AE%97%E6%B3%95)

|LeetCode|力扣|难度|
|---|---|---|
|[292. Nim Game](https://leetcode.com/problems/nim-game/?show=1)|[292. Nim 游戏](https://leetcode.cn/problems/nim-game/?show=1)|🟢|
|[877. Stone Game](https://leetcode.com/problems/stone-game/?show=1)|[877. 石子游戏](https://leetcode.cn/problems/stone-game/?show=1)|🟠|
|[319. Bulb Switcher](https://leetcode.com/problems/bulb-switcher/?show=1)|[319. 灯泡开关](https://leetcode.cn/problems/bulb-switcher/?show=1)|🟠|
|[382. Linked List Random Node](https://leetcode.com/problems/linked-list-random-node/?show=1)|[382. 链表随机节点](https://leetcode.cn/problems/linked-list-random-node/?show=1)|🟠|
|[398. Random Pick Index](https://leetcode.com/problems/random-pick-index/?show=1)|[398. 随机数索引](https://leetcode.cn/problems/random-pick-index/?show=1)|🟠|
|[384. Shuffle an Array](https://leetcode.com/problems/shuffle-an-array/?show=1)|[384. 打乱数组](https://leetcode.cn/problems/shuffle-an-array/?show=1)|🟠|
|[204. Count Primes](https://leetcode.com/problems/count-primes/?show=1)|[204. 计数质数](https://leetcode.cn/problems/count-primes/?show=1)|🟠|
|[372. Super Pow](https://leetcode.com/problems/super-pow/?show=1)|[372. 超级次方](https://leetcode.cn/problems/super-pow/?show=1)|🟠|

#### [其他经典面试题](https://labuladong.online/algo/intro/quick-learning-plan/#%E5%85%B6%E4%BB%96%E7%BB%8F%E5%85%B8%E9%9D%A2%E8%AF%95%E9%A2%98)

|LeetCode|力扣|难度|
|---|---|---|
|[42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/?show=1)|[42. 接雨水](https://leetcode.cn/problems/trapping-rain-water/?show=1)|🔴|
|[11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/?show=1)|[11. 盛最多水的容器](https://leetcode.cn/problems/container-with-most-water/?show=1)|🟠|
|[263. Ugly Number](https://leetcode.com/problems/ugly-number/?show=1)|[263. 丑数](https://leetcode.cn/problems/ugly-number/?show=1)|🟢|
|[264. Ugly Number II](https://leetcode.com/problems/ugly-number-ii/?show=1)|[264. 丑数 II](https://leetcode.cn/problems/ugly-number-ii/?show=1)|🟠|
|[1201. Ugly Number III](https://leetcode.com/problems/ugly-number-iii/?show=1)|[1201. 丑数 III](https://leetcode.cn/problems/ugly-number-iii/?show=1)|🟠|
|[313. Super Ugly Number](https://leetcode.com/problems/super-ugly-number/?show=1)|[313. 超级丑数](https://leetcode.cn/problems/super-ugly-number/?show=1)|🟠|
|[528. Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/?show=1)|[528. 按权重随机选择](https://leetcode.cn/problems/random-pick-with-weight/?show=1)|🟠|
|[1. Two Sum](https://leetcode.com/problems/two-sum/?show=1)|[1. 两数之和](https://leetcode.cn/problems/two-sum/?show=1)|🟢|
|[167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?show=1)|[167. 两数之和 II - 输入有序数组](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/?show=1)|🟠|
|[15. 3Sum](https://leetcode.com/problems/3sum/?show=1)|[15. 三数之和](https://leetcode.cn/problems/3sum/?show=1)|🟠|
|[18. 4Sum](https://leetcode.com/problems/4sum/?show=1)|[18. 四数之和](https://leetcode.cn/problems/4sum/?show=1)|🟠|

# 刷题范围
![](../../imgs/Pasted%20image%2020250304232540.png)
![](../../imgs/Pasted%20image%2020250304232604.png)
![](../../imgs/Pasted%20image%2020250304232633.png)
![](../../imgs/Pasted%20image%2020250304232518.png)

![](../../imgs/Pasted%20image%2020250304232719.png)
---

### **一、设计题解题方法论**
#### 1. **理解问题本质（5分钟）**
   - **明确需求**：将题目抽象为实际系统问题（如 LRU = 缓存淘汰策略 + 快速查询）
   - **输入输出**：明确操作接口（如 `Get(key)`, `Put(key, value)`）
   - **约束条件**：容量限制、时间复杂度要求（如 O(1) 的 Get/Put）

#### 2. **设计数据结构（核心！）**
   - **经典组合**：
     - **哈希表 + 双向链表**：用于 LRU（哈希表快速定位，链表维护顺序）
     - **前缀树（Trie）**：处理字符串匹配（如实现字典树）
     - **堆（优先队列）**：用于实时获取最大值/最小值（如设计股票交易系统）
   - **Golang 选择**：
     ```go
     // 哈希表用 map
     cache := make(map[int]*ListNode)
     // 双向链表自定义结构体
     type ListNode struct {
         Key, Val  int
         Prev, Next *ListNode
     }
     ```

#### 3. **接口与方法拆分**
   - **面向对象设计**：定义结构体（类）和方法
     ```go
     type LRUCache struct {
         capacity int
         cache    map[int]*ListNode
         head, tail *ListNode // 虚拟头尾节点简化操作
     }
     
     func Constructor(capacity int) LRUCache { /* 初始化 */ }
     func (this *LRUCache) Get(key int) int { /* 实现 */ }
     func (this *LRUCache) Put(key int, value int) { /* 实现 */ }
     ```

#### 4. **处理边界条件**
   - **特殊输入**：容量为0、重复操作、超出容量时的淘汰策略
   - **并发问题**：若题目要求线程安全，需加锁（Golang 中用 `sync.Mutex`） 并发不用考虑 

---

### **二、Golang 实现技巧**
#### 1. **利用结构体封装状态**
   ```go
   // 示例：设计哈希集合
   type MyHashSet struct {
       data []bool
   }
   func Constructor() MyHashSet {
       return MyHashSet{make([]bool, 1e6+1)}
   }
   func (s *MyHashSet) Add(key int) { s.data[key] = true }
   ```

#### 2. **预定义工具函数**
   ```go
   // LRU 缓存中移动节点到头部
   func (lru *LRUCache) moveToHead(node *ListNode) {
       // 1. 从原位置删除
       node.Prev.Next = node.Next
       node.Next.Prev = node.Prev
       // 2. 插入头部
       node.Next = lru.head.Next
       lru.head.Next.Prev = node
       lru.head.Next = node
       node.Prev = lru.head
   }
   ```

#### 3. **复杂度优化**
   - **空间换时间**：用冗余数据结构（如哈希表+链表）
   - **惰性删除**：某些场景延迟处理（如设计过期缓存时）

#### 4. **并发安全设计**
   ```go
   type SafeCounter struct {
       mu    sync.Mutex
       count int
   }
   func (c *SafeCounter) Inc() {
       c.mu.Lock()
       defer c.mu.Unlock()
       c.count++
   }
   ```

---

### **三、实战案例：设计 LRU 缓存（Golang 实现）**
#### 1. **数据结构选择**
   - `map[int]*ListNode`：快速查找键值对
   - **双向链表**：维护访问顺序，头部最新，尾部最旧

#### 2. **完整代码**
   ```go
   type ListNode struct {
       Key, Val  int
       Prev, Next *ListNode
   }
   
   type LRUCache struct {
       capacity int
       cache    map[int]*ListNode
       head, tail *ListNode
   }
   
   func Constructor(capacity int) LRUCache {
       lru := LRUCache{
           capacity: capacity,
           cache:    make(map[int]*ListNode),
           head:     &ListNode{},
           tail:     &ListNode{},
       }
       lru.head.Next = lru.tail
       lru.tail.Prev = lru.head
       return lru
   }
   
   func (lru *LRUCache) Get(key int) int {
       if node, ok := lru.cache[key]; ok {
           lru.moveToHead(node)
           return node.Val
       }
       return -1
   }
   
   func (lru *LRUCache) Put(key int, value int) {
       if node, ok := lru.cache[key]; ok {
           node.Val = value
           lru.moveToHead(node)
           return
       }
       if len(lru.cache) == lru.capacity {
           removed := lru.removeTail()
           delete(lru.cache, removed.Key)
       }
       newNode := &ListNode{Key: key, Val: value}
       lru.cache[key] = newNode
       lru.addToHead(newNode)
   }
   
   func (lru *LRUCache) moveToHead(node *ListNode) {
       lru.removeNode(node)
       lru.addToHead(node)
   }
   
   func (lru *LRUCache) addToHead(node *ListNode) {
       node.Prev = lru.head
       node.Next = lru.head.Next
       lru.head.Next.Prev = node
       lru.head.Next = node
   }
   
   func (lru *LRUCache) removeNode(node *ListNode) {
       node.Prev.Next = node.Next
       node.Next.Prev = node.Prev
   }
   
   func (lru *LRUCache) removeTail() *ListNode {
       node := lru.tail.Prev
       lru.removeNode(node)
       return node
   }
   ```

#### 3. **测试用例验证**
   ```go
   func main() {
       lru := Constructor(2)
       lru.Put(1, 1)
       lru.Put(2, 2)
       fmt.Println(lru.Get(1)) // 1
       lru.Put(3, 3)          // 淘汰2
       fmt.Println(lru.Get(2)) // -1
   }
   ```

---

### **四、快速编码训练建议**
1. **模板化代码**：预先练习常见设计题（LRU、Trie、API限流器）
2. **画图辅助**：在草稿纸上画出数据流和结构关系
3. **分模块实现**：先写接口，再填充方法，最后处理边界
4. **复杂度自查**：每写一个操作，检查是否符合题目要求的时间复杂度

通过以上方法，可在 30 分钟内完成大多数 LeetCode 设计题的 Golang 实现，重点关注 **数据结构选择** 和 **边界处理** 两大核心难点。