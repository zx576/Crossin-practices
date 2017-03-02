#-*- coding:utf-8 -*-
from datetime import date
from unicodedata import lookup
dues = date(2017,3,11)

dues2 = date(2017,4,18)

print(type(dues))
print(type(dues2-dues))

a = dues.strftime('%A,%m,%d')
print(a)

b = '123s4'.isnumeric()
print(b)

suits = ['heart', 'diamond', 'spade', 'club']
d = [lookup(('WHITE ' + s.upper() + ' SUIT')) for s in suits]
print(d)

def fuc():
    nonlocal
