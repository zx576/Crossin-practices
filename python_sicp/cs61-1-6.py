# *-* coding:utf-8 *-*

###1.6.3
def average(x,y):
    return (x+y)/2

def improve(update,close,guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def approx_eq(x,y,tolerance=1e-3):
    return abs(x-y) < tolerance

def sqrt(a):
    def sqrt_update(x):
        return average(x,a/x)
    def sqrt_close(x):
        return approx_eq(x**2,a)
    return improve(sqrt_update,sqrt_close)

# result = sqrt(256)
# print(result)

###1.6.4
def func1(g,f):
    def func2(x):
        return f(g(x))
    return func2

print(func1(abs,float)(-1))

###1.6.5
def improve(update,close,guess=1):
    while not close(guess):
        print('guess:',guess)
        guess = update(guess)
    return guess

def approx_eq(x,y,tolerance=1e-3):
    print('abs(x,y):',abs(x-y))
    return abs(x-y) < tolerance

def newton_update(f,df):
    def update(x):
        print('update:',x - f(x)/df(x))
        return x - f(x)/df(x)

    return update

def find_zero(f,df):
    def near_zero(x):
        return approx_eq(f(x),0)
    return improve(newton_update(f,df),near_zero)

def square_root_newton(a):
    def f(x):
        return x*x - a

    def df(x):
        return x * 2

    return find_zero(f,df)


# print(square_root_newton(64))


####1.6.7
def compose(f,g):
    return lambda x:f(g(x))

s =compose(lambda x:x**2,lambda y : y+1)

# print(s(12))

compose1 = lambda f,g: lambda: f(g(x))

print(compose1(int,abs)(-5))





####1.6.6
def curry_pow(x):
    def g(y):
        return pow(x,y)

    return g

print(curry_pow(5)(6))


def map_to_range(start,end):
    def f(x):
        return x**2
    while start < end:
        print(f(start))
        start += 1



    # return
# map_to_range(1,5)
