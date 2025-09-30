---
title: fluid 左侧显示分类列表
date: 2023-05-18 23:54:21
modificationDate: 2023 五月 18日 星期四 23:54:21
categories: 
	- 工具
tags: []
sticky: []
hide: true
category_bar: false
---

![](../../imgs/Pasted%20image%2020230518235455.png)



```
<%
// var parent = page.categories.filter(c => !c.parent)
var parent = site.categories
if (Array.isArray(site.category_bar)) {
  // parent = page.categories.filter(cat => page.category_bar.indexOf(cat.name) !== -1)
  parent = site.categories
}
// var filterIds = page.categories.map(c => c._id)
var filterIds = site.categories.map(c => c._id)
// filterIds.push(page._id)
%>

<%- partial('_partials/category-list', {
  curCats  : parent,
  params: {
    type     : 'post',
    filterIds: filterIds,
    postLimit: theme.post.category_bar.post_limit,
    postOrderBy: theme.post.category_bar.post_order_by || config.index_generator.order_by
  }
}) %>

```
