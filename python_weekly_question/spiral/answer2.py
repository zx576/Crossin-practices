# https://paste.ubuntu.com/24948175/ 错误
# 队长别开枪aa
# n = input("Input the N: ")
# n = int(n)
n = 3
matrix = [[ 0 for i in range(n)] for i in range(n)]
left = 0
right = n
top = 0
bottom = n
start = 1
while (left <= right) and (top <= bottom):
    for i in range(left,right):
        matrix[top][i] = start
        start += 1
    for i in range(top+1, bottom - 1):
        matrix[i][right - 1] = start
        start += 1
    if top!=bottom:
        for i in range(right - 1, left - 1, -1):
            matrix[bottom - 1][i] = start
            start += 1
    if left != right:
        for i in range(bottom - 2, top, -1):
            matrix[i][left] = start
            start += 1
    left += 1
    right -= 1
    top += 1
    bottom -= 1
for i in matrix:
    print(i)
