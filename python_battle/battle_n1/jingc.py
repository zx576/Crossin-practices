#coding:utf-8
from tkinter import *
from tkinter.filedialog import askdirectory,askopenfilename
# import Tkinter, Tkconstants, tkFileDialog

def selectPath():
    path_ = askdirectory()      #askdirectory()方法是返回文件夹路径不是文件路径。
    #path_ = tkFileDialog.askopenfilename()  #tkFileDialog.askopenfilename()返回文件路径
    path1.set(path_)
    print('调用selectPath()')
def selectPath2():
    path_ =askopenfilename()  #tkFileDialog.askopenfilename()返回文件路径
    path2.set(path_)
    print('调用selectPath()   2')
def function():
    print('function')
    pass

root = Tk()

path1 = StringVar()

Label(root, text = '目录路径：').grid(row = 0, column = 0)
Entry(root, textvariable = path1).grid(row=0, column=1)
Button(root, text='选择文件夹', command=selectPath, width = 12,height=1).grid(row=0, column=2)

path2 = StringVar()
Label(root, text = '文件路径：').grid(row = 2, column = 0)
Entry(root, textvariable = path2).grid(row=2, column=1)
Button(root, text='选择文件夹', command=selectPath2, width = 12,height=1).grid(row=2, column=2)

# print 111

# 创建按钮
root.btSearch = Button(root,
                       text = '执行',
                       width = 12,height=1,
                       command = lambda arg1 = root:function()
                       )
root.btSearch.grid(row = 3,column = 2)


# 创建搜索结果列表
root.lbResults = Listbox(root)
root.lbResults.grid(row = 111,column = 0,columnspan = 112,stick = E + W + N + S)

#Frame(height=20, width=300).pack()

root.mainloop()
# print 222
