from math import sqrt
fr

def week4_Goldbach( num ):
    # 验证哥德巴赫猜想
    num = int(num)
    if mod(num,2)==0:
        for m in range(2,num):
            n = num - m
            if week4_isPrime(m) and week4_isPrime(n):
                print(m,' + ',n,' == ',num)
                return
    elif num>5:
        for m in range(2,num-4):
            for n in range(2,num-2-m):
                k = num-m-n
                if week4_isPrime(m) and week4_isPrime(n) and week4_isPrime(k):
                    print(m,' + ',n,' + ',k,' == ',num)
                    return
    print('Failed')
    return

def week4_isPrime( num ):
    # 判断是否质数
    num = int( num )
    if num>=1 and num<=3:
        return True
    for x in range(2, int( sqrt(num) )+1 ):
        if mod(num,x)==0:
            return False
    return True


week4_Goldbach(123456)
