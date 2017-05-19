
class Set:

    def __init__(self):
        self.setadt = []


    def __len__(self):
        return len(self.setadt)


    def appenditem(self,item):
        self.setadt.append(item)


    def interset(self,SetB):
        inter = Set()
        for i in self.setadt:
            if i in SetB.setadt:
                inter.appenditem(i)
        return inter


    def union(self,SetB):
        un = Set()
        for i in self.setadt:
            un.appenditem(i)
        for j in SetB.setadt:
            if j in un.setadt:
                continue
            else:
                un.appenditem(j)

        return un


    def difference(self,SetB):
        diff = Set()
        inter = self.interset(SetB)
        un = self.union(SetB)

        for i in un.setadt:
            if i in inter.setadt:
                continue
            else:
                diff.appenditem(i)

        return diff

    def __str__(self):
        return str(self.setadt)

set1 = Set()
set2 = Set()

for i in range(5):
    set1.appenditem(i)

for i in range(3,8):
    set2.appenditem(i)

new_s = set1.difference(set2)

print(new_s)
