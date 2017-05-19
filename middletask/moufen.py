import chardet
with open('report.txt', 'rb') as f:
    contents = f.read()
    contents_code = chardet.detect(contents)
with open('report.txt', encoding=contents_code['encoding']) as f:
    raw_scores = f.readlines()
list_scores = [i.split() for i in raw_scores]
for i in list_scores:
    i.append('%d' % sum(list(map(int, i[1:]))))
    i.append('%.2f' % (sum(list(map(int, i[1:])))/9))
average = ['平均']
for i in range(1, 11):                                                           # 9门课和总分的平均分
    score = 0
    for j in list_scores:
        score += int(j[i])
    average.append('%d' % (score/len(list_scores)))
score = 0
for i in list_scores:                                                           # 平均分的平均分
    score += float(i[11])
average.append('%.2f' % (score/len(list_scores)))
list_scores_sort = sorted(list_scores, key=lambda x: x[-1], reverse=True)       # 按总成绩从高排序
list_scores_sort.insert(0, average)                                              # 加入平均成绩
for i in list_scores_sort:                                                      # 加入名次和不及格替换
    x = 1
    for j in i[1:10]:
        if int(j) < 60:
            i[x] = '不及格'
        x += 1
    i.insert(0, str(list_scores_sort.index(i)))
list_scores_final = [['名次', '姓名', '语文', '数学', '英语', '物理', '化学', '生物', '政治', '历史', '地理', '总分', '平均分']] + list_scores_sort
list_scores_out1 = []
for i in list_scores_final:
    list_scores_out1.append('  '.join(i))
list_scores_out2 = '\n'.join(list_scores_out1)
with open('report_scores.txt', 'w') as f:
    f.write(list_scores_out2)
