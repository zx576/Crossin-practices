#-*- coding:utf-8 -*-
import requests
import re
import time
import json
from crwal.user_agents import agents
import random
from bs4 import BeautifulSoup
# a = [1,1,2,3,5,6,6]
# c = [1,2,34,5]
#
# a = set(a)
# b = list(a)
# print(a,'\n',b)
# print(type(b))
# #
# dic = {}
#
# dic['a'] = a
#
# print(dic)
#
# new = json.dumps(dic)
#
# data = json.loads(new)
#
# print(new)
# print(data)

# dic = {'a':1}
#
# dic['a'] = 3
#
# print(dic)
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
    'Connection':'keep-alive',
    'Cache-Control':'max-age=0',
    # 'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':'wb_publish_fist100_2426968121=1; wb_publish_fist100_6055629257=1; wb_g_upvideo_6055630039=1; wb_publish_fist100_6055630039=1; wb_g_upvideo_6055501997=1; CNZZDATA1260210782=928241306-1483959022-null%7C1484056210; SINAGLOBAL=976599875082.1892.1484059342992; TC-Ugrow-G0=0149286e34b004ccf8a0b99657f15013; login_sid_t=fb14b5e104743e2a7ea8677183e320d7; _s_tentry=-; TC-V5-G0=8518b479055542524f4cf5907e498469; Apache=361780690135.78894.1484098107301; ULV=1484098108290:2:2:2:361780690135.78894.1484098107301:1484059343007; TC-Page-G0=1bbd8b9d418fd852a6ba73de929b3d0c; UOR=,www.weibo.com,login.sina.com.cn; WBtopGlobal_register_version=c689c52160d0ea3b; SCF=AhpUAUcSW-Jr21YdIICYmB2Uqi9-xfS-RhaYkn24qYkB5HVwMwOiFXfLJ0ZKkQT1JPJcftXZKUXnPed6h0nJTkg.; SUB=_2A251ceaiDeRxGeBO7lcU8C_FwjuIHXVWB19qrDV8PUNbmtAKLW6gkW99m2IX16n0_8BZLTrTZLLKYGO8DA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFokzwjWnmxV9AlIku6A4JZ5JpX5K2hUgL.Foq7SK-feh241KM2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMceh-fSK5p1K.N; SUHB=0h1J0FpK2wdzjL; ALF=1484706163; SSOLoginState=1484101362; un=18773615242; wvr=6',
    'DNT':'1',
    'Upgrade-Insecure-Requests':'1',
    'Host':'weibo.com',
    'User-Agent':'"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",',
    }
# import requests
# url = 'http://weibo.com/p/1005056058954791/info'
# res = requests.get(url,headers=headers)
# # print(res)
# ress = res.text
# print(ress)

# Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
# Accept-Encoding:gzip, deflate, sdch
# Accept-Language:zh-CN,zh;q=0.8,en;q=0.6
# Cache-Control:max-age=0
# Connection:keep-alive
# Cookie:wb_publish_fist100_2373503412=1; CNZZDATA1260210782=1605005909-1482013361-%7C1483772945; wvr=6; SINAGLOBAL=7086009847100.679.1483775376139; ULV=1483775376153:1:1:1:7086009847100.679.1483775376139:; UOR=,www.weibo.com,spr_sinamkt_buy_srwj1_weibo_t130; TC-Ugrow-G0=02e35d9240e6933947925d24232af628; SSOLoginState=1484013019; SCF=Ar4ddKlMQr970wayXJnyyx8a-BVDF1qYge1IO7lWctSwjFnn0Sa4t_51UK_lwvDMBF2mNsUWg1KsQjbUoVfPsEI.; SUB=_2A251cE22DeTxGeRN7FEU8C3Iyj6IHXVWBDh-rDV8PUNbmtAKLXimkW-e4bnatUo2yqKkY0hpbOmYpsVV3w..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W54ln0wJQEAZ8ux9eaQd.q75JpX5K2hUgL.Foz0S0efeheXeKz2dJLoIEBLxK-L12qLBonLxK.LBK.LB-eLxK-L1KzL1KBLxK-L1KzL1KBt; SUHB=0A0YMnsCB79SYJ; ALF=1515549030; TC-V5-G0=26e4f9c4bdd0eb9b061c93cca7474bf2
# DNT:1
# Host:weibo.com
# Upgrade-Insecure-Requests:1
# User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36

# string = '注册时间：<\/span>\r\n\t\t\t\t\t\t\t\t\t<span class=\"pt_detail\">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t2016-10-29\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<\/span>'
# re_registertime = re.compile(r'注册时间：<\\\/span>.*<span class=\\\"pt_detail\\\">.*\t(\w+-\w+-\w+)\t.*<\\\/span>')
# r = re.match(re_registertime,string)
# print(r)

# string = '注册时间：<\/span>\r\n\t\t\t\t\t\t\t\t\t<span class=\"pt_detail\">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t2016-10-29\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<\/span>'
# # re_registertime = re.compile(r'.*\t(\w+-\w+-\w+)\t.*'
# print(string)
# re_registertime = re.compile(r'注册时间：[\s\S]*\t(\d+-\d+-\d+)\t')
# r = re.findall(re_registertime,string)
# # print(r)
# with open('testbs.txt','r',encoding='utf-8')as f:
#     strings = f.read()
# # print(string)
# soup = BeautifulSoup(ress,'lxml')
# # print(soup.prettify())
# scripts = soup.find_all('script')
# news = ''
# for i in scripts:
#     # data = {}
#     # print(i.string)
#     # print(type(i.string))
#     if '基本信息' in i.string:
#         s = str(i.string)
#         news = s.replace('\\t','').replace('\\r','').replace('\\n','')
#         # print(news)
#         # data['name']
#         # append
#
# # result
# # start = news.find('html')
# # new_s = news[133:]
# # print(news)
# news = news.replace('\\','')
# # print([news])
# soup2 = BeautifulSoup(news,'lxml')
# print(soup2.prettify())




# tag_li = soup2.find_all('li',attrs={'class':True})
# tag_li = soup2.find_all('li',attrs={'class':True})
# print(tag_li.prettify())
# span = tag_li.span
# print(span.string)
# dec = {}
# for lis in tag_li:
#     # print(lis.prettify())
#     # break
#     # s = li.span
#     # print(s)
#     tag_span1 = lis.find('span')
#     att = tag_span1.get_text()
#     # print(att)
#     tag_span2 = tag_span1.next_sibling
#     val = tag_span2.get_text()
#     # print(val)
#     dec[att] = val

# print(dec)
# c = 0
# b = 0
# for i in range(30):
#     c += 1
#     if c == 3:
#         b += 1
#         c = 0
#         print('b:',b)
#     print('c:',c)