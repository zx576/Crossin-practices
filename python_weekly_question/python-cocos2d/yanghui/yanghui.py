
# 杨辉三角形

def yanghui_lst(n):
    res = []
    for i in range(n):
        if i < 2:
            row = [1 for j in range(i+1)]

        else:
            last_row = res[-1]
            new_row = list(map(lambda i :last_row[i]+last_row[i+1],range(len(last_row)-1)))
            row = [1] + new_row + [1]

        res.append(row)

    print(res)
    return res

# print(yanghui_lst(5))


def yanghui(m,n):

    yh_lst = yanghui_lst(m)
    num = yh_lst[-1][n]

    print(num)
    return num

yanghui(5,1)
