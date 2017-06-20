# coding=utf-8

class QueueCur:

    def __init__(self, maxsize):
        self._count = 0
        self._front = 0
        self._back = maxsize-1
        self.qarray = [None for i in range(maxsize)]

    def __len__(self):
        return self._count

    def isEmpty(self):
        return self._count == 0

    def isFull(self):
        return self._count == len(self.qarray)

    def enqueue(self, item):
        assert not self.isFull(), 'the queue is full'
        self._back = (self._back + 1) % len(self.qarray)
        self.qarray[self._back] = item
        self._count += 1

    def dequeue(self):
        assert not self.isEmpty(), 'the queue is empty'
        item = self.qarray[self._front]
        self._front = (self._front + 1) % len(self.qarray)
        self._count -= 1
        return item

    def __str__(self):
        return str(self.qarray)


qc = QueueCur(5)
qc.enqueue(5)
qc.enqueue(6)

print(qc)

qc.dequeue()

print(qc.dequeue())
qc.dequeue()
