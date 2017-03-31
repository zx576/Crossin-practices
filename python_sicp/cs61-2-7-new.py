


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



c = ComplexRI(5,12)
print(c.magnitude)
