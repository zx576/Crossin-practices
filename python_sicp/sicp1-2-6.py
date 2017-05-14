'''
寻找素数
'''
# import sys
# import math
# sys.setrecursionlimit(1500)
# 一般解法
def ss(n,b=2):
    if n == b:
        return n
    # elif b % 2 == 0:
    #     return ss(n,b=b+1)
    elif n % b == 0:
        return b
    else:
        return ss(n,b=b+1)

print(ss(199))

# 费马定理
# def fm(b,n=3):
