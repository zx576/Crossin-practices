import requests
import re
import time
import json
from crwal.user_agents import agents
import random

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    # 'Content-Type':'application/x-www-form-urlencoded',
    'Cookie': 'SCF=AhpUAUcSW-Jr21YdIICYmB2Uqi9-xfS-RhaYkn24qYkB4zo2yeR3rBb250YJYTc8dHImjSVPh4yocEqBFU65xPg.; SUB=_2A251cIKZDeRxGeBO7lcX8ifOzjuIHXVWB_NRrDV8PUNbmtBeLRTVkW8K8dZCQBHlJJNPcnvtQvH5Pa2_EQ..; bai=16.; wvr=6; _s_tentry=-; Apache=976599875082.1892.1484059342992; SINAGLOBAL=976599875082.1892.1484059342992; ULV=1484059343007:1:1:1:976599875082.1892.1484059342992:; UOR=,www.weibo.com,spr_sinamkt_buy_srwj1_weibo_t130; BAYEUX_BROWSER=3cb5-tt2do4tndil6ixrmmbwkbzp',
    # 'DNT': '1',
    # 'Upgrade-Insecure-Requests': '1',
    'Host': 'weibo.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
}

# 获取数据
def fetch_data(url,uid_list):
    # 拼凑 re 表达式
    rule = re.compile(r'\[\'page_id\'\]=\'(\d{16})\'')
    # 存放 page_id 的 list
    page_id = []
    # 不能使用 id
    wrong_id = []
    # 遍历 user_id
    i = 1004
    for id in uid_list:
        print('请求',id,i)
        # 组装 url
        r_url = url + id
        print(r_url)
        i += 1
        # 请求
        response = requests.get(r_url,headers=headers)
        content = response.text
        # print(content)
        # print(type(content))
        # 获取 page_id
        try:
            id = re.findall(rule,content)[0]
        except:
            print(id,'错误')
            wrong_id.append(id)
            continue
        print(id)
        # 判断 id
        if id:
            page_id.append(id)
        else:
            print(id,'失败')
            continue
        print(page_id)
        print(wrong_id)
        # break
        time.sleep(1)
    return page_id

def save(uid):
    # 组装为 json 格式
    dic = {}
    dic['repost_data'] = uid
    repost_data_str = json.dumps(dic)
    with open('page_id.txt','w') as f:
        f.write('\n')
        f.write(repost_data_str)
    print('successly save')

def main():
    # 打开文件
    with open('repostdata.txt','r') as file:
        content = file.read()
        # print(content)
    # 拿到 list 数据
    data = json.loads(content)
    uid_list = data['repost_data'][1005:2100]
    # print(len(uid_list))
    # uid_list = [6057391443,]
    url = 'http://weibo.com/u/'
    page_id,wrong_id = fetch_data(url,uid_list)
    # print('错误id：',wrong_id)
    save(page_id)



if __name__ == '__main__':
    main()