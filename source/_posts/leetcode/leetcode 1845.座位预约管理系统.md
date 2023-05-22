---
title: leetcode 1845.座位预约管理系统
date: 2023-05-23 00:06:33
modificationDate: 2023 五月 23日 星期二 00:06:33
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---

[1845. 座位预约管理系统 - 力扣（Leetcode）](https://leetcode.cn/problems/seat-reservation-manager/description/)
![](../../imgs/Pasted%20image%2020230523000703.png)
### 超时版本

```go
type seat struct {
	seatId int
	isFree int // 空
}

type SeatManager struct {
	seats   map[int]*seat
	isFrees []int // 可预约的使用list 保存一份,记得被占用的时候，删除该座位，空缺则添加
}

func Constructor(n int) SeatManager {
	var a = SeatManager{make(map[int]*seat, n), make([]int, n)}
	for i := 0; i < n; i++ {
		id := i + 1
		a.seats[id] = &seat{id, 1}
		a.isFrees[i] = id // 初始化
	}
	return a
}

func (this *SeatManager) Reserve() int {
	sort.Ints(this.isFrees)
	top := this.isFrees[0]
	this.seats[top].isFree = 0
	this.isFrees = this.isFrees[1:]
	return top
}

// 遍历 或者使用map
func (this *SeatManager) Unreserve(seatNumber int) {
	this.seats[seatNumber].isFree = 1
	this.isFrees = append(this.isFrees,seatNumber)
}
```


### 通过版本
```go

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
	this.seats[seatNumber]=0
	if seatNumber < this.min{
		this.min=seatNumber
	}
	return
}


```
