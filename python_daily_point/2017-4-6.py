import requests
import json


headers = {

'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch, br',
'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.6',
'Cache-Control':'no-cache',
'Connection':'keep-alive',
'Cookie':'q_c1=f7e55bb3da114e48b8b47a2c051a391c|1490523713000|1490523713000; r_cap_id="NTY3NGFhMTZmNWFiNGJmY2I5Y2IxYzdhOGQwYWU5NzI=|1490523713|595f80670737baeda6b0582524888d1202165c57"; cap_id="NTliZmNhNTFlYTdjNGM5ODk4ZmE4OThmNTkxZTE3NTA=|1490523713|0dc097724709fd32a1a451edadb88c7c594624e7"; d_c0="AFBCwmecgguPTrOFy4K33gxARSNb7HMiuPs=|1490523714"; _zap=0998a8d2-fb50-4495-aabd-2bf99b3853a1; _xsrf=2|49f4ec1e|8c02548c7bffec6fa0b1bcd953cbdbda|1490668463; __utma=243313742.401858163.1490790646.1490790646.1490790646.1; __utmz=243313742.1490790646.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; z_c0=Mi4wQUFBQWtPd2RBQUFBVUVMQ1o1eUNDeGNBQUFCaEFsVk5TaVBfV0FCa2s4TnBzN1hKWjJlQi1IWkg2YzlVOXBrNjdB|1491464191|8a7e52097a99b9f2a134087a9bfb4eb6cd5b4d65; aliyungf_tc=AQAAAM7rX2w5ag0AmC/iiyoL45P4OPSd; __utma=51854390.1614846103.1490523714.1491464107.1491464107.35; __utmb=51854390.0.10.1491464107; __utmc=51854390; __utmz=51854390.1491400213.33.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.100-1|2=registration_date=20130908=1^3=entry_date=20130908=1; XSRF-TOKEN=2|b63359bb|73c5e129843859ca5f76097cac0c6e7f|1490668463',
'Host':'zhuanlan.zhihu.com',
'Pragma':'no-cache',
'Referer':'https://www.zhihu.com/',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'


}

url = 'https://zhuanlan.zhihu.com/api/columns/crossin/posts?limit=20&offset=20'

req = requests.get(url,headers=headers)

info = req.json()
data = {}

for i in info:
    url = 'https://zhuanlan.zhihu.com' + i.get('url')
    title = i.get('title')

    data[title] = url


print(data)
