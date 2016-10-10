import random
setnum = random.randint(0, 100)
#输入数字并判断
def inputnum():
    yournum = input('type in a number:')
    try:
        yournum = int(yournum)
    except:
        print('输入的不是数字哦')
        GuessNum()
    return yournum
# 猜一次的函数
def GuessNum():
    times = 0
    print('1.选择困难模式，2.选择一般模式')
    mode = input('>>>>')
    if mode == '1':
        print('您自己设定一个小于10的最大次数吧')
        t = inputnum()
        print('设定的数字在0-99之间，游戏开始咯')
        while times < t:
            times += 1
            yournum = inputnum()
            if setnum == yournum:
                print('right number')
                break
            elif setnum > yournum:
                print('try a bigger number')
            elif setnum < yournum:
                print('try a lesser number')
        print('次数用光了,重新开始吧！')
        GuessNum()
    elif mode == '2':
        print('设定的数字在0-99之间，游戏开始咯')
        while True:
            times += 1
            yournum = inputnum()
            if setnum == yournum:
                print('right number')
                break
            elif setnum > yournum:
                print('try a bigger number')
            elif setnum < yournum:
                print('try a lesser number')
    else:
        GuessNum()
    return times
# 记录游戏
def recode():
    res = startgame()
    with open('guess.txt', res) as f:
        result = str(GuessNum())
        print('您本次游戏共猜了%s次' % (result))
        f.write(result)
        f.write('\n')
#输出游戏
def output_recode():
    recode()
    total = 0
    fre = 0
    averge = 0
    with open('guess.txt', 'r') as f:
        for time in f.readlines():
            if time:
                total += int(time)
                fre += 1
    averge = round(total / fre, 2)

    print('在游戏中您一共猜了%d次' % (total))
    print('游戏已经进行了%d轮' % (fre))
    print('平均每次游戏您要猜%d次' % (averge))
#退出游戏
def exit_game():
    print('欢迎再次启动游戏，再见')
    exit()
#开始游戏
def startgame():
    print('starting game...')
    print('1.新建游戏，2.继续游戏，3.退出')
    choice = input('>>>>')
    if choice == '1':
        return 'w'
    elif choice == '2':
        return 'a'
    else:
        exit_game()
#启动游戏		
while True:
    output_recode()

