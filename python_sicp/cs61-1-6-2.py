'''
solution for golden ratio
'''

def impove(update,close,guess=1):
    '''
    abstracts a process which obtain a optimal solution

    update - func,aim to return a new 'guess' if the old one can not meet requirement
    close - func ,aim to judge wheather the program obtain a optimal solution
    guess - value,as a result for the solution,dynamic changed,\
            default is 1 and it could be any integer.

    '''
    while not close(guess):
        guess = update(guess)
    return guess


def golden_update(guess):
    '''
    function - return a new 'guess',here it is for golden ratio
    guess - value,as a value which could not meet the requirement
    '''
    return 1/guess+1

def square_close_to_successor(guess):
    '''
    function - as a judgement depend on what approx_eq returns
                return True if approx_eq return True
    '''
    return approx_eq(guess*guess,guess+1)

def approx_eq(x,y,tolerance=1e-15):
    '''
    function - as a judgement to see if guess is required
    '''
    return abs(x-y) < tolerance

# result = impove(golden_update,square_close_to_successor)
# print(result)

from math import sqrt
'''
test - compare a real phi to caculated value
'''
phi = 1/2 + sqrt(5)/2
def impove_test():
    approx_phi = impove(golden_update,square_close_to_successor)
    assert approx_eq(phi,approx_phi)

# impove_test()

'''
function - solution for square root
'''
def squrt(a):
    def sqrt_update(x):
        return (x+a/x)/2

    def sqrt_close(x):
        return approx_eq(x*x,a)

    return impove(sqrt_update,sqrt_close)

print(sqrt(16))















#.//////////////
