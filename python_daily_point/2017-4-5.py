#-*- coding:utf-8 -*-
# from .models import Proxy
import requests
import bs4
import json
import re
import os
import threading
import time
from selenium import webdriver
import chardet
# 通用请求头
headers_general = {
        'User-Agent':'"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) '
                     'AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",',
}


# 通用处理模块


def req_url(url,headers,rep_count=1):
    ''' 请求网页，返回 bs 处理过的字符串

    请求过程如果对方拒绝或者状态码不为 200 ，调用 selenium 重新获取 cookie,然后再次请求
    再失败，就直接返回 None

    :param url: 请求地址
    :param headers: 请求头
    :param rep_count: 请求次数，默认为 1，
    :return: bs4 处理过的网页
    '''
    try:
        req = requests.get(url,headers=headers,timeout=2)
        assert req.status_code == 200
        print(req.encoding)
    except:
        if rep_count == 1:
            cookie = get_cookie_by_selenium(url)
            headers['Cookie'] = cookie
            return req_url(url,headers,rep_count=2)
        else:
            return None

    else:
        content = req.text
        # soup = bs4.BeautifulSoup(content,'lxml')
        return content


def get_cookie_by_selenium(url):
    '''使用 selenium 获取 cookie

    :param url: 获取 cookie 的地址
    :return: 返回字符串形式的
    '''
    driver = webdriver.Chrome()
    driver.get(url)
    # cookie =
    cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
    cookiestr = ';'.join(item for item in cookie)
    driver.quit()
    return cookiestr

def verify_ip(dic):
    '''

    :param dic: 字典形式的 IP
    :return: 如果请求成功则返回 True,反之则 False
    '''
    fixed_url = 'http://www.baidu.com/'
    try:
        res = requests.get(fixed_url, proxies=dic, timeout=1)
        assert res.status_code == 200
        return True
    except:
        return False



# 66代理


# 快代理请求头
headers_kuai = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.6',
        'Cache-Control':'max-age=0',
        'Cookie':'sessionid=a76e1c82e71492eba1869a1973610bd6; channelid=0; sid=1491370147849899; _ydclearance=cc9a9863170f0895f520b2e4-c32a-4d36-962f-305f58d952d7-1491385315; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1491011473,1491139506,1491187701,1491370620; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1491378119; _ga=GA1.2.511320761.1490863522',
        'Host':'www.kuaidaili.com',
        'Proxy-Connection':'keep-alive',
        'Referer':'https://www.google.com.hk/',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
}
# Cookie:
#
def fetch_k1():
    '''下载 快代理 网站IP'''
    urls = ['http://www.kuaidaili.com/free/inha/',
            'http://www.kuaidaili.com/free/intr/',
            'http://www.kuaidaili.com/free/outha/',
            'http://www.kuaidaili.com/free/outtr/']
    for url in urls:

        content = req_url(url,headers_kuai)
        soup = bs4.BeautifulSoup(content,'lxml')

        if not soup:
            return None
        soup_tb = soup.find('tbody')
        soup_tr = soup_tb.find_all('tr')
        for tr in soup_tr:
            all_td = tr.find_all('td')

            ip        = all_td[0].string
            port      = all_td[1].string
            http_type = all_td[2].string
            http_head = all_td[3].string
            district  = all_td[4].string

            if '高匿' in http_type:
                type = 'G'
            elif '透明' in http_type:
                type = 'T'
            else:
                type = 'O'


            dic = {}
            dic[http_head] = ip + ':' + port

            if verify_ip(dic):
                print(dic)
                print(type)
                print(district)
            # save_proxy(dic,resource='快代理')


fetch_k1()