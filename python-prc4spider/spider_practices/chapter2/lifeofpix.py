import requests
import bs4
import threading
import queue
import os


'''
url = http://www.lifeofpix.com/
爬取该网站的首页图片，使用的技术包括 requests+bs4+threading+queue
为了加快下载速度，使用到了多线程技术

'''

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
                        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}


# 获取某一页所有图片地址
def get_pic_urls(url):
    pic_adds = []

    req = requests.get(url,headers=header)
    page = req.text
    soup = bs4.BeautifulSoup(page,'lxml')
    soup_img = soup.find_all('img',alt=True)
    for img in soup_img:
        try:
            raw_url = img['src']
            if 'svg' in raw_url:
                continue
            pic_adds.append(raw_url)

        except:
            continue

    return pic_adds


# 下载图片
def downliad_pic(pic_url):

    req = requests.get(pic_url,headers=header)
    content = req.content
    pic_name = pic_url.split('/')[-1]
    with open(pic_name,'wb')as f:
        f.write(content)


# 主函数
def main():
    url = 'http://www.lifeofpix.com/page/{}/'
    for i in range(1,3):
        print('正在下载第 {} 页图片'.format(i))
        l_url = url.format(i)
        pic_urls = get_pic_urls(l_url)
        # 多线程
        threads = []
        for i in pic_urls:
            t = threading.Thread(target=downliad_pic,args=(i,))
            threads.append(t)

        for i in threads:
            i.start()



if __name__ == '__main__':
    main()
