# /user/bin/python2.7
# coding=utf-8

def add_up(score): #计算总分
    sum=0
    for i in range(1,10):
        sum+=float(score[i])
    return sum
def campare(grade): #替换不及格的分数
    t=grade[:]
    for i in t:
        for ii in range(1,10):
            if int(i[ii])<60:
                i[ii]='不及格'
    return t
def addall(grade): #计算每科平均成绩
    ave=['平均']
    global stu
    for i in range(1,10):
        sum=0
        for ii in range(stu):
            sum+=int(grade[ii][i])
        ave.append(str(float('%.1f'%(1.0*sum/stu))))
    t=add_up(ave)
    ave.append(str(float('%.1f' %t)))
    ave.append(str(float('%.1f' %(t/9.0))))
    return ave
stu=ii=0
with open('report.txt') as f:
    grades=f.readlines()  #读入成绩
    grade=[]
    for i in grades:  #将每人成绩写成一个列表
        t=i.split()
        grade.append(t)
        stu+=1
    average=addall(grade)
    al=[[str(int(add_up(score))),str(float('%.1f' %(add_up(score)/9.0)))] for score in grade] #统计每个人的总成绩及平均分
    all_grade=campare(grade)
    text=['名次','姓名','语文','数学','英语','物理','化学','生物','政治','历史','地理','总分','平均分']
    for i in all_grade:
        i.append(al[ii][0])
        i.append(al[ii][1])
        ii+=1
    all_grade=sorted(all_grade, key=lambda x: x[10],reverse=True)
    all_grade.insert(0,text)
    all_grade.insert(1,average)
    t=0
with open('summary.txt','w') as f:
    for i in all_grade:
        if (t-1)>=0:
            print str(t-1).center(6),
            f.write(str(t-1).center(6))
        t+=1
        for ii in i:
            print ii.center(6),
            f.write(ii.center(6))
        f.write('\n')
        print
