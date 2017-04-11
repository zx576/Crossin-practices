import schedule
import time
from threading import Thread


STUTAS = True
def job():
    print('job1',time.ctime())

def job2():
    print('job2',time.ctime())
def func1():
    schedule.every(1).hours.do(job2)
    schedule.every(3).seconds.do(job)

    schedule.run_all()
    while True:
    #     if not STUTAS:
    #         schedule.clear()
    #         break
        schedule.run_pending()

    # print('jieshu')

# func1()
def func2():
    global STUTAS
    time.sleep(10)
    STUTAS = False

# t1 = Thread(target=func1)
# t2 = Thread(target=func2)
#
# t1.start()
# t2.start()

from selenium import webdriver
import requests

def get_cookie_by_selenium(url):
    options = webdriver.ChromeOptions()
    prefs = {"browser.privatebrowsing.autostart": False}
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome()
    driver.get(url)
    # cooo = driver.execute_script("return document.cookie")
    cookie_ = driver.get_cookies()
    cookie = [item["name"] + "=" + item["value"] for item in cookie_]
    cookiestr = ';'.join(item for item in cookie)
    driver.quit()
    print(cookie_)
    print(cookie)
    print(cookiestr)
    # time.sleep(100)
    # print(cooo)
    # return cooo
    return cookiestr



headers_general = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
}

headers_kuai = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.6',
        'Cache-Control':'max-age=0',
        # 'Cookie':'sessionid=7eb2f2abb2c1aa07f4425340c99f3573; _ydclearance=d5ff8d4b8bf6d7fc8482fb97-fea3-4f3c-9efd-9fd125124e21-1491018647; channelid=0; sid=1491011180605899; _ga=GA1.2.511320761.1490863522; _gat=1; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1490863522,1490881958,1490883412,1491011454; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1491011454',
        'Host':'www.kuaidaili.com',
        'Proxy-Connection':'keep-alive',
        'Referer':'https://www.google.com.hk/',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
}

def req():
    url = 'http://www.kuaidaili.com'
    url3 = 'http://www.66ip.cn'
    # url2 = 'http://www.baidu.com'
    coo = get_cookie_by_selenium(url)
    headers_general['Cookie'] = coo
    req_ = requests.get(url,headers=headers_general)
    print(req_.status_code)


req()
