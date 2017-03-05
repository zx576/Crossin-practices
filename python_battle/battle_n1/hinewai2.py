 # -*- coding: utf-8 -*-
import requests, json
def func(info):
    apikey="9f8fb092b5bb4788b9886398fe0841c7"
    url='http://www.tuling123.com/openapi/api?key=%s&info%s'%(apikey,info)
    response=requests.get(url)
    info= response.text
    info=json.loads(info)
    # print info
    cc=info['text']
    print cc
    print type(cc)

a = '5+2等于'
print a
func(a)
