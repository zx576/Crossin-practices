#-*- coding:utf-8 -*-
import bs4
import requests

'''
题目描述：
爬取糗事百科首页内容，将结果保存为 txt 文件

'''

def qiushibaike(url):

    req = requests.get(url)
    page = req.text

    soup = bs4.BeautifulSoup(page,'lxml')
    soup_div = soup.find_all('div',class_='content')

    list_info = []
    for div in soup_div:
        info = div.span.string
        if info:
            list_info.append(info)

    return list_info

def save(list_info):
    with open('qiushibaike.txt','w',encoding='utf-8') as f:
        for info in list_info:
            f.write(info)
            f.write('\n')


def main():
    list_info = qiushibaike(url)
    save(list_info)

if __name__ == '__main__':
    url = 'https://www.qiushibaike.com/'
    main()
