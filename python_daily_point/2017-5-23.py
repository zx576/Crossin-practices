
# import requests
from selenium import webdriver
from lxml import etree


header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
                        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}

url = 'http://irm.cninfo.com.cn/ircs/interaction/viewQuestionForSzse.do?questionId=5651078'

# req = requests.get(url,headers=header)
# print(req.status_code)
# page = req.text

driver = webdriver.PhantomJS()
driver.get(url)

tree = etree.HTML(driver.page_source)

x_div = tree.xpath('//div[@class="msgCnt cntcolor"]')

for div in x_div:

    print(div.xpath('./text() | ./div/text()'))
