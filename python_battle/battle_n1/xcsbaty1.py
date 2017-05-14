#  coding=utf-8

import time
import requests
from bs4 import BeautifulSoup
import re
# import sys
# reload(sys)
# sys.setdefaultencoding('gbk')

m = time.strftime('%m',time.localtime())
day = time.strftime('%m/%d/',time.localtime())
y = time.strftime('%Y',time.localtime())
age = int(y) - 1984


time_now = time.strftime('%Y%m%d',time.localtime())
print("today is %s"%time_now)
print("movies:")


###get douban movie list ###

url = "http://movie.douban.com/later/ziyang"
html = requests.get(url)
content = html.text
# html.close()

l = []

soup = BeautifulSoup(content,'lxml')
soup.prettify()

movies = soup.find_all("div",class_="intro")#get info from web

for items in movies:
    movie_name = items.a.get_text() #movie name
    movie_date = items.li.get_text()#display date

    str_movie_date = str(movie_date)
    str_movie_date = str_movie_date.replace('yue','/').replace('ri','/')

    movie_info = str_movie_date + movie_name
    n = ''.join(movie_info)
    m_list = []
    # if str_movie_date == day:
    #     today_movie = ''.join(n)
    #     print today_movie
    # else:
    #     str_movie_date.startswith(m)
    #     month_movie = ''.join(n)
    #     print month_movie

url2 = "http://movie.douban.com/nowplaying/shanghai/"
html2 = requests.get(url2)
content2 = html2.text
# html2.close()

soup2 = BeautifulSoup(content2,'lxml')


movie2 = soup2.find_all("li",class_="stitle")
for i in movie2:
    print(i.a.get_text())
