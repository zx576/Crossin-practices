#-*-coding:utf-8-*
f=open('report.txt','r',encoding='utf-8')
lines=f.readlines()#读完整个文件，每行作为一个元素存入列表中
f.close()
lst=[]
for line in lines:#遍历列表中的每一个元素
    s=line.split()#将每个元素转成列表
    total_scores=0
    for i in s[1:]:
        total_scores+=int(i)
        avg_scores=float(total_scores)/len(s[1:])
    result= '%d,%.1f' % (total_scores, avg_scores)
    results=result.split(',')
    s.extend(results)#总成绩与平均成绩同时加到s列表中
    lst.append(s)
    index = 1
    for j in s[1:10]:#在更改后的s的每个元素进行操作
        if int(j)<60:
            s[index]='不及格'
        index+=1
lst.sort(key=lambda x:x[-1],reverse=True)#在总列表中按照平均成绩从大到小排序

title='名次\t姓名\t语文\t数学\t英语\t物理\t化学\t生物\t政治\t历史\t地理\t总分\t平均分\n'
new_file = open('new.txt','w')
new_file.write(title)
num = 0
for i in lst:
    num += 1
    i.insert(0,str(num))
    b = '\t'.join(i)
    print(b)
    new_file.write((b)+'\n')
new_file.close()
