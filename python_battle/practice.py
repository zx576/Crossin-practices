# coding=utf-8
import requests
import re
from bs4 import BeautifulSoup



headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

url = 'http://www.mafengwo.cn/mdd/'

req = requests.get(url,headers=headers)

page = req.text

soup = BeautifulSoup(page,'lxml')

# 找到所有的有效的 a 标签
soup_a = soup.find_all('a',href=True,attrs={'target':'_blank'})
# 编译一个去数字的表达式
rule = re.compile(r'\d+')
# 存数据的 dict
dict = {}
for a in soup_a:
    # 拿出地名
    addr = a.get_text()
    # 拿出地名对应的数字
    num = re.findall(rule,a.get('href'))
    # 确认不为空
    if len(num) > 0:
        num = num[0]
        if addr:
            dict[addr] = num

print(dict)
