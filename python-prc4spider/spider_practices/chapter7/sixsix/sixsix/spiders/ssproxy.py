# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from sixsix.items import SixsixItem
import bs4

class SsproxySpider(scrapy.Spider):
    name = "ssproxy"
    allowed_domains = ["http://www.66ip.cn/"]
    start_urls = ['http://www.66ip.cn/']

    def parse(self, response):

        # 取出各地分页面链接地址
        addr_urls_ul = response.xpath('//ul[@class="textlarge22"]')[0]
        addr_urls = addr_urls_ul.xpath('./li[not(@class)]/a/@href')
        for addr in addr_urls:
            url = addr.extract()
            print(url)
            yield Request(url='http://www.66ip.cn'+url,callback=self.get_details,dont_filter=True)
            # break

        # print(response)
        # print(response.body)

    def get_details(self,response):

        soup = bs4.BeautifulSoup(response.body,'lxml')

        soup_table = soup.find('table',attrs={'bordercolor':True})
        soup_tr = soup_table.find_all('tr')

        for tr in soup_tr:
            item = SixsixItem()
            data = tr.find_all('td')
            item['proxy'] = data[0].string
            item['port'] = data[1].string
            item['location'] = data[2].string
            item['proxy_type'] = data[3].string
            yield item
