# coding:utf-8
'''
鑿叉尝閭ｅ垏鏁板垪
'''
# 閫掑綊瑙ｆ硶
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

a = fib(9)
print(a)

# 涓�鑸В娉�
def fib2(n):
    int1= 0
    int2 = 1
    while n >= 2:
        af = int1 + int2
        int1 = int2
        int2 = af
        n -= 1
    return af

b = fib2(9)
print(b)
print('鍛ㄩ懌')
