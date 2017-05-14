
class Link:
    empty = ()
    def __init__(self,first,rest=empty):
        assert rest is Link.empty or isinstance(rest,Link)
        self.first = first
        self.rest = rest

    def __getitem__(self,i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1+len(self.rest)

# s = Link(3, Link(4, Link(5)))
# print(len(s))
# print(s.__getitem__(2))
# print(s.__len__())

class Tree:
    def __init__(self,entry,branches=()):
        self.entry = entry
        for branch in branches:
            assert isinstance(branch,Tree)

        self.branches = branches
    def __repr__(self):
        if self.branches:
            return 'Tree(%r,%r)'%(self.entry,repr(self.entry))
        else:
            return 'Tree(%r)'%(repr(self.entry))

    def is_leaf(self):
        return not self.branches

def fib_tree(n):
    if n == 1:
        return Tree(0)
    elif n == 2:
        return Tree(1)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        return Tree(left.entry+right.entry,(left,right))


# print(fib_tree(5))
def empty(s):
    return s in Link.empty

def set_contains(s,v):
    if empty(s):
        return False

    elif s.first == v:
        return True

    else:
        return set_contains(s.rest,v)

s = Link(4, Link(1, Link(5)))
print(set_contains(s,2))

















####################################################
