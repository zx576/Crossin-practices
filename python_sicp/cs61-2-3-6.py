def tree(root,branches=[]):
    for branch in branches:
        assert is_tree(branch),'branches must be trees'
    return [root] + list(branches)

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in tree:
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

t = tree(3,[tree(1),tree(2,[tree(1),tree(1)])])
# print(t)




def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)

    else:
        left,right = fib_tree(n-2),fib_tree(n-1)
        fib_n = root(left)+root(right)
        return tree(fib_n,[left,right])


print(fib_tree(5))













        ################
