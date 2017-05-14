'''
牛顿法求导数

'''
def deriv(x,g):
    return (g(x+dx)-g(x))/dx

def cube(x):
    return x*x*x

# dx = 0.00001
# print(deriv(5,cube))

def newton(x,g):
    return x-(g(x)/deriv(x,g))

def g(x):
    return x*x
def find_fixed_piont(next,x,g):
    if -0.001 < next(x,g)-x < 0.001:
        return x
    else:
        print(x)
        return find_fixed_piont(next,next(x,g),g)
dx = 0.00001
res = find_fixed_piont(newton,9,g)
print(res)
