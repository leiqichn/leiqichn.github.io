---
title: 代码随想录 day25 回溯part04
date: 2024-11-24 11:32:10
modificationDate: 2024 十一月 24日 星期日 11:32:10
categories: 
	- carl
tags: []
sticky: []
published: false
category_bar: true
---



# 第七章 回溯算法 part04

## 491.递增子序列

本题和大家刚做过的 90.子集II 非常像，但又很不一样，很容易掉坑里。

[https://programmercarl.com/0491.%E9%80%92%E5%A2%9E%E5%AD%90%E5%BA%8F%E5%88%97.html](https://programmercarl.com/0491.%E9%80%92%E5%A2%9E%E5%AD%90%E5%BA%8F%E5%88%97.html)

视频讲解：[https://www.bilibili.com/video/BV1EG4y1h78v](https://www.bilibili.com/video/BV1EG4y1h78v)

## 46.全排列

本题重点感受一下，排列问题 与 组合问题，组合总和，子集问题的区别。 为什么排列问题不用 startIndex

[https://programmercarl.com/0046.%E5%85%A8%E6%8E%92%E5%88%97.html](https://programmercarl.com/0046.%E5%85%A8%E6%8E%92%E5%88%97.html)

视频讲解：[https://www.bilibili.com/video/BV19v4y1S79W](https://www.bilibili.com/video/BV19v4y1S79W)

## 47.全排列 II

本题 就是我们讲过的 40.组合总和II 去重逻辑 和 46.全排列 的结合，可以先自己做一下，然后重点看一下 文章中 我讲的拓展内容： used[i - 1] == true 也行，used[i - 1] == false 也行

[https://programmercarl.com/0047.%E5%85%A8%E6%8E%92%E5%88%97II.html](https://programmercarl.com/0047.%E5%85%A8%E6%8E%92%E5%88%97II.html)

视频讲解：[https://www.bilibili.com/video/BV1R84y1i7Tm](https://www.bilibili.com/video/BV1R84y1i7Tm)

下面这三道题都非常难，建议大家一刷的时候 可以适当选择跳过。

因为 一刷 也不求大家能把这么难的问题解决，大家目前能了解一下题目的要求，了解一下解题思路，不求能直接写出代码，先大概熟悉一下这些题，二刷的时候，随着对回溯算法的深入理解，再去解决如下三题。

## 332.  重新安排行程（可跳过）

本题很难，一刷的录友刷起来 比较费力，可以留给二刷的时候再去解决。

本题没有录制视频，当初录视频是按照 《代码随想录》出版的目录来的，当时没有这道题所以就没有录制。

[https://programmercarl.com/0332.%E9%87%8D%E6%96%B0%E5%AE%89%E6%8E%92%E8%A1%8C%E7%A8%8B.html](https://programmercarl.com/0332.%E9%87%8D%E6%96%B0%E5%AE%89%E6%8E%92%E8%A1%8C%E7%A8%8B.html)

## 51.  N皇后（适当跳过）

N皇后这道题目还是很经典的，一刷的录友们建议看看视频了解了解大体思路 就可以 （如果没时间本次就直接跳过） ，先有个印象，二刷的时候重点解决。

[https://programmercarl.com/0051.N%E7%9A%87%E5%90%8E.html](https://programmercarl.com/0051.N%E7%9A%87%E5%90%8E.html)

视频讲解：[https://www.bilibili.com/video/BV1Rd4y1c7Bq](https://www.bilibili.com/video/BV1Rd4y1c7Bq)

## 37.  解数独（适当跳过）

同样，一刷的录友们建议看看视频了解了解大体思路（如果没时间本次就直接跳过），先有个印象，二刷的时候重点解决。

。

[https://programmercarl.com/0037.%E8%A7%A3%E6%95%B0%E7%8B%AC.html](https://programmercarl.com/0037.%E8%A7%A3%E6%95%B0%E7%8B%AC.html)

视频讲解：[https://www.bilibili.com/video/BV1TW4y1471V](https://www.bilibili.com/video/BV1TW4y1471V)

## 总结

刷了这么多回溯算法的题目，可以做一做总结了！

[https://programmercarl.com/%E5%9B%9E%E6%BA%AF%E6%80%BB%E7%BB%93.html](https://programmercarl.com/%E5%9B%9E%E6%BA%AF%E6%80%BB%E7%BB%93.html)