import xlwings as xw
import datetime


starttime = datetime.datetime.now()

# test_data = [i for i in range(702)]
# workbook = xw.Book()
# workarea = workbook.sheets('Sheet1').range('A1:ZZ1000')
# for j in range(1,1001):
#     workarea.rows(j).value = 1
#
# workbook.save(r'e:/xlwingstest_5.xlsx')
b = xw.Book(r'e:/pandastest1.xlsx')
data = b.sheets('Sheet1').range('ZZ1000').value
print(data)
# xw.Book(r'e:/openpyxltest_3.xlsx')

endtime = datetime.datetime.now()

print(endtime-starttime)

