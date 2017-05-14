#-*- coding:utf-8 -*-
import requests
import bs4
import os

header = {'User-Agent':
                  'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
          }
#请求网址，抓取从N页到M页妹子图片链接，返回list，包含所有链接地址
def req(start_page,end_page):
    #生成图片地址的空列表
    fecthed_pic_add_all = []
    #逐一访问页面
    for i in range(start_page,end_page+1):
        jiandan_url = 'http://jandan.net/ooxx/page-'+str(i)
        #防止请求错误
        try:
            response = requests.get(jiandan_url,headers= header)
        except Exception as e:
            print('请求出现错误，错误信息：%s' %e)
        else:
            #确定访问正常后，得到页面信息
            content = response.text
            #将信息传入bs4
            fecthed_info = bs4.BeautifulSoup(content,'html.parser')
            #寻找所有包含图片地址的tag
            fecthed_info_tagA = fecthed_info.find_all('a','view_img_link')
            #得到本页面所有图片地址
            fecthed_pic_add = [l.get('href') for l in fecthed_info_tagA]
            #将该页面图片地址添加到总表
            for i in fecthed_pic_add:
                fecthed_pic_add_all.append(i)
    #返回图片地址列表
    print(fecthed_pic_add_all)
    return fecthed_pic_add_all
#下载图片
def downliad_pic(pic_addresses):
    #遍历图片地址
    for i in pic_addresses:
        try:
            #请求图片网址
            pic_resp = requests.get(i,headers = header)
            #二进制方式读取网页
            pic = pic_resp.content
            pic_name = i.split('/')[-1]
            #以‘wb’写入文件
            with open('pic/'+pic_name,'wb') as f:
                f.write(pic)
                print('文件\t'+pic_name+'\t已下载')
        except Exception as e:
            print('下载出现错误，信息：%s' %e)

def main():
    #判断是否创建下载文件夹
    create_file = os.path.exists('pic')
    #print(create_file)
    if not create_file:
        os.mkdir('pic')
        print('已创建了下载文件夹')
    print('设置您要下载的开始页与最终页：')
    while True:
        try:
            start_page = int(input('起始页：'))
            end_page = int(input('最终页：'))
            if end_page < start_page:
                print('最终页小于起始页')
                continue
        except:
            print('输入不合法')
        else:
            break
    print('正在下载...')
    pic_addresses = req(start_page,end_page)
    downliad_pic(pic_addresses)
    print('全部下载完成')

main()
