import random

g = [3,6,9]
t = [2,5,8]

def q1(g,t):
    # s1 = (max(g),min(t))
    g.sort(reverse=True)
    t.sort(reverse=True)

    return [(g[0],t[2]),(g[1],t[0]),(g[2],t[1])]

# print(q1(g,t))


def tianji(t):
    random.shuffle(t)
    return t


# def gongzi(g,last_turn=''):
#     if not last_turn:
#         return 9
#
#     elif last_turn == 8:
#         return 6
# 
#     elif last_turn == 5:
#         return 3
#
#     elif last_turn == 2:
#         return 3

def gongzi(g,last_turn=''):
    if not last_turn:
        return 3

    elif last_turn == 8:
        return 6

    elif last_turn == 5:
        return 9

    elif last_turn == 2:
        return 3

# def

def calc(n):
    resu = []
    for i in range(n):
        last_turn = ''
        res = []
        new_l = tianji(t)
        for j in new_l:
            # last_turn =
            result = gongzi(g,last_turn) - j
            if result > 0:
                res.append('win')

            else:
                res.append('lose')

            last_turn = j
        # print(res)
        if res.count('win') == 2:
            resu.append('win')

    rate = resu.count('win')/n

    return rate

print(calc(10000))

# print(tianji(t))
