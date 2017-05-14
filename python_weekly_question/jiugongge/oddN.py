

def oddN(n):
    # 构造二维列表
    lst = [[0 for i in range(n)] for i in range(n)]
    # 初始化列表位置
    x,y = 0,n//2
    for num in range(1,n*n+1):
        lst[x][y] = num
        xa,ya = x-1,y+1
        # 回绕情况
        if xa < 0:
            xa = n-1
        if ya > n-1:
            ya = 0
        # 占位情况
        if lst[xa][ya] != 0:
            x = x + 1
            if x > n-1:
                x = 0
        else:
            x,y = xa,ya
    return lst
#
# lst = oddN(5)
# for row in lst:
#     print(row)


def fourN(n):
    # 初始化列表
    lst = [[i+j for i in list(range(1,n*n+1))[::n]] for j in range(n)]

    # 交换对角线位置
    for i in range(n//2):
        lst[i][i],lst[n-1-i][n-1-i] = lst[n-1-i][n-1-i],lst[i][i]
        lst[i][n-1-i],lst[n-1-i][i] = lst[n-1-i][i],lst[i][n-1-i]

    return lst


def acc(p,lst):
    # print(lst)
    for row in lst:
        for index in range(len(row)):
            row[index] += p

    return lst

def fourNplus2(n):
    m = n//2
    A,B,C,D = oddN(m),oddN(m),oddN(m),oddN(m)
    B = acc(m**2,B)
    C = acc(m**2*2,C)
    D = acc(m**2*3,D)

    for row_index in range(len(A)):
        A[row_index].extend(C[row_index])
        D[row_index].extend(B[row_index])

    matrix = A+D
    t = (n-2)//4
    # 列交换
    for col_index in range(len(matrix[0])):
        if col_index < t or col_index > n-t:
            for row_index in range(len(matrix)//2):
                # print(col_index,row_index+m-1)
                matrix[row_index][col_index] , matrix[row_index+m][col_index] = \
                matrix[row_index+m][col_index],matrix[row_index][col_index]
    # 交换特殊位置
    matrix[t][0],matrix[m+t][0] = matrix[m+t][0],matrix[t][0]
    matrix[t][t],matrix[m+t][t] = matrix[m+t][t],matrix[t][t]

    return matrix


def check(lst,n):
    total = (1 + n*n) * n / 2
    for row in lst:
        assert sum(row) == total,'xx'

    for col in zip(*lst):
        assert sum(col) == total,'xx'

    t1 = [lst[row][row] for row in range(len(lst))]
    t2 = [lst[row][len(lst)-row-1] for row in range(len(lst))]

    assert sum(t1) == sum(t2),'error'

# lst = fourN(8)
# print(lst)
# lst = fourNplus2(18)

lst = oddN(9)
check(lst,9)
