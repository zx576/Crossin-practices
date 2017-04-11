


def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0

    else:
        return fib(n-1)+fib(n-2)

def count_frame(f):
    def counted(*args):
        counted.opencount += 1
        counted.maxcounted = max(counted.max_count,counted.opencount)
        result = f(*args)
        counted.opencount -= 1
        return result
    counted.max_count = 0
    counted.opencount = 0
    return counted

# fib = count_frame(fib)
# print(fib(19))
# print(fib.opencount)
# print(fib.max_count)

################################
from math import sqrt
def count_factors(n):
    sqrt_n = sqrt(n)
    k,factors = 1,0
    while k < sqrt_n:
        print(factors)
        if n % k == 0:
            factors += 2
        k += 1

    if k**2 == n:
        factors += 1

    return factors

# res = count_factors(578)
# print(res)


##############################
class Link():
    empty = ()
    def __init__(self,first,rest=empty):
        assert rest is Link.empty or isinstance(rest,Link)
        # print(first,rest)
        self.first = first
        self.rest = rest
    def __getitem__(self,i):
        if i == 0 :
            return self.first

        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)

def link_expression(s):
    if s.rest is Link.empty:
        rest = ''
    else:
        rest = '' + link_expression(s.rest)
    return 'Link({0},{1})'.format(s.first,rest)


c = Link(5,Link(4,Link(3)))

# print(c)

# print(link_expression(c))

# Link.__repr__ = link_expression
# print(c)


# s_first = Link(c,Link(6))
# print(s_first)

def extend_link(s,t):
    if s is Link.empty:
        return t
    else:
        return Link(s.first,extend_link(s.rest,t))

# print(extend_link(c,c))

class Tree:
    def __init__(self,entry,branches=()):
        self.entry = entry
        # for branch in branches:
        #     assert isinstance(branches,Tree)
        self.branches = branches
    def __repr__(self):

        if self.branches:
            return 'Tree({0},{1})'.format(self.entry,repr(self.branches))
        else:
            return 'Tree({0})'.format(repr(self.entry))

    def is_leaf(self):
        return not self.branches

def fib_tree(n):
    if n == 1:
        return Tree(0)

    elif n == 2:
        return Tree(1)

    else:
        # print('this is %s'%n,fib_tree(4).entry)
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        print('this is %s'%n,left.entry,right.entry,left)
        return Tree(left.entry+right.entry,(left,right))

# print(fib_tree(1).entry)
print(fib_tree(5).entry)



#########################################
