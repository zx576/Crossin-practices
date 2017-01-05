#-*- coding:utf-8 -*-
import requests
import json

header = {'User-Agent':
                  'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
          }
def fetchData():
    #访问排名页面
    response = requests.get('http://rj.baidu.com/soft/ranking/1',headers=header)
    #拿到网页数据
    content = response.text
    #将unicode转为str
    str_content = content.encode('utf8')
    #采用索引的方式拿到需要的数据
    start_index = str_content.find('var configs =  ') + len('var configs =  ')
    end_index = str_content.find(('var loginUrl'))
    content = str_content[start_index:end_index].strip()
    content = content[:-1]
    #将str使用json处理
    content = json.loads(content)
    info = content.get('data').get('softList').get('list')
    software_urls = []
    #取出软件地址
    for i in info:
        url = i.get('url')
        software_urls.append(url)
    print software_urls
    return software_urls

def download(urls):
    #逐个拿出软件地址
    for url in urls[:2]:
        #获取软件名
        software_name = url.split('/')[-1]
        print '正在下载',software_name
        #请求软件数据
        response = requests.get(url,headers=header)
        software = response.content
        #下载
        with open(software_name,'wb') as f:
            f.write(software)
            print '文件',software,'已下载'



def main():
    print '开始下载'
    urls = fetchData()
    download(urls)
    print '下载完成'


if __name__ == '__main__':
    main()