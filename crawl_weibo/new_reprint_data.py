import bs4
import requests
import re
import time
import json
from crwal.cookies import cookies
from crwal.user_agents import agents
import random
'''
1.10:
下载杜蕾斯某一条消息下面的所有转载人的信息

'''


# 变换cookies,agents,ip请求网址, 发生错误后，更换 cookies,agents,ip 继续请求，直到有结果返回
def request_url(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        # 'Content-Type':'application/x-www-form-urlencoded',
        'Cookie': 'wb_publish_fist100_2426968121=1; wb_publish_fist100_6055629257=1; wb_g_upvideo_6055630039=1; wb_publish_fist100_6055630039=1; wb_g_upvideo_6055501997=1; CNZZDATA1260210782=928241306-1483959022-null%7C1484056210; SINAGLOBAL=976599875082.1892.1484059342992; wvr=6; un=14794601372; wb_g_upvideo_6055629257=1; SCF=AhpUAUcSW-Jr21YdIICYmB2Uqi9-xfS-RhaYkn24qYkBOj15UYEn13kalfzC0T7Z0y2DYEGEFmnXgbV_AyWp9CI.; SUB=_2A251foFCDeRxGeBO7lcX8ifOzjuIHXVWDfWKrDV8PUNbmtBeLUXtkW8ID5EwVGUcWpp3ZSLaucJrtaYrxw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh8VT9hUEzW9FOqAGr5nzPz5JpX5KMhUgL.Foq7SK-ceo.ESKM2dJLoIXnLxKMLB.-L1--LxKnL122LBo2LxK.L1KnLB--LxKqL1-zLB.eLxKqLBozLBoeLxK.L1K-L1hMLxKML1KqLB.eLxKML1KML1-zt; SUHB=0D-FSxFj6AjuRg; ALF=1515988111; SSOLoginState=1484452114; _s_tentry=login.sina.com.cn; YF-Ugrow-G0=1eba44dbebf62c27ae66e16d40e02964; YF-V5-G0=e2def7ce19d3add53399b18462da454a; Apache=811575399088.3756.1484470021319; ULV=1484470021353:6:6:1:811575399088.3756.1484470021319:1484295157617; UOR=,www.weibo.com,www.baidu.com; YF-Page-G0=c47452adc667e76a7435512bb2f774f3',
        # 'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        'Host': 'weibo.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }
    t = 1
    while t < 10:
        try:
            print(url)
            res = requests.get(url,headers=headers)
            content = res.json()
        # 错误后继续 while 循环
        except:
            # t += 1
            continue
        return content
    print('请求 %s 失败'%url)
def fetch_repost(content):
    rule = re.compile(r'uid=(\d{10})')
    # status = content['code']
    # print(status)
    # 总页数
    # total_page = content['data']['page']['totalpage']
    # print(total_page)
    # 当前页数
    currentpage = content['data']['page']['pagenum']
    print(currentpage)
    # print('request success on page %r' %currentpage)
    # 抓取内容
    data = content['data']['html']
    all_uid = re.findall(rule,data)
    uid = set(all_uid)
    # 返回
    return uid

# 写入文件
def save(uid):
    # 组装为 json 格式
    dic = {}
    dic['repost_data'] = uid
    repost_data_str = json.dumps(dic)
    with open('repostdata1.txt','w') as f:
        f.write('\n')
        f.write(repost_data_str)
    print('successly save')

def main():
    url = 'http://weibo.com/aj/v6/mblog/info/big?ajwvr=6&id=4060642426157630&max_id=4062289714329117&page='
    # print('start crwal')
    start_page = 1
    # 需要手动设置
    end_page = 100
    total_id = set()
    while start_page < end_page:
        newurl = url + str(start_page)
        print('request url：%s' %newurl)
        # print('')
        start_page += 1
        content = request_url(newurl)
        if not content:
            continue
        uid_once = fetch_repost(content)
        total_id.update(uid_once)
        time.sleep(1)
        break
    # print('下载了 %r 页'%page)
    total_id = list(total_id)
    save(total_id)

if __name__ == '__main__':
    main()
