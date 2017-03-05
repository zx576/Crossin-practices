


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

fib = count_frame(fib)
print(fib(19))
# print(fib.opencount)
print(fib.max_count)

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

res = count_factors(578)
print(res)
