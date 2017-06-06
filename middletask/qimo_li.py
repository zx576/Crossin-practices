# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from functools import reduce
import time
import threading


class Webspider:

    def __init__(self, start_page, end_page):
        self.start_page = start_page
        self.end_page = end_page
        self.html = 'http://jandan.net/ooxx/page-' + str(start_page) + '#comment'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64)"
                          "AppleWebKit/537.36"
                          "(KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
        }

    def max_page_num(self):
        find_max_nums_pages = requests.get('http://jandan.net/ooxx/', headers=self.headers)
        find_max_nums_pages.encoding = 'utf-8'
        max_nums_page_info = BeautifulSoup(find_max_nums_pages.text, 'lxml')
        max_num = max_nums_page_info.find('span', attrs='current-comment-page')
        max_num = eval(max_num.string)
        for i in max_num:
            if eval(self.start_page) > i:
                print('你输入的页面超过最大页数!')
                break
            elif eval(self.end_page) > i:
                print('你输入的页面超过最大页数!')
                break

    def crawl(self):
        ls = []
        super(Webspider, self).__init__()
        if self.start_page == self.end_page:
            for i in range(1):
                html = requests.get(self.html, headers=self.headers)
                html.encoding = 'utf-8'
                html_source = BeautifulSoup(html.content, 'lxml')
                meizi = html_source.select('.commentlist .view_img_link')
                ls.append(meizi)
        else:
            for i in range(eval(self.end_page) - eval(self.start_page)):
                if self.start_page <= self.end_page:
                    html_source = requests.get(self.html, headers=self.headers)
                    html_source.encoding = 'utf-8'
                    page_source = BeautifulSoup(html_source.content, 'lxml')
                    meizi = page_source.select('.commentlist .view_img_link')
                    ls.append(meizi)
                else:
                    print('起始页面大于末尾页面！')
                    break
        return ls

    def download_img(self):
        count = 0
        meizi_all_img = len(list(reduce(lambda x, y : x+y, Webspider.crawl(self))))
        for meizi_picture in list(reduce(lambda x, y: x + y, Webspider.crawl(self))):
            count += 1
            meizi_picture = meizi_picture['href']
            meizi_picture = meizi_picture.replace('//', '')
            download_img = requests.get('http://' + meizi_picture, headers=self.headers, stream=True)
            filename = meizi_picture.split('/')[-1]
            with open(filename, 'wb') as file:
                print('正在下载第{0}/{1}张图片'.format(count, meizi_all_img))
                file.write(download_img.content)


if __name__ in '__main__':
    start_time = time.time()
    img = Webspider(input('请输入起始页数:'), input('请输入末尾页数:'))
    img.max_page_num()
    img.crawl()
    try:
        t = threading.Thread(target=img.download_img(), daemon=True)
        t.start()
        t.join()
    except TypeError:
        print('数据异常,爬取失败')
    end_time = time.time()
    print('总共耗时%.2fs' % (end_time-start_time))
