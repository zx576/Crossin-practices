# coding=utf-8

# 稀疏矩阵的单链表实现
class SparseMatrix:

    def __init__(self, row, col):
        self.col = col
        self.row = row
        self.arrayRow = [None for i in range(row)]

    def numRows(self):
        return len(self.arrayRow)

    def numCols(self):
        return self.col

    # 获取特定行列的值
    def __getitem__(self, ndxTuple):
        row, col = ndxTuple
        # 检查行列符合规则
        pass
        curNode = self.arrayRow[row]
        while curNode is not None and curNode.col != col:
            curNode = curNode.next

        return curNode.value if curNode else 0

    # 设置某特定行列的值
    def __setitem__(self, ndxTuple, value):
        row, col = ndxTuple
        preNode = None
        curNode = self.arrayRow[row]
        # 在特定行寻找该节点
        while curNode is not None and curNode.col != col:
            preNode = curNode
            curNode = curNode.next
        # 存在该节点
        if curNode is not None and curNode.col == col:
            # 赋值为 0 ，移除元素
            if value == 0.0:
                # 该元素为链表头
                if curNode is self.arrayRow[row]:
                    self.arrayRow[row] = curNode.next
                else:
                    preNode.next = curNode.next
            else:

                curNode.value = value
        # 不存在节点
        elif value != 0:
            newNode = Node(col, value)
            # 链表头为 none
            if self.arrayRow[row] is None:
                self.arrayRow[row] = newNode
            # 插入链表尾
            elif preNode.col < col:
                preNode.next = newNode
            # 插入链表中
            else:
                nowNode = self.arrayRow[row]
                beforeNode = None
                while nowNode.col < col:
                    beforeNode = nowNode
                    nowNode = nowNode.next

                beforeNode.next = newNode
                newNode.next = nowNode

    # 矩阵相加
    def __add__(self, otherMatrix):
        pass

    def __str__(self):
        res = [[None for i in range(self.col)] for j in range(self.row)]
        for i in range(len(self.arrayRow)):
            curNode = self.arrayRow[i]
            while curNode is not None:
                res[i][curNode.col] = curNode.value
                curNode = curNode.next

        return str(res)


class Node:
    def __init__(self, col, value):
        self.col = col
        self.value = value
        self.next = None

sm = SparseMatrix(5,5)
sm.__setitem__((2,3), 6)
sm.__setitem__((2,4), 1)

print(sm)
res = sm.__getitem__((2,3))
print(res)
