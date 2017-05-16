#### 【题目描述】

1. 仔细查看提供的 API 接口和使用方法。

2. 根据搜索 API 接口，搜索出以 '程序员' 或其他词为关键字的 10 条歌单信息，返回所有歌单 id。

3. 根据歌单 ID 以及歌单信息 API 接口，获取歌单信息，并将其保存在 mongodb 中。
4. 从 mongodb 中提取出歌单中所有歌曲 ID，请求该歌曲的歌词信息，并将结果保存到 mongodb 中。


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
123456 为歌单 ID

##### 根据歌曲 ID 获取歌词信息:

url = 'http://music.163.com/api/song/lyric?os=pc&id=123456&lv=-1&kv=-1&tv=-1'
GET 方法请求
123456 为歌曲 ID


#### 【解决思路】

##### API接口使用方法

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

##### mongodb

向数据库内插入一条或多条数据

连接 MongoDB：

```python
from pymongo import MongoClient
client = MongoClient()
```

获取数据库：

```python
db = client.test_database
```

获取集合：

```python
collection = db.test_collection
```

查找数据：

```python
collection.find_one({'name': 'abc'})
```

插入数据：

```python
collection.insert_one({'name': 'abc', 'age': 1})

new_docs = [
    {'name': 'haha', 'age': 17},
    {'name': 'wow', 'age': 21}
]
collection.insert_many(new_docs)
```

更新数据：

```python

new_item = {'name': 'abc', 'age': 21}
collection.update_one({'name':new_item['name']},{'$set':new_item},upsert=True)

```
