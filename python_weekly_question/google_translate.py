import requests
import json

url = 'http://fanyi.baidu.com/sug'
url2 = 'http://fanyi.baidu.com/v2transapi'

'''
from:zh
to:en
query:我想吃
transtype:realtime
simple_means_flag:3
'''
keywords = {
    'from':'zh',
    'to':'en',
    'query':'我想吃苹果',
    # 'transtype':'realtime',
    # 'simple_means_flag':3
}

req = requests.post(url2,keywords)
print(req)
res = req.text
data = json.loads(res)

print(data)
result = data['data']
print(result)
# for i in data['data'][]:
