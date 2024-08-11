---
title: docker容器打包成本地压缩镜像并load
date: 2024-08-11 11:59:34
modificationDate: 2024 August 11th Sunday 12:05:20
categories: 
	- Docker
tags: []
sticky: []
hide: false
category_bar: true
---

# docker容器打包成镜像和压缩
（1）将容器保存成新的镜像
相当于加了一层，使用docker commit

```
sudo docker commit -a 'run_code' b4293c3b9202  myimage:v2
```


（2）将镜像打包

```
docker save -o mask_detection_v5.tar myimage:v5
```


(3) 将镜像包压缩

```
 sudo tar -zcvf myimage.tar.gz myimage.tar
```


**还有一种容器的打包和压缩一步到位的方法**：

```
docker save myimage:v5 | gzip > myimage.tar.gz
```


docker镜像压缩包解压及镜像载入

一步加载压缩的镜像命令


```sh
docker load < myimage.tar.gz

```

（1）压缩包解压

```
tar -zxvf myimage.tar.gz
```


得到.tar格式的镜像包

（2）镜像载入

```
sudo docker load -i myimage.tar
```


载入后查看已经加载的镜像


```
sudo docker images
```



# 运行镜像


```sh
# 交互式运行
docker run -it myimage:v1 bash

```

# 进入已经运行的容器


```sh

docker exec -it [imagesID] bash
```
