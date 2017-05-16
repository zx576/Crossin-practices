from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://www.s.cn/', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        pq_div = response.doc('.brand_yd')
        for each in pq_div('a[href^="http"]').items():
            if 'brand' in each.attr.href:
                self.crawl(each.attr.href, callback=self.list_page)

    @config(priority=2)            
    def list_page(self,response):

        for each in response.doc('a[href^="http"]').items():
            if 'list' in each.attr.href:
                continue
            self.crawl(each.attr.href, callback=self.detail_page)


    @config(priority=2)
    def detail_page(self, response):
        try:
            return {
                "url": response.url,
                "title": response.doc('.goodsname').text(),
                'price':response.doc('.salePrice_big').text(),

            }
        except:
            return None
