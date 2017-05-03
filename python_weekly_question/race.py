import random
import itertools

tianji = [1,3,5,7,9]
gongzi = [2,4,6,8,10]

#
# t.remove(9)
#
# print(t)
#
#
# for ti in t:
#     for qi in q:
#         yield (ti,qi)


# t_l = list(itertools.permutations(q,len(q)))
# print(t_l)

def fj2(g,t):

    gongzi_l = list(itertools.permutations(g))
    print(len(gongzi_l))
    res_all_turns = []
    for i in gongzi_l:
        res_one_turn = []
        for horses in zip(i,t):
            if horses[0] > horses[1]:
                res_one_turn.append('lose')
            else:
                res_one_turn.append('win')

        if res_one_turn.count('win') >= 3:
            res_all_turns.append('win')

    return len(res_all_turns)


print(fj2(gongzi,tianji))

# import itertools
# def fujia2(gz,tj):
#     '''
#     现在将马分为 优、上、中、下、劣 五等，五局三胜制，抽象为列表[2,4,6,8,10] 与 [1,3,5,7,9] ，
#     其他条件不变，计算出田忌有多少种赢得比赛的可能。
#     '''
#     win_time = 0
#     gz_l = list(itertools.permutations(gz,len(gz)))
#     tj_l = list(itertools.permutations(tj,len(tj)))
#     for i in gz_l:
#         for j in tj_l:
#             if fujia2_win(i,j):
#                 win_time += 1
#                 print(i,"<--",j)
#     print("Tj win %s" %win_time)
# def fujia2_win(g,t):
#     n = 0
#     for i in range(len(g)):
#         if t[i] > g[i]:
#             n += 1
#     if n >= 3:
#         return True
#     else:
#         return False
#

#
# gz = [2,4,6,8,10]
# tj = [1,3,5,7,9]
# fujia2(gz, tj)















#
# g = [3,6,9]
# t = [2,5,8]
#
# def q1(g,t):
#
#     g.sort(reverse=True)
#     t.sort(reverse=True)
#
#     return [(g[0],t[2]),(g[1],t[0]),(g[2],t[1])]
#
# # print(q1(g,t))
#
#
# def tianji(t):
#     random.shuffle(t)
#     return t
#
#
# # def gongzi(g,last_turn=''):
# #     if not last_turn:
# #         return 9
# #
# #     elif last_turn == 8:
# #         return 6
# #
# #     elif last_turn == 5:
# #         return 3
# #
# #     elif last_turn == 2:
# #         return 3
#
# def gongzi(g,last_turn=''):
#     if not last_turn:
#         return 3
#
#     elif last_turn == 8:
#         return 6
#
#     elif last_turn == 5:
#         return 9
#
#     elif last_turn == 2:
#         return 3
#
# # def
#
# def calc(n):
#     resu = []
#     for i in range(n):
#         last_turn = ''
#         res = []
#         new_l = tianji(t)
#         for j in new_l:
#             # last_turn =
#             result = gongzi(g,last_turn) - j
#             if result > 0:
#                 res.append('win')
#
#             else:
#                 res.append('lose')
#
#             last_turn = j
#         # print(res)
#         if res.count('win') == 2:
#             resu.append('win')
#
#     rate = resu.count('win')/n
#
#     return rate
#
# # print(calc(10000))
#
# # print(tianji(t))
#
#
