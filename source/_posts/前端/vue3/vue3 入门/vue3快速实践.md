---
title: vue3快速实践
date: 2024-06-24 22:32:19
modificationDate: 2024 六月 24日 星期一 23:08:13
categories: 
	- vue3 入门
tags: []
sticky: []
hide: false
category_bar: true
---

[教程 | Vue.js (vuejs.org)](https://cn.vuejs.org/tutorial/#step-7)

# 声明式渲染

你在编辑器中看到的是一个 Vue 单文件组件 (Single-File Component，缩写为 SFC)。SFC 是一种可复用的代码组织形式，它将从属于同一个组件的 HTML、CSS 和 JavaScript 封装在使用 `.vue` 后缀的文件中。

Vue 的核心功能是**声明式渲染**：通过扩展于标准 HTML 的模板语法，我们可以根据 JavaScript 的状态来描述 HTML 应该是什么样子的。当状态改变时，HTML 会自动更新。
能在改变时触发更新的状态被称作是**响应式**的。我们可以使用 Vue 的 `reactive()` API 来声明响应式状态。由 `reactive()` 创建的对象都是 JavaScript [Proxy](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy)


```vue
import { reactive } from 'vue'

const counter = reactive({
  count: 0
})

console.log(counter.count) // 0
counter.count++

```

`reactive()` 只适用于对象 (包括数组和内置类型，如 `Map` 和 `Set`)。而另一个 API `ref()` 则可以接受任何值类型。`ref` 会返回一个包裹对象，并在 `.value` 属性下暴露内部值。

在双花括号中的内容并不只限于标识符或路径——我们可以使用任何有效的 JavaScript 表达式。

template

```
<h1>{{ message.split('').reverse().join('') }}</h1>
```

现在，试着自己创建一些响应式状态，
# Attribute 绑定 v-bind



```vue

<script setup>
import { ref } from 'vue'

const titleClass = ref('title')
</script>

<template>
  <h1 :class="titleClass">Make me red</h1>
</template>

<style>
.title {
  color: red;
}
</style>

```

![](../../../../imgs/Pasted%20image%2020240624225914.png)


# 时间监听 v-on : click
v-on: click = "aaa" : 或者 @click= "aaa"
```vue
<script setup>
import { ref } from 'vue'

const count = ref(0)

function increment() {
  // 更新组件状态
  count.value++
}
</script>

<template>
  <!-- 使此按钮生效 -->

  <button v-on:click="increment">Count is: {{ count }}</button>
</template>


```
![](../../../../imgs/Pasted%20image%2020240624225635.png)

# 表单绑定 v-model

![](../../../../imgs/Pasted%20image%2020240624230352.png)
`v-model` 会将被绑定的值与 `<input>` 的值自动同步，这样我们就不必再使用事件处理函数了。

`v-model` 不仅支持文本输入框，也支持诸如多选框、单选框、下拉框之类的输入类型。我们在[指南 - 表单绑定](https://cn.vuejs.org/guide/essentials/forms.html)中讨论了更多的细节。




```vue


<script setup>
import { ref } from 'vue'

const text = ref('')

function onInput(e) {
  text.value = e.target.value
}
</script>

<template>
  <input :value="text" @input="onInput" placeholder="Type here">
  <p>{{ text }}</p>
</template>



# 使用v-model 简化
<script setup>
import { ref } from 'vue'

const text = ref('')

</script>

<template>
  <input v-model="text" placeholder="Type here">
  <p>{{ text }}</p>
</template>

```


# 条件渲染

![](../../../../imgs/Pasted%20image%2020240624230722.png)


```vue
<script setup>
import { ref } from 'vue'

const awesome = ref(true)

function toggle() {
  awesome.value = !awesome.value # 做取反
}
</script>

<template>
  <button @click="toggle">Toggle</button>
  <h1 v-if="awesome">Vue is awesome!</h1>
  <h1 v-else>Oh no 😢</h1>
</template>

```

