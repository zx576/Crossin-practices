# coding=utf-8
with open ("report.txt", 'r') as f:
    file = f.readlines()
    lstn = []
    for x in file:
        sum = 0
        avg = 0
        lst = x.split()

        for y in lst[1:]:
            y  = int(y)
            sum += y
            avg = sum/9

        lst.append(str(sum))
        lst.append(str(avg))

        for i in lst[1:]:
            if int(i) < 60:
                lst[lst.index(i)] = "不及格"
        lstn.append(lst)
    s = sorted(lstn,key=lambda x:x[-2],reverse=True)

with open ("score.txt",'w+')as G:
    G.write("名次 姓名 语文 数学 英语 物理 化学 生物 政治 历史 地理 总分 平均分")
    count = 0
    for k in s:
        count += 1
        G.write("\n")
        G.write("%s "% count)
        G.write(" ".join(k))
