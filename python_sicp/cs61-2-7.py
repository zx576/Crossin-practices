

def find_index(L,x,k):
    '''
    return the index of L
    '''

    for i in range(len(L)):
        if L[i] == x:
            if k == 0:
                return i

            k -= 1

print(find_index([1,2,3,4,5],4,0))

#######
class rational:
    def __init__(self,num,dem):
        self.numer = num
        self.denom = dem
    def __str__(self):
        return '%d/%d'%(self.numer,self.denom)
    def __repr__(self):
        return 'rational:%d/%d'%(self.numer,self.denom)

a = rational(30,4)
print(a)
rational(3,4)
print(a.__str__())
a.__str__ = lambda x:'foo'
print(a.__str__)

print(a.__str__(1))
print(a)

############3
from fractions import gcd
class Rational():
    def __init__(self,num,dem):
        self.numer = num
        self.denom = dem

    def __repr__(self):
        return 'rational %d/%d'%(self.numer,self.denom)
    def add(self,other):
        nx,dx = self.numer,self.denom
        ny,dy = other.numer,other.denom
        return Rational(nx*dy,ny*dx,dx*dy)
    def mul(self,other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(numer,denom)


a = Rational(1,2) + Rational(3,4)
print(a)

















########################3
