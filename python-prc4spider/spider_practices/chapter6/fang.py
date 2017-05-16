# -*- coding: utf-8 -*-
from selenium import webdriver
import threading
from lxml import etree
import requests
import time
import os

# selenium 请求首页、填充数据搜索、点击下一页
def sln_search(keywords,pagecount):
    zu_url = 'http://zu.sh.fang.com/'
    driver = webdriver.PhantomJS(service_args=['--load-images=no'])
    driver.set_window_size(1920,2000)
    driver.get(zu_url)

    ipt_ele = driver.find_element_by_id('input_key')
    ipt_ele.send_keys(keywords)

    click_btn = driver.find_element_by_id('rentid_39')
    click_btn.click()

    # 点击下一页
    count = 1
    while count < pagecount:
        time.sleep(1)
        print('downloading page ',count)
        page = driver.page_source
        # 获取信息
        fetch_detail(page)
        driver.find_element_by_link_text('下一页')
        count += 1

def fetch_detail(page):

    tree = etree.HTML(page)
    xpath_dd = tree.xpath('//dd[@class="info rel"]')


    for dd in xpath_dd:

        x_title = dd.xpath('./p[@class="gray6 mt20"]')[0]
        title = x_title.xpath('string(.)')

        x_rent = dd.xpath('.//p[@class="mt5 alingC"]')[0]
        rent = x_rent.xpath('string(.)')


        pic_url = dd.xpath('..//img[@class="b-lazy"]/@data-src')[0]
        pic_end_name = pic_url.split('.')[-1]

        pic_name = str(title) + str(rent) + '.' + pic_end_name

        pic_name = pic_name.replace('/','-').replace(' ','')

        threading.Thread(target=download,args=(pic_url,pic_name)).start()
        while threading.active_count() > 3:
            print('目前线程数:',threading.active_count())
            time.sleep(3)


def download(pic_url,pic_name):

    if not os.path.exists('pic'):
        os.mkdir('pic')
    req = requests.get(pic_url)
    cont = req.content
    with open(r'pic/'+pic_name,'wb')as f:
        f.write(cont)






def main():
    keyw = input('输入搜索内容:')
    page = int(input('输入搜索页面'))
    sln_search(keyw,page)

if __name__ == '__main__':
    main()
