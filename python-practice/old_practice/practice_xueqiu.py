#-*- coding:utf-8 -*-
import urllib.request
import json
import re

#request xueqiu.com and download data
def download_data(url):
    headers_data = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    rep = urllib.request.Request(url,headers=headers_data)
    reps = urllib.request.urlopen(rep)
    res = reps.read().decode('utf-8', errors = 'ignore')
    #print(type(res))
    #print(res)
    return res
#handling and output data 
def handle_data():
    namelist = fetch_list()
    for i in namelist:
        url = 'https://xueqiu.com/p/'+i
        content = download_data(url)
        start_data = content.find('SNB.cubeInfo = ')+ len('SNB.cubeInfo = ')
        end_data = content.find('SNB.cubePieData')
		#抓下来的数据死活不能json，经过在线校检工具检测后发现数据最后多了个“;”,去掉后OK
        data = content[start_data:end_data][:-2]
        info = json.loads(data)
        print('投资组合：',info.get('name'))
        #print(info)
        info = info.get('view_rebalancing').get('holdings')
        #print(info)
        for i in info:
            stock = i.get('stock_name')
            print(stock)
        print('========')
#通过RE匹配雪球首页获取四个投资热门组合
def fetch_list():
    url = 'https://xueqiu.com/'
    res = download_data(url)
    #print(res)
    listq = re.findall(r'\((ZH\d{6})\)',res)
    #print(listq)
    return listq



print('今日热门组合')
print('===========')
handle_data()
