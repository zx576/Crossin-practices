from numpy import *
def week2_magic(n):
    if mod(n,2):
        # 奇数阶
        A = week2_oddMagic(n)
    elif mod( int(n/2) ,2 ):
        # 仅能被2整除，可拆分成四个奇数阶幻方
        a = int(n/2)
        A = zeros([n,n])
        A[:a,:a] = week2_oddMagic(a)
        A[a:,a:] = week2_oddMagic(a) + a**2
        A[:a,a:] = week2_oddMagic(a) + 2*a**2
        A[a:,:a] = week2_oddMagic(a) + 3*a**2
    else:
        # 仅能被4整除
        A = mat([i for i in range(1,n**2+1)]).reshape([n,n])
        J = mod( array([i for i in range(1,n+1)]) ,4 )>1.2
        for x in range(0,n):
            for y in range(0,n):
                if (J[x] == J[y]):
                    A[x,y] = n**2+1 - A[x,y]
    print(A)
    print(type(A))
    return A

def week2_oddMagic(n):
    # 罗伯特法求奇数阶幻方/楼梯法
    A = zeros([n,n])
    posX = 0
    posY = int(n/2)
    for val in range(1,n**2+1):
        if int(A[posX,posY]):
            posX = mod(posX+2,n)
            posY = mod(posY-1,n)
        # 赋值并更新位置
        A[posX,posY] = int(val)
        posX = mod(posX-1,n)
        posY = mod(posY+1,n)
    return A


def check(lst):

    t1 = [lst[row][row] for row in range(len(lst))]
    t2 = [lst[row][len(lst)-row-1] for row in range(len(lst))]

    assert sum(t1) == sum(t2),'error'

if __name__ == '__main__':
    # week1_romantic()
    lst = week2_magic(8)
    check(lst)
