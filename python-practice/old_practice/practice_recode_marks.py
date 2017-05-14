#-*- coding:utf-8 -*-
from random import choice,randint
import re
#生成随机文件
def generate_score():
    names = ('张飞', '赵云', '刘备', '关羽')
    with open('score.txt', 'w') as f:
        for x in range(10):
            #生成10行成绩
            scores = choice(names) + choice((' ', '')) + str(randint(60, 100))
            #print(scores)
            #写入文件
            f.write(scores)
            f.write('\n')
#处理数据，逻辑：定义一个dict={name：[total_score,times,average]},读取文件行后向dict里添加数据
def handle_data():
    #定义字典
    marks_dict = {}
    with open('score.txt','r') as f:
        for line in f.readlines():
            #确定内容不为空
            if line:
                #re找到人名
                name = re.findall(r'[\u4e00-\u9fa5]+',line)[0]
                #re找到成绩并转为数字
                mark = int(re.findall(r'[0-9]+',line)[0])
                #如果该名字不在dict中，添加新的key，并生成成绩列表
                if name not in marks_dict.keys():
                    marks_dict[name] = [mark,1,0]
                    marks_dict[name][2] = round(marks_dict[name][0]/marks_dict[name][1],2)
                #如果该名字在dict中，对成绩列表进行处理
                else:
                    marks_dict[name][0] += mark
                    marks_dict[name][1] += 1
                    marks_dict[name][2] = round(marks_dict[name][0] / marks_dict[name][1],2)
        #print(marks_dict)
    #返回最终的dict
    return marks_dict
#将成绩写入文件并输出
def output_data(value):
    #以总成绩为依据，对dict进行排序，返回dict.keys（即人名）的list
    basis = sorted(value, key=lambda x: value[x][0], reverse=True)
    with open('result.txt','w')as f:
        #遍历排序后的人名list
        for name in basis:
            #提取其成绩list
            person_list = value[name]
            #插入人名
            person_list.insert(0,name)
            print(person_list)
            #将list转为str写入文件
            f.write(repr(person_list))
            f.write('\n')

generate_score()
result = handle_data()
output_data(result)







