'''
1-2-4
'''
# 线性迭代
def func(b,n,res = 1):
    if n == 0:
        return res
    else:
        return func(b,n-1,res=b*res)

print(func(9,10))
# 迭代优化
def func2(b,n,res=1,count=1):
    if n == 0:
        print(count)
        return res
    elif n % 2 == 0:
        return func2(b*b,n/2,res = res,count=count+1)
    else:
        return func2(b,n-1,res=b*res,count=count+1)

print(func2(9,10))


# 递归
def fun0(b,n):
    if n == 0:
        return 1
    else:
        return b*fun0(b,n-1)

print(fun0(9,10))
# 优化算法
def func1(b,n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return func1(b,n/2)*func1(b,n/2)
    else:
        return func1(b,n-1)*b

print(func1(9,10))
