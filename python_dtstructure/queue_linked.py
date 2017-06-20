# coding=utf-8

class QueueLink:

    def __init__(self):
        self._qhead = None
        self._qtail = None
        self._count = 0

    def isEmpty(self):
        return self._qhead == None

    def __len__(self):
        return self._count

    def enqueue(self, item):
        newNode = Node(item)
        # queue is empty
        if self._qhead is None:
            self._qhead = newNode
        else:
            self._qtail.next = newNode

        self._qtail = newNode
        self._count += 1

    def dequeue(self):
        assert not self.isEmpty(), 'the queue is empty'
        node = self._qhead
        if self._qhead.next is None:
            self._qhead, self._qtail = None, None
        else:
            self._qhead = self._qhead.next

        self._count -= 1
        return node.item

    def __str__(self):
        res = []
        curNode = self._qhead
        while curNode is not None:
            res.append(curNode.item)
            curNode = curNode.next
        return str(res)


class Node:

    def __init__(self, item):
        self.item = item
        self.next = None


ql = QueueLink()
print(ql)
ql.enqueue(5)
print(ql)
ql.enqueue(6)
print(ql)
print(ql.dequeue())
print(ql.dequeue())
print(ql.dequeue())
