#### 【题目描述】

1. 使用 selenium 配合 PhantomJS 打开[房天下租房板块]('http://zu.sh.fang.com/')，以 '闵行' 作为关键字搜索租房信息

2. 在搜索的结果中获取租房信息中的价格、图片、地址等信息，并保存。以地址+价格作为图片名，如 `闵行-古美-东苑佳佳花园4000元-月.jpg`

3. 模拟点击下一页，继续获取结果。

4. 至少获取 5 页信息。

#### 【解题思路】

##### selenium 启动进入网页

启动 selenuium + PhantomJS，进入租房板块，填写搜索信息，点击搜索。

```python
from selenium import webdriver

url = 'http://zu.sh.fang.com/'
driver = webdriver.PhantomJS(service_args=['--load-images=no'])
driver.get(url)
driver.find_element_by_id('input_key').send_keys('闵行')
driver.find_element_by_id('rentid_39').click()


```

##### 获取信息

```python
from lxml import etree

page = driver.page_source
tree = etree.HTML(page)
# 房屋地址
x_title = dd.xpath('./p[@class="gray6 mt20"]')[0]
title = x_title.xpath('string(.)')
# 房屋价格
x_rent = dd.xpath('.//p[@class="mt5 alingC"]')[0]
rent = x_rent.xpath('string(.)')
# 获取图片地址
pic_url = dd.xpath('..//img[@class="b-lazy"]/@data-src')[0]
pic_end_name = pic_url.split('.')[-1]
# 组装并处理图片名称
pic_name = str(title) + str(rent) + '.' + pic_end_name
pic_name = pic_name.replace('/','-').replace(' ','')

```

##### 下载信息

```python

content = requests.get(pic_url).content
with open('pic_name','wb')as f:
  f.write(content)

```

##### 点击下一页

一页内容获取完之后，点击下一页内容继续进行页面分析。
```python

driver.find_element_by_link_text('下一页').click()

```
