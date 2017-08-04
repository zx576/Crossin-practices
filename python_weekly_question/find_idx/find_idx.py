# 寻找插入位置

# 题目描述

'''
给定一个升序排列的整数集 nums 和一个整数 target,
寻找 target 在 nums 中的位置
如果 nums 中存在 target 则返回该索引
例 ： nums=[1,2,3] target=2  >>> 1
如果不存在，则按照升序返回 target 插入位置的索引
例 ： nums=[1,5,9] target=7  >>> 2
'''

def find_idx(nums, target):
    '''
    :type nums: list
    :type target: int
    rtype : int
    '''

    # your code


assert find_idx([], 2) == 0
assert find_idx([2,3,4], 1) == 0
assert find_idx([2,3,4], 3) == 1
assert find_idx([3,5,9], 7) == 2
assert find_idx([7,8,9], 11) == 3


'''
推荐 strawhat 同学的答案，思路清新，程序中各部分功能独立，非常好理解
strawhat￼: http://pastebin.ubuntu.com/25147394/
同时也给出其他两位同学的答案
疯琴： https://github.com/YngwieWang/python_practice/blob/master/AmericanCaptain.py
xuxiaojiao: http://pastebin.ubuntu.com/25160891/

'''