# coding=utf-8
import math

def goldbach(num):
    # 断言 num 为偶数并且大于 2
    assert num % 2 == 0 and num > 2 , 'num 应为偶数'
    # 仅找出一组数据
    for i in range(2,num):
        # 满足两数之和为 num 并且都为质数
        if is_prime(i) and is_prime(num-i):
            print('数{0}可由两个素数：{1}和{2}组成'.format(num,i,num-i))
            break


def is_prime(num):
    # 判断特殊情况
    if num % 2 == 0:
        return False
    # 从 3 到 sqrt(num)循环判断，并且去除其中偶数
    sqrt_num = int(math.sqrt(num))
    for i in range(3,sqrt_num+1,2):
        if num % i == 0:
            return False
    return True


'''
张贺 : 遍历２以上Ｎ的平方根以下的每一个整数或奇数，是不是能整除Ｎ，并比较了两种方法耗时。
http://paste.ubuntu.com/24666659/

徐大龙 : 遍历２以上Ｎ的平方根以下的每一个整数，是不是能整除Ｎ，写法简单易懂
https://github.com/PeytonXu/learn-python/blob/master/cases/gold_bach/gold_bach.py

'''


print(is_prime(3))

# goldbach(1234567888)
