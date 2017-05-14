#-*- coding:utf-8 -*-
import random

#输入模块，1.在程序运行过程中任何时候输入exit可退出，2.判断数字
def input_Num():
    while True:
        yournum = input('>>>>>>')
        if yournum == 'exit':
            exit_game()
        else:
            try:
                yournum = int(yournum)
                break
            except:
                print('invalid number')
                pass
    return yournum
#记录模块，传入文件打开方式以及猜数字结果以便处理
def recode(open_ways,times):
    with open('guess.txt', open_ways) as f:
        result = str(times)
        if result:
            print('您本次游戏共猜了%s次' % (result))
            f.write(result)
            f.write('\n')
#读取recode文件并输入结果
def output():
    total = 0
    fre = 0
    averge = 0
    with open('guess.txt', 'r') as f:
        for time in f.readlines():
            if time:
                total += int(time)
                fre += 1

    averge = total / fre

    print('在游戏中您一共猜了%d次' % (total))
    print('游戏进行了%d轮' % (fre))
    print('平均每次游戏您要猜%0.2f次' % (averge))

#猜数字游戏主体，传入limit参数，控制猜数字次数
def Guess_Num(limit):
    print('the set-number is between 0-99,type in a number')
    times = 0
    while times < limit:
        outcome = input_Num()
        times += 1
        if setnum == outcome:
            print('congratulations,you win')
            return times
        elif setnum > outcome:
            print('%d is too small,try again' %(outcome))
        elif setnum < outcome:
            print('%d is too large,try again'%(outcome))
    print('times up')


#模式选择
def Mode_choose():
    print('choose a mode to play')
    print('1.easy,2.hard')
    while True:
        outcome = input_Num()
        if outcome == 1:
            #10000000等同于无限次
            return 10000000
        elif outcome == 2:
            #有限次猜数字
            print('input a limit number which is less than 10')
            limit = input_Num()
            return limit

#退出游戏模块
def exit_game():
    print('looking forward to coming back,have fun')
    exit()
#开始游戏，返回文件打开方式
def start():
    print('welcome to the game...')
    print('choose game mode: 1.new game,2.continue game,3.exit game')
    while True:
        outcome = input_Num()
        if outcome == 1:
            #写 模式打开文件，等同于新游戏
            return 'w'
        elif outcome == 2:
            #添加 模式打开问价，等同于存档模式
            return 'a'
        elif outcome == 3:
            exit_game()
        print('type in 1 or 2 or 3')

#游戏主体逻辑关系
def main():
    global setnum
    setnum = random.randint(0, 100)
    #开始游戏
    outcome =start()
    #选择模式
    mode = Mode_choose()
    #进入游戏
    result = Guess_Num(mode)
    #猜对了，返回结果并输出，然后进入下一个循环
    if result:
        recode(outcome,result)
        output()
    #猜错了，不记录人文件，进入下一个循环
    else:
        pass
    print('please continue game...')

#游戏循环
while True:
    main()







