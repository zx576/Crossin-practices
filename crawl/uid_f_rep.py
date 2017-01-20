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
        'Cookie': 'wb_publish_fist100_2426968121=1; wb_publish_fist100_6055629257=1; wb_g_upvideo_6055630039=1; wb_publish_fist100_6055630039=1; wb_g_upvideo_6055501997=1; CNZZDATA1260210782=928241306-1483959022-null%7C1484056210; SINAGLOBAL=976599875082.1892.1484059342992; wvr=6; wb_g_upvideo_6055629257=1; TC-Ugrow-G0=5e22903358df63c5e3fd2c757419b456; login_sid_t=16e46bbc135d08a302fedeae1f091120; TC-V5-G0=866fef700b11606a930f0b3297300d95; _s_tentry=-; UOR=,www.weibo.com,www.baidu.com; Apache=4236363804304.171.1484529465788; ULV=1484529465794:7:7:2:4236363804304.171.1484529465788:1484470021353; SCF=AhpUAUcSW-Jr21YdIICYmB2Uqi9-xfS-RhaYkn24qYkBCuEySENedq0nZ9q-8fikGeEmAutvTFDVh3mqmojOSqk.; SUB=_2A251eG9vDeRxGeBO7lcX8ifOzjuIHXVWDMenrDV8PUNbmtAKLRHHkW9mKFUWjH-GJ5AX1ThbnKzsOQJKHw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh8VT9hUEzW9FOqAGr5nzPz5JpX5K2hUgL.Foq7SK-ceo.ESKM2dJLoIXnLxKMLB.-L1--LxKnL122LBo2LxK.L1KnLB--LxKqL1-zLB.eLxKqLBozLBoeLxK.L1K-L1hMLxKML1KqLB.eLxKML1KML1-zt; SUHB=0pHx1wTmUZIJAy; ALF=1516065470; SSOLoginState=1484529471; un=14794601372; TC-Page-G0=b1761408ab251c6e55d3a11f8415fc72',
        # 'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        'Host': 'weibo.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }
    # print('请求url:%s' % url)
    # 请求数据
    try:
        req = requests.get(url, headers=headers)
        content = req.json()
        # print('请求成功')
    except:
        return
    return content
    # print('请求 %s 失败'%url)
# 总页数
total_page = 10000
def fetch_repost(content):
    global total_page
    rule = re.compile(r'uid=(\d{10})')
    # status = content['code']
    # print(status)
    # 总页数
    total_page = content['data']['page']['totalpage']
    # print('inside func ttp :%r'%total_page)
    # 当前页数
    # currentpage = content['data']['page']['pagenum']
    # print(currentpage)
    # print('request success on page %r' %currentpage)
    # 抓取内容
    data = content['data']['html']
    all_uid = re.findall(rule,data)
    uid = set(all_uid)
    print(uid)
    # 返回
    return uid

# 写入文件
def save(uid,id,filecount):
    # 组装为 json 格式
    dic = {}
    dic[id] = uid
    repost_data_str = json.dumps(dic)
    with open('E:/GIT/practice/Crossin-practices/crwal/uid_f_re/uid_%r.txt'%filecount,'a+',errors='ignore') as f:
        f.write('\n')
        f.write(repost_data_str)
    print('successly save')

def distribute_url(f_url):
    # print('start crwal')
    start_page = 1
    # 需要手动设置
    # end_page = 100
    total_id = set()
    global total_page
    while start_page <= total_page:
        newurl = f_url + str(start_page)
        print('request url：%s' % newurl)
        # print('')
        start_page += 1
        content = request_url(newurl)
        if not content:
            continue
        uid_once = fetch_repost(content)
        total_id.update(uid_once)
        time.sleep(2)
        print('outside func ttp:%r'%total_page)
        # break
    return total_id

def openfile():
    with open('mid.txt','r') as f:
        pre_data = f.read()
    content = json.loads(pre_data)
    data = content['mid_data']
    return data

def main():
    pre_url = 'http://weibo.com/aj/v6/mblog/info/big?ajwvr=6&id=%s&page='
    # print('下载了 %r 页'%page)
    data = openfile()
    file_count = 3
    loop_count = 1
    for id in range(773,len(data)):
        print('mid:%d'%id)
        f_url = pre_url%(data[id])
        result = distribute_url(f_url)
        total_id = list(result)

        if loop_count == 100:
            file_count += 1
            loop_count = 1
        loop_count += 1
        save(total_id, data[id],file_count)
        # break

if __name__ == '__main__':
    main()
