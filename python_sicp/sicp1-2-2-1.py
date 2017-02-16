'''
换零钱
'''
def count(n,coun):
    if n == 0:
        return 1
    elif n < 0 or coun == 0:
        return 0
    else:
        return count(n,coun-1)+count(n-func(coun),coun)

def func(n):
    if n == 1:
        return 1
    elif n == 2:
        return 50
    elif n == 3:
        return 10
    elif n == 4:
        return 25
    elif n == 5:
        return 5

print(count(100,5))

# 一般解法
currency = [1,5,10,20,50]
def countt(cash):
