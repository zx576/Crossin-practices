#-*- coding:utf-8 -*-
def level_num(x,init_num = 0):
    '''
    func:返回一个数的逆序

    x - 需要被处理的数
    init_num - x的逆序数，初始为0

    level_num(123)
    >>>321
    '''
    if x < 10:
        return init_num*10+x
    else:
        return level_num(x//10,init_num*10+x%10)

def compare(pre_num,after_num):
    '''比较两个数是否相同'''
    if pre_num == after_num:
        return True
    else:
        return False

def accumulate(x,init_sum=0):
    '''
    func - 返回一个数的各位数之和

    x - 需要被处理的数，初始为0
    init_sum - 和

    accumulate(15)
    >>>6

    '''
    if x < 10:
        return init_sum+x
    else:
        return accumulate(x//10,init_sum+x%10)

def main(n):
    '''
    func - 寻找 10000 到 1000000 之间满足各位数之和为 n 的回文数
    n - 预先定义的各位数之和

    main(52)
    >>>
    899998
    989989
    998899
    '''
    for i in range(10000,1000000):
        # 找到 i 的逆序数
        level_i = level_num(i)
        # 确定回文数
        if compare(i,level_i):
            # 获得各位数之和
            level_sum = accumulate(i)
            # 判断各位数之和为 n
            if compare(level_sum,n):
                print(i)
if __name__ == '__main__':
    main(52)
