import pandas as pd
import datetime
starttime = datetime.datetime.now()
# col = [i for i in range(703)]
# row = []
# for j in range(1000):
#     row.append(col)
#
# df = pandas.DataFrame(row,columns=col)
# df.to_excel(r'e:/pandastest3.xlsx', sheet_name='Sheet1')


# xlsx = pd.ExcelFile(r'e:/xlwingstest_2.xlsx')
xlsx = pd.ExcelFile(r'e:/openpyxltest_2.xlsx')
# df = pd.read_excel(xlsx, 'Sheet1')

endtime = datetime.datetime.now()

print(endtime-starttime)