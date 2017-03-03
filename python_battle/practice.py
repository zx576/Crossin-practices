#-*- coding:utf-8 -*-
# import io
# import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
# l0 = [[1,2], [2,3,4], [3,4]]
# for x in l0:
#     print(x)
#     print(x[0])
#     print(x[1])
#     print(x[0]*x[1])
#
# l1 = [(1,2),(3,4),(5,6),(7,8)]
# l2 = [5,6,7,8]
# for i in zip(l1,l2):
#     print(i)
# >>>
# ((1, 2), 5)
# ((3, 4), 6)
# ((5, 6), 7)
# ((7, 8), 8)

# if userinput == 'cls':
#     func1()
#
# elif userinput == 'bck':
#     func2()
# import random
# a = [random.randint(1, 16), sorted(random.sample(range(1, 34), 6))]
# print(a)


list = []
def f2(nums):
    if len(nums) == 0:
        return nums
    nums.remove(min(nums))
    return nums

print(f2(list))


def create_cards():
    '''生成一副手牌'''

    cards = ['j','j','j']
    return cards
def player_cards_n(n):
    dict = {}
    player = 'player'
    for i in range(n):
        dict[player+str(i)] = create_cards()
    print(dict)

print(player_cards_n(5))


def players_cards():
    player1 = create_cards()
    player2 = create_cards()
    ...
    playern = create_cards()



############
