


'''
nums - 存数据的列表
sum - 求和的结果，最开始为0
'''
nums = [23,40,25,56,6,8]
sum = 0
for n in nums:
    '''
    for n in nums:表示从 nums 这个列表中逐一获取其中元素
    sum = sum + n:表示将 nums 中的元素逐一加起来，
            得到的结果赋给 sum 变量
    if sum > 100 break: 表示如果加起来的综合超过100了
                        就执行 if 下面break ，跳出循环，不在遍历向 nums 取值了

    '''
    sum = sum + n
    if sum > 100:
        break

print(sum)
