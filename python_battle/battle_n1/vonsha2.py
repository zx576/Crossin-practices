#-*- coding:utf-8 -*-
import io
# import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
import chardet
# import sys
# reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
# sys.setdefaultencoding('utf-8')

# coding=utf-8
def load_dict_from_open(data):
    _dict={}
    try:
        with open('data.txt','r') as dict_file:
            for line in dict_file:
                (Cname,Ename)=line.strip().split(':')
                _dict[Cname]=Ename
    except IOError as ioerr:
        print 'file %s does not exist'%('data.txt')
    return _dict

def save_dict_to_open(_dict,data):
    try:
        with open('data.txt','w') as dict_data:
            for (Cname,Ename) in _dict.items():
                dict_data.write('%s:%s\n'%(Cname,Ename))
    except IOError as ioerr:
        print'file %s can not set up'%(data)

if __name__=='__main__':
    _dict=load_dict_from_open('dict_txt')
    print _dict
    save_dict_to_open(_dict,'dict_copy.txt')

import random
print random.choice(['苹果'])
word=raw_input("what is it in English?")
if word == 'apple':
    print "that's correct, go on!"
else:
    print "not correct"
