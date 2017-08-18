# coding = utf-8


'''
如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。
解决该问题的核心是实现：一个n位正整数等于其各位数字的n次方之和　
那么我们先写一个程序来判断一个数字是否为阿姆斯特朗数

'''

def judge_arms(i):
    # 将该数转换为列表　123 --> ['1', '2', '3']
    tem = list(str(i))
    # 按照　n位正整数等于其各位数字的n次方　进行求和
    # sum = 1**3 + 2**3 + 3**3
    tem_sum = sum([int(j)**len(tem) for j in tem])
    # 判断求和之后的数是否和原数相等
    if i == tem_sum:
        return True

'''
寻找小于 1000 的　阿姆斯特朗　数
逐一遍历小于 1000 的数
判断是否为阿姆斯特朗数

'''

def arms(N):
    for i in range(1, N+1):
        if judge_arms(i):
            print(i)


# arms(1000)

'''
附加题: 输入一个正整数，输出距离它最近的阿姆斯特朗数。

以指定的数为基准，同时向前向后寻找阿姆斯特朗数
找到即返回该数
'''
def near_arms(N):

    forward, backward = N, N
    while True:
        if judge_arms(forward):
            return forward
        elif judge_arms(backwrad):
            return backwrad

        forward += 1
        backward -= 1


r = near_arms(100000)
print(r)


'''
本期答案精选
王任￼ 同学写的比较精简，参考地址： http://paste.ubuntu.com/25238978/
成仙￼　同学写的比较直观,容易理解，各部分代码清楚：　https://paste.ubuntu.com/25268753/

'''
