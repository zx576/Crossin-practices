import xlwings as xw

# A.编辑活动工作表
#xw.Range('A1').value = '编辑活动工作表'
#print(xw.Range)

#B.xlwings提供两种方式连接excel
#1.通过xw.Book()，不确定 通过xw.Book()操作后，自动将已连接到的excel表转为正在编辑的excel

#xw.Book()  #新建一个excel ？？？是否支持命名，还有此时的excel表保存在哪里？

# xw.Book('2.xlsx') #连接到已打开的excel
# xw.Range('A1').value = 2
#
# xw.Book(r'e:/54.xlsx') #连接到未打开的excel
#
#
# 2.通过xw.books
#
# xw.books.add()   #新建excel文件，与xw.Book不同之处在于，此时需要打开excel应用才能新建excel，即先打开任意一张excel
#
# xw.books['1111.xlsx'] #连接到已打开excel文件

# xw.books.open(r'e:/54.xlsx')  #连接到未打开excel文件，注意与Book的区别


# C.xlwings语法
# 引入xlwings
# import xlwings as xw
#
# app = xw.apps.active #官方解释为 excel instance 注意此时的excel实例并非某个excel工作表，而是系统的excel进程
# print(app) >>>>>>> <Excel App 2616>
# app.books['2.xlsx'].sheets[0].range('A1:e5').value = 1
# print(app.books['2.xlsx'].sheets[0].range('A1'))  >>>>>>> <Range [2.xlsx]Sheet1!$A$1>

#完整给出excel表的赋值语句，共有四种方式
# app_1 = xw.apps[0].books[0].sheets[1].range('A1')
#######  关于apps:可以将其理解为进程;books为excel表名称，sheets为表内工作薄名称（0或者'Sheet1'）,range为单元格范围
# app_2 = xw.apps[0].books['1111.xlsx'].sheets[0].range('A1')
# print(app_1)
# app_1.value = 5
# app_2.value = 10
#同样还有一下三种表达方式
# a = xw.apps(1).books('2.xlsx').sheets(2).range('A1')  #???????????为什么上面的语句使用[1]就报错而(1)就没问题呢？
####################()是以1开始，而[]是以0开始
# print(a)
# xw.apps[0].books['2.xlsx'].sheets['Sheet1'].range('A1:H10')
# xw.apps(1).books('Book1').sheets('Sheet1').range('A1')

# a = xw.books['2.xlsx'].sheets['Sheet1'].range('A1:zz1000')
# a.rows(12).value = 1
# # B = xw.apps[0].books['2.xlsx'].sheets['Sheet1'].range('A1:B10')
# # C = xw.apps[0].books['2.xlsx'].sheets['Sheet1'].range('e1:F10')
# # D = xw.apps[0].books['2.xlsx'].sheets['Sheet1'].range('t1')
# a.range('M1').value = 'www.baidu.com'
import datetime
import time

a = datetime.datetime.now()
time.sleep(3)
b = datetime.datetime.now()

print(b-a)



# workbook = xw.Book('2.xlsx')
# data_range = workbook.sheets('Sheet1').range('A1')
# data_range.value = 123344
# workbook.save()





#索引单元格
#采用excel索引
# xw.Range('A1') #从A1开始
# xw.Range('A1:E3')  #指定范围
#采用xlwings索引
# xw.Range((2,1)).value = 567   #(1,1)相对A1
# xw.Range((1,1),(5,5)).value = 10
# xw.Range('namerange')  #namerange表示已经在excel中设定好的单元格范围名称


#数据结构：float，unnicode，none,datetime
# sht = xw.Book('2.xlsx').sheets('Sheet1') #推荐如此简单明了的写法
# print(sht)
####单一单元格
# sht.range('A1').value = 'sdfs'

####list
# sht.range('A1').value = [[1,2,3],[4,5,6]] #列表中的每个列表为一行
###等价于
# sht.range('A1:C3').value = [[1,2,3],[4,5,6]]
# sht.range('A1:C3').value = [1,2,4,5,6]

#范围扩展
# sht.range('A1:B2').value = [[1,2],[3,4]] ###初始范围
# est = sht.range('A1:B2').options(expand='table')  ###赋予扩展
# print(est.value)
# sht.range('a3').value = [[5,6]]   ###扩展范围
# print(est.value)


#接入numpy,pandas数据格式

# 接入numpy arrarys
import numpy as np
# sht.range('A5').value = np.eye(3)

#接入pandas Dataframes
import pandas as pd
# df = pd.DataFrame([[1.1,2.2],[3.3,None]],columns=['one','two'])
# sht.range('A9').value = df

#接入pandas series

# s = pd.Series([1,2,3,4,5,6],name='myseries')
# sht.range('A10').value = s

#在VBA中调用xlwings
#步骤如下
#首先在VBA中加载xlwings.bas
# alt+f11打开VBA界面--文件---导入文件---选择xlwings.bas(不清楚该文件路径，可在运行 import xlwings;xlwings.__path__ 查看)
#此时可在左侧窗口模块分支下看到xlwings模块已经导入成功
#然后新建模块
#模块----插入----模块
#在编辑VBA之前，首先应该编辑好需要执行的py文件，注意py文件路径要与excel文件路径相同，推荐单独建立文件夹存放
# Sub HelloWorld()      #用户自定义函数名
#     RunPython ("import hello1; hello1.world()")
#################这里的hello1表示python文件名，world()表示需要执行的函数
# End Sub


#在py下直接作用于excel
#在py中写好函数后
# if __name__ == '__main__':
    #xw.Book('myfile.xlsx').set_mock_caller()
    #helloworld()
#然后直接跑起来吧

#与matplotlib协作
