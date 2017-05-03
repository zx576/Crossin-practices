#-*- coding:utf-8 -*-
import json

from qqbot import QQBotSlot as qqbotslot, RunBot

# 分别导入数据库操作相关类
from handle_r_dt import Resource_dt
from handle_group_dt import Group_dt

# 预导入
rdt = Resource_dt()


@qqbotslot
def onQQMessage(bot, contact, member, content):
    '''处理个人消息和群消息

    处理个人消息：
        使用 -Z 口令作为标识,handle_info_from_friend 函数处理
    处理群消息
        管理模式使用 -G 口令作为标识,handle_info_from_member 函数处理
        信息搜索模式使用 # 前缀作为标识,manage_groups 函数处理

    '''
    from_name = contact.__str__()

    # 个人消息处理
    if from_name.startswith('好友'):

        if content.startswith('-Z'):
            res_info = handle_info_from_friend(content)
            bot.SendTo(contact, res_info)

        else:
            bot.SendTo(contact, '本 QQ 号暂不回复个人消息，敬请谅解')

    # 处理群消息
    elif from_name.startswith('群'):

        if content.startswith('#'):
            res_info = handle_info_from_member(content)
            bot.SendTo(contact, res_info)

        elif content.startswith('-G'):
            res_info = manage_groups(bot, from_name[2:-1], content)
            bot.SendTo(contact, res_info)
        else:
            pass

    else:
        pass


def handle_info_from_friend(content):
    '''处理好友消息，处理 -Z 前缀的消息，目前仅能处理 4 个命令

    - insert : 插入数据
        用法: -Zinsert;title=xxxx;url=xxxx;keywords=xxxx;content=xxxx
        有严格的用法格式判断标准，数据不能缺少，以分号隔开
        17-4-20 数据的输入顺序很重要，必须按照 title-url-keywords-content 的顺序

    -search : 搜索内容
        用法：-Zsearch;id=x;title=xxxx;url=xxxx;keywords=xxxx;content=xxxx
        遵循 id=x 这样的输入格式，数据不要求都有
        17-4-20 目前仅支持 id 搜索和关键字搜索
            使用方法：  -Zsearch;id=1
            或者       -Zsearch;keywords=exe

    -update: 更新内容
        用法：-Zupdate;id=x;title=xxxx;url=xxxx;keywords=xxxx;content=xxxx
        有严格的用法格式判断标准，数据不能缺少，以分号隔开
        17-4-20 数据的顺序

    -group: 查询群成员
        用法：-Zgroup;name='编程教室中级一班'

    '''

    content = content[2:].strip()
    cont_list = content.split(';')
    words = ['id', 'title', 'url', 'keywords', 'content']

    if content.startswith('insert'):

        if len(cont_list) == 5:

            title = cont_list[1].split('=')[1]
            url = cont_list[2].split('=')[1]
            keywords = cont_list[3].split('=')[1]
            content = cont_list[4].split('=')[1]

            rdt.insert_item(title, url, keywords, content)
            return '存入成功'

        else:
            return '数据格式错误'

    elif content.startswith('search'):

        id, title, url, keywords, content = 'none', 'none', 'none', 'none', 'none'
        s_dict = {}

        for item in cont_list:
            k_v = item.split('=')
            if 'id' in k_v:
                id = k_v[1]
            elif 'title' in k_v:
                title = k_v[1]
            elif 'url' in k_v:
                url = k_v[1]
            elif 'keywords' in k_v:
                keywords = k_v[1]
            elif 'content' in k_v:
                content = k_v[1]

        res = rdt.search_items(id, title, url, keywords, content)

        return str(res)

    elif content.startswith('update'):

        update_dict = {}

        # if not cont_list[1].startswith('id='):
        #     return '缺乏id'

        if len(cont_list) == 6:

            id = cont_list[1].split('=')[1]
            title = cont_list[2].split('=')[1]
            url = cont_list[3].split('=')[1]
            keywords = cont_list[4].split('=')[1]
            content = cont_list[5]. split('=')[1]

        else:
            return '条目数目不为 5'

        try:
            id = int(id)
        except:
            return 'id 值错误'

        res = rdt.update_items(id, title, url, keywords, content)
        return '更新结果：' + res

    elif content.startswith('group'):
        groupname = cont_list[1].split('=')[1]
        gt = Group_dt(groupname)
        return gt.__str__()


'''
def handle_info_from_authority(content):
    if content.startswith('#'):
        content = content[1:]
        res_dict = rdt.search_items_for_group(content)
        if res_dict:
            # for value in res_dict.values():
            #
            res_info = json.dumps(res_dict)
            return res_info
        else:
            return '没有查询结果'


    elif content.startswith('-'):
        pass
    else:
        pass

'''


def handle_info_from_member(content):
    '''回复群消息中带有 # 前缀的消息

    '''

    content = content[1:]
    res_dict = rdt.search_items_for_group(content)
    if res_dict:
        res_list = []
        for value in res_dict.values():
            title = value['title']
            url = value['url']
            content = value['content']
            if content == 'none':
                summary = title + ':' + url + '\n'
            else:
                summary = title + ':' + url + '\n' + '简介：' + content

            res_list.append(summary)

        return '\n'.join(res_list)
    else:
        return '没有查询结果'


def manage_groups(bot, from_name, content):
    '''管理群，目前提供建表和查询新增用户的功能
    - 建表 将本群所有用户导入到数据库
        用法： -G建表
    - 查新 查询是否有新用户添加
        用法： -G查新
    '''
    content = content[2:]

    if content.startswith('建表'):
        gt = Group_dt(from_name.replace(' ', ''))
        g = bot.List('group', from_name)[0]
        members = bot.List(g)
        # print(members)
        if gt.all_members:
            return '表中已经存在内容'
        else:
            res = gt.update(members)
            return '建表成功'

    elif content.startswith('查新'):
        gt = Group_dt(from_name.replace(' ', ''))
        g = bot.List('group', from_name)[0]
        members = bot.List(g)
        res = gt.update(members)
        # print(members)
        if res:
            return '新成员' + str(res)
        else:
            return '无更新'

    # elif content


if __name__ == '__main__':
    RunBot()
