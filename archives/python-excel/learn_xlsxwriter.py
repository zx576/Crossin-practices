import xlsxwriter as xw
import numpy as np

# 新建文件，文件地址为当前目录下
# wb = xw.Workbook('ne.xlsx')
# #新建文件下，同样需要新建sheet
# ws = wb.add_worksheet()
# ws.activate()
# #写入数据 ？？？？？？？？？该包一次只能写入一个cell
# da = np.eye(3)
# ws.write('A1','HELLO')
# expenses = (
#     ['rent',100],
#     ['gas',20],
#     ['food',200],
#     ['gym',50],
# )
# row = 0
# col = 0
# for item,cost in expenses:
#     ws.write(row,col,item)
#     ws.write(row,col+1,cost)
#     row += 1
# ws.write(row,0,'Total')
# ws.write(row,1,'=SUM(B1:B4)')
# wb.close()

# wc = wb.add_chart({type:'column'})