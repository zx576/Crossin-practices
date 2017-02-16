#-*- coding:utf-8 -*-
import os
import json
import re
import jieba
import jieba.analyse
# 打开文件
def openfile(add):
    with open(add,'r',errors='ignore',encoding='utf-8') as f:
        data = f.readlines()
    # print(type(data))
    # for i in data:
    #     yield i
    return data


# 数据分发
def distribute_data(data):
    '''
    data:{"1661845933": {"初中：": "广州十六中 (1994年)   初中四班",
    "标签：": "CICFEXPO編輯原创漫画bilibili二次元移动互联网漫友漫画SHOW动漫",
     "注册时间：": "2009-11-18", "大学：": "华南师范大学 (2000年)   旅游管理系",
      "个性域名：": "http://weibo.com/gscwl",
       "公司：": "bilibili（哔哩哔哩）  (2016 - )    地区：上海 ，       浦东新区 职位：内容合作部",
       "昵称：": "大魔王小狐君",
       "简介：": "中国动漫一小狐/资深二次元宅男/前《漫友》《漫画秀》主编&CICFEXPO创办人",
       "博客：": "http://blog.sina.com.cn/gscwl",
       "性别：": "男",
       "生日：": "1981年10月22日",
       "所在地：": "广东 广州",
       "高中：": "广州市第十六中学 (1997年)   高中二班"}}
    :return:
    '''
    # 取到 id 号
    uid = data[2:12]
    # print(uid)
    # json 处理文档
    unpack_data = json.loads(data)
    # print(unpack_data)
    # 得到所有有效数据
    info_dict = unpack_data[uid]
    # print(info_dict)
    for key in info_dict:
        # print(key)
        val = info_dict[key]
        # 分发地区数据
        if key == '所在地：':
            # val = info_dict[key]
            # 分发到处理 ‘所在地’ 的函数
            location(val)
        elif key == '性别：':
            # val = info_dict[key]
            sex(val)
        elif key == '标签：':
            # val = info_dict[key]
            tags(val)
        elif key == '生日：':
            # 尝试拿到性别
            try:
                se = info_dict['性别：']
            except:
                se = 'none'
            # 把生日和性别发给 birthday 函数
            birthday(val,se)
        elif key == '注册时间：':
            register_time(val)
        # if key == '大学：':
    # 学历发送给 degree
    degree(data)

# 学历
degree_dict = {
    '大学':0,
    '中专技校':0,
    '高中':0,
    '初中':0,
    '小学':0,
    '未知':0,
}
def degree(data):
    if '大学' in data:
        degree_dict['大学'] += 1
        return
    elif '高中' in data:
        degree_dict['高中'] += 1
        return
    elif '中专技校' in data:
        degree_dict['中专技校'] += 1
        return
    elif '初中' in data:
        degree_dict['初中'] += 1
        return
    elif '小学' in data:
        degree_dict['小学'] += 1
        return
    else:
        degree_dict['未知'] += 1
        return
# 注册时间
register_dict = {
    '2009':0,
    '2010':0,
    '2011':0,
    '2012':0,
    '2013':0,
    '2014':0,
    '2015':0,
    '2016':0,
    '2017':0,

}
def register_time(val):
    rule = re.compile(r'(\d{4})')
    register_year = ''
    try:
        register_year = re.findall(rule,val)[0]
    except:
        pass
    else:
        register_dict[register_year] += 1

# 城市数据
location_list = [{'name': 'x', 'value': 1}]
cities = set()
def location(val):
    # 分离省市区，只保留城市
    city = val.split(' ')[0]
    # 如果 city 在 cities 中，直接添加数据
    if city in cities:
        for data in location_list:
            if data['name'] == city:
                data['value'] += 1
    # 否则新建数据
    else:
        new_data = {'name': city, 'value': 1}
        location_list.append(new_data)
        cities.add(city)

# 性别数据
sex_list = [{'name': '男', 'value': 0},{'name': '女', 'value': 0}]
def sex(val):
    # 遍历 sex_list，根据 val 的值累加 value
    for sex in sex_list:
        if sex['name'] == val:
            sex['value'] += 1

# 标签数据
all_tags = ''
def tags(val):
    global all_tags
    all_tags += val

# jieba 统计词频
word_freq = {}
def jieba_tags():
    # 获得权重 大的数
    data = jieba.analyse.extract_tags(all_tags, topK=20, withWeight=False, allowPOS=())
    # 添加到字典
    for i in data:
        word_freq[i] = all_tags.count(i)


# 统计生日 并得到星座
cons_dict = {
    '白羊座':{'male':0,'female':0},
    '金牛座':{'male':0,'female':0},
    '双子座':{'male':0,'female':0},
    '巨蟹座':{'male':0,'female':0},
    '狮子座':{'male':0,'female':0},
    '处女座':{'male':0,'female':0},
    '天秤座':{'male':0,'female':0},
    '天蝎座':{'male':0,'female':0},
    '射手座':{'male':0,'female':0},
    '水瓶座':{'male':0,'female':0},
    '双鱼座':{'male':0,'female':0},
    '摩羯座':{'male':0,'female':0},
    '其他':{'male':0,'female':0},
}
year = {
    '60sm':{'male':0,'female':0},
    '60s':{'male':0,'female':0},
    '70s':{'male':0,'female':0},
    '80s':{'male':0,'female':0},
    '90s':{'male':0,'female':0},
    '00s':{'male':0,'female':0},
}
def birthday(val,sex):
    if val == '1900年1月1日':
        return
    if val == '1月1日':
        return
    # 统计 星座
    rule = re.compile(r'(\d{1,2})月(\d{1,2})')
    # 统计 年
    # rule2 = re.compile(r'(\d{4})年.*')
    rule2 = re.compile(r'(\d{4})年')
    # 获取星座
    if '月' in val:
        res = ''
        try:
            res = re.findall(rule,val)[0]
        except:
            pass
        else:

            res = [i for i in res]
            if len(res[1]) == 1:
                res[1] = '0'+ res[1]
            birth = ''.join(res)
            birth2int = int(birth)
            # if birth2int == 101
            if 319 <= birth2int <= 419:
                constellation = '白羊座'
            elif 420 <= birth2int <= 520:
                constellation = '金牛座'
            elif 521 <= birth2int <= 621:
                constellation = '双子座'
            elif 622 <= birth2int <= 722:
                constellation = '巨蟹座'
            elif 723 <= birth2int <= 822:
                constellation = '狮子座'
            elif 823 <= birth2int <= 922:
                constellation = '处女座'
            elif 923 <= birth2int <= 1023:
                constellation = '天秤座'
            elif 1024 <= birth2int <= 1122:
                constellation = '天蝎座'
            elif 1123 <= birth2int <= 1221:
                constellation = '射手座'
            elif  1231 >= birth2int >= 1222 or 101 < birth2int <= 119:
                constellation = '摩羯座'
            elif 120 <= birth2int <= 218:
                constellation = '水瓶座'
            elif 219 <= birth2int <= 320:
                constellation = '双鱼座'
            else:
                constellation = '其他'
            # 判断男女
            if sex == '男':
                cons_dict[constellation]['male'] += 1
            elif sex == '女':
                cons_dict[constellation]['female'] += 1
            else:
                pass
        # 添加 年
        try:
            year_str = re.findall(rule2,val)[0]
        except:
            pass
        else:
            year2int = int(year_str)
            if 1960 <= year2int <= 1969:
                year_key = '60s'
            elif 1970 <= year2int <= 1979:
                year_key = '70s'
            elif 1980 <= year2int <= 1989:
                year_key = '80s'
            elif 1990 <= year2int <= 1999:
                year_key = '90s'
            elif 2000 <= year2int :
                year_key = '00s'
            else:
                year_key = '60sm'
            if sex == '男':
                year[year_key]['male'] += 1
            elif sex == '女':
                year[year_key]['female'] += 1
            else:
                pass
    elif '座' in val:
        if sex == '男':
            cons_dict[val]['male'] += 1
        elif sex == '女':
            cons_dict[val]['female'] += 1
        else:
            pass
    else:
        pass


# 测试
def main():
    pa = 'E:\GIT\practice\Crossin-practices\crawl\weibodata'
    allfiles = []
    for roots,dirs,files in os.walk(pa):
        for file in files:
            add = roots + os.sep +file
            allfiles.append(add)
    count = 0
    for addr in allfiles:
        userinfo = openfile(addr)
        count += len(userinfo)
        gen = (i for i in userinfo)
        for i in range(len(userinfo)):
            data = gen.__next__()
            distribute_data(data)
    print(count)
    # 最后统计一下词频
    jieba_tags()

    with open('location2.txt','w') as f:
        # 写入地区
        f.write(str(location_list))
        f.write('\n')
        # 写入性别
        f.write(str(sex_list))
        f.write('\n')
        # 写入年代
        f.write(str(year))
        f.write('\n')
        # 写入星座
        f.write(str(cons_dict))
        f.write('\n')
        # 写入标签词频
        f.write(str(word_freq))
        f.write('\n')
        # 写入注册时间
        f.write(str(register_dict))
        f.write('\n')
        # 写入学历信息
        f.write(str(degree_dict))

    # print(location_list)
    # print(cities)

main()
print('suc')