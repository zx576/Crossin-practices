#-*- coding:utf-8 -*-
import requests
import json
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
# 地址
url = 'http://api.douban.com/v2/movie/subject/1764796'
# 网络请求
req = requests.get(url)
# 响应信息
# info = req.json()
info = req.text
info = json.loads(info,encoding='utf-8')
print(type(info))
print(info)
