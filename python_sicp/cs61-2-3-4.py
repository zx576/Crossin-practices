
def right_binarize(tree):
    if is_leaf(tree):
        return tree
    if len(tree)>2:
        tree = [tree[0],tree[1:]]

    return [right_binarize(b) for b in tree]

tree = [1,2,3,4,5,6,7]
print(right_binarize(tree))
