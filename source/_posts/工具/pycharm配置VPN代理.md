---
title: pycharm配置VPN代理
date: 2025-06-09 00:18:16
modificationDate: 2025 六月 9日 星期一 00:18:16
categories: 
	- 工具
tags: []
sticky: []
published: true
category_bar: true
---
确定本地VPN的代理端口：

![](../../imgs/Pasted%20image%2020250609001902.png)

![](../../imgs/Pasted%20image%2020250609001826.png)


点击check connetion 输入http://www.google.com
![](../../imgs/Pasted%20image%2020250609001953.png)
![](../../imgs/Pasted%20image%2020250609001820.png)



也可以使用requests 包验证, 返回内容，不爆红即可。


```python
import requests  
  
if __name__ == "__main__":  
    response = requests.get("http://www.youtube.com")  
    print(response.text)
```

![](../../imgs/Pasted%20image%2020250609002055.png)