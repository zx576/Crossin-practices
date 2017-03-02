#-*- coding:utf-8 -*-

def accumulate(n):
    '''
    func - 返回一个数的各位数之和

    accumulate(15)
    >>>6

    '''
    return sum([int(x) for x in str(n)])

def level_num(n):
    '''
    func:返回一个数的逆序

    level_num(123)
    >>>321
    '''
    return int(str(n)[::-1])

def compare(pre_num,after_num):
    '''比较两个数是否相同'''
    if pre_num == after_num:
        return True
    else:
        return False

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
        # 确定回文数
        if compare(i,level_num(i)):
            # 判断各位数之和为 n
            if compare(accumulate(i),n):
                print(i)

if __name__ == '__main__':
    main(52)
