#### 【问题描述】

下载 lifeofpix 前 N 页高清大图 地址 : http://www.lifeofpix.com

#### 【解决思路】

##### 请求页面

采用 requests 或者内置的 urllib请求 http://www.lifeofpix.com 注意请求时添加 UA。
通过翻页按钮可发现该网站翻页链接为 http://www.lifeofpix.com/page/x/ x 为页数。

##### 解析网页

得到网页响应后，分析图片地址所在位置，针对某张图片标签

`<img src="http://www.lifeofpix.com/wp-content/uploads/2017/04/img-2021-1600x1067.jpg" alt="burjkhalifa" />`

获取其中的 `src` 属性, 即图片地址。

##### 下载图片

获取到图片地址后，请求该地址，注意以二进制方式下载内容，在 requests 下应为：

```python

req = requests.get(url)
pic = req.content

```

##### 写入文件

写入文件时，注意以 `wb` 形式保存

```python

with open('xxx.jpg','wb') as f:
  f.write(content)

```


##### 多线程

在本题可以针对每一个页面开启一个线程，也可以针对每一张图片链接开启一个线程， 这取决于你的代码结构设计。
