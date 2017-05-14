#-*- coding:utf-8 -*-
import re

def generate_txt():
    content = ['上海','你好,hello,world','do it best','  ，，程序，boom']
    with open('from.txt','w')as f:
        for i in content:
            f.write(i)
            f.write('\n')


def collect_words():
    with open('from.txt','r') as f, open('to.txt','w')as l:
        for i in f.readlines():
            collect_info = re.findall(r'[A-Za-z]+',i)
            if collect_info:
                for i in collect_info:
                    l.write(i)
                    l.write('\n')

generate_txt()
collect_words()


