# coding:utf-8

# sparse matrix

class SparseMatrix:

    def __init__(self,row,col):
        self._rows = row
        self._cols = col

        self._matrix = list()


    def numrows(self):
        return self._rows

    def numcols(self):
        return self._cols


    def setitem(self,ndxtuple,value):
        item = self._finditem(ndxtuple)
        if item == None:
            if value == 0.0:
                return

            else:
                # item.value = value
                ele = Element(ndxtuple[0],ndxtuple[1],value)
                self._matrix.append(ele)

        else:
            if value == 0.0:
                self._matrix.remove(item)
            else:
                item.value = value

    def _finditem(self,ndxtuple):
        for item in self._matrix:
            if item.row == ndxtuple[0] and item.col == ndxtuple[1]:
                return item

            else:
                continue

        return None


    def getitem(self,ndxtuple):
        # print(ndxtuple)
        item = self._finditem(ndxtuple)
        if item:
            return item.value
        else:
            return 0

    def length(self):
        return len(self._matrix)

    def showall(self):
        for item in self._matrix:

            print(item.row,item.col,item.value)


    def __add__(self,othermatrix):
        # print(self.numcols,othermatrix.numcols)
        assert self.numrows() == othermatrix.numrows() and \
                self.numcols() == othermatrix.numcols()

        newmatrix = SparseMatrix(self.numrows,self.numcols)

        for item in self._matrix:
            newmatrix._matrix.append(item)

        for item in othermatrix._matrix:
            value = newmatrix.getitem((item.row,item.col))
            value += item.value
            if newmatrix._finditem((item.row,item.col)):
                newmatrix._finditem((item.row,item.col)).value = value
            else:
                newmatrix.setitem((item.row,item.col),value)

        return newmatrix




class Element:

    def __init__(self,row,col,value):

        self.row = row
        self.col = col
        self.value = value


ins = SparseMatrix(3,3)
ins2 = SparseMatrix(3,3)

ins.setitem((0,0),6)
ins.setitem((1,1),60)
ins.setitem((2,2),7)


ins2.setitem((2,0),9)
ins2.setitem((0,1),8)
ins2.setitem((1,2),4)

new = ins + ins2
new.showall()
#
# print(ins.length())
# print(ins.getitem((4,7)))
# ins.showall()
