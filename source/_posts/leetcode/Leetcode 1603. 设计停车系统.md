---
title: Leetcode1603. 设计停车系统
date: 2023-09-27 01:09:22
modificationDate: 2023 九月 27日 星期三 01:09:22
categories: 
	- leetcodel
tags: []
sticky: []
hide: false
category_bar: true
---

> Problem: [1603. 设计停车系统](https://leetcode.cn/problems/design-parking-system/description/)

  [TOC]
  
  # 思路
  > 首先，读清楚题目，需要分别记录3个车的剩余车位数量，并且要在addCar的时候进行判空，这就需要用到查找，在车类型中查找，这里我们可以使用map或数组。因为车的类型是连续的，不是稀疏的。我们更建议使用数组。
  

虽然这是一道简单的设计题，但是我们需要以小见大，认真思考。设计题就是理解题目意思——>建模->选择合适的数据结构-> 优化算法。一定要认真读题，先规划和设计好，再动收，一定要多练习，保持手感。需要注意的是：在 Go 语言 中，new 是一种创建变量的方式。通过 new(T) 可以创建类型为 T 的变量，初始值为 T 类型的零值，返回值为其地址（地址类型是 *T），这样在Constructor 只用返回值，而不是指针，但是在 AddCar 函数中，我们使用了指向 ParkingSystem 的指针接收器（receiver），保证可以修改new 出来的结构体。
  # 解题方法
  > lastCar [3]int 添加上边的数组
  
  # 复杂度
  - 时间复杂度: 
  > 添加时间复杂度, 示例： $O(n)$
  
  - 空间复杂度: 
  > 添加空间复杂度, 示例： $O(1)$
  


  # Code
  ```Go []
  
  type ParkingSystem struct {
    lastCar [3]int
}


func Constructor(big int, medium int, small int) ParkingSystem {
    var parkingSystem  ParkingSystem
    parkingSystem.lastCar[0] = big
    parkingSystem.lastCar[1] = medium
    parkingSystem.lastCar[2] = small
    return parkingSystem
}


func (this *ParkingSystem) AddCar(carType int) bool {
    carIdx := carType - 1
    if this.lastCar[carIdx] > 0 {
        this.lastCar[carIdx]--
        return true
    } 
    return false

}


/**
 * Your ParkingSystem object will be instantiated and called as such:
 * obj := Constructor(big, medium, small); // 在 Go 语言 中，new 是一种创建变量的方式。通过 new(T) 可以创建类型为 T 的变量，初始值为 T 类型的零值，返回值为其地址（地址类型是 *T），这样在Constructor 只用返回值，而不是指针，但是在 AddCar 函数中，我们使用了指向 ParkingSystem 的指针接收器（receiver）
 * param_1 := obj.AddCar(carType);
 */
  ```
  