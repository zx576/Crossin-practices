#-*- coding:utf-8 -*-
import random


def guess(finger):
    if finger == 1:
        return 'Rock'
    elif finger == 2:
        return 'Paper'
    else:
        return 'Scissor'


def gamer(you,computer):
    if you == computer:
        return 0
    elif you == 1:
        if computer == 2:
            return 2
        else:
            return 1
    elif you == 2:
        if computer == 1:
            return 1
        else:
            return 2
    elif you == 3:
        if computer == 1:
            return 2
        else:
            return 1

def play():
    you = int(raw_input('Your Finger is:'))
    computer = random.randint(1, 3)
    result = gamer(you, computer)
    print"your finger is %s and computer's finger is %s " % (guess(you), guess(computer))
    if result == 2:
        print 'Computer Win'
    elif result == 1:
        print 'You Win'
    elif result == 0:
        print 'Tied'


while True:
    choice = raw_input('s or e')
    if choice == 's':
        play()
    elif choice == 'e':
        break
