import jieba
import jieba.analyse
import re
import json
import requests
# seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
# print(seg_list)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式

# with open('info_1.txt','r',errors='ignore',encoding='utf-8')as f:
#     data = f.read()
# res = jieba.analyse.extract_tags(data, topK=20, withWeight=False, allowPOS=())
# for i in res:
#     r = jieba.get_FREQ(i)
#     print(r)
# print(res)
#
# f = jieba.analyse.
# s = "10月1日"
# rule = re.compile(r'(\d+)月(\d+)')
# rule2 = re.compile(r'(\d{4})年(\d+)月(\d+)')
# res = re.findall(rule2,s)
# print(res)
# res = [i for i in res]
# if len(res[2]) == 1:
#     res[2] = '0'+res[2]
# new = ''.join(res[1:])
# print(new)
# 统计生日 并得到星座
# cons_dict = {
#     '白羊座':{'male':0,'female':0},
#     '金牛座':{'male':0,'female':0},
#     '双子座':{'male':0,'female':0},
#     '巨蟹座':{'male':0,'female':0},
#     '狮子座':{'male':0,'female':0},
#     '处女座':{'male':0,'female':0},
#     '天枰座':{'male':0,'female':0},
#     '天蝎座':{'male':0,'female':0},
#     '射手座':{'male':0,'female':0},
#     '水瓶座':{'male':0,'female':0},
#     '双鱼座':{'male':0,'female':0},
#     '摩羯座':{'male':0,'female':0},
# }
# year = {
#     '60sm':{'male':0,'female':0},
#     '60s':{'male':0,'female':0},
#     '70s':{'male':0,'female':0},
#     '80s':{'male':0,'female':0},
#     '90s':{'male':0,'female':0},
#     '00s':{'male':0,'female':0},
# }
# def birthday(val,sex):
#     # 统计 星座
#     rule = re.compile(r'(\d+)月(\d+)')
#     # 统计 年
#     # rule2 = re.compile(r'(\d{4})年.*')
#     rule2 = re.compile(r'(\d{4})年')
#     # 获取星座
#     if '日' in val:
#         res = ''
#         try:
#             res = re.findall(rule,val)[0]
#         except:
#             pass
#         else:
#             res = [i for i in res]
#             if len(res[1]) == 1:
#                 res[1] = '0'+ res[1]
#             birth = ''.join(res)
#             birth2int = int(birth)
#             if 319 <= birth2int <= 419:
#                 constellation = '白羊座'
#             elif 420 <= birth2int <= 520:
#                 constellation = '金牛座'
#             elif 521 <= birth2int <= 621:
#                 constellation = '双子座'
#             elif 622 <= birth2int <= 722:
#                 constellation = '巨蟹座'
#             elif 723 <= birth2int <= 822:
#                 constellation = '狮子座'
#             elif 823 <= birth2int <= 922:
#                 constellation = '处女座'
#             elif 923 <= birth2int <= 1023:
#                 constellation = '天枰座'
#             elif 1024 <= birth2int <= 1122:
#                 constellation = '天蝎座'
#             elif 1123 <= birth2int <= 1221:
#                 constellation = '射手座'
#             # elif  birth2int >= 1222 and birth2int <= 119:
#             #     constellation = '摩羯座'
#             elif 120 <= birth2int <= 218:
#                 constellation = '水瓶座'
#             elif 219 <= birth2int <= 320:
#                 constellation = '双鱼座'
#             else:
#                 constellation = '摩羯座'
#             # 判断男女
#             if sex == '男':
#                 cons_dict[constellation]['male'] += 1
#             elif sex == '女':
#                 cons_dict[constellation]['female'] += 1
#             else:
#                 pass
#         # 添加 年
#         try:
#             year_str = re.findall(rule2,val)[0]
#         except:
#             pass
#         else:
#             year2int = int(year_str)
#             if 1960 <= year2int <= 1969:
#                 year_key = '60s'
#             elif 1970 <= year2int <= 1979:
#                 year_key = '70s'
#             elif 1980 <= year2int <= 1989:
#                 year_key = '80s'
#             elif 1990 <= year2int <= 1999:
#                 year_key = '90s'
#             elif 2000 <= year2int :
#                 year_key = '00s'
#             else:
#                 year_key = '60sm'
#             if sex == '男':
#                 year[year_key]['male'] += 1
#             elif sex == '女':
#                 year[year_key]['female'] += 1
#             else:
#                 pass
#     else:
#         if sex == '男':
#             cons_dict[val]['male'] += 1
#         elif sex == '女':
#             cons_dict[val]['female'] += 1
#         else:
#             pass
# val = "双子座"
# sex = 'none'
# birthday(val,sex)
# print(year)
# print(cons_dict)
# y = '2009-11-18'
# rule = re.compile(r'(\d{4})')
# s = re.findall(rule,y)[0]
# print(type(s))
# register_dict = {
#     '2009':0,
#     '2010':0,
#     '2011':0,
#     '2012':0,
#     '2013':0,
#     '2014':0,
#     '2015':0,
#     '2016':0,
#     '2017':0,
# }
# def register_time(val):
#     rule = re.compile(r'(\d{4})')
#     register_year = ''
#     try:
#         register_year = re.findall(rule,val)[0]
#     except:
#         pass
#     else:
#         register_dict[register_year] += 1
#
#
# register_time('2010-1-3')
# print(register_dict)
# def distribute_data(data):
#     '''
#     data:{"1661845933": {"初中：": "广州十六中 (1994年)   初中四班",
#     "标签：": "CICFEXPO編輯原创漫画bilibili二次元移动互联网漫友漫画SHOW动漫",
#      "注册时间：": "2009-11-18", "大学：": "华南师范大学 (2000年)   旅游管理系",
#       "个性域名：": "http://weibo.com/gscwl",
#        "公司：": "bilibili（哔哩哔哩）  (2016 - )    地区：上海 ，       浦东新区 职位：内容合作部",
#        "昵称：": "大魔王小狐君",
#        "简介：": "中国动漫一小狐/资深二次元宅男/前《漫友》《漫画秀》主编&CICFEXPO创办人",
#        "博客：": "http://blog.sina.com.cn/gscwl",
#        "性别：": "男",
#        "生日：": "1981年10月22日",
#        "所在地：": "广东 广州",
#        "高中：": "广州市第十六中学 (1997年)   高中二班"}}
#     :return:
#     '''
#     # 取到 id 号
#     uid = data[2:12]
#     # print(uid)
#     # json 处理文档
#     unpack_data = json.loads(data)
#     # print(unpack_data)
#     # 得到所有有效数据
#     info_dict = unpack_data[uid]
#     # print(info_dict)
#     for key in info_dict:
#         # print(key)
#         val = info_dict[key]
#         # 分发地区数据
#         # if key == '所在地：':
#             # val = info_dict[key]
#             # 分发到处理 ‘所在地’ 的函数
#         #     location(val)
#         # elif key == '性别：':
#         #     # val = info_dict[key]
#         #     sex(val)
#         # elif key == '标签：':
#         #     # val = info_dict[key]
#         #     tags(val)
#         if key == '生日：':
#             # 尝试拿到性别
#             try:
#                 se = info_dict['性别：']
#             except:
#                 se = 'none'
#             # 把生日和性别发给 birthday 函数
#             print(val,se)
#         # elif key == '注册时间：':
#         #     register_time(val)
#
# data = '{"2483412334": {"昵称：": "chopin永远是个小南部", "高中：": "无锡六中 (2009年)", "简介：": "🇩🇪德吹一枚🇩🇪拜仁死忠🇩🇪萌🌟入坑炉石ing", "标签：": "处女座学生党NBA拜仁死神家庭教师动漫宅90后", "注册时间：": "2011-10-21", "性取向：": "异性恋", "感情状况：": "暗恋中", "生日：": "处女座", "所在地：": "江苏 无锡", "个性域名：": "http://weibo.com/Chopin9394", "性别：": "男"}}'
# distribute_data(data)
#
# a = set()
# b = set()
# a.add('abs')
# b.update(a)
# print(a,b)
headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        # 'Content-Type':'application/x-www-form-urlencoded',
        'Cookie': 'SINAGLOBAL=976599875082.1892.1484059342992; wvr=6; login_sid_t=16e46bbc135d08a302fedeae1f091120; _s_tentry=-; UOR=,www.weibo.com,www.baidu.com; Apache=4236363804304.171.1484529465788; ULV=1484529465794:7:7:2:4236363804304.171.1484529465788:1484470021353; SCF=AhpUAUcSW-Jr21YdIICYmB2Uqi9-xfS-RhaYkn24qYkBCuEySENedq0nZ9q-8fikGeEmAutvTFDVh3mqmojOSqk.; SUB=_2A251eG9vDeRxGeBO7lcX8ifOzjuIHXVWDMenrDV8PUNbmtAKLRHHkW9mKFUWjH-GJ5AX1ThbnKzsOQJKHw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh8VT9hUEzW9FOqAGr5nzPz5JpX5K2hUgL.Foq7SK-ceo.ESKM2dJLoIXnLxKMLB.-L1--LxKnL122LBo2LxK.L1KnLB--LxKqL1-zLB.eLxKqLBozLBoeLxK.L1K-L1hMLxKML1KqLB.eLxKML1KML1-zt; SUHB=0pHx1wTmUZIJAy; ALF=1516065470; SSOLoginState=1484529471; un=14794601372',
        # 'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        'Host': 'weibo.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }


# url = 'http://weibo.com/durexinchina'
# res = requests.get(url,headers=headers)
# content = res.text
# print(content)

i = 1
while i < 1000:
    if i % 3 == 2 and i%5 == 2:
        print(i)
