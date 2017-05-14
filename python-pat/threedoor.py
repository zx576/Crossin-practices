# -*- coding: utf-8 -*-
'''
三门问题
'''
import random
# 随机装配结果
def allocate():
    res = ['sheep','sheep','car']
    # print(type(res))
    random.shuffle(res)
    dic1 = {}
    n = 1
    for i in res:
        dic1[n] = i
        n += 1
    # print(dic1)
    return dic1
# 第一次选择
def make_choice():
    list1 = [1,2,3]
    choice = random.choice(list1)
    return choice
# 主持人第一次选择
def host_choice(f_choice,pre_reslut):
    list1 = [1,2,3]
    # p_choice = make_choice()
    list1.remove(f_choice)
    # pre_reslut = allocate()
    for i in list1:
        if pre_reslut[i] == 'sheep':
            return i

# 不修改选择
def non_switch():
    pre_reslut = allocate()
    f_choice = make_choice()
    if pre_reslut[f_choice] == 'car':
        return True
    else:
        return False

# 修改选择
def switch():
    pre_reslut = allocate()
    f_choice = make_choice()
    h_choice = host_choice(f_choice,pre_reslut)
    # print(pre_reslut[3])
    list1 = [1,2,3]
    list1.remove(f_choice)
    list1.remove(h_choice)
    # print(list1[0])
    if pre_reslut[list1[0]] == 'car':
        return True
    else:
        return False

def main():
    # count = input('>>>')
    count1 = 10000
    nons = 0
    s = 0
    for i in range(count1):
        non_switch_r = non_switch()
        if non_switch_r:
            nons += 1
        switch_r = switch()
        if switch_r:
            s += 1

    non_switch_rate = nons/count1
    switch_rate = s/count1
    print('不改变选择：',non_switch_rate)
    print('改变选择：',switch_rate)

main()
