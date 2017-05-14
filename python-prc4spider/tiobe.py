# -*- coding: utf-8 -*-
import requests
from wordcloud import WordCloud
import bs4

# 访问 TIOBE ,获取数据
def get_data(url):
    req = requests.get(url)
    page = req.text
    soup = bs4.BeautifulSoup(page,'lxml')

    soup_table = soup.find('table',class_='table-top20')
    soup_tr = soup_table.tbody.find_all('tr')

    data = []
    for tr in soup_tr:
        soup_td = tr.find_all('td')

        cur_rank = soup_td[0].string
        last_rank = soup_td[1].string

        try:
            src = soup_td[2].img['src']
            st = src.split('.')[0]
            status = st.split('/')[-1]

        except:
            status = ''

        lang = soup_td[3].string
        rating = soup_td[4].string
        changed = soup_td[5].string

        data.append([cur_rank,last_rank,status,lang,rating,changed])
    print(data)
    return data

# 生成图片一
def plot1(data):
    wc = WordCloud()
    dct = {}
    count = 100
    for item in data:
        lang = item[3]
        dct[lang] = count
        count -= 1

    wc.generate_from_frequencies(dct)
    wc.to_file('tiobe_pic1.png')
# 生成图片二
def plot2(data):
    pass
    
# 生成图片三
def plot3(data):
    pass
# 生成图片四
def plot4(data):
    pass

# 主函数
def main():
    url = 'https://www.tiobe.com/tiobe-index/'
    data = get_data(url)
    plot1(data)
    plot2(data)
    plot3(data)
    plot4(data)

if __name__ == '__main__':
    main()
