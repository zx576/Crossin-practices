import requests
import threading
import bs4
import os


header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
                        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}

# 获取名鞋库某一页下商品条目的图片地址和商品描述
def get_pic(url):

    req = requests.get(url,headers=header)
    page = req.text
    soup = bs4.BeautifulSoup(page,'lxml')
    soup_div = soup.find('div',class_='product_list')
    soup_dl = soup_div.find_all('dl')

    for dl in soup_dl:
        pic_url = 'http:'+dl.a.img['src']
        title = dl.a['title'].replace('/','')
        price_li = dl.find('li',class_='r1')
        price = price_li.i.get_text()[1:]
        describe = '价格'+price+'描述'+title+'.jpg'
        download(pic_url,describe)

# 下载图片，并将描述设置位文件名
def download(pic,des):

    check_dir = os.path.exists('pic')
    if not check_dir:
        os.mkdir('pic')

    req = requests.get(pic,headers=header)
    pic_content = req.content

    with open('pic/{}'.format(des),'wb')as f:
        f.write(pic_content)


# 主函数，按页数设置多线程
def main():
    url = 'http://www.s.cn/list/pg{}?p=NIKE'
    threads = []

    for i in range(1,4):
        p_url = url.format(i)
        t = threading.Thread(target=get_pic,args=(p_url,))
        threads.append(t)

    for i in threads:
        i.start()

    for i in threads:
        i.join()

if __name__ == '__main__':
    main()
