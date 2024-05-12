
---
title: leetcode 355设计推特
date: 2024-05-10 23:26:56
modificationDate: 2024 五月 10日 星期五 23:26:56
categories: 
	- leetcode
tags: []
sticky: []
hide: false
category_bar: true
---

Problem: [355. 设计推特](https://leetcode.cn/problems/design-twitter/description/)



```go

type Twitter struct {
	userMap map[int]*User
}

type User struct {
	userId    int
	followees map[int]bool
	tweets    []*Tweet
}

type Tweet struct {
	tweetId int
	time    int
	userId  int
}

// 推特时间排序
var tweetCount int

func Constructor() Twitter {
	return Twitter{userMap: make(map[int]*User)}
}

func (t *Twitter) PostTweet(userId int, tweetId int) {
	// 新建tweet  将自己设置为关注

	// 如果map 中不存在需要新建，因为User 类中存在map 和 slice
	if _, ok := t.userMap[userId]; !ok {
		t.userMap[userId] = &User{userId: userId, tweets: make([]*Tweet, 0), followees: make(map[int]bool)}
		tweet := &Tweet{tweetId, tweetCount, userId}
		t.userMap[userId].tweets = append(t.userMap[userId].tweets, tweet)
		t.userMap[userId].followees[userId] = true
	} else {
		tweet := &Tweet{tweetId, tweetCount, userId}
		t.userMap[userId].tweets = append(t.userMap[userId].tweets, tweet)

	}

	// 将tweetId 时间做一个新增
	tweetCount++
}

func (t *Twitter) Follow(followerId int, followeeId int) {
    // 如果关注人不存在则新建
    if _, ok := t.userMap[followerId]; !ok {
        t.userMap[followerId] = &User{
            userId:        followerId,
            followees: make(map[int]bool),
        }
        // 每次新建user的时候 将自己加入自己关注
        t.userMap[followerId].followees[followerId] = true
    }

    // 如果被关注人不存在则新建
    if _, ok := t.userMap[followeeId]; !ok {
        t.userMap[followeeId] = &User{
            userId:        followeeId,
            followees: make(map[int]bool),
        }
        // 每次新建user的时候 将自己加入自己关注
        t.userMap[followeeId].followees[followeeId] = true
    }
    t.userMap[followerId].followees[followeeId] = true

}

// 形参上的Id 在使用数据结构的时候一般使用map查找
func (t *Twitter) Unfollow(followerId int, followeeId int) {
	if _, ok := t.userMap[followerId]; ok {
		delete(t.userMap[followerId].followees, followeeId)
	}
}

func (t *Twitter) GetNewsFeed(userId int) []int {
	resTop10 := []int{}
	tweeters := []*Tweet{}
	if _, ok := t.userMap[userId]; ok {

		for followeeId, _ := range t.userMap[userId].followees {
			tweeters = append(tweeters, t.userMap[followeeId].tweets...)
		}

	}
	sort.Slice(tweeters, func(i, j int) bool {
		if tweeters[i].time > tweeters[j].time {
			return true
		}
		return false
	})

	for i := 0; i < len(tweeters) && i < 10 ; i++ {
		resTop10 = append(resTop10, tweeters[i].tweetId)
	}

	return resTop10
}

```
