
# coding=utf-8
# 行业：教育
# 学习编程时间：1月开始学习
# 介绍项目（记单词小游戏，用户通过根据游戏中随机出现的汉语意思，输入英文意思。程序根据用户输入判断对错。）
# 学习感受：（零基础学习编程所以很多概念都很陌生，听完几节课后，感觉是懂了，但是练习的时候无从下手。
# 这次比赛中，码上行动教程和老师给了很多指导和耐心帮助，自己也慢慢地对学过的知识有了点了解，非常感谢码上行动的老师们和这次活动，教程很棒！
# 我会继续学习，希望以后还有机会练习）

import random
def load_dict_from_open(data):
    dict={}
    try:
        with open(data,'r') as dict_data:
            for line in dict_data:
                (Cname,Ename)=line.strip().split(':')
                dict[Cname.decode('utf-8')]=Ename
    except IOError as ioerr:
        print "file %s is not exist"%(data)
    return dict

def select_one_from_dict(dict):
    dict_key=random.choice(dict.keys())
    print dict_key
    return dict_key

def print_to_user_then_input(dict_one):
    #print dict_one
    userinput=raw_input("enter the name in English:")
    print userinput
    return userinput
def compare_userinput_and_default(dict_key,dict,userinput):
    dict_one_value = dict.get(dict_key)
    #print dict_one_value
    #print type(dict_one_value)
    #print type(userinput)
    if dict_one_value == userinput:
        print "correct"
        return True
    else:
        print "wrong"
        return False

def play():
    while False:
        pass
while True:
    choice=raw_input("1.start, 2.quit")
    if choice=="1":
        play()
    elif choice=="2":
        break



    if __name__=='__main__':
       # 打开文件返回字典类型数据
       dict = load_dict_from_open('data.txt')
       # 选择一组数据
       dict_one = select_one_from_dict(dict)
       # 将 key 打印给用户并获取输入
       userinput = print_to_user_then_input(dict_one)
       # 比较
       compare_userinput_and_default(dict_one,dict,userinput)
       #print dict
       #print dict.keys()
