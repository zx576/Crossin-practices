import itchat
from itchat.content import *

itchat.auto_login(hotReload=True)
# itchat.send('hello world',toUserName='filehelper')
# itchat.

itchat.send('hello,helper',toUserName='filehelper')
itchat.send_msg('hello,helper',toUserName='filehelper')
itchat.send_image(r'photo2.png',toUserName='filehelper')


@itchat.msg_register(TEXT,NOTE,SHARING,SYSTEM)
def simple_reply(msg):
    # print(msg['FromUserName'])
    print(msg)
    # return 'I received: %s' % msg['Text']
    # itchat.send_image(r'', toUserName='filehelper'

    # )
    # print('entry 1')
    itchat.send(msg['Text'],toUserName='filehelper')
    # print('out 1')

@itchat.msg_register(MAP,CARD,ATTACHMENT,FRIENDS)
def reply_s(msg):
    print(msg)

@itchat.msg_register
def reply_any(msg):
    print(msg)

@itchat.msg_register(PICTURE,VIDEO,RECORDING)
def reply_pic_video(msg):
    print(msg)
    msg['Text'](msg['FileName'])
    itchat.send('hello world')


print(itchat.search_mps(name='编程'))
print(itchat.search_chatrooms(name='耍娃儿攻'))
res = itchat.search_friends(name='倩女神')
print(res)

itchat.run()

