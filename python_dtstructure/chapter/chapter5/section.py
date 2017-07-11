# coding=utf-8
# 选择排序
import random


def section(lst):

    n = len(lst)
    for i in range(n-1):
        small = i
        for j in range(i+1, n):
            try:
                if lst[j] < lst[small]:
                    small = j
            except:
                print(j, small)

        lst[i], lst[small] = lst[small], lst[i]

    return lst


def test():

    count = 0
    while count < 10000:
        lst = list(range(10))
        random.shuffle(lst)
        b_sort = section(lst)
        py_sort = sorted(lst)
        assert b_sort == py_sort
        count += 1

# test()

lst = [1,2,3,4,3,2,1]
random.shuffle(lst)
b_sort = section(lst)
print(b_sort)
