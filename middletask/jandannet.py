import requests
import re
import threading


def get_pics(num):
    url = 'http://jandan.net/ooxx/page-%i' % num
    a = requests.get(url)
    a.encoding = a.apparent_encoding
    page = a.text
    # print(page[10:])
    result = ['http:' + x[10:] for x in re.findall('<img src=".+.jpg{1}?', page)]
    for url in result:
        # print(url[28:])
        pic = requests.get(url)
        with open(url[28:], 'wb') as f:
            f.write(pic.content)
        print('%s下载完成' % url[28:])


def webspider():
    start = int(input('请输入开始页数：'))
    end = int(input('请输入结束页数：'))
    pages = range(start, end+1)
    threads = []
    for i in pages:
        threads.append(threading.Thread(target=get_pics, args=(i,)))
    for t in threads:
        t.setDaemon(True)
        t.start()


webspider()
input('等待结果，按回车键退出：\n')
