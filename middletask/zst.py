# -*- coding: utf-8 -*-

project = ['姓名', '语文', '数学', '英语', '物理', '化学', '生物', '政治', '历史', '地理']
print(' '.join(project))
with open('report.txt', 'r', encoding='utf-8') as f:
    new_lst = []
    n = 0
    start = 1
    summary = ['0', '平均']
    copy = []
    for a in f.readlines():
        copy_lst = []
        lst = []
        sum = 0
        ave = 0
        n += 1
        a = a.rstrip('\n')
        print(a)
        a = a.split()
        for i in a[1:10]:
            sum = sum + int(i)
        ave = round(sum / 9, ndigits=2)
        a.append(sum)
        a.append(ave)
        copy1 = a[:]
        copy.append(copy1)
        copy_lst = a
        for i in copy_lst[1:10]:
            if int(i) < 60:
                copy_lst[copy_lst.index(i)] = "不及格"
            else:
                copy_lst[copy_lst.index(i)] = str(copy_lst[copy_lst.index(i)])
        for i in copy_lst[10:12]:
            copy_lst[copy_lst.index(i)] = str(copy_lst[copy_lst.index(i)])
        new_lst.append(copy_lst)
    new_lst.sort(key=lambda x: x[-2], reverse=True)
    for x in range(1,12):
        s = 0
        for y in range(0,n):
            s += float(copy[y][x])
        summary.append(str(s / n))

    with open('new_report', 'w',encoding='utf-8') as transcript:
        project.insert(0,'名次')
        project.append('总分')
        project.append('平均分')
        title = ' '.join(project)
        transcript.write(title + '\n')
        z = ' '.join(summary)
        transcript.write(z+'\n')
        for people in new_lst:
            if start <= n:
                people.insert(0, str(start))
                start += 1
            transcript.write(" ".join(people) + "\n")
