import bs4
import requests
import re
import time
import json
from crwal.cookies import cookies
from crwal.user_agents import agents
import random
'''
下载杜蕾斯2016年12个月所有微博id
'''


# 请求网络，获得网络响应
def request_url(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        # 'Content-Type':'application/x-www-form-urlencoded',
        'Cookie': 'wb_publish_fist100_2426968121=1; wb_publish_fist100_6055629257=1; wb_g_upvideo_6055630039=1; wb_publish_fist100_6055630039=1; wb_g_upvideo_6055501997=1; CNZZDATA1260210782=928241306-1483959022-null%7C1484056210; SINAGLOBAL=976599875082.1892.1484059342992; wvr=6; wb_g_upvideo_6055629257=1; TC-Ugrow-G0=5e22903358df63c5e3fd2c757419b456; login_sid_t=16e46bbc135d08a302fedeae1f091120; TC-V5-G0=866fef700b11606a930f0b3297300d95; _s_tentry=-; UOR=,www.weibo.com,www.baidu.com; Apache=4236363804304.171.1484529465788; ULV=1484529465794:7:7:2:4236363804304.171.1484529465788:1484470021353; SCF=AhpUAUcSW-Jr21YdIICYmB2Uqi9-xfS-RhaYkn24qYkBCuEySENedq0nZ9q-8fikGeEmAutvTFDVh3mqmojOSqk.; SUB=_2A251eG9vDeRxGeBO7lcX8ifOzjuIHXVWDMenrDV8PUNbmtAKLRHHkW9mKFUWjH-GJ5AX1ThbnKzsOQJKHw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh8VT9hUEzW9FOqAGr5nzPz5JpX5K2hUgL.Foq7SK-ceo.ESKM2dJLoIXnLxKMLB.-L1--LxKnL122LBo2LxK.L1KnLB--LxKqL1-zLB.eLxKqLBozLBoeLxK.L1K-L1hMLxKML1KqLB.eLxKML1KML1-zt; SUHB=0pHx1wTmUZIJAy; ALF=1516065470; SSOLoginState=1484529471; un=14794601372; TC-Page-G0=b1761408ab251c6e55d3a11f8415fc72',
        # 'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        'Host': 'weibo.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }
    print('请求url:%s' % url)
    # 请求数据
    try:
        req = requests.get(url, headers=headers)
        content = req.text
        # print('请求成功')
    except:
        return
    return content

# 传入响应数据，获取微博 id
def fetch_repost(content):
    rule = re.compile(r'mid=(\d{16})')
    # data = content['data']
    all_uid = re.findall(rule,content)
    uid = set(all_uid)
    # 返回
    print(uid)
    return uid

# 传入所有 id 写入文件
def save(uid):
    # 组装为 json 格式
    dic = {}
    dic['mid_data'] = uid
    repost_data_str = json.dumps(dic)
    with open('mid.txt','a+') as f:
        f.write('\n')
        f.write(repost_data_str)
    print('successly save')

def main():
    # 组装 URL
    pre_url = 'http://weibo.com/p/aj/v6/mblog/mbloglist' \
          '?ajwvr=6&domain=100606&is_all=1&stat_date=2016%s&page=%s&pagebar=0&pl_name=Pl_Official_MyProfileFeed__26&id=1006061942473263'
    # 抓取 12 个月
    months = ['01','02','03','04','05','06','07','08','09','10','11','12']
    # 每月抓取前 6 页
    page_list = ['1','2','3','4','5','6']
    # pagebar_list = ['0','1','2']
    # 所有 URL
    url_list = []
    for month in months:
        for page in page_list:
            # for pagebar in pagebar_list:
            url = pre_url%(month,page)
            url_list.append(url)
    # 去重
    total_id = set()
    # 逐条抓取
    for url_id in range(len(url_list)):
        print(url_id)
        content = request_url(url_list[url_id])
        if not content:
            continue
        uid_once = fetch_repost(content)
        total_id.update(uid_once)
        time.sleep(2)
        # break
    # print('下载了 %r 页'%page)
    total_id = list(total_id)
    # 保存数据
    save(total_id)

if __name__ == '__main__':
    main()
