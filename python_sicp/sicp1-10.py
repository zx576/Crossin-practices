'''
练习 1-10
'''
def func(a,b):
    if b == 0:
        return 0
    elif a == 0:
        return 2*b
    elif b == 1:
        return 2
    else:
        return func(a-1,func(a,b-1))

res = func(2,1)
print(res)
