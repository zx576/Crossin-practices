# coding=utf-8

'''
The factorial of a positive integer n can be used to calculate the number of permutations of n elements. The function is defined as:
n! = n ∗ (n − 1) ∗ (n − 2) ∗ : : : ∗ 1
'''

def fac(n):
    if n == 1:
        return 1
    else:
        return n*fac(n-1)

# res = fac(5)
# print(res)

def fib(n):
    if n == 1 or n == 0:
        
        return 1
    else:
        return fib(n-1) + fib(n-2)

res2 = fib(5)
print(res2)
