# coding=utf-8

class _bagItem:

    def __init__(self, item):
        self.item = item
        self.next = None


class BagAdt:

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def __contain__(self, item):
        curNode = self._head
        while curNode is not None and curNode.item != item:
            print(curNode.item)
            curNode = curNode.next
        return curNode is not None

    def add_front(self, item):
        newNode = _bagItem(item)
        if self._head is None:
            self._tail = newNode
        newNode.next = self._head
        self._head = newNode
        self._size += 1

    def add_end(self, item):
        newNode = _bagItem(item)
        if self._tail is None:
            self._head = newNode
            self._tail = newNode
        else:
            self._tail.next = newNode
            self._tail = newNode
        self._size += 1

    def remove(self, item):
        preNode = None
        curNode = self._head
        while curNode is not None and curNode.item != item:
            preNode = curNode
            curNode = curNode.next
            print(preNode.item, curNode.item)

        assert curNode.item is item , 'the item must be in the list'
        self._size -= 1

        if curNode is self._head:
            self._head = curNode.next
        else:
            preNode.next = curNode.next
        return curNode.item

    def __iter__(self):
        return _BagIterator(self._head)

    def __str__(self):
        curNode = self._head
        lst = []
        while curNode is not None:
            lst.append(curNode.item)
            curNode = curNode.next
        # return 'curhead is {}'.format(self._head.item)
        return str(lst)
class _BagIterator:

    def __init__(self, listhead):
        self._curNode = listhead

    def __iter__(self):
        return self

    def next(self):
        if self._curNode is None:
            raise StopIteration

        else:
            item = self._curNode.item
            self._curNode = self._curNode.next
            return item



bag = BagAdt()
bag.add_end(12)
bag.add_front(13)
bag.add_end(14)
print(bag)
# print(bag.__contain__(13))

# iter_bag = bag.__iter__()
#
# print(iter_bag.next())
# print(iter_bag.next())
