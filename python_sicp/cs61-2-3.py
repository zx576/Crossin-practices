
def tree(root,branches=[]):
    print('this is first',root,branches)
    for branch in branches:
        print('this is branch',branch)
        assert is_tree(branch),'branches must be tree'
        print('assert ok',branch)
    print('this is root',[root]+list(branches))
    return [root]+list(branches)


def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False

    for branch in branches(tree):
        if not is_tree(branch):
            return False

    return True

def is_leaf(tree):
    return not branches(tree)

# t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
#
# print(t)

# for i in []:
#     print('insert loop')
#     print('this is i',i)
#
# t2 = tree(3,[tree(2)])
# print(t2)
# print(is_tree([]))


def fib_tree(n):
    if n ==0 or n ==1 :
        return tree(n)

    else:
        left,right = fib_tree(n-2),fib_tree(n-1)
        fib_n = root(left) + root(right)
        return tree(fib_n,[left,right])

empty = 'empty'

def is_link(s):
    return s == empty or (len(s) == 2 and is_link(s[1]))


def link(first,rest):
    assert is_link(rest)
    return [first,rest]

def first(s):
    print('this is first')
    assert is_link(s)
    assert s != empty
    return s[0]


def rest(s):
    print('this is rest')
    assert is_link(s)
    assert s != empty
    return s[1]

# four = link(1, link(2, link(3, link(4, empty))))
# print(first(four))

def len_link(s):
    length = 0
    while s != empty:
        s,length = rest(s),length+1
    return length

def getitem_link(s,i):
    while i > 0:
        s,i = rest(s),i-1

    return first(s)

















########################################################
