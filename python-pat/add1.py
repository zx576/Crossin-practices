

def add1(lst):
    num = ''.join([str(i) for i in lst])
    num = int(num) + 1
    new_l = [i for i in str(num)]
    new = ' '.join(new_l)
    return new


lst = [7 for i in range(1000)]
print(add1(lst))


