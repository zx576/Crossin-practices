# midterm-homework
# Crossinclass 9-3
result_s = []
result_new = []
result_score = []
with open ('report.txt', 'r', encoding = 'utf-8') as f:
    report_all = f.readlines()
courses = len(report_all[0].split()) - 1     #科目数
sum_c = [0 for i in range(courses)]     #新增重置科目列表

for line in report_all:       #计算总分和平均分
    data = line.split()
    sum_s = 0
    for score in data[1:]:
        sum_s += int(score)     #每个同学总分
        average_s = round(float(sum_s)/(len(data) - 1), 1)     #每个同学平均分
    for goal in range(1, len(data)):
        sum_c[goal-1] += int(data[goal])     #每个科目总分
    average_c = [round(float(i) / len(report_all), 1) for i in sum_c]       #每个科目平均分
    data.append(sum_s)
    data.append(average_s)
    result_s.append(data)
    result_s.sort(key = lambda s : s[11], reverse = True)

#按照平均分排名
loop = 1
for l in result_s:
    l.insert(0, loop)
    loop += 1
    result_new.append(l)

#替换不及格分数
for raw in result_new:
    for k in raw[2:11]:
        if int(k) < 60:
            raw[raw.index(k)] = '不及格'
    result_score.append(raw)

with open('report_new.txt', 'w') as fn:
    fn.write('姓名 名次 语文 数学 英语 物理 化学 生物 政治 历史 地理 总分 平均分\n')
    fn.write('0 平均 ')
    for m in average_c:
        fn.write(str(m))
        fn.write(' ')
    fn.write('\n')
    for t in result_score:
        fn.write(str(t))
        fn.write('\n')
