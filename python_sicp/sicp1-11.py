'''
习题1-11
'''
# 递归解法
def func(n):
    if n < 3:
        return n
    else:
        return func(n-1)+2*func(n-2)+3*func(n-3)

print(func(3))

# 迭代解法
def func2(n):
    n0 =  0
    n1 = 1
    n2 = 2
    if n < 3:
        return n
    while n-3 >= 0:
        n2,n1,n0 = n2+2*n1+3*n0,n2,n1
        n -= 1

    return n2
print(func2(5))
