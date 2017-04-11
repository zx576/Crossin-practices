import bs4
import requests


headers2 = {
        'Connection':'keep-alive',
        'Cookie':'sessionid=7eb2f2abb2c1aa07f4425340c99f3573; _ydclearance=ea8980e5bff59897a63dfac9-4941-41d5-8bf2-048ead64b1b8-1490889144; channelid=0; sid=1490881638017529; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1490863522,1490881958; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1490881958; _ga=GA1.2.511320761.1490863522; _gat=1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
}


proxy = {
"http": "http://1.180.239.133:9999"
}
url = 'http://www.baidu.com'
req = requests.get(url,proxies=proxy)
print(req.text)

# def fetch_k1():
#     urls = ['http://www.kuaidaili.com/free/inha/','http://www.kuaidaili.com/free/intr/','http://www.kuaidaili.com/free/outha/','http://www.kuaidaili.com/free/outtr/']
#     for url in urls:
#         req = requests.get(url,headers=headers2)
#         print(req)
#         page = req.text
#         soup = bs4.BeautifulSoup(page,'lxml')
#         soup_tb = soup.find('tbody')
#         soup_tr = soup_tb.find_all('tr')
#         for tr in soup_tr:
#             ip = tr.find('td',attrs={'data-title':'IP'}).string
#             port = tr.find('td',attrs={'data-title':'PORT'}).string
#             type = tr.find('td',attrs={'data-title':'类型'}).string
#             proxy = ip + ':' + port
#             dic = {}
#             dic[type] = proxy
#             print(dic)

# fetch_k1()
