# -*- coding: gbk -*-

# 本程序的作用：
# 程序运行流程如下：
# step1 : 打开文件
# step2 : ...
# step3 : ....



# 该函数的作用是 打开文件，读取文件内容
#　返回的数据为 list　形式
def readfile(filename):
    # with ... open 为打开文件的方法
    with open(filename,'r+')as f:
        data=f.readlines()
    return data


def cal_score(scores):
    person_score=[]
    for line in scores:
        temp_line=line.split()
        temp_line.append(sum([int(x)for x in temp_line[1:]]))
        temp_line.append(round(temp_line[-1]/(len(temp_line)-2), 1))
        person_score.append(temp_line)
    person_score.sort(key=lambda x:x[10],reverse=True)
    transposed=[list(n)for n in zip(person_score)]
    total=[]
    for x in transposed:
        for s in x[1:]:
            total_sum=sum([int(s)for s in x])
            total.append(round(total_sum/len(x),1))
        total.insert(0,'平均')
        total.insert(0,'0')
    rank=1
    for x in person_score:
        x.insert(0,rank)
        rank+=1
        for element in x[2:-2]:
            if int(element)<60:
                x[x.index(element)]='不及格'
    new_score=person_score
    new_score.insert(0,total)
    new_score.insert(0,['名次','姓名','语文','数学','英语','物理','化学','生物','政治','历史','地理','总分','平均分'])
    return new_score
def writefile(filename,scores):
    with open(filename,'w+')as f:
        for line in scores:
            for index in range(0,len(line)):
                line[index]=str(line[index])
            text=''.join(line)+'\n'
            f.writelines(text)
if __name__ =='__main__':
    scores=readfile('F:\\report.txt')
    new_score=cal_score(scores)
    writefile('new_report.txt', new_score)
