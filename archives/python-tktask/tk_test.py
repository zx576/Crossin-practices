#-*- coding:utf-8 -*-
import functools

#
# def log(func):
#     @functools.wraps(func)
#     def wapper(*args,**kw):
#         print('call,%s'%(func.__name__))
#         return func(*args,**kw)
#     return wapper
#
# @log
# def new(a):
#     b = input()
#     print(b)
#
# new(11)
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s,%s' %(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log('call')
def now():
    print('success')

now()
