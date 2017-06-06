# coding : utf-8

def merge2list(lsta,lstb):

    new_lst = []
    a_idx, b_idx = 0, 0

    while True:

        if a_idx == len(lsta):
            new_lst.extend(lstb[b_idx:])
            break

        elif b_idx == len(lstb):
            new_lst.extend(lsta[a_idx:])
            break

        if lsta[a_idx] >= lstb[b_idx]:
            new_lst.append(lstb[b_idx])
            b_idx += 1

        else:
            new_lst.append(lsta[a_idx])
            a_idx += 1


    return new_lst


lst1 = [1,3,5,7,9,11]
lst2 = []
print(merge2list(lst1,lst2))
