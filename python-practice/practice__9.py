#-*- coding:utf-8 -*-
import requests
import json
import sys, time

#设置头文件，apikey从百度上获取
header = {'User-Agent':
                  'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
          'apikey':'2fd858445546756a2cea84b14c7'
          }
def getInfo(stockname):
    #请求api接口
    response = ''
    try:
        response = requests.get('http://apis.baidu.com/apistore/stockservice/stock?stockid='+stockname,headers=header)
    except:
        print '请求失败'
    #拿到请求信息
    content = response.text
    #json处理
    content = json.loads(content)
    info = content.get('retData')
    #拿到实时股票价格
    currentprice = ''
    if info:
        currentprice = info.get('stockinfo').get('currentPrice')
    else:
        print '查询失败'
        exit()
    return currentprice
#主函数
def main():
    print '输入要实时查询的股票代码'
    stock = raw_input('>>>')
    #设置5次循环，这里可根据自己要求设置
    i = 0
    while i < 5:
        currentp = getInfo(stock)
        sys.stdout.write('\r'+str(currentp))
        sys.stdout.flush()
        #每隔10秒请求一次，设置需小心，频繁请求可能会报错
        time.sleep(10)
        i += 1
    print('\n程序结束')

if __name__ == '__main__':
    main()