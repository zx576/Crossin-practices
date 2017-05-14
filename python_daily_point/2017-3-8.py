#-*- coding:utf-8 -*-

from doctest import run_docstring_examples

def func(x):
    '''
    >>> func(3)
    3
    '''
    return x

assert func(3) == 3,'revoke'

a = run_docstring_examples(func,globals(),True)
print(a)
