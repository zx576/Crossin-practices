#-*- coding:utf-8 -*-
import requests
import json
import re
import sqlite3
import time

'''
功能：提取可用 ip 的接口
从 ip 数据池中获得最新抓取的 ip，这样做的好处是防止过快失效的 ip 影响网络请求进度
'''

# 连接数据库，获取最新获取的 ip
def extrat_lastest_id():
    DATABASE = 'ip_list.db'
    conn = sqlite3.connect(DATABASE)
    sql = r'SELECT max(id) FROM IPLIST'
    last_id = conn.execute(sql).fetchone()[0]
    sql2 = r'SELECT * FROM IPLIST WHERE ID = %d;'%last_id
    lastest_ip = conn.execute(sql2).fetchone()
    conn.close()
    print(lastest_ip)
    return lastest_ip


# 验证 ip
def verify_ip(ip):
    # ip_list = opensql()
    headers1 = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1;'
                      ' en-US)AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20',
    }
    testurl = 'http://www.baidu.com/'
    # for ip in ip_list:
    try:
        res = requests.get(testurl,headers=headers1,proxies=ip,timeout=2)
        if 'STATUS OK' in res.text:
            return 1
            # break
        else:
            return
            # continue
    except:
        return

# 删除 ip
def delectip(id):
    DATABASE = 'ip_list.db'
    # created = os.path.exists(DATABASE)
    conn = sqlite3.connect(DATABASE)
    # ip = str(ip)
    sql = r'DELETE FROM IPLIST WHERE ID = %d;' % id
    query = conn.execute(sql)
    conn.commit()
    conn.close()

# 控制 ip 模块
def extract_ip():
    # 提取 ip
    while True:
        # 提取最新的 ip（包含 id）
        lastest_info = extrat_lastest_id()
        # 如果 ip 被用光了，休息 5 秒再继续，等待多线程爬取 ip
        if not lastest_info:
            time.sleep(5)
            continue
        lastest_id = lastest_info[0]
        lastest_ip = re.sub('\'', '\"', lastest_info[1])
        lastest_ip = json.loads(lastest_ip)
        # print(type(lastest_ip))
        # 验证 ip，成功则返回该 ip
        if verify_ip(lastest_ip):
            # print(lastest_ip)
            return lastest_ip
        # 否则删除
        else:
            delectip(lastest_id)


# ip_main()
# extrat_lastest_id()
extract_ip()