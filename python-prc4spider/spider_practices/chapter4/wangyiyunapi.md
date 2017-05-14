
#### 【题目描述】

根据提供的 API 接口和使用方法，搜索出以 '程序员' 或其他词为关键字的歌单，并且找出其中播放量最高的歌单名，然后下载该歌单中每首歌的歌词。

接口以及使用方法:

网易云 API 特定请求头:
```python

headers = {
    'Cookie': 'appver=1.5.0.75771',
    'Referer':'http://music.163.com/'
}

```

##### 搜索 API :

url = 'http://music.163.com/api/search/pc'

POST 方法请求
参数:

| s     |     offset |   limit   |   type |
| :-------- | --------:| :------: |  :------:|
| 搜索内容    |   偏移量 |  最大搜索结果  | 搜索类型|

搜索类型:

| 歌曲 | 专辑 | 歌手 | 歌单 | 用户 | MV | 歌词 | 电台 |
| :--- | ---:| :---: |:----:| :--- | ---:| :---: |:----:|
| 1    |   10 |  100  | 1000| 1002 |1004 |  1006 | 1009|

##### 根据歌单 id 获取详细信息:

url = 'http://music.163.com/api/playlist/detail?id=123456&updateTime=-1'
GET 方法请求

##### 根据歌曲 ID 获取歌词信息:

url = 'http://music.163.com/api/song/lyric?os=pc&id=123456&lv=-1&kv=-1&tv=-1'
GET 方法请求


#### 【解决思路】

本题主要考察 api 接口的运用，以下给出接口使用实例

POST 请求接口:

```python
headers = {
    'Cookie': 'appver=1.5.0.75771',
    'Referer':'http://music.163.com/'
}
url = 'http://music.163.com/api/search/pc'
data = {'s':keywords,'offset':1,'limit':10,'type':1000}

req = requests.post(url,data=data,headers=headers)
content = req.json()


```

GET 请求接口

```python

url = 'http://music.163.com/api/playlist/detail?id={}&updateTime=-1'.format(28377211)

req = requests.get(url,headers=headers)
content = req.json()


```
