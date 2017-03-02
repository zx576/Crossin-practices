'''
寻找素数优化版
'''
def ss1(n,b=3):
    if n == b:
        return n
    elif n % 2 == 0:
        return 2

    elif n % b == 0:
        return b
    else:
        return ss1(n,b=b+2)

print(ss1(199))
