#coding:utf-8
'''
作者：jingc
行业：工作
学习编程时间：2016 年 12 月 21 日 加入（之前学过其他语言编程）
项目介绍：按照一个文件名清单（Excel固定列）查找对应文件，然后复制倒指定目录。

'''
'''
需要实现：
1、读取文件名清单，保存到列表备用；
2、查找指定文件名，返回该文件路径
3、复制已知文件路径到指定目录
4、GUI编程实现程序窗口化操作
对以上3条细化：
1.知识点
a.读取文件，f = open(）读取TXT文件，
b.列表的操作，list.append（）
2.知识点
a.文件夹操作：for roots, dirs, files in os.walk(path)
3.shutil.copy的用法
知识点：
函数
4.GUI：Tkinter
'''


#getPath.py
from tkinter import *
from tkinter.filedialog import askdirectory,askopenfilename
# import Tkinter, Tkconstants, tkFileDialog

import tkinter.messagebox

import xlrd
import os
import os.path
import time, datetime
import shutil
import chardet


def selectPath():
    path_ = askdirectory()      #askdirectory()方法返回文件夹路径。
    #print type(path_)
    pathFile.set(path_)
    print('调用selectPath()')
def selectPath2():
    path_ =askopenfilename()  #返回文件路径
    pathExcel.set(path_)
    print('调用selectPath()   2')
def selectPath3():
    path_ = askdirectory()
    print(type(path_))
    pathFileTo.set(path_)
    print('调用selectPath()   3')


#copyFile.py_____________________________
#按关键字查找该文件路径
def findFile(key, path):
    suffix = '.txt'     #excel中txt文件
    file_all_name = []
    for roots, dirs, files in os.walk(path):
        for i in files:  # 获取每个文件的名，及完整路径
            file_all_name.append(roots + '\\' + i)
    for i in file_all_name:
        if key+suffix in i:
            return i

#当前日期：20170101
def getCurTime():
    nowTime = time.localtime()
    year = str(nowTime.tm_year)
    month = str(nowTime.tm_mon)
    if len(month) < 2:
        month = '0' + month
        day = str(nowTime.tm_mday)
        if len(day) < 2:
            day = '0' + day
    return (year + '.' + month + '.' + day)

def moveFileto(sourceDir, targetDir):  # 复制指定文件到目录
    shutil.copy(sourceDir, targetDir)

def copyfile(path1, path2):     #将文件path1   copy到path2
    if os.path.exists(path2):  # 如果moveTo文件夹不存在，新建文件夹
        pass
    else:
        # os.mkdir(moveTo)
        os.makedirs(path2)
    moveFileto(path1, path2)
#copyFile.py_____________________________


root = Tk()     #窗体

pathFile = StringVar()
Label(root, text = '搜索范围：').grid(row = 0, column = 0)
Entry(root, textvariable = pathFile, width = 30).grid(row=0, column=1)
Button(root, text='选择文件夹1', command=selectPath, width = 12,height=1).grid(row=0, column=2)

pathExcel = StringVar()
Label(root, text = 'excel路径：').grid(row = 1, column = 0)
Entry(root, textvariable = pathExcel, width = 30).grid(row=1, column=1)
Button(root, text='选择文件  2', command=selectPath2, width = 12,height=1).grid(row=1, column=2)

pathFileTo = StringVar()
Label(root, text = '复制到：').grid(row = 2, column = 0)
Entry(root, textvariable = pathFileTo, width = 30).grid(row=2, column=1)
Button(root, text='选择文件夹3', command=selectPath3, width = 12,height=1).grid(row=2, column=2)

#print 111


#按钮执行包含解析excel等功能的复制函数
def function():
   #print('function被执行')
    path_File = pathFile.get()      #获取label路径
    path_Excel = pathExcel.get()
    path_FileTo = pathFileTo.get()

    #copyFile.py执行代码=====================
    #book = xlrd.open_workbook(u"C:\\test\\te\\2017表格.xlsx")
    book = xlrd.open_workbook(path_Excel)
    sh01 = book.sheet_by_index(0)  # 获取第一个sheet
    data01_list = []  # 关键字list
    for i in range(2, sh01.nrows):  # excel 指定列文件名，查找并返回文件路径
        aa = sh01.cell_value(i, 1).encode("utf-8")
        data01_list.append(aa)

    path2 = path_FileTo + '\\' + getCurTime() + '\\'  # 保存到指定目录下的新建文件夹
    for i in data01_list:
        # print i,
        i = unicode(i, "utf8")
        print(i)
        path1 = findFile(i, path_File)
        # print path1
        copyfile(path1, path2)
    print('已经完成excel文件名复制到指定目录')
    tkinter.messagebox.showinfo("finish", "复制完成")

# 创建按钮
root.btSearch = Button(root,
                       text = '执行',
                       width = 12,height=1,
                       command = lambda arg1 = root:function()      #执行函数function()
                       ).grid(row = 5,column = 2)


root.mainloop()     #
print('Done')

#命令符模式下运行pyinstaller path(C:\getPath.py)将程序打包成exe
