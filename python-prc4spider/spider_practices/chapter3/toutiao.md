#### 【题目描述】

前往 **今日头条** 首页，获取 **体育** 板块的 ajax API 链接，
提取至少 5 个时间戳的内容。

API 响应内容示例:

```python
{
"has_more": false,  
"message": "success",
"data": [...],
"next": {
"max_behot_time": 1494765336 # 下一个时间戳
}
}

```

从响应的 json 数据中提取每条新闻的 标题(title)、概述(abstract)、回复数(comments_count) ，并保存为 CSV 文件。

#### 【解题思路】

##### 获取链接

进入到 体育 板块后，F12 打开开发者工具，然后在页面一直往下拉，等待新内容加载之后，到开发者工具中寻找加载的链接。

寻找的方法:
- 明显带有 api 字样的链接；
- 将链接在新窗口打开，查看请求结果。

最后得到以下链接 `http://www.toutiao.com/api/pc/feed/?category=news_sports&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=1494765718&tadrequire=true&as=A14559C158656BF&cp=5918E5363BAFAE1
`

##### 分析该连接

链接很长，包括了很多信息，可以试着删除或者改变某些参数，查看请求结果。
最后得到翻页的参数并删除一些不必要的参数。
经过不同的参数删除修改之后，发现 `max_behot_time` 为时间戳,改变此参数可以迭代更新内容。
最后的请求链接整理为 `http://www.toutiao.com/api/pc/feed/?category=news_sports&utm_source=toutiao&widen=1&max_behot_time=1494763836`

##### 请求该链接

请求该 API 链接，注意添加 UA 。获取响应后，逐条提取数据，并根据 `max_behot_time ` 参数构造下一个请求链接。

```python
url = 'http://www.toutiao.com/api/pc/feed/?category=news_sports&utm_source=toutiao&widen=1&max_behot_time='
req = requsts.get(url+'1494763836')
content = req.json()
for item in content['data']:
    # 逐条提取数据
    ...

next_time_stamp = content['next']['max_behot_time']
next_url = url + next_time_stamp


```

##### 保存为 CSV 文件

将下载完成的数据保存到 csv 文件。

```python

import csv

with open('toutiao.csv','w') as csv_file:
    writer  = csv.writer(csv_file):
    writer.writerows(data)

```

#### 其他注意

请求和获取过程中都存在失败的可能，使用 `try ... except ...` 语句添加必要的错误处理十分重要。

有余力的同学可以尝试结合多线程获取今日头条所有板块的前五页内容。
