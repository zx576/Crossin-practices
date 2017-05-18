
ss = [1,2,3,4,5,6,7,8]

every_3 = [[ss[i] for i in range(j,j+3)] for j in range(len(ss)-2) ]

print(every_3)
