# coding=utf-8
'''
今天这题，看起来挺简单，实际写出来并不容易。在以前公司我曾把它做过招聘的笔试题，结果惨不忍睹，不得不拿掉。
输出如图的螺旋矩阵：
 1   2   3   4
12  13  14   5
11  16  15   6
10   9   8   7
附加题：
输入一个正整数 N，输出以 N 为边长的螺旋矩阵。（比如上图就是 N 为 4 的结果）
'''

'''
解题思路：

1、由图可知，螺旋数组中的数字运动方向依次 右--> 下 --> 左 --> 上 --> 右 这样的循环，在合适的条件下变换累加方向即可。
2、 1 中变换方向的条件有两个，一是遇到数组边界；二是下一位置被其他数占据。


'''


class Spiral:

    def __init__(self, N):

        # 构造一个二维数组
        self.matrix = [[None for i in range(N)] for j in range(N)]
        # 起始行列数
        self.row = 0
        self.col = 0
        # 数组的边界值
        self.max_row = N
        # 更换方向的标记
        self.mark = 0

    # 按需取出数组运动方向
    def derection(self, mark):
        around = [
                [self.row, self.col+1],  # 向右
                [self.row+1, self.col],  # 向下
                [self.row, self.col-1],  # 向左
                [self.row-1, self.col]   # 向上
                ]
        return around[mark%4]

    # 针对目前位置，获取下一位置的 行列 数
    # 下一位置为边界则更换方向
    # 下一位置已经有元素则更换方向
    def next(self):
        # 下一位置
        i = self.derection(mark=self.mark)
        # 判断是否更换方向，不更换则更新 self.row / self.col
        if -1 not in i and self.max_row not in i:
            if self.matrix[i[0]][i[1]] is None:
                self.row,self.col = i
                return None
        # 更换方向
        self.mark += 1
        return self.next()


    def solution(self):
        # 逐一取出 1 到 n^2 值
        for i in range(1,self.max_row**2+1):
            # 按行列赋值
            self.matrix[self.row][self.col] = i
            # 退出条件
            if i == self.max_row**2:
                break
            # 更新行列值
            self.next()

        # 打印结果
        for r in self.matrix:
            for c in r:
                print('{0:^{1}}'.format(c,self.max_row), end=' ')

            print('\n')

if __name__ == '__main__':
    n = int(input('>>>'))
    s = Spiral(n)
    s.solution()


'''
wuxiaojiao同学的代提交答案中最短的 http://paste.ubuntu.com/24955910/
徐大龙同学的代码使用了 numpy 库 https://github.com/PeytonXu/learn-python/blob/master/cases/helix_matrix/helix_matrix.py

'''
