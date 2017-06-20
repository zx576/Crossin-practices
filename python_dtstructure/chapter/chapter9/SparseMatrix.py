# coding = utf-8

# 多重链表实现稀疏矩阵
class SparseMatrix:

    def __init__(self, row ,col):
        self.row = row
        self.col = col
        self.arrayRow = [None for i in range(self.row)]
        self.arrayCol = [None for i in range(self.col)]

    def setitem(self, ndxtuple, value):
        row, col = ndxtuple


    def getitem(self, ndxtuple):
        pass


class Node:

    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        self.rownext = None
        self.colnext = None
