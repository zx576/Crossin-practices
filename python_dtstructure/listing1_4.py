

class BagIter():
    def __init__(self,lst):
        self.bagitems = lst
        self.crrt = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.crrt < len(self.bagitems):
            item = self.bagitems[self.crrt]
            self.crrt += 1
            return item

        else:
            raise StopIteration


q = BagIter([1,2,3,4])
# print(q.__next__())
# print(q.__next__())
# print(q.__next__())
# print(q.__next__())
# print(q.__next__())
# print(q.__next__())
for i in q.__iter__():
    print(i)
