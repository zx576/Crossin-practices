
'''
欧几里得算法求公约数
'''
def ouj(b,n):
    # print(b,n)
    if n == 0:
        return b
    else:
        # print(b,n)
        b,n = n,b%n
        return ouj(b,n)

print(ouj(206,40))
