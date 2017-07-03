# coding=utf-8
# author = zhouxin
# date = 2017.7.1
import random

def quick(lst):
    n = len(lst)
    if n < 2:
        return lst

    pivtol = lst[0]
    left = []
    right = []
    for i in lst[1:]:
        if i > pivtol:
            right.append(i)
        else:
            left.append(i)

    return quick(left)+[lst[0]]+quick(right)

lst = list(range(10))
random.shuffle(lst)

print(quick(lst))
