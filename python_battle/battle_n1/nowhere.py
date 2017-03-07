'''
作者：nowhere
行业：其他
学习时间：2016.12
项目：抓取豆瓣top250图书
学习感受：时间很紧...ss
'''
from bs4 import BeautifulSoup
import codecs
import requests

DOWNLOAD_URL = 'https://book.douban.com/top250'
def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url,headers=headers).text
    print(data)
    return data

def parse_html(html):
    soup = BeautifulSoup(html)
    # book_list_soup = soup.find('ol',atter={'class':'indent'})
    book_name_list = []
    for book_table in soup.find_all('table',attrs={'width':'100%'}):
        detail = book_table.find('div',attrs={'class':'pl2'})
        books = detail.find('a').getText()
        book_name_list.append(books)
    next_page = soup.find('span',attrs={'class':'next'}).find('a')
    if next_page:
        return book_name_list,next_page['href']
    return book_name_list,None
    return book_name_list

def main():
    url = DOWNLOAD_URL
    with open('movies.txt','w',encoding='utf-8') as fp:
        while url:
            html = download_page(url)
            books = parse_html(html)
            print(books)
            for i in books:
                fp.write('%s'%i)
if __name__ == '__main__':
    main()
