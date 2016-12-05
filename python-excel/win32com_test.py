import win32com.client as wc
import datetime
#启动Excel应用
starttime = datetime.datetime.now()
excel_app = wc.Dispatch('Excel.Application')
excel_app.Visible = False
#连接excel
# workbook = excel_app.Workbooks.Add()
# workarea = workbook.Worksheets('Sheet1').Range('A1:ZZ1000')
# test_data = [i for i in range(4000)]
# #写入数据
# for j in range(1,4001):
#     workarea.Rows(j).Value = 1
# #关闭并保存
# workbook.SaveAs('win32te1.xlsx')

# wb = excel_app.Workbooks.Open(r'e:/xlwingstest_2.xlsx')
wb = excel_app.Workbooks.Open(r'e:/openpyxltest_2.xlsx')

excel_app.Application.Quit()
endtime = datetime.datetime.now()

print(endtime-starttime)
a='0:00:02.995171'