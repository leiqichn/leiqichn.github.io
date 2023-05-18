---
title: leetcode 1396.设计地铁系统
date: 2023-05-18 23:31:58
modificationDate: 2023 五月 18日 星期四 23:31:58
categories: 
	- leetcode
tags: [设计题]
sticky: []
hide: false
category_bar: true
---
[1396. 设计地铁系统 - 力扣（Leetcode）](https://leetcode.cn/problems/design-underground-system/description/)
![](../../imgs/Pasted%20image%2020230518233218.png)

设计题：

设计数据结构

* user
	* startTime int  
	* endTime int
	* startStationName string
	* endStatationName string
* UndergroundSystem
	* userMap map[int]*user
	* pathMap map[string][]int // 存放对应路程的用时，用于计算平均时间

注意点：go语言针对结构体包含指针的，需要在具体实现前初始化。


```go
type user struct {
	id int
	startTime int
	endTime int
	startStationName string
	endStatationName string
}

type UndergroundSystem struct {
	userMap map[int]*user
	pathMap map[string][]int // 存放对应路程的用时，用于计算平均时间
}

func Constructor() UndergroundSystem {
	// 初始化
	return UndergroundSystem{make(map[int]*user),make(map[string][]int)}
}

func (this *UndergroundSystem) CheckIn(id int, stationName string, t int) {
	//userMap 添加
	this.userMap[id] = &user{id:id} // 重点！！！ 这里多层嵌套指针的时候现需要新建指针初始化，否则会报错找不到该地址
	this.userMap[id].startTime = t
	this.userMap[id].startStationName = stationName
	

}

func (this *UndergroundSystem) CheckOut(id int, stationName string, t int) {
	//出站时，更新user.end* ;append pathmap
	useTime := 0
	if _,ok := this.userMap[id] ;ok {
		this.userMap[id].endTime = t
		this.userMap[id].endStatationName = stationName
	}

	mapKey := this.userMap[id].startStationName +"->" + this.userMap[id].endStatationName
	useTime = this.userMap[id].endTime - this.userMap[id].startTime
	this.pathMap[mapKey] = append(this.pathMap[mapKey],useTime)

}
	

func (this *UndergroundSystem) GetAverageTime(startStation string, endStation string) float64 {
	mapKey := startStation +"->" + endStation
	return average(this.pathMap[mapKey])
}

func average(s []int) float64 {
	sum := 0
	for _,v := range s {
		sum +=v
	}
	return float64(sum)/float64(len(s))
}


/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * obj := Constructor();
 * obj.CheckIn(id,stationName,t);
 * obj.CheckOut(id,stationName,t);
 * param_3 := obj.GetAverageTime(startStation,endStation);
 */

```
