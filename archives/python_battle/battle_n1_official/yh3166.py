# coding=utf-8
from Tkinter import *

def userinput(text):    #按键返回函数
    content = display.get() + text
    display.set(content)

def clear():   #清空函数
    display.set('')

def dell():     #删除一字符函数
    display.set(str(display.get()[:-1]))

def calculate():   #调用eval计算表达式
    try:
        num=display.get()
        res=eval(num)
        display.set(num+'='+str(res))
    except:
        display.set('error!')

def main():
    root = Tk()
    root.title('计算器-yh')
    global display
    display = StringVar()
    root.geometry('275x215+200+200')
    root.resizable(0,0)
    label = Label(root,relief='sunken',borderwidth=3, anchor=SE)#显示窗口
    label['textvariable'] = display
    label.config(bg='white', width=38, height=2)
    label.grid(row=0, column=0, columnspan=4,pady=10)
    positions=[(x,y) for x in range(1,6) for y in range(4)]
    tests=['Cls','Bck','(',')',
           '7','8','9','/',
           '4','5','6','*',
           '1','2','3','-',
           '0','.','=','+']
    for i in zip(tests,positions): #将两个列表并列
        text=i[0]
        row=i[1][0]
        column=i[1][1]
        if text=='Cls':
            Button(root, text=text, width=8, command=lambda text=text: clear()).grid(row=row, column=column)
        elif text=='Bck':
            Button(root, text=text, width=8, command=lambda text=text: dell()).grid(row=row, column=column)
        elif text=='=':
            Button(root, text=text, bg='green', width=8, command=lambda text=text: calculate()).grid(row=row, column=column)
        else:
            Button(root, text=text, width=8, command=lambda text=text: userinput(text)).grid(row=row, column=column)
    root.mainloop()
main()
