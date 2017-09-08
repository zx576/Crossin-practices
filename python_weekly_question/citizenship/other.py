# coding=utf-8


# _ = [print(i) for p in __import__('itertools').permutations('美俄德法意英') if all([p[0] not in "美俄德法", p[1] not in "德美", p[2] not in "美俄德意法", p[4] not in "美俄德", p[5] not in "德"]) for i in zip('ABCDEF', p)]
import random

list1 = ['A', 'B', 'C', 'D', 'E', 'F']
list2 = ['Am', 'Ge', 'En', 'Fr', 'Ru', 'It']

while True:
    random.shuffle(list2)
    
    if list2[list1.index('A')] not in ['Am', 'Ge', 'Ru']: pass
    else: continue
    
    if list2[list1.index('E')] not in ['Am', 'Ge', 'Ru']: pass
    else: continue

    if list2[list1.index('C')] not in ['Am', 'Ge', 'Ru']: pass
    else: continue

    if list2[list1.index('B')] != 'Ge' and list2[list1.index('F')] != 'Ge': pass
    else: continue

    if list2[list1.index('A')] != 'Fr' and list2[list1.index('C')] != 'It': pass
    else: continue

    if list2[list1.index('B')] != 'Am' and list2[list1.index('C')] != 'Fr':
        print(list2)
        break
    else: continue