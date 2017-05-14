#-*- coding:utf-8 -*-

import itertools


# 装满 6 格，金额小于 10000
equipment = [690,1500,2100,1740,2140,2080]
def func1():
    conb = itertools.combinations_with_replacement(equipment,6)
    count = 0
    for i in conb:
        if sum(i) < 10000:
            count += 1

    return count

print(func1())


# 没有格子的限制，
def func2():
    count = 0
    for j in range(1,(10000//min(equipment)+1)):
        conb = itertools.combinations_with_replacement(equipment,j)
        for i in conb:
            if sum(i) < 10000:
                count += 1
                # print(i)
    return count

print(func2())

# 在附加题一的限制下，价值690的鞋子最多出现一次
def func3():
    count = 0
    for j in range(1,(10000//min(equipment)+1)):
        conb = itertools.combinations_with_replacement(equipment,j)
        for i in conb:
            if sum(i) < 10000 and i.count(690) <= 1:
                count += 1
                # print(i)
    return count

print(func3())
