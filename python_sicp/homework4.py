#question1

def make_counter():
    dct = {}
    def counter(x):
        dct[x] = dct.get(x,0) + 1
        return dct[x]
    return counter


c = make_counter()
c('a')
c('b')
# print(c('c'))


# question2

def make_fib():
    fib_num = 0
    next_num = 1
    def fib():
        nonlocal fib_num
        nonlocal next_num
        next_num,fib_num = next_num+fib_num,next_num
        return fib_num

    return fib
f = make_fib()
print(f())
print(f())
print(f())
print(f())
