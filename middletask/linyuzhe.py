with open('report.txt', encoding='utf-8') as grades_class:
    students_lines_whole = []
    students_grade_whole = []
    students_grade_last = []
    list_finish = []
    students_score = ['0', '平均']
    count_num = 1
    for grades_per_line in grades_class:
        students_lines_whole.append([grades_per_line.strip()])
    students_lines_whole.insert(0, "姓名 语文 数学 英语 物理 化学 生物 政治 历史 地理")
    for search_per_index in students_lines_whole[1:]:
        search_per_index = ','.join(search_per_index)
        search_per_index = search_per_index.split(' ')
        search_per_index = ' '.join(search_per_index)
        search_per_index = search_per_index.split()
        sum_grade = sum(int(x) for x in search_per_index[1:])
        average_grade = round(sum_grade / len(search_per_index[1:]), 1)
        search_per_index.append(str(sum_grade))
        search_per_index.append(str(average_grade))
        students_grade_whole.append(search_per_index)
        students_grade_whole = sorted([x for x in students_grade_whole], reverse=True, key=lambda x: x[-1])
    for x in students_grade_whole:
        x.insert(0, str(count_num))
        count_num += 1
        students_grade_last.append(x)
    for count_time in range(2, 13):
        sum_num = 0
        for search_per_index_next in range(len(students_grade_last)):
            sum_num = sum_num + eval(students_grade_last[search_per_index_next][count_time])
        students_score.append('%.1f' % (sum_num / len(students_grade_last)))
    students_score = ' '.join(students_score)
    for m in students_grade_last:
        for j in m[2:-2]:
            if int(j) < 60:
                m[m.index(j)] = '不及格'
        m = ' '.join(m)
        list_finish.append(m)
    list_finish.insert(0, students_score)
    list_finish.insert(0, '名次 姓名 语文 数学 英语 物理 化学 生物 政治 历史 地理 总分 平均分')
    with open('output.txt', 'w+', encoding='utf-8') as output:
        output.write('\n'.join(list_finish))
