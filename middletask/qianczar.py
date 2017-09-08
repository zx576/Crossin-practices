#coding=utf-8
import os
def get_report(path):#导入文件数据，并str转换成list形式
    report = []
    with open(path) as f:
        for i in f.readlines():
            report.append(i.strip())
    datalist=[]
    for each in report:
        each_data = each.split()  # 转成list
        each_data1 = [int(i) for i in each_data[1:]] # 转成int
        each_data1.insert(0, each_data[0])
        datalist.append(each_data1)
    return datalist

def count(data):
    new_data=[]
    result=[]
    for each in data:          #计算每个人的总分平均分，然后添加到new_data里面去
        sum_score=sum([j for j in each[1:]])
        ave_score=round(sum_score/len(each[1:]),1)
        each.append(sum_score)
        each.append(ave_score)
        new_data.append(each)

    sorted_newdata=sorted(new_data,key=lambda x:x[-2],reverse=True)#按照总分逆序排序
    trans_newdata=[[row[i] for row in sorted_newdata] for i in range(len(sorted_newdata[0]))] #转置，便于计算各科平均分
    ave_eachcourse=[str(int(round(sum(a)/len(a),0))) for a in trans_newdata[1:]]#每门课的平均分
    ave_eachcourse.insert(0,'平均')
    ave_eachcourse.insert(0,'0')
    trans_newdata1 =[['不及格' if j < 60 else str(j) for j in i] for i in trans_newdata[1:]] #将60分以下换成不及格
    trans_newdata1.insert(0,trans_newdata[0])
    trans_newdata=trans_newdata1
    trans_newdata.insert(0,[str(i+1) for i in range(len(trans_newdata[0]))]) #添加名次
    final_data=[[row[i] for row in trans_newdata] for i in range(len(trans_newdata[0]))]  #再将列表转置回来成为最初的样子
    final_data.insert(0,ave_eachcourse) #将每门课的平均分插入
    final_data.insert(0,['名次','姓名','语文','数学','英语','物理','化学','生物','政治','历史','地理','总分','平均分'])
    for every in final_data:
        result.append(' '.join(every)+'\n')
    return result

def write_txt(data,topath):
    with open(topath, 'w+') as ff:
        ff.writelines(data)

txt=count(get_report('report.txt'))
write_txt(txt,'new_report.txt')
