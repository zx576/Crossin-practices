# coding=utf-8
# 插入排序

import random

def insertion(lst):

    n = len(lst)
    for i in range(1, n):
        pos = i
        while pos>0 and lst[pos]<lst[pos-1]:
            lst[pos],lst[pos-1] = lst[pos-1],lst[pos]
            pos -= 1

    return lst

lst = list(range(20))
random.shuffle(lst)
b_sort = insertion(lst)
print(b_sort)
