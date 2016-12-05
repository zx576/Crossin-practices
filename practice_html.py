import bs4
import requests

'''
思路：请求一个网址，然后拿到网址的信息，从其中找出所有的超链接标签，最后将其分类
'''
#请求网址,拿到html数据
def request_url(url):
    #构造header
    header = {'User-Agent':
                  'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
              }
    try:
        response = requests.get(url,headers=header)
    except Exception as e:
        print('错误信息：',e)

    else:
        fetched_info = response.text
        return fetched_info

#获取其中所有的超链接
def bs_filter(data):
    if data != None:
        info = bs4.BeautifulSoup(data,'html.parser')
        get_tag_a = info.find_all('a')
        get_href = [i.get('href') for i in get_tag_a]
        print(get_href)



def main():
    print('input a website')
    # url = 'http://www.duitang.com/'
    url = input('>>>')
    data = request_url(url)
    bs_filter(data)

if __name__ == '__main__':
    main()