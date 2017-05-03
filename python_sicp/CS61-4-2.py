#-*- coding:utf-8 -*-

class LetterIter:
    def __init__(self,start='a',end='e'):
        self.next_letter = start
        self.end   = end

    def __next__(self):
        if self.next_letter == self.end:
            raise StopIteration

        letter = self.next_letter
        self.next_letter = chr(ord(letter)+1)

        return letter


class Letter:
    def __init__(self,start='a',end='e'):
        self.start = start
        self.end   = end

    def __iter__(self):
        return LetterIter(self.start,self.end)

# b_to_k = Letter('b','k')
#
# first_iterator = b_to_k.__iter__()
#
# for i in range(5):
#     print(next(first_iterator))

# caps = list(map(lambda x : x.upper(),b_to_k))
# print(caps)

#
# let = LetterIter()
# for i in range(5):
#     print(let.__next__())


###

# counts = [1,2,3,4,5]
# counts = counts.__iter__()
# try:
#     while True:
#         next_num = counts.__next__()
#         print(next_num)
# except:
#     raise StopIteration

def letters_gernerator():
    current = 'a'
    while current < 'd':
        yield current
        current = chr(ord(current)+1)

# for i in letters_gernerator():
#     print(i)
class Stream:
    class empty:
        def __repr__(self):
            return 'Stream empty'

    empty = empty()
    def __init__(self,first,compute_rest=lambda:empty):
        assert callable(compute_rest),'compute_rest must be callable'
        self.first = first
        self._compute_rest = compute_rest

    @property
    def rest(self):
        if self._compute_rest is not None:
            self._rest = self._compute_rest()
            self._compute_rest = None

        return self.rest

    def __repr__(self):
        return 'Stream({0},<...>)'.format(repr(self.first))

# r = Link(1,Link(2+3,Link(9)))

s = Stream(1,lambda:Stream(2+3,lambda:Stream(9)))
print(s.first)
print(s.rest)
# from lo



##############3
