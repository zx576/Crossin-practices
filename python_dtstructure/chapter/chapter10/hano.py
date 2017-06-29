# coding=utf-8
'''
The Towers of Hanoi puzzle, invented by the French mathematician Edouard
Lucas in 1883, consists of a board with three vertical poles and a stack of disks. The
diameter of the disks increases as we progress from the top to bottom, creating a
tower structure. The illustration in Figure 10.12 shows the board, the three towers,
and five disks. Any number of disks can be used with the puzzle, but we use five
for ease of illustration.
'''

def move(n, src, dest, temp):
    # print('move({0}, {1}, {2}, {3})'.format(n, src, dest, temp))
    if n >= 1:
        move(n-1, src, temp, dest)
        print("Move %d -> %d" % (src, dest))
        move(n-1, temp, dest, src)

move(1, 1, 3, 2)

'''
汉诺塔递归解法：
简单描述：将 A 上 N 个盘子经过 B 移动到 C。
1、首先考虑最简单的情况，A 柱上只有一个圆盘，这时候只需要将该圆盘从 A --> C 即可。
2、然后考虑 A 柱上有两个圆盘， 这时候需要将第一个圆盘 A --> B ，然后将第二个圆盘 A --> C ,
最后 B --> C，就完成了移动。
3、关键一步，谨记递归的思想是不考虑细节。
4、 现在有 N 个圆盘，我们需要将其分为两部分，第 N 个圆盘和第 N-1 以上的圆盘，比如现在 N=4,
那么就将圆盘分为 [4, (3,2,1)] 两部分，按照第二步中的想法，我们的思想是 (3,2,1) 移动到 B，然后
将 4 移动到 C，最后将(3,2,1) 移动到 C 完成。
5、现在的问题是 (3,2,1) 并不是一个圆盘，我们要将 (3,2,1) 移动到 B，就可以将此抽象为另一个汉诺塔问题，
将 A 上 N-1 个盘子经过 C 移动到 B。

解法：
所有的递归问题都由两部分组成: 基础情况 和 递归情况
基础情况简单来说就是该递归函数的终点。
递归情况就是该递归函数继续递归的条件。

汉诺塔的基础情况就是 A 上只有一个圆盘时，将 A 移动到 C
递归情况就是 A 上有不止一个圆盘，需要把该(些)圆盘经过 C 移动到 B

'''
# 将 N 个圆盘从 A 经过 BUFFER 移动到 C
def hano(n, A, buffer, C):
    # 基础情况
    if n == 1:
        print('%s --> %s'%(A,C))
    # 递归情况
    else:
        # 将前 n-1 个圆盘从 A 经过 C 移动到 buffer
        hano(n-1, A, C, buffer)
        # 将第 n 个圆盘从 A 移动到 C
        hano(1, A, buffer, C)
        # 将前 n-1 个圆盘从 B 经过 A 移动到 C
        hano(n-1, buffer, A, C)
