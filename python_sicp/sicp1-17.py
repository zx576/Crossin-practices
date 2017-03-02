'''

'''
# 乘法：以加法实现
def func(a,b):
    if b == 0:
        return 0

    else:
        return a+func(a,b-1)
# print(func(2,3))
# 2倍：以加法实现

def double(n):
    return n*2
# print(double(2))

def halve(n):
    return n/2

# def accumulation(b,n):
#     if n == 0:
#         return 0
#     # if b == n:
#     #     return
#     else:
#         return b+accumulation(b,n-1)

# 练习的解法
def multi(b,n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return multi(double(b),halve(n))
    else:
        return multi(b,n-1)+b

print(multi(2,3))











#######end
