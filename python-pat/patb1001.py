
def func(n,i):
    # global count
    if not n == i:
        quchong(n)
    if n == 1:
        return
    elif n % 2 == 0:
        return func(n/2,i)
    elif n % 2 == 1:
        return func((3*n+1)/2,i)

def quchong(n):
    global u_input
    u_input = u_input - {n}
u_input = {3,4,6,7,9,10,5,8,12,34,56,78}
def main():
    for i in u_input:
        func(i,i)
    return u_input

print(main())
