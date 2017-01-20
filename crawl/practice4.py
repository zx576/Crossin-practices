import requests
import re
import json
import random
import sqlite3
# requests.get(timeout=)

# rule = re.compile(r'http')
# string = 'httpfdghfdjghjkgh'
# rs = re.match(rule,string)
# print(rs)
# headers = {
# 'User-Agent':'"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",',
# }
#
#
# def openfile():
#     with open('iplist.txt','r')as f:
#         all_d = f.readlines()
#     iplist = []
#     for i in all_d:
#         test = re.sub('\'', '\"', i)
#         lis1 = json.loads(test)
#         for ip in lis1:
#             iplist.append(ip)
#     return iplist
#
#
#
# def req(url):
#     iplist = openfile()
#     print(iplist)
#     proxy = random.choice(iplist)
#     res = requests.get(url,proxies=proxy,headers=headers,timeout=2)
#     rest = res.text
#     print(rest)
#
# url = 'http://www.xicidaili.com/wt/'
# req(url)

# a = set()
# a.add('s')
# a.add('b')
# for i in a:
#     print(i)
# 连接 ip 数据库
def opensql():
    DATABASE = 'ip_list.db'
    # created = os.path.exists(DATABASE)
    conn = sqlite3.connect(DATABASE)
    sql = r'SELECT * FROM IPLIST'
    query = conn.execute(sql)
    alldata = query.fetchall()
    ip_list = []
    for i in alldata:
        str_ip = i[1]
        # str_ip = re.sub('\'', '\"', str_ip)
        dict_ip = json.loads(str_ip)
        ip_list.append(dict_ip)
    conn.close()
    return ip_list


# 验证 ip
def handleip(ip):
    # ip_list = opensql()
    headers1 = {
        'User-Agent': '"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",',
    }
    testurl = 'http://www.baidu.com/'
    # for ip in ip_list:
    try:
        res = requests.get(testurl,headers=headers1,proxies=ip)
        if 'STATUS OK' in res.text:
            return 1
            # break
        else:
            return
            # continue
    except:
        return

# 删除 ip
def delectip(ip):
    DATABASE = 'ip_list.db'
    # created = os.path.exists(DATABASE)
    conn = sqlite3.connect(DATABASE)
    ip = str(ip)
    sql = r'SELECT * FROM IPLIST WHERE IP = "%s"' % ip
    query = conn.execute(sql)
    print('删除成功')
    conn.commit()
    conn.close()

# 控制 ip 模块
def ip_main():
    # 获取 ip_list
    ip_list = opensql()
    for ip in ip_list:
        # u_ip = json.loads(ip)
        print(ip)
        print(type(ip))
        if handleip(ip):
            return ip
        else:
            delectip(str(ip))
            continue

ip_main()