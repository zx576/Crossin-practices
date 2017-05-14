import xlsxwriter as xw
import datetime

starttime = datetime.datetime.now()

# test_data = [i for i in range(702)]
workbook = xw.Workbook('xlsxwritertest_3.xlsx')
worksheet = workbook.add_worksheet()
for j in range(1,1001):
    for i in range(1,703):
        worksheet.write(j,i,1)

workbook.close()
endtime = datetime.datetime.now()

print(endtime-starttime)
a='0:00:14.168810'