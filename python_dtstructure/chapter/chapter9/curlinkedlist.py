# coding=utf-8

# 循环单向链表
class CurLinkedList:

    def __init__(self):
        self._count = 0
        self._tail = None

    def __len__(self):
        return self._count

    def additem(self, value):
        newNode = Cnode(value)
        # 如果 tail 为 none
        if self._tail is None:
            self._tail = newNode
            newNode.next = newNode
        # 加在链表尾
        elif self._tail.val <= value:
            newNode.next = self._tail.next
            self._tail.next = newNode
            self._tail = newNode
        else:
            curNode = self._tail.next
            preNode = self._tail
            while curNode.val <= value:
                preNode = curNode
                curNode = curNode.next

            preNode.next = newNode
            newNode.next = curNode

    def searchitem(self, value):
        pass

    def __str__(self):

        curNode = self._tail.next
        res = []
        mark = 1
        while curNode is not self._tail.next or mark:
            mark = 0
            res.append(curNode.val)
            curNode = curNode.next
        return str(res)

class Cnode:

    def __init__(self, val):
        self.val = val
        self.next = None

cl = CurLinkedList()
cl.additem(5)
print(cl)
cl.additem(7)
cl.additem(9)
cl.additem(6)
print(cl)
