# coding=utf-8

class Array2d:

    def __init__(self, row, col):
        self._array = [['#' for i in range(col)] for j in range(row)]
        self.row = row
        self.col = col

    def set(self, row, col, value):
        self._array[row][col] = value

    def numRows(self):
        return self.row

    def numCols(self):
        return self.col

    def getnext(self, row, col):
        if row-1 >= 0 and self._array[row-1][col] == '#':
            return (row-1, col)
        elif col+1 <= self.col and self._array[row][col+1] == '#':
            return (row, col+1)
        elif row+1 <= self.row and self._array[row+1][col] == '#':
            return (row+1, col)
        elif col-1 >= 0 and self._array[row][col-1] == '#':
            return (row, col-1)
        else:
            return False


class Cell:

    def __init__(Self, row, col):
        self.row = row
        self.col = col

    def get(self):
        return (self.row, self.col)

class Stack:

    def __init__(self):
        self.stack = list()

    def push(self, item):
        if item in self.stack:
            return False

        self.stack.append(item)
        return True

    def pop(self):
        assert self.stack
        return self.stack.pop(-1)

    def result(self):
        return self.stack


class Maze:

    MAZE_WALL = '*'
    PATH_TOKEN = 'X'
    TRIED_TOKEN = 'O'

    def __init__(self, row, col):
        self._mazecells = Array2d(row,col)
        self.startcell = None
        self.exitcell = None

    def numRows(self):
        return self._mazecells.numRows()

    def numCols(self):
        return self._mazecells.numCols()

    def setwall(row, col):
        self._mazecells.set(row, col, MAZE_WALL)

    def setStart(row, col):
        self.startcell = Cell(row, col)

    def setExit(row, col):
        self.exitcell = Cell(row, col)

    def _getnext(row, col):
        return self._mazecells.getnext(row,col)

    def findpath(self):
        path = Stack()
        curNode = self.startcell.get()
        while curNode is not self.exitcell.get():
            stackin = path.push(curNode)
            if stackin is False:
                return 'there is no way out'
            nextTuple = self._getnext(curNode[0], curNode[1])
            if nextTuple is None:
                curNode = path.pop()

            else:
                curNode = nextTuple

        return path.result()
