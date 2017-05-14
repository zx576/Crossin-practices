import itertools


def ge_lists(n,total):

    array_n = list(range(1,n*n+1))
    iter_n = itertools.permutations(array_n,n)
    dct = {}

    for lst in iter_n:
        for i in range(1,n+1):
            # print(lst)
            if lst[0] == i and sum(lst) == total :
                if str(i) in dct.keys():
                    dct[str(i)].append(lst)
                else:
                    dct[str(i)] = [lst]
            else:
                continue

    print(dct)
    return dct

ge_lists(3,15)


def ge4lists(n,total,dct,ins_l,set_n):

    # pass




def ngongge(n):
    # total = (1 + n*n) * n / 2
    pass
