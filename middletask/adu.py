# -*- coding: utf-8 -*-
#读取数据
with open("report.txt",'r',encoding='utf-8') as f:
     r1 = f.readlines()

#计算每一科的平均成绩，平均值总分，总平均分
AVG = []
for i in range(0,9):
    avg = 0
    for r in r1:
        temp = r.split()
        res = temp[1:]
        avg= avg + int(res[i])
    avg = round(float(avg)/len(r1),1)
    AVG.append(avg)
SUM = 0
for x in AVG:
    SUM = SUM + x
AVG_Z = round(float(SUM)/len(AVG),1)
AVG.append(SUM)
AVG.append(AVG_Z)
AVG.insert(0,'平均')

# 计算总成绩和平均成绩，将低于60的分数替换为“不及格”
result = []
for r in r1:
    sum = 0
    line = r.split()
    for i in line[1:]:
        sum += int(i)
        if int(i) < 60:
            line[line.index(i)] = '不及格'
    line.append(sum)
    line.append(round(float(sum)/9,1))
    result.append(line)

#按总成绩（或平均分）排序
result.sort(key=lambda x:x[-1],reverse=True)

#添加名次
result.insert(0,AVG)
fin_result=[]
rank = 0
for k in result:
    k.insert(0,rank)
    rank += 1
    fin_result.append(k)

#将结果写入文件，注意先添加一行项目名
with open('report_result.txt', 'w') as fin:
    fin.write('名次  姓名  语文  数学  英语  物理  化学  生物  政治  历史  地理  总分  平均分\n')
    for m in fin_result:
        for n in m:
            fin.write(str(n).center(6,' '))
        fin.write('\n')
