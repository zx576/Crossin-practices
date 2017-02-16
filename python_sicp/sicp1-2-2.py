'''
菲波那切数列
'''
# 递归解法
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

a = fib(9)
print(a)

# 一般解法
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
