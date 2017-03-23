#coding:utf-8
import re
import requests
import os
from threading import Thread
from bs4 import BeautifulSoup
#返回指定页面信息
def page(num):
        url='http://jandan.net/pic/page-%d#comments'%num
        data=requests.get(url)
        return data.text
#匹配页面图片地址
#抓取图片信息保存到本地
def data(page,path):
    soup=BeautifulSoup(page)
    for soup_a in soup.find_all('a',class_='view_img_link'):
        Image=soup_a.get('href')
        print Image,
        print '下载完成'
        ImageName=Image.split('/')[-1]
        PathName=path+'/'+ImageName
        req=requests.get('http:'+Image)
        add=req.content
        with open(PathName,'wb+') as f:
            f.write(add)
if __name__ == '__main__':
    num1=input('Search from:')
    num2=input('To:')
    name='boring'
    os.makedirs(name,exist_ok=True)
    print '开始下载'
    for num in range(num1,num2+1):
        T1=Thread(target=data, args=(page(num), name)) #多线程
        T1.start()
