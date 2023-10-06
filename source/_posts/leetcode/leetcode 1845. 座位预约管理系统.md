---
title: leetcode 1845. 座位预约管理系统
date: 2023-10-06 12:09:42
modificationDate: 2023 十月 6日 星期五 12:10:36
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---

> Problem: [1845. 座位预约管理系统](https://leetcode.cn/problems/seat-reservation-manager/description/)

个人博客,记录学习: https://leiqicn.gitee.io/
  [TOC]

  # 思路
  > 座位 使用n+2 长度的map或者slice. 最小值可以使用一个结构体变量来保存.

  # 解题方法
  > 使用slice 的index来表示座位号, 
1.在每次操作Unreserve的时候,记得更新seat 为可用(将对应值置为0),且要比较更新最小座位号,因为Unreserve会释放该seat.
2.在每次reserve的时候, 使用中间变量返回最小座位号,因为this.min 要用来更新下一次的最小座位号.更新下一次的最小座位号,这里需要注意 i<length+1 ,slice make的时候长度要为n+2, 保证遍历到n;

  # 复杂度
  - 时间复杂度:
  > 添加时间复杂度, 示例： $O(n)$

  - 空间复杂度:
  > 添加空间复杂度, 示例： $O(n)$
  


  # Code
**使用slice**
  ```Go []

  
type SeatManager struct {
	seats []int
	min int
}

func Constructor(n int) SeatManager {
	set:=make([]int,n+2)
	return SeatManager{seats:set,min:1}
}

func (this *SeatManager) Reserve() int {
	value := this.min
	this.seats[value]=1
	length := len (this.seats)
	fmt.Println(length)
	i:=value
	for ;i<length+1;i++{
		if this.seats[i]==1{
			continue
		}
		this.min=i // 中间变量，更新下次的最小座位号
		break
	}
	return value // 最小的座位号
}

func (this *SeatManager) Unreserve(seatNumber int)  {
	this.seats[seatNumber] = 0
	if seatNumber < this.min{
		this.min=seatNumber
	}
}
  ```
**使用map**
map 有个用例会超时
```go
type SeatManager struct {
	seatMap   map[int]int
	minSeat   int
}

func Constructor(n int) SeatManager {
	seatMap := make(map[int]int, n+1)
	for i := 0; i <= n; i++ { // 注意从0 开始初始化
		seatMap[i] = 0
	}
	seatMan := SeatManager{
		seatMap,
		1,
	}
	return seatMan
}

func (this *SeatManager) Reserve() int {
  value := this.minSeat
	this.seatMap[value] = 1

  for i:= value; i <= len(this.seatMap);i++ {
    if this.seatMap[i] == 1 {
      continue
    }
    this.minSeat = i
    break
  }
	return value
}

func (this *SeatManager) Unreserve(seatNumber int) {
  this.seatMap[seatNumber] = 0
  if seatNumber < this.minSeat {
    this.minSeat = seatNumber
  }

}


func min(a, b int) int {
  if a < b {
    return a
  }
  return b
}
```
  