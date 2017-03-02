'''

'''
def curry2(f):
    def g(x):
        def h(y):
            print('liner')
            return f(x,y)
        return h
    return g


def f(x,y):
    return x+y

# print(curry2(f)(2)(3))a
