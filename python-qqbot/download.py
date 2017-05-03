import requests
import json
import bs4
from selenium import webdriver

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate, sdch, br', 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.6', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Cookie': 'q_c1=f7e55bb3da114e48b8b47a2c051a391c|1490523713000|1490523713000; r_cap_id="NTY3NGFhMTZmNWFiNGJmY2I5Y2IxYzdhOGQwYWU5NzI=|1490523713|595f80670737baeda6b0582524888d1202165c57"; cap_id="NTliZmNhNTFlYTdjNGM5ODk4ZmE4OThmNTkxZTE3NTA=|1490523713|0dc097724709fd32a1a451edadb88c7c594624e7"; d_c0="AFBCwmecgguPTrOFy4K33gxARSNb7HMiuPs=|1490523714"; _zap=0998a8d2-fb50-4495-aabd-2bf99b3853a1; __utma=243313742.401858163.1490790646.1490790646.1490790646.1; __utmz=243313742.1490790646.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; _xsrf=2|fdea5d47|f3e1db4ae5450ab815acac8ebd415c44|1491998260; z_c0=Mi4wQUFBQWtPd2RBQUFBVUVMQ1o1eUNDeGNBQUFCaEFsVk5TaVBfV0FCa2s4TnBzN1hKWjJlQi1IWkg2YzlVOXBrNjdB|1492419428|e19ce89830ae309c934325be9d6209beee6e3264; aliyungf_tc=AQAAACmRzQIpgAEAmC/ii/+5o+zKzclv; __utma=51854390.1614846103.1490523714.1492350992.1492419426.53; __utmb=51854390.0.10.1492419426; __utmc=51854390; __utmz=51854390.1491925492.43.6.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/38409342/answer/76338969; __utmv=51854390.100-1|2=registration_date=20130908=1^3=entry_date=20130908=1; XSRF-TOKEN=2|9922608d|9729e680818d377271649144d989618e|1491998260', 'Host': 'zhuanlan.zhihu.com', 'Pragma': 'no-cache', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}


url = 'https://zhuanlan.zhihu.com/api/columns/crossin/posts?limit=20&offset='

FIXED_URL = 'https://zhuanlan.zhihu.com'

def download(url):
    page = [0,20]

    result = []

    for i in page:
        url = url + str(i)
        req = requests.get(url,headers=headers)
        content = req.text
        content = json.loads(content)
        for j in content:
            # print(type(j))
            items = []
            item = j

            items.append(item['title'])
            items.append(FIXED_URL+item['url'])
            items.append('none')

            result.append(items)
            print(items)

    return result


# download(url)

headers_sougou = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate, sdch', 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.6', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Cookie': 'SUV=009D4DE331DDE63A58E0FA963B4D3578; _ga=GA1.2.2015739736.1491380989; ssuid=9203727452; SUID=982FE28B3921940A0000000058E60FCD; ABTEST=6|1491472415|v1; weixinIndexVisited=1; CXID=27F122C280C2638C7D0A66B64C17F765; SNUID=A068B7C2ECE8A1B150CDC759EDF295C1; sct=7; ld=Tyllllllll2Yik@blllllV01ZoclllllAMwsulllll9lllll9v7ll5@@@@@@@@@@; LSTMV=409%2C68; LCLKINT=1954; JSESSIONID=aaaTn9LtLCt-i8LY1yFSv; IPLOC=CN3100', 'Host': 'weixin.sogou.com', 'Pragma': 'no-cache', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}


we_url = 'http://weixin.sogou.com/weixin?query=crossin%E7%9A%84%E7%BC%96%E7%A8%8B%E6%95%99%E5%AE%A4&_sug_type_=&s_from=input&_sug_=n&type=2&page=%s&ie=utf8'

after_url = "&pass_ticket=qMx7ntinAtmqhVn+C23mCuwc9ZRyUp20kIusGgbFLi0=&uin=MTc1MDA1NjU1&ascene=1"

def download_weixin():

    res = []

    driver = webdriver.PhantomJS()

    for i in range(1,11):
        # n_url = '%s
        url = r'http://weixin.sogou.com/weixin?query=crossin%E7%9A%84%E7%BC%96%E7%A8%8B%E6%95%99%E5%AE%A4&_sug_type_=&s_from=input&_sug_=n&type=2&page='
        n_url = url + str(i)
        req = requests.get(n_url,headers=headers_sougou)
        content = req.text
        soup = bs4.BeautifulSoup(content,'lxml')
        soup_div = soup.find_all('div',class_= 'txt-box')
        for div in soup_div:

            items = []

            soup_a = div.find('a')
            t_url = soup_a['href']
            title = soup_a.get_text()

            # last_url = handle_url(t_url)
            driver.get(t_url+after_url)

            t_url = driver.current_url

            items.append(t_url)
            items.append(title)
            items.append('none')
            items.append('none')

            print(items)
            res.append(items)
            # break


    return res



# def handle_url(url):
#     url = url + "&pass_ticket=qMx7ntinAtmqhVn+C23mCuwc9ZRyUp20kIusGgbFLi0=&uin=MTc1MDA1NjU1&ascene=1"

# driver =
res = download_weixin()

with open('wedata.txt','w')as f:
    for i in res:
        f.write(str(i)+',')
        f.write('\n')













