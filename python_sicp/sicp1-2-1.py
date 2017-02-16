'''
递归法求解阶乘
'''

def fac(x):
    if x == 1:
        return 1
    return x * fac(x-1)
print(fac(300))


'''
迭代法求解
'''
def fac2(x):
    result = 1
    count = 1
    while count <= x:
        result *= count
        count += 1
    return result

# print(fac2(300))
