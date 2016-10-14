#-*- coding:utf-8 -*-
import urllib.request
import json
import re

#request xueqiu.com and download data
def download_data(url):
    headers_data = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Connection':'keep-alive',
    'Host':'xueqiu.com',
    'Cookie':r's=7512d72g25; xq_a_token=7f757b49bad857c0e0010141ddcfeb2c212c6afe;'
             r' xq_r_token=ee16af62ae60b52f23869019e7231cd655156d57;'
             r' Hm_lvt_1db88642e346389874251b5a1eded6e3=1475921087,1475921820,1475976041;'
             r' Hm_lpvt_1db88642e346389874251b5a1eded6e3=1475976051',
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
