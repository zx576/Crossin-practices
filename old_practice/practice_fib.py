#-*- coding:utf-8 -*-

#输入数字判断
def input_num():
    t = input('>>>')
    try:
        t = int(t)
        if t > 3:
            pass
        else:
            fib()
    except:
        fib()
    return t
# 斐波那契输出
def fib():
    print('输入一个大于3的数字')
    a = 0
    b = 1
    n = input_num()
    for i in range(n):
        print(b)
        a,b = b,a+b
fib()
