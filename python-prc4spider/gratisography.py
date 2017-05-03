import requests
import bs4
import threading
import queue
import os


'''
url = http://www.lifeofpix.com/
爬取该网站的首页图片，使用的技术包括 requests+bs4+threading+queue

'''

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}


queue_url = queue.Queue()

def get_pic_urls(url):
    global queue_url
    req = requests.get(url,headers=header)
    page = req.text
    soup = bs4.BeautifulSoup(page,'lxml')
    soup_img = soup.find_all('img',alt=True)
    for img in soup_img:
        try:
            raw_url = img['src']
            if 'svg' in raw_url:
                continue
            queue_url.put(raw_url)

        except:
            continue

def downliad_pic():
    global queue_url
    while True:
        if queue_url.empty():
            print('over')
            break
        pic_url = queue_url.get()
        req = requests.get(pic_url,headers=header)
        content = req.content
        pic_name = pic_url.split('/')[-1]
        with open(pic_name,'wb')as f:
            f.write(content)

def main():
    url = 'http://www.lifeofpix.com/'
    get_pic_urls(url)
    threads = []
    for i in range(5):
        t = threading.Thread(target=downliad_pic)
        threads.append(t)

    for i in threads:
        i.start()

    for i in threads:
        i.join()

if __name__ == '__main__':
    main()
