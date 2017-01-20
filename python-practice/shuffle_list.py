#-*- coding:utf-8 -*-
#python3.5
import random
def allocate():
    list_h = ['A','B','C','D']
    list_s = range(1,14)
    all = ['dw','xw']
    for i in list_h:
        for j in list_s:
            all.append(i+str(j))
    random.shuffle(all)
    list_d = []
    # for i in range(3):
    a = random.sample(all,3)
    player1 = []
    player2 = []
    player3 = []
    for i in a:
        all.remove(i)
        list_d.append(i)
    for m in range(51):
        if m % 3 == 0:
            player1.append(all[m])
        elif m % 2 == 0:
            player2.append(all[m])
        else:
            player3.append(all[m])

    print(player1,'\n',player2,'\n',player3,'\n',list_d)
    # print(len(player1),len(p))
allocate()