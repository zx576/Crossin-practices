# import itertools
#
# tianji = [1,3,5,7,9]
# qiwang = [2,4,6,8,10]
#
# def fj2(qiwang,tianji):
# 	# 获取田忌所有派遣马匹的方式
#     tianji_l = list(itertools.permutations(tianji,len(tianji)))
# 	# 全部赛果
#     res_all_turns = []
#     # 遍历所有的方式
#     for i in tianji_l:
# 	    # 某一轮的比赛结果
#         res_one_turn = []
#         # 某一轮比拼中，双方马匹对阵情况
#         for horses in zip(i,qiwang):
#             if horses[0] < horses[1]:
#                 res_one_turn.append('lose')
#             else:
#                 res_one_turn.append('win')
#         if res_one_turn.count('win') >= 3:
#             res_all_turns.append('win')
#     return len(res_all_turns)
#
# print(fj2(qiwang,tianji))

a = 1
if a == 2:
    print('x')
else:
    print('y')
