import xlwt
import xlrd
import datetime

starttime = datetime.datetime.now()

#新建excel
# wb = xlwt.Workbook()
# #添加工作薄
# sh = wb.add_sheet('Sheet1')
# #写入数据
# # test_data = [i for i in range(702)]
# for i in range(1000):
#     for j in range(256):
#         sh.write(i,j,1)
#
# #保存文件
# wb.save('xlutils_test3.xls')

# book = xlrd.open_workbook(r'e:/xlwingstest_2.xlsx')
book = xlrd.open_workbook(r'e:/openpyxltest_2.xlsx')

endtime = datetime.datetime.now()

print(endtime-starttime)
a = '0:00:03.845220'