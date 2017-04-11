#-*- coding:utf-8 -*-
'''

作者:
行业：
年龄：(可不填)
学习编程时间：(从参加码上行动开始算起吧)
介绍项目：(言简意赅)
学习感受：(本次参赛的感受，对码上行动的感受)

'''
import random
def load_dict_from_open(data):
    _dict={}
    try:
        with open(data,'r') as dict_data:
            for line in dict_data:
                (Cname,Ename)=line.strip().split(':')
                _dict[Cname]=Ename
    except IOError as ioerr:
        print "file %s is not exist"%(data)
    return _dict
if __name__=='__main__':
    _dict=load_dict_from_open('data.txt')
    # print _dict.decode('utf-8')
    for i,j in _dict.items():
        print i.decode('utf-8') , j
    print _dict.keys()


# print "choice(_dict.keys():",random.choice(_dict.keys()).decode('utf-8')
word=random.choice(_dict.keys())
print word
s=_dict[word]
print s
s1= raw_input("input the name in English:")

if s1!= s:
    print "not correct, go on"
else:
    print "bingo!"
