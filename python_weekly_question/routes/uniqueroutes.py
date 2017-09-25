#coding=utf-8

def uniquePath(m, n):
    '''
    :type m: int
    :type n: int
    :rtype: int
    '''

    matrix = [[1 for i in range(m)] for j in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]

    return matrix[-1][-1]


assert uniquePath(1, 2) == 1
assert uniquePath(3, 3) == 6
assert uniquePath(10, 20) == 6906900
