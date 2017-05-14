#### 【问题描述】

爬取 名鞋库 网站 nike 品牌下所有商品的 图片、价格、描述，将图片名修改为 价格+描述，如图所示。

Nike 品牌 url 为：url = 'http://www.s.cn/list/pg{}?p=NIKE' , 大括号部分为页码。

#### 【解决思路】

1. 分析网页

进入 url = 'http://www.s.cn/list/pg1?p=NIKE' , 右键查看源代码,分析商品所在的 html 结构, 可以发现所有商品都包含在 `<div class='product_list'>...</div>` 这个标签下,而每个商品又包含在 `<dl>...</dl>` 标签下。


2. 请求网页

请求网页,获取图片地址和价格还有商品描述。

```python

req = requests.get(url)
page = req.text
soup = bs4.BeautifulSoup(page,'lxml')
soup_div = soup.find('div',class_='product_list')
soup_dl = soup_div.find_all('dl')
for dl in soup_dl:
    ...

```

3. 下载图片

下载图片并且将价格和描述赋予图片名

```python

req = requests.get(pic_url)
pic_content = req.content
pic_name = 'price' + 'describe'
with open('pic_name','wb') as f:
    f.write(pic_content)


```
