import requests
import json


def baidu_trans(info):
    url = 'http://fanyi.baidu.com/v2transapi'
    keywords = {
        'from': 'zh',
        'to': 'en',
        'query': info,

    }
    req = requests.post(url, keywords)
    data = req.json()
    try:
        result = data['dict_result']['simple_means']['word_means']
        return ';'.join(result)

    except:

        return data['trans_result']['data'][0]['dst']


print(baidu_trans('周鑫鑫是二货'))