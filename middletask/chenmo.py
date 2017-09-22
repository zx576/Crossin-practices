#1.读取 report.txt 文件中的成绩；
scores=[]
f=open('report.txt')
for line in f.readlines():
    # print(line)
    s=line.split()
    scores.append([s[0]]+[int(i) for i in s[1:]])
f.close()
# print(scores)

#2.统计每名学生总成绩、计算平均并从高到低重新排名；
totalScores=[[x[0],sum(x[1:])] for x in scores]
print(sorted(totalScores,key=lambda x: x[1]))
avgScores=[[x[0],round((sum(x[1:]))/9,1)] for x in scores]
print(sorted(avgScores,reverse=True,key=lambda x: x[1]))


#3.汇总每一科目的平均分和总平均分（见下表第一行）；
with open('scores.txt','w') as f:
    f.writelines('姓名\t语文\t数学\t英语\t物理\t化学\t生物\t政治\t历史\t地理\t总分\t平均分\n')
    #计算每科总分和平均分
    courseAvg = []
    for j in range(1, 10):
        total = 0
        for i in range(len(scores)):
            # print(scores[i][j])
            total += scores[i][j]
        avg = round(total / 30)
        # print(avg)
        courseAvg.append(avg)
    f.writelines('平均'+'\t')
    for c in courseAvg:
        f.writelines(str(c)+'\t')
    f.writelines(str(sum(courseAvg[:]))+'\t')
    f.writelines(str(round(sum(courseAvg[:])/9,1)))
    f.writelines('\n')
    #写入每个人的每科成绩,总分和平均分
    for line in scores:
        for l in line:
            f.writelines(str(l)+'\t')
        f.writelines(str(sum(line[1:]))+'\t'+str(round((sum(line[1:]))/9,1))+'\n')



#4.添加名次，替换60分以下的成绩为“不及格”；
out_list=[]
for i in scores:
    for new in i[2:11]:
        if int(new)<60:
            i[i.index(new)]='不及格'
    out_list.append(i)

with open('report_new.txt', 'w') as fout:
    fout.write('姓名\t语文\t数学\t英语\t物理\t化学\t生物\t政治\t历史\t地理\t总分\t平均分\n')
    for line in out_list:
        for l in line:
            fout.write(str(l)+'\t')
        fout.writelines('\n')