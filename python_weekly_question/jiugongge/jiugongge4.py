import itertools


def get4list(n,total):

    array_n = list(range(1,n*n+1))
    iter_n = itertools.permutations(array_n,n*n)

    for item in iter_n:
        # print(item)
        spt_lst = split_item(n,total,item)
        # print(spt_lst)
        if spt_lst:
            # print(spt_lst)
            res = judge(n,total,spt_lst)
            if res:
                print(res)
                break


def split_item(n,total,item):

    result = []
    m = 0
    k = n
    count = 0
    while count < n:
        lst = item[m:k]
        # print(item,m)
        # print(lst)
        if sum(lst) != total:
            return
        result.append(lst)
        m = m+n
        k = k+n
        count += 1
        # print(m,k,count)

    # print(result)
    return result


def judge(n,total,lst):

    t1 = [lst[row][row] for row in range(len(lst))]
    t2 = [lst[row][len(lst)-row-1] for row in range(len(lst))]
    if sum(t1) != total or sum(t2) != total:
        return
    for li in zip(*lst):
        # print(li)
        if sum(li) != total:
            return

    return lst

def main(n):
    total = (1 + n*n) * n / 2
    get4list(n,total)


main(4)
