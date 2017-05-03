import copy
import itertools

# def product(n):
#     list_n = list(str(n))
#
#     # res_stage1 = []
#     max_num = 0
#     for i in range(1,len(list_n)):
#         new_l = copy.copy(list_n)
#         new_l.insert(i,'*')
#         res_in_turn = eval(''.join(new_l))
#         if res_in_turn > max_num:
#             max_num = res_in_turn
#         # res_stage1.append(new_l)
#     # print(res_stage1)
#     # res_stage2 = []
#     # for j in res_stage1:
#     #     res_in_turn = eval(''.join(j))
#     #     res_stage2.append(res_in_turn)
#
#     # return max(res_stage2)
#     return max_num
#
#
# print(product(1234568976446876432690))
#
# def product_2(n):
#     str_n = str(n)
#     all_cond = itertools.permutations(str_n)
#     all_res = []
#     for cond in all_cond:
#         num = int(''.join(cond))
#         res_one_turn = product(num)
#         all_res.append(res_one_turn)
#
#     return max(all_res)
#

# print(product_2(123456))

### =====================
#
# def product(num):
#     # 数字转为字符串
#     num2str = str(num)
#     # 预设最大的结果
#     max_num = 0
#     len_str = len(num2str)
#
#     for i in range(1,len_str):
#         # 分别得到字符串两边
#         left = num2str[:i]
#         right = num2str[i:]
#         res = int(left) * int(right)
#         # 如果现在的乘积超过目前的乘积，则更新最大值
#         if res > max_num:
#             max_num = res
#
#     return max_num
#

def product_2(num):
    num2str = str(num)
    max_num = 0
    for n in itertools.permutations(num2str):
        mixnumber = "".join(n)
        res = product(int(mixnumber))
        if res > max_num:
            max_num = res
    return max_num


def product(num):
    # 转为字符串并获取长度
    len_str = len(str(num))
    # 预设最大值
    max_num = 0
    for i in range(1,len_str):
        # 分别得到数字两边
        left = num//(10**i)
        right = num%(10**i)
        res = left * right
        # 判断是否更新
        if res > max_num:
            max_num = res
    return max_num


print(product_2(123456))
