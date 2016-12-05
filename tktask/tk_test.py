from tkinter import *
from tkinter import ttk
import time
# Code to add widgets will go here...
# top = Tk()
#
# mainframe = ttk.Frame(top,padding='3 3 12 12')
# mainframe.grid(column=0,row=0,sticky=(N,W,E,S))
#
# def test_pra():
#     a = float(pra.get())
#     if a == 1:
#         new = 2
#     else:
#         new = 4
#     print(new,time.ctime())
#     print(aaa['text'])
# pra = StringVar()
# aaa = ttk.Radiobutton(mainframe,text='有效沙粒',value='1',variable=pra,command=test_pra)
# aaa.grid(column=0,row=5,sticky=W)
# top.mainloop()
#
# l = [1,2,3,4,5,[1]]
# print(len(l))
# del l[1]
# print(l)

with open('record.txt','r') as r:
    a = r.readlines()

    for i in a:
        c = i.strip()
        print(c)
        v = c.split(',',5)
        print(v)




# q = 'zxc,sadfa,trety,jhg'
# c = q.split(',')
# print(c)



