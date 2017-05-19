


f=open('report.txt','r',encoding='utf-8')
zong=[]
sum =0
for line in f.readlines():
    line = line.split()
    for i in line[1:10]:
        sum = sum + int(i)
    line.append(sum)
    line.append(round(sum/9.0,1))
    zong.append(line)
    sum = 0

d

zong.sort(key= lambda x:x[-2])
zong = zong[::-1]
print(zong)


# 索引 zong 的每一行
for row_idx in range(len(zong)):
    print(zong[row_idx])  #  ['小沈', '94', '95', '72', '86', '78', '78', '43', '95', '96', 737, 81.9]
    # 索引每一行中的每个元素, 去掉姓名 和 总分平均分
    for item_idx in range(1,len(zong[row_idx])-2):
        print(zong[row_idx][item_idx]) # 94
        if int(zong[row_idx][item_idx]) < 60:
            zong[row_idx][item_idx] = '不及格'



print(zong)

# pj=[]
# for i in range(1,12):
#     sum = 0.0
#     for j in range(len(zong)):
#         sum = sum + int(zong[j][i])
#     pj.append(round(sum/len(zong),1))
#
# print(pj)
# print pj
# for i in zong:
#     for j in i:
#         print j,
