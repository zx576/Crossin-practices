#-*- coding:utf-8 -*-
import os

#检索数据
def index(keywords,path):
    foundlist = []
    for path, dirnames, filenames in os.walk(path):
        # print(path,dirnames,filenames)
        for i in filenames:
            if keywords in i:
                #print('filenames:',keywords +' in '+path+'\\'+i)
                foundlist.append(path+'\\'+i)
            #添加errors='ignore'解决编码问题
            with open(path+'\\'+i,errors = 'ignore')as f:
                for line in f.readlines():
                    if keywords in line:
                        #print('in_files:',path+'\\'+i+'\\'+line)
                        foundlist.append(path+'\\'+i+'>>>>>>'+line)
    return foundlist
path = input('path:')
keywords = input('keywords:')
result = index(keywords,path)
for i in result:
    print(i)

