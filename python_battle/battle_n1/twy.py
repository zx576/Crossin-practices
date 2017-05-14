# coding:utf-8
import urllib
import urllib2
from bs4 import BeautifulSoup


baseurl = 'http://www.40ssss.com/t01/'
host = 'http://www.40ssss.com/'


def get_page_menu(baseurl,pagenum):
    pagenum.reverse()
    for page in pagenum:
        url = baseurl + page
        response = urllib2.urlopen(url).read().decode('utf-8')
        soup = BeautifulSoup(response,"html.parser")
        title = soup.find_all(name='a', attrs={
            'target': "_blank"
        })
        hrefs = []
        content = []
        for item in title:
            content.append(item.get_text())
        content.pop(0)
        for page in title:
            hrefs.append('http://www.40ssss.com/'+ page.attrs['href'])
        hrefs.pop(0)
        novel_info = zip(content,hrefs)
        d = {}
        for title,url in novel_info:
            d[title] = url
        for info in d:
            get_novel(d[info],info)
            name = info
            print "%r" % name + "下载完成！"





def get_pagenum():
    global url_lst
    url_lst = ['index.html']
    url = 'http://www.40ssss.com/t01/index.html'
    response = urllib2.urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(response, "html.parser")
    pagenum = soup.find(name='strong')
    total = pagenum.get_text()[2:]
    for i in range(1,int(total)):
        url_lst.append('list_'+str(i)+'.html')
    return url_lst

def get_novel(url,name):
    response = urllib2.urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(response, "html.parser")
    novel = soup.find_all(name='p')
    content = ""
    novel_1 = soup.find_all(name='font', attrs={
        'style': "font-size:15px;",
        'color': "#0000FF"
    })
    novel_2 = soup.find_all(name='div', attrs={
        'id': "view2",
        'class': "mtop"
    })
    if novel is not None:
        for m in novel:
            for i in m.get_text().split():
                content = content + i + '\r\n'
    if novel_1 is not None:
        for m in novel_1:
            for i in m.get_text().split():
                content = content + i + '\r\n'
    if novel_2 is not None:
        for m in novel_1:
            for i in m.get_text().split():
                content = content + i + '\r\n'

    content = content.encode('utf-8')
    with open(r"%s.txt" % name,'wb') as f:
        f.write(content)





get_pagenum()
get_page_menu(baseurl,url_lst)
