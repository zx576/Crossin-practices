
empty = 'empty'

def is_linked(x):
    return x == empty or (len(x)==2 and is_linked(x[1]))

def link(first,rest):
    assert is_linked(rest)
    return [first,rest]

def first(s):
    assert is_linked(s)
    assert s != empty
    return s[0]

def rest(s):
    assert is_linked(s)
    assert s != empty
    return s[1]

four = link(1, link(2, link(3, link(4, empty))))
print(first(four))
print(rest(four))
