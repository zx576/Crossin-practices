'''
双重函数定义
def incr(n):
    def func(x):
        return n+x
    return func

print(incr(5)(6))
'''

# '''
# 注释写法
# from operator import mul
# def square(x):
#     # '''
#     #function:return square x
#     #x - the paramater which will be squared
#     # '''
#     return mul(x,x)
#
# x = -2
#
# print(square(x))
# '''

# x = 1
# assert x == 2

import random
a = random.sample(range(33),6)
print(a)
