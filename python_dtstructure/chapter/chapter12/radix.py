# coding=utf-8
# author : zhouxin
# date : 2017.7.1

from queue import Queue
import random

def radix(lst, numDigits):

    binArray = [None for i in range(10)]
    for i in range(10):
        binArray[i] = Queue()

    common = 1

    for d in range(numDigits):
        for i in lst:
            r = (i // common) % 10
            binArray[r].put(i)

        j = 0
        for b in binArray:
            while not b.empty():
                lst[j] = b.get()
                j += 1

        common *= 10

    return lst


lst = list(range(1000))
newlst = random.sample(lst,10)
max_n = 0
for i in newlst:
    n = len(str(i))
    if n > max_n:
        max_n = n
print(radix(newlst,max_n))
