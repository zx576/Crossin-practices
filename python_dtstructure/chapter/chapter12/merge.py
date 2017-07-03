# coding=utf-8
# author = zhouxin
import random

def merge(lst):
    n = len(lst)
    if n < 2:
        return lst

    mid = n // 2
    left = merge(lst[:mid])
    right = merge(lst[mid:])

    return sortlst(left, right)

def sortlst(left, right):

    res = []
    len_left = len(left)
    len_right = len(right)
    while left and right:
        print('==',res)
        if left[0] > right[0]:
            res.append(right.pop(0))
        else:
            res.append(left.pop(0))

    res.extend(left or right)

    return res

lst = list(range(10))
random.shuffle(lst)

print(merge(lst))
