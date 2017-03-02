import requests
import json

apikey = '45656518563a4623a4eb008f620d6b57'
content = '5-7='
url = 'http://www.tuling123.com/openapi/api?key=%s&info=%s'%(apikey,content)

req = requests.get(url)

info = req.text
info = json.loads(info,encoding='utf-8')

# cc = info['text']
print(info)
