#### 【问题描述】
爬取糗事百科热门段子 https://www.qiushibaike.com/
要求：
爬取前 N 页所有段子，包括段子内容、段子作者、作者性别和年龄、"好笑" 数、评论数。
将以上信息存入 txt 文件。

#### 【解决思路】

##### 分析糗事百科链接

点击下一页之后，可发现 URL 规律
URL ： https://www.qiushibaike.com/8hr/page/x/   x为页数。

##### 请求页面

对于每个页面，使用 requests 或者 urllib 来访问。

requests 代码

```python
import requests

req = requests.get(url)
data = req.text

```

urllib 代码

```python
import urllib.request

req = urllib.request.urlopen(url)
data = req.read().decode('utf-8')

```


##### 解析页面

得到页面后，观察到每一部分段子信息在一个 `class = 'article block untagged mb15'` 的 div 标签下。
遍历每个 div 标签，分别取到 作者、年龄、段子内容、好评数、评论数。

```python

from lxml import etree

html = etree.HTML(data)
xpath_div = html.xpath('//div[@class="article block untagged mb15"]')
for div in xpath_div:
    ...

```

##### 保存文件

获取到内容后，将数据保存进 txt 文件中

```python

with open('qsbk.txt', 'w') as f:
    f.write(data)


```
