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
        'Cookie': 'wb_publish_fist100_2426968121=1; wb_publish_fist100_6055629257=1; wb_g_upvideo_6055630039=1; wb_publish_fist100_6055630039=1; CNZZDATA1260210782=928241306-1483959022-null%7C1483969827; SINAGLOBAL=2458790768267.9624.1483971207167; TC-Ugrow-G0=02e35d9240e6933947925d24232af628; login_sid_t=2eddfd292275e945938e8072bbd88005; TC-V5-G0=52dad2141fc02c292fc30606953e43ef; _s_tentry=-; Apache=2157019250719.7073.1484019017838; ULV=1484019017844:3:3:3:2157019250719.7073.1484019017838:1484013812105; TC-Page-G0=fd45e036f9ddd1e4f41a892898506007; wb_g_upvideo_6055501997=1; SSOLoginState=1484035531; WBtopGlobal_register_version=c689c52160d0ea3b; SCF=AhpUAUcSW-Jr21YdIICYmB2Uqi9-xfS-RhaYkn24qYkBdBsp-MRZPVnO19UjTC4uDeQDnp7MiZSKabNrxX-SoxY.; SUB=_2A251cOh6DeRxGeBO7lUS-S_Izz-IHXVWBF6yrDV8PUNbmtAKLULjkW8RSmtTdHgNLG7KMrbye6lAq0FT4Q..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhCbcWsBWNV7dR0rp4hzLi.5JpX5K.hUgL.Foq7SKM01K2XShe2dJLoIXnLxKMLBKML12zLxKqL1h2L12zLxK-L1K5L1K-LxK-L122LBozLxKnL12qLBo2LxKqL12-L12qLxK-LBoBL1hMLxKqL12zL1-et; SUHB=0FQriybQVk3wAZ; ALF=1484640939; un=15224074401; wvr=6; UOR=,www.weibo.com,www.baidu.com',
        # 'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        'Host': 'weibo.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }

    t = 1
    while t < 10:
        # 随机选择 cookies
        # cookie = random.choice(cookies)
        # print(cookie)
        # 随机选择 agents
        # agent = random.choice(agents)
        # print(agent)
        # headers['Cookie'] = cookie
        # headers['User-Agent'] = agent
        # 尝试请求
        try:
            print(url)
            res = requests.get(url,headers=headers)
            content = res.json()
        # 错误后继续 while 循环
        except:
            # t += 1
            continue
        # 成功后返回内容
        # print(content['data']['page']['totalpage'])
        # if content['data']['page']['totalpage'] != 8:
        #     t += 1
        #     continue
        # t += 1
        return content

def fetch_repost(url):
    # 起始页数
    page = 140
    # 用户 id
    uid = []
    # download_pages = []
    # 正则抓取用户 id
    rule = re.compile(r'uid=(\d{10})')
    url_d = url
    while page < 164:
        print('抓取第 %r 页'%page)
        # print(page)
        # 拼接 url
        # url[-1] = str(page)
        # 调用 request_url 返回内容
        new_url = url_d + str(page)
        content = request_url(new_url)
        status = content['code']
        # print(status)
        # 总页数
        total_page = content['data']['page']['totalpage']
        # print(total_page)
        # 当前页数
        currentpage = content['data']['page']['pagenum']
        print(currentpage)
        # print('request success on page %r' %currentpage)
        # 抓取内容
        data = content['data']['html']
        all_uid = re.findall(rule,data)
        print(all_uid)
        # 合并列表
        uid = uid + all_uid
        print(uid)
        # 页数加 1 ，继续循环
        page += 1
        # # 抓完所有数据
        # if currentpage > total_page:
        #     print('all done')
        #     break
        break
        time.sleep(1)
    # 去重
    uid = set(uid)
    uid = list(uid)
    # 返回
    return uid

# def fetch_comment(url):


# 写入文件
def save(uid):
    # 组装为 json 格式
    dic = {}
    dic['repost_data'] = uid
    repost_data_str = json.dumps(dic)
    with open('repostdata.txt','a+') as f:
        f.write('\n')
        f.write(repost_data_str)
    print('successly save')

def main():
    url = 'http://weibo.com/aj/v6/mblog/info/big?ajwvr=6&id=4060642426157630&max_id=4062289714329117&page='
    print('start crwal')
    uid = fetch_repost(url)
    # print('下载了 %r 页'%page)
    save(uid)

if __name__ == '__main__':
    main()
