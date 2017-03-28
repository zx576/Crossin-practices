"""
CrossinWeekly
在不考虑装备重复的情况之下，即可以多次购买一件装备，要填满六格物品栏，有多少种购买方式？
写一个程序，输出所有可行的购买组合。
"""

import itertools

equip_value = [690, 1500, 2100, 1740, 2140, 2080]
cash = 10000
comb_equip = itertools.combinations_with_replacement(equip_value, 6)
result = []
for x in comb_equip:
    if sum(x) <= cash:
        result.append(x)
print('总共有 %d 种可行的购买组合' %len(result))

# 附加题1：如果没有6格物品栏限制，有多少种购买方式？
items = 1
result_bonus1 =[]
while items <= 6:
    comb_equip_bonus1 = itertools.combinations_with_replacement(equip_value, items)
    for x1 in comb_equip_bonus1:
        if sum(x1) <= cash:
            result_bonus1.append(x1)
    items += 1
print('附加题1总共有 %d 种可行的购买组合' %len(result_bonus1))

# 附加题2：在 1 的前提下，影忍之足最多购买一次，现在有多少种购买方式？
items2 = 1
result_bonus2 =[]
while items2 <= 6:
    comb_equip_bonus2 = itertools.combinations_with_replacement(equip_value, items2)
    for x2 in comb_equip_bonus2:
        if sum(x2) <= cash and x2.count(690) == 1:
            result_bonus2.append(x2)
    items2 += 1
print('附加题2总共有 %d 种可行的购买组合' %len(result_bonus2))
# print(result_bonus2)

