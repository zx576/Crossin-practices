#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re
import time
import json
import random
import sqlite3

'''
爬取用户信息，组装为 dict,json 处理后存入 txt。
'''


headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
    'Connection':'keep-alive',
    'Cache-Control':'max-age=0',
    'Upgrade-Insecure-Requests':'1',
    'Host':'weibo.com',
    'User-Agent':'"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",',
    }

# 打开用户 id 文件，传递 id_list
def openfile():
    # 打开文件，读取信息
    with open('total_data_new.txt','r')as f:
        content = f.read()
    # json 处理
    content = re.sub('\'', '\"', content)
    data = json.loads(content)
    uid_list = data['alldata']
    # print(uid_list)
    # print('读取文件成功')
    return uid_list
# 请求网址，返回数据
def req(url,ip,cookie):
    print('请求url:%s'%url)
    headers['Cookie'] = cookie
    try:
        # print(url, headers)
        req = requests.get(url,headers=headers,timeout=5,proxies=ip)
        print(req)
        content = req.text
        # print(content)
    except:
        return
    # print(content)
    return content
# 匹配信息，组装数据
def fetchdata(info,userid):
    # print('开始清洗 %r 用户的数据')
    # 将响应数据做第一次处理
    soup = BeautifulSoup(info, 'lxml')
    # 获取所有 script
    scripts = soup.find_all('script')
    new_s = ''
    if len(scripts) == 0:
        return
    # 遍历 script
    for i in scripts:
        # print(i.string)
        # print(type(i.string))
        # 分离出有效信息
        if '基本信息' in i.string:
            # 将有效信息转为字符串处理
            s = str(i.string)
            # 去除 '\t' '\r' '\n', 并得到新的字符串
            new_s = s.replace('\\t', '').replace('\\r', '').replace('\\n', '')

    # 继续对字符串做处理
    new_s = new_s.replace('\\', '')
    if new_s == '':
        return
    # 将分离的字符串拿到 bs 再处理一次
    soup2 = BeautifulSoup(new_s, 'lxml')
    # 拿到所有的 li 标签
    tag_li = soup2.find_all('li', attrs={'class': True})
    user_info = {}
    for lis in tag_li:
        # print(lis.prettify())
        # 拿到 li.span
        try:
            tag_span1 = lis.find('span')
            # 拿到信息属性
            att = tag_span1.get_text()
            # print(att)
            # 拿到值
            tag_span2 = tag_span1.next_sibling
            val = tag_span2.get_text()
            # print(val)
            user_info[att] = val
        except:
            user_info['nodata'] = 'nodata'
    # 组装最后的格式
    data = {}
    data[userid] = user_info
    # print('清洗成功')
    print(data)
    return data

# 保存数据
def savedata(data,file):
    # print(data)
    # data.decode()
    data = json.dumps(data,ensure_ascii=False)
    # print(data)
    with open(file,'a+',errors='ignore',encoding='utf-8') as f:
        f.write(data)
        f.write('\n')
            # print('数据保存成功')

# 连接 ip 数据库
def opensql():
    DATABASE = 'ip_list.db'
    # created = os.path.exists(DATABASE)
    conn = sqlite3.connect(DATABASE)
    sql = r'SELECT * FROM IPLIST'
    query = conn.execute(sql)
    alldata = query.fetchall()
    # ip_list = []
    # for i in alldata:
        # str_ip = i[1]
        # str_ip = re.sub('\'', '\"', str_ip)
        # dict_ip = json.loads(str_ip)
        # ip_list.append(dict_ip)
    conn.close()
    return alldata


# 验证 ip
def handleip(ip):
    # ip_list = opensql()
    headers1 = {
        'User-Agent': '"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",',
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
def delectip(ip):

    DATABASE = 'ip_list.db'
    # created = os.path.exists(DATABASE)
    conn = sqlite3.connect(DATABASE)
    # ip = str(ip)
    sql = r'DELETE FROM IPLIST WHERE ID = %d;' % ip[0]
    query = conn.execute(sql)
    conn.commit()
    conn.close()

# 控制 ip 模块
def ip_main():
    # 获取 ip_list
    ip_list = opensql()
    print(ip_list)
    for ip in ip_list:
        # u_ip = json.loads(ip)
        u_ip = ip[1]
        # print(u_ip)
        str_ip = re.sub('\'', '\"', u_ip)
        dict_ip = json.loads(str_ip)
        # print(dict_ip)
        # print(type(dict_ip))
        # ip_list.append(dict_ip)
        print('测试 %r'%dict_ip)
        if handleip(dict_ip):
            return dict_ip
        else:
            delectip(ip)
            print('删除 %r'%ip[1])
            # continue
        # break


# 控制请求模块
def request_main(url,ip,cookie,id):
    content = req(url,ip,cookie)
    if content:
        data = fetchdata(content, id)
        return data

# 文件保存模块
def save_main(data,count):
    file = 'info_%r.txt' % count
    savedata(data,file)


# 保存未能请求的id
def savebad(id):
    with open('bad_id.txt','a+')as f:
        f.write(id)
        f.write('\n')

cookies = [
    'wb_publish_fist100_2426968121=1; wb_publish_fist100_6055629257=1; wb_g_upvideo_6055630039=1; wb_publish_fist100_6055630039=1; wb_g_upvideo_6055501997=1; wb_g_upvideo_6055629257=1; wb_g_upvideo_6057391443=1; wb_g_upvideo_2426968121=1; wb_g_upvideo_6086295808=1; wb_g_upvideo_6092062264=1; wb_g_upvideo_6085900561=1; wb_g_upvideo_6092064553=1; wb_publish_fist100_6092064553=1; CNZZDATA1260210782=928241306-1483959022-null%7C1484664262; SINAGLOBAL=6025747651929.787.1484669044262; _s_tentry=login.sina.com.cn; Apache=9823866260763.922.1484708650841; ULV=1484708651818:2:2:2:9823866260763.922.1484708650841:1484669044303; TC-Ugrow-G0=e66b2e50a7e7f417f6cc12eec600f517; TC-V5-G0=40eeee30be4a1418bde327baf365fcc0; WBtopGlobal_register_version=c689c52160d0ea3b; TC-Page-G0=e2379342ceb6c9c8726a496a5565689e; login_sid_t=6d63355f0fbcd34ab470594a6d1c30b9; UOR=,weibo.com,login.sina.com.cn; WBStorage=ffbf906cea1ff551|undefined; SCF=AhpUAUcSW-Jr21YdIICYmB2Uqi9-xfS-RhaYkn24qYkBz2Nqdq3PBaNTdc8erC9GZG3urH1We9cxYp7fLFrZXRg.; SUB=_2A251e1PGDeRxGeBO7lcX8ifOzjuIHXVW8cIOrDV8PUNbmtAKLXfWkW-PLtMJwn_zpjl2c_ghkyvtewyzbA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh8VT9hUEzW9FOqAGr5nzPz5JpX5K2hUgL.Foq7SK-ceo.ESKM2dJLoIXnLxKMLB.-L1--LxKnL122LBo2LxK.L1KnLB--LxKqL1-zLB.eLxKqLBozLBoeLxK.L1K-L1hMLxKML1KqLB.eLxKML1KML1-zt; SUHB=010GF68q7Yhk87; ALF=1516263190; SSOLoginState=1484727191; un=14794601372; wvr=6',
    # 'SINAGLOBAL=4644124115143.593.1484552712462; ULV=1484724064418:2:2:2:3269292300363.5156.1484724064341:1484552712482; TC-Ugrow-G0=e66b2e50a7e7f417f6cc12eec600f517; login_sid_t=89e812c285244102035068762d2aefd9; TC-V5-G0=2bdac3b437dd23e235b79a3d6922ea06; _s_tentry=-; Apache=3269292300363.5156.1484724064341; SUB=_2A251e2e9DeRxGeBO41QT-SvEyzSIHXVW8d51rDV8PUNbmtAKLXbZkW9ph3Xls0yjbpZjikbKw-A9uHMisA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWd-wGLnVE0Vqpgm_2iG0yi5JpX5K2hUgL.Foq71hqE1K-Rehn2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMcehnceo.f1h5R; SCF=ApP9AKeHLvGhZd8WZPKm3BYhvhG_bSQdSXvbMHiUmN7Uc4qx7ZPs3s2Xf1T4X_llVoauz3K8tMBgUaDgioPB-Fk.; SUHB=06ZFj_nq8VpYU5; ALF=1516260204; SSOLoginState=1484724154; un=17740675026; wvr=6; wb_g_upvideo_6086295808=1; TC-Page-G0=1e758cd0025b6b0d876f76c087f85f2c; WBtopGlobal_register_version=c689c52160d0ea3b'
    ]

#  引擎及分配中心
def main():
    # 初始 url
    pre_url = 'http://weibo.com/p/100505%s/info'
    # 获取所有用户 id
    userid_list = openfile()
    # 文件计数
    filecount = 17
    # 文件存入次数计数
    savecount = 300
    # 请求计数
    req_count = 1
    for id in userid_list[14995:40000]:
        print('开始第 %d 次抓取，目标 id 为%r' % (req_count, id))
        req_count += 1
        url = pre_url % id
        ip = ip_main()
        print(ip)
        print(type(ip))
        cookie = random.choice(cookies)
        data = request_main(url,ip,cookie,id)
        if not data:
            savebad(id)
            print('请求 %s 失败'%id,'已经保存')
            continue
        save_main(data, filecount)
        savecount += 1

        if savecount == 1000:
            filecount += 1
            savecount = 0
        time.sleep(1)
        # break

# def main():
#     pre_url = 'http://weibo.com/p/100505%s/info'
#     userid_list = openfile()
#     '''
#     每1000次写入，则重新建立 txt 文件
#     '''
#     # 100 次计数
#     count = 0
#     # 获取 ip
#     # ip_list = opensql()
#
#     # txt 标记
#     s = 17
#     # 请求计数
#     c = 1
#     # 错误列表
#     error_list = []
#     for id in userid_list[14484:40000]:
#         print('开始第 %d 次抓取，目标 id 为%r'%(c,id))
#         c += 1
#         # 组装请求 url
#         url = pre_url%id
#         # 请求
#         content = req(url)
        # 传入响应后的内容和用户id，清洗数据后得到字典格式的数据
        # if not content:
        #     print('第 %d 次抓取时失败'%c)
        #     error_list.append(id)
        #     continue
#         data = fetchdata(content,id)
#         # 计数加 1
#         count += 1
#         # 保存数据到文件
#         savedata(data, s)
#         if count == 1000:
#             s += 1
#             count = 0
#         time.sleep(2)
#         # 测试用
#         # if c == 5:
#         #     break
#     with open('errorid.txt','w')as f:
#         f.write(str(error_list))

if __name__ == '__main__':
    main()