'''
练习1.34
'''
def func(g):
    print(g)
    return g(2)

print(func(func))
