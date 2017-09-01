# coding = utf-8


def rotate2(matrix):
    """
    :type matrix: List[List[int]]
    :rtype matrix: List[List[int]]
    """
    length = len(matrix)
    for i in range(int(length/2)):
        count = 0
        for j in range(i,length-1-i):

            matrix[i][j], matrix[i+count][length-i-1], matrix[length-i-1][length-j-1], matrix[length-j-1][i] = \
            matrix[length-j-1][i], matrix[i][j], matrix[i+count][length-i-1], matrix[length-i-1][length-j-1]

            count += 1
    return matrix


def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype matrix: List[List[int]]
    """

    return zip(*matrix[::-1])

'''
本题目

'''
