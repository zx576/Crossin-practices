
def pair(x,y):
    def get(n):
        if n == 0:
            return x
        elif n == 1:
            return y

    return get


def select(p,n):
    return p(n)

p = pair(20,13)
print(select(p,1))
