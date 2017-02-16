#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re
import time
import json
import random

'''
1.11：爬取用户信息，组装为 dict,json 处理后存入 txt。
'''

cookies = [
    'SINAGLOBAL=9199334009195.088.1484059697508; login_sid_t=f47cdef129bf89b6ca3d51220ca054ef; YF-Ugrow-G0=169004153682ef91866609488943c77f; YF-V5-G0=5f9bd778c31f9e6f413e97a1d464047a; _s_tentry=www.baidu.com; UOR=ent.qianzhan.com,widget.weibo.com,www.baidu.com; Apache=9379679466808.977.1484616101488; ULV=1484616102485:2:2:2:9379679466808.977.1484616101488:1484059697519; SCF=Aq6jU4HEhhSaE0QfcTQvDmYWBDSI5PfSi8tSbcJ9CbgxoyHMEYzfGUGNLX6Uv8glAAQY_gJXchcYiix1pcBwOYc.; SUB=_2A251eQO5DeRxGeBO7lcX8ifOzjuIHXVWD3JxrDV8PUNbmtBeLVLDkW8dxVjxbAvKU7_4eiqX3sYqaCEM4w..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh8VT9hUEzW9FOqAGr5nzPz5JpX5K2hUgL.Foq7SK-ceo.ESKM2dJLoIXnLxKMLB.-L1--LxKnL122LBo2LxK.L1KnLB--LxKqL1-zLB.eLxKqLBozLBoeLxK.L1K-L1hMLxKML1KqLB.eLxKML1KML1-zt; SUHB=0rr7KFVWdbr8jH; ALF=1516152681; SSOLoginState=1484616681; un=14794601372; wvr=6; wb_g_upvideo_6055629257=1; YF-Page-G0=46f5b98560a83dd9bfdd28c040a3673e',
    'SCF=Aq6jU4HEhhSaE0QfcTQvDmYWBDSI5PfSi8tSbcJ9CbgxIIhVDFDLyicMY12xUr8ga2lP1WRbA2RETFoI2driC3M.; SUB=_2A251eQYjDeRxGeBO7lcX8y7MyDWIHXVWD3DrrDV8PUNbmtBeLUXTkW8xiXT6YMv3MOeu8ZdlGHUDTZ5OlQ..; bai=16.; YF-Ugrow-G0=57484c7c1ded49566c905773d5d00f82; wvr=6; YF-V5-G0=d22a701aae075ca04c11f0ef68835839; wb_g_upvideo_6055630039=1; _s_tentry=-; Apache=4646976744565.257.1484617333656; SINAGLOBAL=4646976744565.257.1484617333656; ULV=1484617333679:1:1:1:4646976744565.257.1484617333656:; UOR=,www.weibo.com,spr_sinamkt_buy_srwj1_weibo_t130; YF-Page-G0=b98b45d9bba85e843a07e69c0880151a',
    'UOR=games.sina.com.cn,games.sina.com.cn,; SINAGLOBAL=220.179.147.23_1481030190.795652; ULV=1481722652012:3:3:1::1481030160454; lxlrttp=1481696010; Apache=183.167.211.89_1484616103.95722; SCF=Aq6jU4HEhhSaE0QfcTQvDmYWBDSI5PfSi8tSbcJ9CbgxHQM-2GdkBjKUD6-1nthHxmJsgEJMcqgHK28ULFIIipw.; ULOGIN_IMG=gz-ef17125b7c8c58bb5af1a128cbd10b5d6f17; SUB=_2A251eQaODeRxGeBO41QT-SvEyzSIHXVWD39GrDV_PUNbm9BeLUn4kW8JFAgC5lQfh548wxPuJhKyJ5pCtA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWd-wGLnVE0Vqpgm_2iG0yi5NHD95Qcehnceo.f1h5RWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNSo5RSoz4SKn715tt; ALF=1516153438; sso_info=v02m6alo5qztKWRk5yljpOQpZCToKWRk5iljoOgpZCjnLaMg6C2jKOktY6DgLiJp5WpmYO0toyDoLaMo6S1joOAuA==',
    'Apache=4646976744565.257.1484617333656; SINAGLOBAL=4646976744565.257.1484617333656; ULV=1484617333679:1:1:1:4646976744565.257.1484617333656:; login_sid_t=7a9b35619cf779daebfd884ed79b659b; UOR=,www.weibo.com,login.sina.com.cn; SCF=Aq6jU4HEhhSaE0QfcTQvDmYWBDSI5PfSi8tSbcJ9CbgxdmsyBLQbqAJIxlsJXAaNGUqwZTOehYO74BTppj7InbA.; SUB=_2A251eQd5DeRxGeBO4lAR9izOzTiIHXVWD3-xrDV8PUNbmtBeLVrXkW8ypg6WBbEJDON62YmF7x1jrfhthQ..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5z976v4-92_s__.7uI5LjO5JpX5K2hUgL.Foq71Kz7SozESoB2dJLoI0qLxK-L12qLBKBLxK.LBKqLBKnLxK.LBKqL1K.LxK-L12BL1K-LxKnLB-qL12BLxKqL1heLBKMt; SUHB=0FQbj9frpk8DGP; ALF=1516153512; SSOLoginState=1484617513; un=15527509152; wvr=6',
    'YF-Ugrow-G0=169004153682ef91866609488943c77f; YF-V5-G0=5f9bd778c31f9e6f413e97a1d464047a; wb_g_upvideo_6055629257=1; YF-Page-G0=46f5b98560a83dd9bfdd28c040a3673e; CNZZDATA1260210782=135847981-1484614831-null%7C1484614831; _s_tentry=-; Apache=4646976744565.257.1484617333656; SINAGLOBAL=4646976744565.257.1484617333656; ULV=1484617333679:1:1:1:4646976744565.257.1484617333656:; login_sid_t=7a9b35619cf779daebfd884ed79b659b; wb_g_upvideo_6086295808=1; wb_g_upvideo_6092062264=1; WBStorage=5d1a8eee17d84880|undefined; UOR=,www.weibo.com,login.sina.com.cn; SCF=Aq6jU4HEhhSaE0QfcTQvDmYWBDSI5PfSi8tSbcJ9CbgxzrIbIZM24-Oxzq-TM3EUYPbwtJL8iITlYufW7J1dqmk.; SUB=_2A251eQlkDeRxGeBO41cY8C7JzT2IHXVWD32srDV8PUNbmtBeLVbwkW8OjVb5eGjIpIUtVJyuuTECDgl79Q..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Whnn2Pd1TjXsUk8gRToSEUi5JpX5K2hUgL.Foq71h-4eh5fSo22dJLoIEXLxKML1-zLB.-LxKMLB.2LBKzLxKqLBoqLBKqLxK.L1-eL1hMLxKqL1h5L1Kzt; SUHB=0XDVGHc-BjkcXY; ALF=1516154036; SSOLoginState=1484618037; un=13913994425; wvr=6; wb_g_upvideo_6085900561=1; WBtopGlobal_register_version=c689c52160d0ea3b',
    'YF-Ugrow-G0=169004153682ef91866609488943c77f; YF-V5-G0=5f9bd778c31f9e6f413e97a1d464047a; wb_g_upvideo_6055629257=1; YF-Page-G0=46f5b98560a83dd9bfdd28c040a3673e; CNZZDATA1260210782=135847981-1484614831-null%7C1484614831; _s_tentry=-; Apache=4646976744565.257.1484617333656; SINAGLOBAL=4646976744565.257.1484617333656; ULV=1484617333679:1:1:1:4646976744565.257.1484617333656:; login_sid_t=7a9b35619cf779daebfd884ed79b659b; wb_g_upvideo_6086295808=1; wb_g_upvideo_6092062264=1; wb_g_upvideo_6085900561=1; WBStorage=5d1a8eee17d84880|undefined; UOR=,www.weibo.com,login.sina.com.cn; SCF=Aq6jU4HEhhSaE0QfcTQvDmYWBDSI5PfSi8tSbcJ9Cbgx4vKpn2N4NEg7yEzcf5UFewAZZ1_yoNaM6ql-q63jeF8.; SUB=_2A251eQnGDeRxGeBO4lAR9irJzj-IHXVWD3wOrDV8PUNbmtBeLW_WkW-Tx2k6yndKzIYRs56VFvN_x8Z8xg..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWDDLpLbAIosNE1KpW1W1yh5JpX5K2hUgL.Foq71Kz7SoBfSKe2dJLoIXnLxK-L1-zL1--LxKML1-qLB--LxK-LBo5L12qLxKqL1h-L1hnLxKMLBK-LBK-LxK-L12BL1KMLxK-L12eL1KMLxKqL1KMLBK.t; SUHB=0V5l6jQMbN1Je7; ALF=1516154134; SSOLoginState=1484618134; un=13178514328; wvr=6; wb_g_upvideo_6092064553=1; WBtopGlobal_register_version=c689c52160d0ea3b',

]


headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
    'Connection':'keep-alive',
    'Cache-Control':'max-age=0',
    # 'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':'SINAGLOBAL=976599875082.1892.1484059342992; login_sid_t=b32fa71263f9c17d903ba452c8278c30; _s_tentry=-; Apache=1290663051427.7961.1484128287798; ULV=1484128287818:3:3:3:1290663051427.7961.1484128287798:1484098108290; UOR=,www.weibo.com,login.sina.com.cn; SCF=AhpUAUcSW-Jr21YdIICYmB2Uqi9-xfS-RhaYkn24qYkBYvzALX4Zqp5wp3CMBoXHDqbxV_luPhkgzpTLcHnK9So.; SUB=_2A251cnAdDeRxGeBO7lcX8ifOzjuIHXVWBubVrDV8PUNbmtAKLVX8kW9SYtdHy-TFXUFSeNIHUU2ZfIAqQg..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh8VT9hUEzW9FOqAGr5nzPz5JpX5K2hUgL.Foq7SK-ceo.ESKM2dJLoIXnLxKMLB.-L1--LxKnL122LBo2LxK.L1KnLB--LxKqL1-zLB.eLxKqLBozLBoeLxK.L1K-L1hMLxKML1KqLB.eLxKML1KML1-zt; SUHB=02Mvxh6sHIFgnM; ALF=1515664333; SSOLoginState=1484128333; un=14794601372; wvr=6',
    'DNT':'1',
    'Upgrade-Insecure-Requests':'1',
    'Host':'weibo.com',
    'User-Agent':'"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",',
    }

# 打开用户 id 文件，传递 id_list
def openfile():
    # 打开文件，读取信息
    with open('repostdata.txt','r')as f:
        content = f.read()
    # json 处理
    data = json.loads(content)
    uid_list = data['repost_data']
    # print(uid_list)
    # print('读取文件成功')
    return uid_list
# 请求网址，返回数据
def req(url):
    print('请求url:%s'%url)
    cook = random.choice(cookies)
    headers['Cookie'] = cook
    # 计数
    cont = 1
    # 请求数据
    while cont < 5:

        try:
            req = requests.get(url,headers=headers)
            content = req.text
            # print('请求成功')
        except:
            return
        cont += 1
        return content

# 匹配信息，组装数据
def fetchdata(info,userid):
    '''
    # re_nickname = re.compile(r'昵称：<\\\/span><span class=\\\"pt_detail\\\">(.*)<\\\/span>')
    # re_area = re.compile(r'所在地：<\\\/span><span class=\\\"pt_detail\\\">(.*)<\\\/span>')
    # # re_sexual_orentation = re.compile(r'性取向：<\\\/span><span class=\\\"pt_detail\\\">(.*)<\\\/span>')
    # re_status = re.compile(r'感情状况：<\\\/span><span class=\\\"pt_detail\\\">(.*)<\\\/span>')
    # re_birthday = re.compile(r'生日：<\\\/span><span class=\\\"pt_detail\\\">(.*)<\\\/span>')
    # re_bloodtype = re.compile(r'血型：<\\\/span><span class=\\\"pt_detail\\\">(.*)<\\\/span>')
    # re_blogad = re.compile(r'博客地址：<\\\/span><span class=\\\"pt_detail\\\">(.*)<\\\/span>')
    # re_domin = re.compile(r'个性域名：<\\\/span>.*<span class=\\\"pt_detail\\\">(.*)<\\\/span>')
    # re_brief = re.compile(r'简介：<\\\/span><span class=\\\"pt_detail\\\">(.*)<\\\/span>')
    # re_registertime = re.compile(r'注册时间：<\\\/span>.*<span class=\\\"pt_detail\\\">.*(\d+\-\d+\-\d+).*<\\\/span>')
    '''
    # print('开始清洗 %r 用户的数据')
    # 将响应数据做第一次处理
    soup = BeautifulSoup(info, 'lxml')
    # 获取所有 script
    scripts = soup.find_all('script')
    new_s = ''
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
    # 将分离的字符串拿到 bs 再处理一次
    soup2 = BeautifulSoup(new_s, 'lxml')
    # 拿到所有的 li 标签
    tag_li = soup2.find_all('li', attrs={'class': True})
    user_info = {}
    for lis in tag_li:
        # print(lis.prettify())
        # 拿到 li.span
        tag_span1 = lis.find('span')
        try:
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
    # print(data)
    return data

# 保存数据
def savedata(data,count):
    # print(data)
    # data.decode()
    data = json.dumps(data,ensure_ascii=False)
    print(data)
    try:
        with open('info_%r.txt'%count,'a+',errors='ignore',encoding='utf-8') as f:
            f.write(data)
            f.write('\n')
            # print('数据保存成功')
    except:
        with open('info_%r.txt'%count,'w',errors='ignore',encoding='utf-8') as f:
            f.write(data)
            f.write('\n')
            # print('数据保存成功')


#  引擎及分配中心
def main():
    pre_url = 'http://weibo.com/p/100505%s/info'
    userid_list = openfile()
    '''
    每一百次写入，则重新建立 txt 文件
    '''
    # 100 次计数
    count = 0
    # txt 标记
    s = 8
    # 倒计时计数
    c = 1
    for id in userid_list:
        print('开始第 %d 次抓取，目标 id 为%r'%(c,id))
        c += 1
        # 组装请求 url
        url = pre_url%id
        # 请求
        content = req(url)
        # 传入响应后的内容和用户id，清洗数据后得到字典格式的数据
        if not content:
            print('第 %d 次抓取时失败'%c)
            break
        data = fetchdata(content,id)
        # 计数加 1
        count += 1
        # 保存数据到文件
        savedata(data, s)
        if count == 100:
            s += 1
            count = 0
        time.sleep(2)
        # 测试用
        # if c == 5:
        #     break

if __name__ == '__main__':
    main()