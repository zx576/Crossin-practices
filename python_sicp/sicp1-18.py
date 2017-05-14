'''
练习1.18
'''
def double(n):
    return n*2
# print(double(2))

def halve(n):
    return n/2

def multi(b,n,result=0):
    if n == 0:
        return result
    elif n % 2 == 0:
        return multi(double(b),halve(n),result)
    else:
        return multi(b,n-1,result=result+b)

print(multi(2,11))
