# coding=utf-8
# author = zhouxin
# data = 2017.7.2

import time

class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:

    def __init__(self):
        self._hashlist = [None for i in range(7)]

    def __len__(self):
        return len(self._hashlist)

    def is_full(self):
        return None not in self._hashlist

    def additem(self, key, value):
        # assert not self.is_full()
        is_inlist = self._finditem(key)
        if is_inlist:
            is_inlist.value = value
        else:
            assert not self.is_full()
            newitem = HashItem(key, value)
            pv = hash(key) % len(self._hashlist)
            if self._hashlist[pv] is None:
                self._hashlist[pv] = newitem
            else:
                count = 1
                next_pv = (hash(key)+count) % len(self._hashlist)
                while True:
                    if self._hashlist[next_pv] is None:
                        self._hashlist[next_pv] = newitem
                        break

                    count += 1
                    next_pv = (hash(key) + count) % len(self._hashlist)


    def _finditem(self, key):
        pv = hash(key) % len(self._hashlist)
        if self._hashlist[pv] is not None:
            if self._hashlist[pv].key == key:
                return self._hashlist[pv]
            else:
                count = 1
                next_pv = (hash(key)+count) % len(self._hashlist)
                while next_pv != pv and self._hashlist[next_pv] is not None:
                    # print(next_pv , count)
                    # time.sleep(2)
                    if self._hashlist[next_pv].key == key:
                        return self._hashlist[next_pv]

                    count += 1
                    next_pv = (hash(key) + count) % len(self._hashlist)

                return False
        else:
            return False

    def __str__(self):
        return str(self._hashlist)


hs = HashTable()
hs.additem(5,10)
print(hs)
hs.additem(12, 20)
print(hs)
hs.additem(19,30)
hs.additem(19,30)
print(hs)

