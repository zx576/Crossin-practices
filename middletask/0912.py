# !/user/bin/env pyhton
# coding: utf-8

import codecs

scores = []

with open('report.txt', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        total = 0
        i = 0
        if line:
            score = line.split()
            for s in score[1:]:
                total += int(s)
                i += 1
            #     if float(s) < 60:
            #         score[score.index(s)] = '不及格'
            avg_temp = total / (i)
            avg = '%.1f' % (avg_temp)
            score.append(str(total))
            score.append(str(avg))
            # for m in score[1:]:
            #     if float(m) < 60:
            #         score[score.index(m)] = '不及格'
            print(score)
            scores.append(score)


# print(scores)

scores.sort(key=lambda s: s[-1], reverse=True)
print(scores)

head = ['名次','姓名','语文','数学','英语','物理','化学','生物','政治','历史','地理','总分','平均分']
scores.insert(0, head)
class_aveg = [0,'平均']
for i in range(1,len(scores[1])):
    for j in range(1,len(scores)):
        single = []
        single.append(scores[j][i])
        avg_temp2 = sum(float(a) for a in single[:])/len(single)
        avg_temp2 = '%.1f' %avg_temp2
    class_aveg.append(avg_temp2)
scores.insert(1,class_aveg)
print(scores)

j = 1
for i in scores[2:]:
    i.insert(0,j)
    j += 1
    for n in i[2:-2]:
        if int(n) < 60:
            i[i.index(n)] = '不及格'
nf = open('newreport.txt', 'w')
for ns in scores:
    for i in range(0,len(ns)):
        if type(ns) != str:
            ns = str(ns)
    ns2 = ''.join(ns)+'\n'
    print(ns2)
    nf.write(ns2)
nf.close()
