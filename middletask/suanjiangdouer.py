# -*- coding:utf-8-*-
#【项目一】统计成绩
import os

sum = 0
all = []
for line in open('report.txt'):
    line = line.rstrip('\n')    #删除结尾换行符
    line = line.split(' ')      #转换为列表

    for i in line[1:10]:
        sum = sum + int(i)
    line.append(sum)
    line.append(round(sum/9.0,1))

    all.append(line)    #每行信息保存到all列表中
    sum = 0

all.sort(key = lambda x:x[10])      #all[10]总分小到大排序
all = all[::-1]


tot = []
for i in range(1, 12):
    sum = 0.0
    for j in range(len(all)):
        sum = sum + int(all[j][i])
    tot.append(round(sum/len(all),1))    #保留小数点后一位round(sum/9.0,1)



title = '名次 姓名 语文 数学 英语 物理 化学 生物 政治 历史 地理 总分 平均分'
title = title.split(' ');

fff = open('report_1.txt', 'w')       #print换为f.write(i)即字符写入文件
for i in title:
    #print str(i).center(6,' '),     #title每项占位，出来效果貌似没用
    fff.write(str(i).center(6,' '),)
fff.write('\n')

fff.write('0'.center(6,' ')),
fff.write('平均'.center(6,' ')),
for i in tot:       #打印平均
    fff.write(str(i).center(6,' ')),
fff.write('\n')


n = 1
for i in all:       #打印all
    fff.write(str(n).center(6,' ')),
    for ii in i:
        fff.write(str(ii).center(6,' ')),
    fff.write('\n')
    n += 1

fff.close()
print '成绩单保存在 report_1.txt'
