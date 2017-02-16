#-*- coding:utf-8 -*-
import requests
import bs4
import json
import re
import sqlite3
import os
import threading
import time


headers = {
        'User-Agent':'"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) '
                     'AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",',
}

# 西刺代理
def fetch_xici():
    url = 'http://www.xicidaili.com/wt'
    page_content = requests.get(url,headers=headers)
    str_content = page_content.text
    # print(str_content)
    soup = bs4.BeautifulSoup(str_content,'lxml')
    # 筛选出所有包含 ip 的 tr 标签
    tr_list = soup.find_all('tr',attrs={'class':['odd','']})
    # ip 列表
    ip_list = []
    # 编译 ip 地址正则表达式
    ip_rule = re.compile(r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})')
    # 编译 ip 端口正则表达式
    port_rule = re.compile(r'\>(\d+)\<')
    for tr in tr_list:
        str_tr = str(tr)
        # print(str_tr)
        re_m = re.search(r'HTTP',str_tr)
        # print(re_m)
        if re_m:
            dic1 = {}
            # 匹配 ip 地址
            ip = re.findall(ip_rule,str_tr)[0]
            # 匹配端口
            port = re.findall(port_rule,str_tr)[0]
            # 组装为可用的 ip 地址
            dic1["http"] = "http://" + ip + ":" + port
            # print(dic1)
            # 验证 ip 是否可用
            if verify_ip(dic1):
                # print('可用')
                # 验证可用后存入数据库
                insertdata(dic1)
                print(dic1)
                # ip_list.append(dic1)
    # print('西刺',ip_list)
    # return ip_list

# =================================================================================

# 有代理网
def fetch_udaili():
    url = 'http://www.youdaili.net/Daili/http/29487.html'
    page_content = requests.get(url, headers=headers)
    str_content = page_content.text
    # print(str_content)
    soup = bs4.BeautifulSoup(str_content, 'lxml')
    # script_tag = soup.find('script',text='@HTTP')
    p_tags = soup.find_all('p')
    rule = re.compile(r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d+)')
    # alldata = []
    for p in p_tags:
        try:
            ip = re.findall(rule,str(p))[0]
            # print(ip)
            dic = {}
            if ip:
                dic["http"] = "http://"+ip
                if verify_ip(dic):
                    # print('通过')
                    insertdata(dic)
                    print(dic)
        except:
            pass

# =========================================================================
# 66代理
ss_url ='http://www.66ip.cn/mo.php?tqsl=50'
headers1 = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.6',
        'Connection':'keep-alive',
        'Cookie':'__cfduid=dc82e63a299dce97b98b94d949f5a9bb61484641816;'
                 ' CNZZDATA1253901093=1728273565-1484639487-http%253A%252F%252Fwww.baidu.com%252F%7C1484701785; '
                 'Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1484646251,1484646378,1484702884,1484703157; '
                 'Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1484704429',
        'Host':'www.66ip.cn',
        'Referer':'http://www.66ip.cn/pt.html',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
            }
def fetch_ss():
    url = ss_url
    page_content = requests.get(url, headers=headers1)
    # print(page_content)
    str_content = page_content.text
    rule = re.compile(r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d+)')
    result = re.findall(rule,str_content)
    # print(result)
    alldata = []
    for ip in result:
        dic = {}
        dic["http"] = "http://"+ip
        if verify_ip(dic):
            # print('通过')
            print(dic)
            insertdata(dic)
            # alldata.append(dic)

    # print('66代理',alldata)
    # return alldata

# fetch_ss(ss_url)

# 首次验证 ip 是否可用
def verify_ip(dic):
    proxies = dic
    fixed_url = 'http://www.baidu.com/'
    try:
        res = requests.get(fixed_url,proxies=proxies,timeout=2)
        # print(res.text)
        if 'STATUS OK' in res.text:
            return 1
        else:
            return
    except:
        return


######################################################

# 建立或连接数据库
def nsqlite():
    DATABASE = 'ip_list.db'
    created = os.path.exists(DATABASE)
    conn = sqlite3.connect(DATABASE)
    if not created:
        conn.execute('''
            CREATE TABLE IPLIST
            (
                ID INTEGER PRIMARY KEY,
                IP CHAR(30) NOT NULL
            );
            ''')
    # return conn

# 查重
def inspect_ip(ip):
    sql = r'SELECT * FROM IPLIST WHERE IP= "%s";' %(ip)
    query = db.execute(sql)
    result = query.fetchall()
    if len(result) == 0:
        return 1

# 插入
def insertdata(ip):
    DATABASE = 'ip_list.db'
    # created = os.path.exists(DATABASE)
    conn = sqlite3.connect(DATABASE)
    # 查重
    if inspect_ip(ip):
        sql = r'''
                  INSERT INTO IPLIST (ID,IP)
                  VALUES (NULL,"%s")
               '''%(ip)
        conn.execute(sql)
        conn.commit()



# 多线程
funcs = [fetch_xici,fetch_udaili,fetch_ss]
# funcs = [fetch_ss]
def main():
    # 查看是否建立了 ip_list.db,无则新建
    nsqlite()
    # 连接到数据库
    DATABASE = 'ip_list.db'
    # created = os.path.exists(DATABASE)
    conn = sqlite3.connect(DATABASE)
    # 执行多线程
    threads = []
    total_list = []
    for i in range(len(funcs)):
        t = threading.Thread(target=funcs[i])
        threads.append(t)
    for i in range(len(funcs)):
        threads[i].start()
    for i in range(len(funcs)):
        threads[i].join()

    conn.close()



'''
# 为多进程调用准备
def fetch_ip():
    while True:
        main()
        time.sleep(60)
'''


if __name__ == '__main__':
    while True:
        print('crawling...')
        main()
        print('resting...')
        # 休息一分钟
        time.sleep(60)

# 测试
# nsqlite()
# print('打开建立ok')
# DATABASE = 'ip_list.db'
# conn = sqlite3.connect(DATABASE)
# ip = '{"http":"123.123.345.67:8080"}'
# insertdata(conn,ip)
# print('存入ok')