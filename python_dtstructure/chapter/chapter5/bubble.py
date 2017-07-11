# coding=utf-8
import random

def bubble(lst):

    n = len(lst)
    for i in range(n):
        for j in range(n-1-i):
            print(lst)
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]

        print('...................')

    return lst



# print(bubble(lst))
def test():

    count = 0
    while count < 10000:
        lst = list(range(10))
        random.shuffle(lst)
        b_sort = bubble(lst)
        py_sort = sorted(lst)
        assert b_sort == py_sort
        count += 1

# test()

lst = [1,2,3,2,1,5]
random.shuffle(lst)
b_sort = bubble(lst)
print(b_sort)
