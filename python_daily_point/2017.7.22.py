# coding=utf-8
# author = zhouxin

import requests
import bs4
import re

url = 'http://wenda.guixue.com/article/2079'

def get_zip_url(url):

    req = requests.get(url)
    print(req.encoding)
    req.raise_for_status()

    soup = bs4.BeautifulSoup(req.text.encode('ISO-8859-1'), 'lxml')
    soup_zip = soup.find_all('a', href=re.compile('.zip'))
    for z in soup_zip:
        # print(z)
        z_url = z.get('href')
        name = z.get('title')
        print(z_url, name)
        save_zip(z_url, name)

def save_zip(url, name):

    req = requests.get(url)
    req.raise_for_status()
    # name = url.split('/')[-1]
    with open('zip/{}'.format(name), 'wb')as f:
        f.write(req.content)

get_zip_url(url)
