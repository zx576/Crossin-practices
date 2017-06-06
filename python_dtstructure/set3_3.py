# coding:utf-8
from functools import reduce

class MultiArray:

    def __init__(self,*dim):
        assert len(dim) > 1
        self._dims = dim
        size = reduce(lambda x,y : x*y,dim)

        self._data = []
        for i in range(size):
            self._data.append(None)


    def numdim(self):
        return len(self._dims)


    def length(self,dim):

        return self._dims[dim-1]

    def clear(self,value):
        for i in range(len(self._data)):
            self._data[i] = value

    def _getitem(self,ndxtuple):
        index = self._compute(ndxtuple)
        return self._data[index]

    def _setitem(self,ndxtuple,value):
        index = self._compute(ndxtuple):
        self._data[index] = value

    def _compute(self,ndxtuple):
        offset = 0
        for i in range(len(ndxtuple)):
            offset += (ndxtuple[i]-1) * self._factors(self._dims[i+1:])

        return offset+1

    def _factors(self,ndxlist):
        product = 1
        for i in ndxlist:
            product *= i

        return product

    
