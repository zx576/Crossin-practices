'''
高阶函数抽象
'''
# 求立方
def cube(x):
    return x*x*x

def inc(n):
    return n+1

# 高级抽象 求和
def sums(term,a,next,b):
    if a > b:
        return 0
    else:
        # print(a)
        return sums(term,next(a),next,b)+term(a)

# 求立方和
def sum_cubes(a,b):
    return sums(cube,a,inc,b)

# print(sum_cubes(1,10))
# jjkkkkkpppppppp
def identity(x):
    return x

# 求和
def sum_integer(a,b):
    return sums(identity,a,inc,b)

print(sum_integer(1,10))

# 求定积分
def add_dx(x):
    global dx
    return x+dx

def integral(f,a,b):
    a = a + dx/2
    return dx*sums(f,a,add_dx,b)
dx = 0.01
print(integral(cube,0,1))
