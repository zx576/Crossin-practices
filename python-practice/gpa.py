#-*- coding:utf-8 -*-
#python3.5
#建立变量，存入循环次数
c = 1
# 总分数以及总学分
total_score = 0
total_marks = 0
#循环开始
while True:
    #输入课程分数及学分
    scores = float(input('输入第%d门课程分数：'%c))
    mark = float(input('输入第%d门课程学分：'%c))
    # print(dict,total_marks,total_score)
    #根据课程分数得到课程绩点
    if 90 <= scores <= 100:
        gpa = 4.0
    elif 85 <= scores <= 89:
        gpa = 3.7
    elif 82 <= scores <= 84:
        gpa = 3.0
    elif 78 <= scores <= 81:
        gpa = 3.0
    elif 75 <= scores <= 77:
        gpa = 2.7
    elif 71 <= scores <= 74:
        gpa = 2.3
    elif 66 <= scores <= 70:
        gpa = 2.0
    elif 62 <= scores <= 65:
        gpa = 1.7
    elif 60 <= scores <= 61:
        gpa = 1.3
    elif scores == 60:
        gpa = 1.0
    else:
        gpa = 0
    #累加总分数以及总学分
    total_score += gpa * mark
    total_marks += mark
    #算出当前平均绩点
    averge_gpa =total_score / total_marks
    #打印
    print('现在的平均绩点为：%.2f' %averge_gpa)
    #循环次数累加
    c += 1



#python2.7
#建立变量，存入循环次数
# c = 1
# # 总分数以及总学分
# total_score = 0
# total_marks = 0
# #循环开始
# while True:
#     #输入课程分数及学分
#     scores = input('输入第%d门课程分数：'%c)
#     mark = input('输入第%d门课程学分：'%c)
#     # print dict,total_marks,total_score
#     #根据课程分数得到课程绩点
#     if 90 <= scores <= 100:
#         gpa = 4.0
#     elif 85 <= scores <= 89:
#         gpa = 3.7
#     elif 82 <= scores <= 84:
#         gpa = 3.0
#     elif 78 <= scores <= 81:
#         gpa = 3.0
#     elif 75 <= scores <= 77:
#         gpa = 2.7
#     elif 71 <= scores <= 74:
#         gpa = 2.3
#     elif 66 <= scores <= 70:
#         gpa = 2.0
#     elif 62 <= scores <= 65:
#         gpa = 1.7
#     elif 60 <= scores <= 61:
#         gpa = 1.3
#     elif scores == 60:
#         gpa = 1.0
#     else:
#         gpa = 0
#     #累加总分数以及总学分
#     total_score += gpa * mark
#     total_marks += mark
#     #算出当前平均绩点
#     averge_gpa =total_score / total_marks
#     #打印
#     print '现在的平均绩点为：%.2f' %averge_gpa
#     #循环次数累加
#     c += 1
