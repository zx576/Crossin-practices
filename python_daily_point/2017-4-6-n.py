import requests
import bs4

url = 'http://weixin.sogou.com/weixin?query=crossin%E7%9A%84%E7%BC%96%E7%A8%8B%E6%95%99%E5%AE%A4&_sug_type_=&sut=1612&lkt=1%2C1491472425348%2C1491472425348&s_from=input&_sug_=y&type=2&sst0=1491472425449&page=1&ie=utf8&w=01019900&dr=1'



headers = {

'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'


}

def req_url(url):
    req = requests.get(url,headers=headers)
    content = req.text

    soup = bs4.BeautifulSoup(content,'lxml')

    soup_div = soup.find_all('div',class_='txt-box')
