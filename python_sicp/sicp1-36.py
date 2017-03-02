'''
练习1-36
'''
from math import log

def find_fixed_piont(next,x):
    if -0.001 < next(x)-x < 0.001:
        return x
    else:
        print(x)
        return find_fixed_piont(next,next(x))

def next(x):
    return 0.5*(log(1000)/log(x)+x)

print(find_fixed_piont(next,10))
