#-*- coding:utf-8 -*-
from Tkinter import *

def main():
    root = Tk()
    root.title('计算器-yh')
    root.geometry('200x250+100+100')
    label = Label(root, relief='sunken', borderwidth=3, anchor=SE)
    label.config(bg='white', width=28, height=1)
    label.grid(row=0, column=0, columnspan=4)

    positions = [(x,y) for x in range(1,6) for y in range(4) ]

    tests = ['Cls', 'Bck', '', 'Close',
             '7', '8', '9', '/',
            '4', '5', '6', '*',
             '1', '2', '3', '-',
            '0', '.', '=', '+']


    for i in zip(tests,positions):
        text = i[0]
        row = i[1][0]
        column = i[1][1]
        Button(root,text=text,width=8,command=lambda text=text:userinput(text)).grid(row=row,column=column)
        print text

    Button(root, text='1', width=3,).grid(row=1, column=0)
    Button(root, text='2', width=3,).grid(row=1, column=1)
    Button(root, text='3', width=3,).grid(row=1, column=2)
    Button(root, text='*', width=3,).grid(row=1, column=3)
    Button(root, text='4', width=3,).grid(row=2, column=0)
    Button(root, text='5', width=3,).grid(row=2, column=1)
    Button(root, text='6', width=3,).grid(row=2, column=2)
    Button(root, text='/', width=3,).grid(row=2, column=3)
    Button(root, text='7', width=3,).grid(row=3, column=0)
    Button(root, text='8', width=3,).grid(row=3, column=1)
    Button(root, text='9', width=3,).grid(row=3, column=2)
    Button(root, text='+', width=3,).grid(row=3, column=3)
    Button(root, text='Del', width=3,).grid(row=4, column=0)
    Button(root, text='0', width=3,).grid(row=4, column=1)
    Button(root, text='.', width=3,).grid(row=4, column=2)
    Button(root, text='-', width=3,).grid(row=4, column=3)
    Button(root, text='=', width=18).grid(row=5, column=0, columnspan=3)
    Button(root, text='C', bg='red',width=3).grid(row=5, column=3)

    root.mainloop()

def userinput(text):
    print(text)

main()
