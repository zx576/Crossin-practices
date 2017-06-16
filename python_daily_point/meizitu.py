# -*- coding: UTF-8 -*-
#auther: xiang

import requests
import urllib.request
# import lxml
# import bs4
from bs4 import BeautifulSoup
import re
import os
import threading
from time import ctime


start_page = int(input("输入下载起始页:"))
end_page= int(input("输入终止页面:"))
headers = {
    "Host": "jandan.net" ,
    "User-Agent": "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"
}

download_dir= r"/pic"
if not os.path.exists(download_dir):
    os.makedirs(download_dir)
    print("下载目录%s已经创建,%s开始下载!"%(download_dir,ctime()))

def get_page(url):
    pic_list=[]
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    data = response.read().decode('utf-8')
    soup = BeautifulSoup(data)
    pictures = soup.find_all(name="a", attrs={
        "target": "_blank",
        "class": "view_img_link"
    })
    for picture in pictures:
        pic = "http:" + picture.attrs['href']
        pic_list.append(pic)
    return pic_list

def down_pic():
    for i in range(start_page,end_page + 1):
        url = "http://jandan.net/ooxx/page-%d#comments"%(i)
        url_list =get_page(url)
        for pic_url in url_list :
            name = pic_url[-18:]
            dir_picture_name = str(download_dir) + "\\" + str(name)
            try :
                if requests.get(pic_url).status_code == 200 :
                    print("正在下载第%d页,%s"%(i,pic_url))
                    urllib.request.urlretrieve(pic_url,filename=dir_picture_name)
            except:
                continue

threads = []
t1 = threading.Thread(target=down_pic)
threads.append(t1)
t2 = threading.Thread(target=down_pic)
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
        t.join()
    input('防止窗口消失:')
print("全部下载完毕%s"%ctime())
