# coding=utf-8

'''
指数运算
'''

def expt(n, p):
    if p == 1:
        return n
    elif p % 2 == 0:
        return expt(n*n, p//2)
    else:
        return n*expt(n*n, p//2)
