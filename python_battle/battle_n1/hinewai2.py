 # -*- coding: utf-8 -*-
import sys, requests, json
apikey="9f8fb092b5bb4788b9886398fe0841c7"
content="你才傻呢"
url='http://www.tuling123.com/openapi/api?key=%s&info%s'%(apikey,content)
response=requests.get(url)
info= response.text
info=json.loads(info)
cc=info['text']


print cc
print type(cc)
