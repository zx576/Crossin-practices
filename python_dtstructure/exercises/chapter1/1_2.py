import random

class GrabBag:

    def __init__(self):
        self._lst = []


    def add(self,item):
        self._lst.append(item)


    def grabItem(self):
        assert len(self._lst) > 0,'no items in list'
        item = random.choice(self._lst)
        return item


    def contain(self,item):
        bl_res = item in self._lst
        return bl_res

    def __len__(self):
        length = len(self._lst)
        return length


    def __iter__(self):
        return iter(self._lst)

    def __str__(self):
        return str(self._lst)

    def numof(self,item):
        cnt = self._lst.count(item)
        return cnt



gb = GrabBag()
gb.add(1)
gb.add(2)
gb.add(3)
gb.add(1)

gb.grabItem()

gb.contain(4)

# print(gb.__len__())
# print(gb)


# for i in gb.__iter__():
#     print(i)

print(gb.numof(1))
