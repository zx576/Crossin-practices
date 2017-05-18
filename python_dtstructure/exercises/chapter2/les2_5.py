
class Vetor:

    def __init__(self,item=1):
        self.vetor = [None for i in range(item*2)]

        # self.start = self.vetor[0]
        # self.end = self.vetor[item-1]

        self.end_idx = item - 1
        self.exp_ix = self.end_idx*2
    def _expand(self,exnum):

        ex_vetor = [None for i in range(exnum)]

        for idx in range(len(self.vetor)):
            ex_vetor[idx] = self.vetor[idx]

        self.vetor = ex_vetor


    def getitem(self,ndx):
        assert ndx <= self.end_idx
        return self.vetor[ndx]

    def setitem(self,ndx,item):

        assert ndx <= self.end_idx
        self.vetor[ndx] = item

    def length(self):
        return self.end_idx+1

    def appenditem(self,item):
        if len(self.vetor) - self.end_idx == 1:
            self._expand(self.exp_ix)
        self.vetor[self.end_idx+1] = item
        self.end_idx += 1

    def removeitem(self,ndx):
        if self.end_idx == -1:
            raise 'empty vetor'
        assert ndx <= self.end_idx

        if ndx == self.end_idx:
            self.vetor[self.end_idx] = None
            # self.end_idx -= 1

        else:
            for i in range(ndx,self.end_idx+1):
                 self.vetor[i] = self.vetor[i+1]

        self.end_idx -= 1

    def insertitem(self,ndx,item):

        assert ndx <= self.end_idx+1
        if len(self.vetor) - self.end_idx == 1:
            self._expand()
        for i in list(range(ndx,self.end_idx+1))[::-1]:
            self.vetor[i+1] = self.vetor[i]

        self.vetor[ndx] = item
        self.end_idx += 1

    def extendvetor(self,othervetor):

        if len(self.vetor) < self.end_idx + othervetor.end_idx +2:
            exnum = (self.end_idx + othervetor.end_idx +2)*2
            self._expand(exnum)

        # print('===============')
        for i in othervetor.vetor[:othervetor.end_idx+1]:
            # print(self.vetor)
            self.appenditem(i)


    def __str__(self):
        return str(self.vetor[:self.end_idx+1])

    def __iter__(self):
        return iter(self.vetor[:self.end_idx+1])


vt = Vetor(5)
assert vt.length() == 5
for i in range(5):
    vt.setitem(i,i)

# print(vt.getitem(4))
vt.appenditem(6)

print(vt)

vt.removeitem(3)
print(vt)

vt.insertitem(4,7)
print(vt)

vt2 = Vetor(7)
for i in range(7):
    vt2.setitem(i,i*10)

vt.extendvetor(vt2)
print(vt.end_idx)
print(vt)

ss = vt.__iter__()
print(ss.__next__())
