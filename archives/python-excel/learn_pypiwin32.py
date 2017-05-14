import win32com.client as wc

#启动excel应用
xl = wc.Dispatch('Excel.Application')

#新建excel
# ss = xl.Workbooks.Add()
#打开excel
workbook = xl.Workbooks.Open(r'e:/54.xlsx' )

#连接到工作薄
# worksheet = workbook.Worksheets('Sheet1')
#新建工作薄
worksheet = workbook.Worksheets.Add()
pic = worksheet.Pictures()

