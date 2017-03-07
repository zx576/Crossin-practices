# coding=utf-8
import requests
import re
from bs4 import BeautifulSoup



headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

url = 'http://www.mafengwo.cn/mdd/'

req = requests.get(url,headers=headers)

page = req.text
 # <div class="hot-list clearfix">
soup = BeautifulSoup(page,'lxml')

soup_a = soup.find_all('a',href=True,attrs={'target':'_blank'})

rule = re.compile(r'\d+')

dict = {}
for a in soup_a:
    addr = a.get_text()
    num = re.findall(rule,a.get('href'))
    if len(num) > 0:
        num = num[0]
        if addr:
            dict[addr] = num

print(dict)
