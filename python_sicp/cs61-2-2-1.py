from operator import rshift,concat,delitem
from fractions import gcd

def rational(n,d):
    g = gcd(n,d)
    return (n//g,d//g)

# print(rational(1,3))

x = rshift(10,2)
# print(x)

# y = concat({3,45},{4})

# print(y)
z = delitem([1,2,3],1)

print(z)
