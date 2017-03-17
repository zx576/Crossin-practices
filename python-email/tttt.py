#-*- coding:utf-8 -*-
import json
import textwrap
from bs4 import BeautifulSoup
import requests

req = requests.get('http://mp.weixin.qq.com/s/UZ_okX1SDNJLVjzUSHV6qg')

res = req.text
# for i in range(100):
#     res.replace('\xa0','')
soup = BeautifulSoup(res,'lxml')
soup_p = soup.find('div',class_ ="rich_media_content",id=True)

# print(req)
print(soup_p.get_text())

# for p in soup_p:
#     print(p.get_text())