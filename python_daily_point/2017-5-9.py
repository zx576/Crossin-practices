import itertools


l = [1,2,3,4,5,6,7,8,9]

all_l = itertools.permutations(l,3)

p_l = itertools.permutations(l,3)

for i in all_l:
    if sum(i) == 15:
        print(i)


print('===============00')
#
# for j in p_l:
#     print(j)
