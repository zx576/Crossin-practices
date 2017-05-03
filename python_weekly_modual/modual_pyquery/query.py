#-*- coding:utf-8 -*-
import requests
import pyquery

# 导入信息到 pyquery
url = 'http://www.jianshu.com/'
req = requests.get(url)
page = req.text
pq = pyquery.PyQuery(page)

# 定位所有文章的 ul
pq_ul = pq('ul').filter('.note-list')

# 定位所有文章 li
pq_li = pq_ul.find('li')

result = []
# 逐个遍历文章
for li in pq_li:
    li_tag = pq(li)

    title = li_tag('.title').text()
    href = li_tag('.title').attr('href')
    raw_href = 'http://www.jianshu.com' + href
    item = title + ':' + raw_href
    result.append(item)

for i in result:
    print(i)
