# coding=utf-8

class QueueList:

    def __init__(self):
        self._qlist = list()

    def isEmpty(self):
        return len(self._qlist) == 0

    def __len__(self):
        return len(self._qlist)

    def enqueue(self, item):
        return self._qlist.append(item)

    def dequeue(self):
        assert not self.isEmpty , 'the queue is empty'
        return self._qlist.pop(0)

    def __str__(self):
        return str(self._qlist)

ql = QueueList()
ql.enqueue(5)
ql.enqueue(6)
ql.enqueue(7)
ql.enqueue(8)

print(ql)

ql.dequeue()
ql.dequeue()
ql.dequeue()
ql.dequeue()
ql.dequeue()

print(ql)
