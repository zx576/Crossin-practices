'''
求乘积的高阶抽象
'''
def multi(f,a,next,b,res=1):
    if a > b:
        return 1

    else:
        print(a,res)
        return multi(f,next(a),next,b,res=f(a)*res)

def next(x):
    return x+2

def func(x):
    res = x/(x+1)
    return res*res

def cacu_pi(a,b):
    return 8*multi(func,a,next,b)

print(cacu_pi(4,10))
