# coding=utf-8
output_list = []
course_avg = ['0', '平均', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
course = ['名次', '姓名', '语文', '数学', '英语', '物理', '化学', '生物', '政治', '历史', '地理', '总分', '平均分']
final_output = []
file = open('report.txt', 'r')
output_file = open('result.txt', 'w')

def loaddata():
    global sum, avg
    sum = 0
    avg = 0
    lines = file.readlines()
    for line in lines:
        temp1 = line.split('\n')
        one_student = temp1[0].split(' ')
        #print(one_student)
        for i in range(1, int(len(one_student))):
            sum = sum + int(one_student[i])
            avg = round(sum / 9, 2)
        temp2 = one_student
        temp2.append(sum)
        temp2.append(avg)
        sum = 0
        avg = 0
        output_list.append(tuple(temp2))
    # sorted(output_list, key = lambda student:student[11], reverse = True)
    output_list.sort(key = lambda student:student[11], reverse = True)
    for j in range(2,13):
        for i in output_list:
            course_avg[j] += int(i[j-1]) / int(len(output_list))
        course_avg[j] = round(course_avg[j], 2)
        #print(course_avg[j])
    output_list.insert(0, tuple(course_avg))
    output_list.insert(0, tuple(course))
    for i in range(0,int(len(output_list)) - 1):
        print(list(output_list[i]))
        temp = list(output_list[i])
        if i < 2:
            for j in temp:
                final_output.append(str(j) + ' ')
        else:
            final_output.append(str(i - 1) + ' ')
            final_output.append(str(temp[0]) + ' ')
            for j in range(1,int(len(temp))):
                if int(temp[j]) < 60:
                    temp[j] = '不及格'
                final_output.append(str(temp[j]) + ' ')
        final_output.append('\n')
    print(final_output)
    file.close()
    output_file.writelines(final_output)
    output_file.close()

if __name__ == '__main__':
    loaddata()
