# coding=utf-8

# 双向链表

class Dlinkedlist:

    def __init__(self):
        self._count = 0
        self._head = None
        self._tail = None

    def __len__(self):
        return self._count

    def additem(self, value):
        newNode = Dnode(value)
        # 当 _head 和 _tail 为 none
        if self._head is None:
            self._head, self._tail = newNode, newNode
        # 加在链表头
        elif self._head.val > value:
            newNode.next = self._head
            self._head.prev = newNode
            self._head = newNode
        # 加在链表尾
        elif self._tail.val < value:
            self._tail.next = newNode
            newNode.prev = self._tail
            self._tail = newNode
        # 加在链表中间
        else:
            curNode = self._head
            while curNode.val <= value:
                curNode = curNode.next
            curNode.prev.next = newNode
            newNode.prev = curNode.prev
            newNode.next = curNode
            curNode.prev = newNode

    def removeitem(self, value):
        pass

    def searchitem(self, value):
        pass

    def __str__(self):
        curNode = self._head
        res = []
        while curNode is not None:
            res.append(curNode.val)
            curNode = curNode.next
        return str(res)

    def strftail(self):
        curNode = self._tail
        res = []
        while curNode is not None:
            res.append(curNode.val)
            curNode = curNode.prev
        return str(res)

# 双向链表节点
class Dnode:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


dl = Dlinkedlist()
dl.additem(5)
print('str==',dl, '\nstr2==',dl.strftail() )
dl.additem(6)
dl.additem(9)
dl.additem(8)
print('str==',dl, '\nstr2==',dl.strftail() )
