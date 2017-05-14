#-*- coding:utf-8 -*-
from qqbot import QQBotSlot as qqbotslot, RunBot

@qqbotslot
def onQQMessage(bot, contact, member, content):

    # 群消息处理
    # 群中管理员消息
    # if contact
    #
    # if contact.card == '周鑫鑫':
    #     return_info = give_info_to_authority(content)
    #     bot.SendTo(contact,return_info)
    # else:
    #
    print('============================')
    # print('bot:',bot)
    print('contact:',contact,';',contact.nick,contact.mark,contact.card,contact.name)
    print('member:',member)
    print(content)

    if '群' in contact.__str__():
        print('this message comes from group')

    if '好友' in contact.__str__():
        print('this message comes from friend')










if __name__ == '__main__':
    RunBot()
