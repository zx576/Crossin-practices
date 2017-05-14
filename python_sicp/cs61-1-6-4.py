'''

'''

def func(x,y):
    print('pre')
    def func1(z):
        print('sub')
        return x+y+z
    x = x+y
    return func1

print(func(1,2)(3))
