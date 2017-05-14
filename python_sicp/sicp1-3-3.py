'''
求方程的解
求不动点
'''

def func(f,a,b):
    print(a,b)
    c = (a+b)/2
    if  -0.0001< a-b < 0.0001:
        return c
    if f(c) > 0:
        return func(f,a,c)
    elif f(c) < 0:
        return func(f,c,b)

def f(c):
    res = c*c - 4*c -1
    return res

def func2(a,b):
    return func(f,a,b)

# print(func2(2,5))
import math
# 求不动点
def func3(f2,b):
    if -0.01 < f2(b) - b < 0.01:
        return b
    else:
        return func3(f2,f2(b))

def f2(b):
    return 1+1/b

# print(func3(f2,1))
# 不动点寻找平方根
def func4(f4,b,c):
    if -0.001 < f4(b,c) - b < 0.001:
        return b
    else:
        print(b)
        return func4(f4,f4(b,c),c)

def f4(b,c):
    return 0.5*(b+c/b)

print(func4(f4,9,16))
