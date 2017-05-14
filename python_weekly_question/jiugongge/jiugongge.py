import itertools

def ngonge(n,total):
    # total = (1 + n*n) * n / 2
    list1 = list(range(1,n*n+1))
    all_list = itertools.permutations(list1,n)
    meet_list = []
    for i in all_list:
        # print(i)
        if sum(i) == total:
            meet_list.append(i)
    # print(len(meet_list))
    return meet_list


def choose_1(n,meet_list):

    dct = {}
    count = 0

    for m in meet_list:
        # print(m)
        require_l = []
        require_l.append(m)
        new_n = n
        while new_n > 1:
            for i in meet_list:
                if compare(i,require_l):
                    require_l.append(i)
                    new_n -= 1
                    break
                else:
                    continue


        if len(require_l) == n:
            # print(dct)
            # print(require_l)
            dct['cnt'+str(count)] = require_l
            count += 1

        # break

    # print(dct)
    return dct

def compare(l1,l2):
    set1 = set(l1)
    # set2 = set(l2)
    for lst in l2:
        setn = set(lst)
        # print
        if set1&setn:
            return False

    return True





def handle(n,total,dct):
    for value in dct.values():
        oders = itertools.permutations(value)
        for oder in oders:
            res = judge(n,total,oder)
            if res:
                print(res)



def judge(n,total,lst):

    t1 = [lst[row][row] for row in range(len(lst))]
    t2 = [lst[row][len(lst)-row-1] for row in range(len(lst))]
    if sum(t1) != total or sum(t2) != total:
        return
    for li in zip(*lst):
        print(li)
        if sum(li) != total:
            return

    return lst


def main(n):
    total = (1 + n*n) * n / 2
    mt_lst = ngonge(n,total)
    dct = choose_1(n,mt_lst)
    handle(n,total,dct)


main(3)






    #
    # # for j in meet_list:
    # all_meet_list = itertools.permutations(meet_list,n)
    # for i in all_meet_list:
    #     if i[0][0] in i[1]:
    #         continue
    #     # print(i)
    #     t1 = [i[row][row] for row in range(len(i))]
    #     t2 = [i[row][len(i)-row-1] for row in range(len(i))]
    #     # print(t1)
    #     # print(t2)
    #     if sum(t1) != total or sum(t2) != total:
    #         continue
    #
    #
    #     res = [m for m in zip(*i) if sum(m) == total]
    #     if len(res) == n:
    #         print(i)

# ngonge(4)
