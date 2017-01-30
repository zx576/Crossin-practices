#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re
import time
import json
import random
import sqlite3

'''
step3:
爬取用户信息，组装为 dict,json 处理后存入 txt。
'''

# headers,注意不包括Cookie
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
def req(url,cookie):
    # 代理服务器，使用阿布云代理
    # 方案二：自建ip池
    proxyHost = "proxy.abuyun.com"
    proxyPort = "9010"

    # 代理隧道验证信息
    proxyUser = "HT44XXXXXX7O8D0D"
    proxyPass = "5E72XXXXXXD79F23"

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": proxyHost,
        "port": proxyPort,
        "user": proxyUser,
        "pass": proxyPass,
    }

    proxies = {
        "http": proxyMeta,
        "https": proxyMeta,
    }


    print('请求url:%s'%url)
    # 多设置几个登录 cookie
    headers['Cookie'] = cookie
    # 异常处理
    try:
        # print(url, headers)
        req = requests.get(url,headers=headers,timeout=5,proxies=proxies)
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
'''
# 自建 ip 池部分，连接已有 ip 池，逐一使用 ip ，如果过期，则删除
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
        'User-Agent': '"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US)
        AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",',
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

'''
# 控制请求模块
def request_main(url,cookie,id):
    content = req(url,cookie)
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
# 登录 cookie ，淘宝可买
cookies = [
# 'wb_pub
    # 'wb_publish_fist100_2426968121=1; wb_publish_fist100_6055629257=1; wb_g_upvideo_6055630039=1; wb_publish_fist100_6055630039=1; wb_g_upvideo_6055501997=1; wb_g_upvideo_6055629257=1; wb_g_upvideo_6057391443=1; wb_g_upvideo_2426968121=1; wb_g_upvideo_6086295808=1; wb_g_upvideo_6092062264=1; wb_g_upvideo_6085900561=1; wb_g_upvideo_6092064553=1; wb_publish_fist100_6092064553=1; CNZZDATA1260210782=928241306-1483959022-null%7C1484664262; SINAGLOBAL=6025747651929.787.1484669044262; _s_tentry=login.sina.com.cn; Apache=9823866260763.922.1484708650841; ULV=1484708651818:2:2:2:9823866260763.922.1484708650841:1484669044303; TC-Ugrow-G0=e66b2e50a7e7f417f6cc12eec600f517; TC-V5-G0=40eeee30be4a1418bde327baf365fcc0; WBtopGlobal_register_version=c689c52160d0ea3b; TC-Page-G0=e2379342ceb6c9c8726a496a5565689e; login_sid_t=6d63355f0fbcd34ab470594a6d1c30b9; UOR=,weibo.com,login.sina.com.cn; WBStorage=ffbf906cea1ff551|undefined; SCF=AhpUAUcSW-Jr21YdIICYmB2Uqi9-xfS-RhaYkn24qYkBz2Nqdq3PBaNTdc8erC9GZG3urH1We9cxYp7fLFrZXRg.; SUB=_2A251e1PGDeRxGeBO7lcX8ifOzjuIHXVW8cIOrDV8PUNbmtAKLXfWkW-PLtMJwn_zpjl2c_ghkyvtewyzbA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh8VT9hUEzW9FOqAGr5nzPz5JpX5K2hUgL.Foq7SK-ceo.ESKM2dJLoIXnLxKMLB.-L1--LxKnL122LBo2LxK.L1KnLB--LxKqL1-zLB.eLxKqLBozLBoeLxK.L1K-L1hMLxKML1KqLB.eLxKML1KML1-zt; SUHB=010GF68q7Yhk87; ALF=1516263190; SSOLoginState=1484727191; un=14794601372; wvr=6',
    # 'SINAGLOBAL=4644124115143.593.1484552712462; ULV=1484724064418:2:2:2:3269292300363.5156.1484724064341:1484552712482; TC-Ugrow-G0=e66b2e50a7e7f417f6cc12eec600f517; login_sid_t=89e812c285244102035068762d2aefd9; TC-V5-G0=2bdac3b437dd23e235b79a3d6922ea06; _s_tentry=-; Apache=3269292300363.5156.1484724064341; SUB=_2A251e2e9DeRxGeBO41QT-SvEyzSIHXVW8d51rDV8PUNbmtAKLXbZkW9ph3Xls0yjbpZjikbKw-A9uHMisA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWd-wGLnVE0Vqpgm_2iG0yi5JpX5K2hUgL.Foq71hqE1K-Rehn2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMcehnceo.f1h5R; SCF=ApP9AKeHLvGhZd8WZPKm3BYhvhG_bSQdSXvbMHiUmN7Uc4qx7ZPs3s2Xf1T4X_llVoauz3K8tMBgUaDgioPB-Fk.; SUHB=06ZFj_nq8VpYU5; ALF=1516260204; SSOLoginState=1484724154; un=17740675026; wvr=6; wb_g_upvideo_6086295808=1; TC-Page-G0=1e758cd0025b6b0d876f76c087f85f2c; WBtopGlobal_register_version=c689c52160d0ea3b',
    # 'YF-Ugrow-G0=ad06784f6deda07eea88e095402e4243; login_sid_t=e0c57e4cb8d7c1c55f3bfb61e020e4c8; YF-V5-G0=572595c78566a84019ac3c65c1e95574; WBStorage=ffbf906cea1ff551|undefined; _s_tentry=-; Apache=8980172505915.266.1484741767740; SINAGLOBAL=8980172505915.266.1484741767740; ULV=1484741767747:1:1:1:8980172505915.266.1484741767740:; SCF=AjpUP0C8sXzdTUgCXAL6A3JsoutiRhU8FB6HBmqwQEc9yhD5MIDZhuABlDLXT3HG5ZYbObCs1E7hHHS6h2xeG3U.; SUB=_2A251eyzuDeRxGeBO4lAQ8ifKyjmIHXVW8RkmrDV8PUNbmtBeLRf8kW9I_4OCJS3lKAlWcKKS1PDz9vnuBQ..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF0yjaKzpd5QV.-_8psP1fw5JpX5K2hUgL.Foq71Kzpeo.ceK-2dJLoI0qLxKML1heLB-BLxKML1h.LBKMLxK-LB--LBoBLxK-L12-L1hzLxKML1h.LBKMLxKML1-qLB-Bt; SUHB=0idrrgaJR2QaX_; ALF=1516277818; SSOLoginState=1484741822; un=13255650757; wvr=6; wb_g_upvideo_6092129615=1; YF-Page-G0=f27a36a453e657c2f4af998bd4de9419',
    # 'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFyE8_Vj0fmzzPJBWRnDjrD5JpX5K2hUgL.Foq71h-4e0eRSKn2dJLoI0qLxKnL1h5LBoeLxKBLB.qL122LxKMLB.-L12-LxKqL1h5L1-BLxKqL1h-L1K-LxKML1K-L12qt; WBStorage=ffbf906cea1ff551|undefined; SINAGLOBAL=641159491808.484.1484741899707; ULV=1484741899817:1:1:1:641159491808.484.1484741899707:; SCF=AgLkSv6ITWQWx1x2W8AZzDwisfoD9b9IbTga1Du2kV997f8QthE4b8WWmUKjy2xRLtxmbUaWMvU-nRqqJblu2J0.; SUHB=0wnFQgUeo2zePF; ALF=1516277969; un=15552725946; wvr=6; wb_g_upvideo_6085933858=1; YF-Ugrow-G0=57484c7c1ded49566c905773d5d00f82; login_sid_t=bbd26f6104bae23f3300078f8f1f3c85; YF-V5-G0=b1e3c8e8ad37eca95b65a6759b3fc219; _s_tentry=-; Apache=641159491808.484.1484741899707; SUB=_2A251ey0EDeRxGeBO41cY8y3EzjSIHXVW8RnMrDV8PUNbmtBeLW79kW8kSfLxHuTlb1LirRYT7Y1oa02KRw..; SSOLoginState=1484741973',
    # 'SINAGLOBAL=6025747651929.787.1484669044262; wvr=6; login_sid_t=056baab4bb5031c0581146fb79ac1877; _s_tentry=www.baidu.com; UOR=,weibo.com,www.baidu.com; Apache=1223015029383.9514.1484786198671; ULV=1484786199022:4:4:4:1223015029383.9514.1484786198671:1484741334703; SCF=AhpUAUcSW-Jr21YdIICYmB2Uqi9-xfS-RhaYkn24qYkBDtabL19wJeXRNXkMX86E68I2EJH6IgAKpkYlZzKnDcc.; SUB=_2A251hHpiDeRxGeBO4lAQ8y7MwzqIHXVW8OyqrDV8PUNbmtBeLWOjkW8DD_gd00MCOZS1yg0uyQ-ifUXVpQ..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Whs3ZAz0qw-5rSow1AVG5Oc5JpX5K2hUgL.Foq71Kzpe0571hq2dJLoIXnLxK-L1h-L1hqLxKnL1h2L1hzLxK.L1KBLB-qLxKML12-LB-qLxKnL1h2L1hzLxKnLBoBL1-BLxKqL1-eL1h.LxKnL1h2L1hzt; SUHB=0M2FZY3n2ChlgF; ALF=1516322221; SSOLoginState=1484786226; un=13256318112',
    # 'SCF=AgLkSv6ITWQWx1x2W8AZzDwisfoD9b9IbTga1Du2kV993-skMVU8Hy3ndhnpWlEBbst3U7kObER0RzPULWmHj_0.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5-RceGV6fsTpGOcjTTfQLy5JpX5K2hUgL.Foq71Kzpe0M7SK52dJLoIXnLxK.LB-2L1K2LxKqL1h-L12-LxKMLB.2LBKqLxKML1KqLB.-LxKqL1h-L12-LxKqL1h.LB-qLxKMLB.zL1-BLxKqL1h-L12-t; WBStorage=ffbf906cea1ff551|undefined; UOR=,weibo.com,spr_sinamkt_buy_srwj1_weibo_t130; SINAGLOBAL=1260567973171.5634.1484786303477; ULV=1484786303662:1:1:1:1260567973171.5634.1484786303477:; SUHB=0mxU4LAlOY1yb4; ALF=1516322329; un=17189229223; wvr=6; wb_g_upvideo_6092137050=1; bai=16.; login_sid_t=a6a679f18c460d01d1fbcdddb525243e; YF-Ugrow-G0=56862bac2f6bf97368b95873bc687eef; YF-V5-G0=e2def7ce19d3add53399b18462da454a; _s_tentry=-; Apache=1260567973171.5634.1484786303477; SUB=_2A251hHrKDeRxGeBO4lAQ8ynMzjyIHXVW8OsCrDV8PUNbmtBeLVOnkW9eSBACwA-GNmvgJcRfRxbhFUCMjg..; SSOLoginState=1484786330; YF-Page-G0=59104684d5296c124160a1b451efa4ac; WBtopGlobal_register_version=c689c52160d0ea3b',
    'SCF=AgLkSv6ITWQWx1x2W8AZzDwisfoD9b9IbTga1Du2kV998mHgFZSvss3mQK26oXSxmhD4qupcozpOkPTEexryzz8.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5.4ZBgWEVnw4GVKfReE9EF5JpX5K2hUgL.Foq71hq0SoeXe0n2dJLoI0YLxK-L122LBKeLxK.LB.zL1K2LxKqL1-2L1KMLxKnL12zL12BLxKML1K.LB.BLxKqL1h5L1-BLxK-L1hMLBK2t; UOR=,weibo.com,www.baidu.com; SINAGLOBAL=1260567973171.5634.1484786303477; ULV=1484822832499:2:2:2:4048948315346.705.1484822832043:1484786303662; SUHB=0u5h656XPc97IV; ALF=1516358865; un=13798857937; wvr=6; wb_g_upvideo_6092137050=1; WBStorage=ffbf906cea1ff551|undefined; wb_g_upvideo_6086363438=1; TC-Ugrow-G0=02e35d9240e6933947925d24232af628; login_sid_t=77da23af49c80eedf774e407b2d652a6; TC-V5-G0=666db167df2946fecd1ccee47498a93b; _s_tentry=-; Apache=4048948315346.705.1484822832043; SUB=_2A251hOkDDeRxGeBO41QS9i3IyDSIHXVW8F3LrDV8PUNbmtAKLWnNkW8CPSXZ44pjEgy0d6AZkUcSQaFyMQ..; SSOLoginState=1484822867; TC-Page-G0=2b304d86df6cbca200a4b69b18c732c4; WBtopGlobal_register_version=c689c52160d0ea3b',
    'TC-Ugrow-G0=02e35d9240e6933947925d24232af628; login_sid_t=43e4e94ecfbb05aa9690b11c1fe0ca11; TC-V5-G0=b8dff68fa0e04b3c8f0ba710d783479a; _s_tentry=-; WBStorage=ffbf906cea1ff551|undefined; Apache=7518958386294.261.1484822708161; SINAGLOBAL=7518958386294.261.1484822708161; ULV=1484822708173:1:1:1:7518958386294.261.1484822708161:; SCF=AphQz8myQ2vFCByO8xFZCBT8vTeW_Zdlx1PYbL7r27hzk5IHo7tZFUa-9RtOMqiiqDV6Rxd5K3uSAzQRV4QNMdk.; SUB=_2A251hOioDeRxGeBO4lAQ-SnMzDiIHXVW8F1grDV8PUNbmtAKLUGkkW8-MvNylqR1b6_AnqLuhSgEESM19A..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWKvvqMZe.b8-3EUSPUiyi45JpX5K2hUgL.Foq71Kzp1KM7S0B2dJLoI0YLxK-LB.-LBK2LxKnLBoBLB-2LxKqL1h2L12zLxK-LBKnL1hMLxKMLB.-L12-LxKqL1h5L1-BLxK.L1-qLBo-t; SUHB=0y0ZTfq_c74Q0a; ALF=1516358776; SSOLoginState=1484822776; un=15296074032; wvr=6; wb_g_upvideo_6092197074=1; TC-Page-G0=4e714161a27175839f5a8e7411c8b98c; WBtopGlobal_register_version=c689c52160d0ea3b',
    ]

#  引擎及分配中心
def main():
    # 初始 url
    pre_url = 'http://weibo.com/p/100505%s/info'
    # 获取所有用户 id
    userid_list = openfile()
    # 文件计数
    filecount = 44
    # 文件存入次数计数
    savecount = 1
    # 请求计数
    req_count = 1
    for id in userid_list:
        print('开始第 %d 次抓取，目标 id 为%r' % (req_count, id))
        req_count += 1
        url = pre_url % id
        # ip = ip_main()
        # print(ip)
        # print(type(ip))
        cookie = random.choice(cookies)
        data = request_main(url,cookie,id)
        if not data:
            savebad(id)
            print('请求 %s 失败'%id,'已经保存')
            continue
        save_main(data, filecount)
        savecount += 1

        if savecount == 1000:
            filecount += 1
            savecount = 0
        time.sleep(0.5)
        # break

if __name__ == '__main__':
    main()