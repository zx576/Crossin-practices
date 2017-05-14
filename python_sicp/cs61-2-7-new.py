


class Adder():
    def __init__(self,n):
        self.n = n

    def __call__(self,k):
        return self.n + k


# add3 = Adder(3)

# print(add3(4))

from math import atan2
class ComplexRI():
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

    @property
    def magnitude(self):
        return (self.real**2+self.imag**2)*0.5



# c = ComplexRI(5,12)
# print(c.magnitude)

#

from fractions import gcd

class Rational():
    def __init__(self,numor,denom):
        g = gcd(numor,denom)
        self.numor = numor // g
        self.denom = denom // g

    def __repr__(self):
        return 'Rational(%d ,%d)'%(self.numor,self.denom)

    def add(self,other):
        nx , dx = self.numor,self.denom
        ny , dy = other.numor,other.denom
        return Rational(nx*dy+ny*dx,dx*dy)

    def mul(self,other):
        numor = self.numor * other.numor
        denom = self.denom * other.denom
        return Rational(numor,denom)

a = Rational(1,2)
print(a.add(Rational(3,5)))




















############
