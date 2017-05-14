# -*- coding: utf-8 -*-
# 2017/02/16 12:17 begin
# 2017/02/18 00:27 end

score_file = open('report.txt')
score_file_read = score_file.readlines()
score_file.close


results = []
lst_n = []

for line in score_file_read:
    data = line.split()
    sum = 0
    avg_s = 0
    for score in data[1:]:
        sum += int(score)
        avg_s += 1
        # print sum
    avg_tmp = float(sum) / avg_s
    avg = '%.1f' % (avg_tmp)
    data.append(str(sum))
    data.append(avg)
    lst_n.append(data)

lst_n.sort(key=lambda x:x[-2],reverse=True)

score_new_file = open('score_new.txt','w')
head = '名次 姓名 语文 数学 英语 物理 化学 生物 政治 历史 地理 总分 平均分'
score_new_file.write((head)+'\n')
num = 0
for i in lst_n:
    num += 1
    i.insert(0,str(num))
    b = '   '.join(i)
    print(b)
    score_new_file.write((b)+'\n')
