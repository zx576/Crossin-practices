#-*- coding:utf-8 -*-
from Tkinter import *
import ttk
import tkMessageBox
import math
import time

#---------------------------------------------------------------------
# 数据处理函数
result = []
def formula():
    #一般粒径与有效粒径选择计算公式
    choose_f = choose_formula.get()
    #是否为岩土
    choose_f2 = choose_formula2.get()
    # 触探杆长度
    l = L.get()
    #输入判断
    l = num_judge(l)
    #拿到处理之前的N
    pre_n = N.get()
    pre_n = num_judge(pre_n)
    # 由触探杆长度得到a
    a = pramater_a(l)
    Cn = None
    e0 = None
    new_n = None
    # 有效粒径沙粒
    if choose_f == 'F1':
        if pre_n > 15:
            new_n = 15 + (a * pre_n - 15) / 2
        else:
            new_n = pre_n
    # 一般粒径沙粒
    else:
        new_n = a * pre_n
    # 岩土
    if choose_f2 == 'F2':
        e0 = e.get()
        e0 = num_judge(e0)
        middle_n = new_n
        Cn = 0.77 * math.log10(2000 / e0)
        new_n = middle_n*Cn
    #记录计算出的N与结果
    result_n.set(new_n)
    result.append([pre_n, a, Cn, e0, new_n,time.ctime()])

def pramater_a(l):
    if l <= 3:
        a = 1.00
    elif 3<l<=6:
        a = 0.92
    elif 6<l<=9:
        a = 0.86
    elif 9<l<=12:
        a = 0.81
    elif 12<l<=15:
        a = 0.77
    elif 15<l<=18:
        a = 0.73
    else:
        a = 0.70
    return a
#判断数字
def num_judge(num):
    try:
        num = float(num)
        if num < 0:
            tkMessageBox.showinfo('error', '数值小于0，不符合计算要求')
        return num
    except:
        tkMessageBox.showinfo('error', '输入不为数值')
#修改e0的可编辑状态
def changestate():
    choice = choose_formula2.get()
    if  choice == 'F2':
        e_entry.config(state=ACTIVE)
    else:
        e_entry.config(state=DISABLED)
#保存
def savetxt():
    try:
        f = open('record.txt','a+')
    except:
        f = open('record.txt','w')
    finally:
        try:
            for i in result[-1]:
                element = str(i)
                f.write(element)
                f.write(',')
            f.write('\n')
            f.close()
            del result[:]
            tkMessageBox.showinfo('sucees', '保存成功')
        except:
            tkMessageBox.showinfo('error', '无计算数据')
#显示查询信息
def showrecord():
    if child_window.state() == 'withdrawn':
        child_window.deiconify()
        child_window.attributes("-topmost", 1)
        with open('record.txt', 'r') as r:
            all_data = r.readlines()
            i = 0
            for data in all_data:
                strip_data = data.strip()
                info = strip_data.split(',',5)
                tree.insert('', i,values=(info[0], info[1], info[2], info[3], info[4],info[5]))
                i += 1
#关闭子窗口
def close_child_window():
    child_window.withdraw()
    tree.delete(*tree.get_children())
#---------------------------------------------------------------------
top = Tk()
child_window = Toplevel(top)
child_window.withdraw()
#设置gui标题
top.title('标贯击数的校正')
#添加框架
mainframe = ttk.Frame(top,padding='3 3 12 12')
childframe = ttk.Frame(child_window,padding='3 3 12 12')
#添加grid
mainframe.grid(column=0,row=0,sticky=(N,W,E,S))
childframe.grid(column=0,row=0,sticky=(N,W,E,S))
#添加label，位置以column/row确定
ttk.Label(mainframe,text='标贯击数的校正',font=20).grid(column=1,row=1,sticky=(W,E))
ttk.Label(mainframe,text='N\':').grid(column=0,row=2,sticky=W)
ttk.Label(mainframe,text='触探杆长度:').grid(column=0,row=3,sticky=W)
ttk.Label(mainframe,text='e0:').grid(column=0,row=7,sticky=W)
ttk.Label(mainframe,text='N:').grid(column=0,row=9,sticky=W)

#添加输入框，输入值设定为待处理的N值
N = StringVar()
n_entry = ttk.Entry(mainframe,width=20,textvariable=N)
n_entry.grid(column=1,row=2)
#添加输入框，输入值设定为触探杆长度L
L = StringVar()
L_entry = ttk.Entry(mainframe,width=20,textvariable=L)
L_entry.grid(column=1,row=3)

#添加复选按钮，默认为一般粒径、可选有效粒径、可选岩土
choose_formula = StringVar()
choose_formula2 = StringVar()
ttk.Checkbutton(mainframe,text='有效沙粒',onvalue='F1',variable=choose_formula).grid(column=0,row=5,sticky=W)
ttk.Checkbutton(mainframe,text='沙土',onvalue='F2',variable=choose_formula2,command=changestate).grid(column=0,row=6,sticky=W)
##添加输入框，输入值设定为实测深度处土的实际上覆压力e0
e = StringVar()
e_entry = ttk.Entry(mainframe,width=20,textvariable=e,state=DISABLED)
e_entry.grid(column=1,row=7)
#计算按钮
ttk.Button(mainframe,text='计算',command=formula).grid(column=1,row=8,sticky=(W,E))
#添加输入框，
result_n = StringVar()
N_entry = ttk.Entry(mainframe,width=20,textvariable=result_n)
N_entry.grid(column=1,row=9)
#保存按钮
ttk.Button(mainframe,text='保存',command=savetxt).grid(column=0,row=10,sticky=(W,E))
#查询按钮
inquiry = ttk.Button(mainframe,text='查询',command=showrecord)
inquiry.grid(column=2,row=10,sticky=(W,E))
#子窗口校正记录
ttk.Label(childframe,text='校正记录',font=50).grid(column=0,row=1,sticky=(W,E))
tree = ttk.Treeview(childframe,show="headings",columns=('a','b','c','d','e','f'))
tree.grid(column=0,row=2,rowspan=15)
tree.heading('a',text='N\'')
tree.heading('b',text='a')
tree.heading('c',text='Cn')
tree.heading('d',text='e0')
tree.heading('e',text='N')
tree.heading('f',text='time')
tree.column('a',width=50)
tree.column('b',width=50)
tree.column('c',width=50)
tree.column('d',width=50)
tree.column('e',width=50)
tree.column('f',width=200)
vbar = ttk.Scrollbar(childframe, orient=VERTICAL, command=tree.yview)
vbar.grid(row=2,column=2,rowspan=15,sticky=NS)
tree.configure(yscrollcommand=vbar.set)

#添加右上角关闭响应
child_window.protocol('WM_DELETE_WINDOW',close_child_window)
#添加padding
for child in mainframe.winfo_children():
    child.grid_configure(padx=5,pady=5)
top.mainloop()