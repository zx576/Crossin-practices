#-*- coding:utf-8 -*-
import bs4
import requests

'''
题目描述：
爬取糗事百科首页内容，将结果保存为 txt 文件

'''

# 爬取某一页下文字
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

# 保存内容到 txt 文件
def save(list_info):
    with open('qiushibaike.txt','a+',encoding='utf-8') as f:
        for info in list_info:
            f.write(info)
            f.write('\n')


# 循环请求并保存内容
def main():
    url = 'https://www.qiushibaike.com/8hr/page/{0}'
    for i in range(1,6):
        q_url = url.format(i)
        list_info = qiushibaike(q_url)
        save(list_info)

if __name__ == '__main__':
    main()
