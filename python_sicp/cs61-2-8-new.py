
#
# @count
def fib(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fib(n-1)+fib(n-2)

def count(f):
    def counted(*args):
        counted.call_count += 1
        return f(*args)

    counted.call_count = 0
    # print(counted.)
    return counted

fib = count(fib)

print(fib(19))
print(fib.all_count)
