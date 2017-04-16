# -*- coding: utf-8 -*-

import sys,requests,json
# import chardet
def succesion(info):
    appkey="e5ccc9c7c8834ec3b08940e290ff1559"

    url="http://www.tuling123.com/openapi/api?key=%s&info=%s"%(appkey,info)
    content=requests.get(url)
    answer=content.text

    ans=json.loads(answer)
    aa=ans['text']
    # print(aa)
    return aa

def main(info):
    info = info.decode('gbk').encode('utf-8')
    aa=succesion(info)
    print 'tuling:%s'%aa

if __name__ == '__main__':
    print '开始聊天吧:'.decode('utf-8').encode('gbk')
    while True:
        info = raw_input('hinewai:')
        if '88' in info:
            break
        main(info)
#
# succesion(a)
