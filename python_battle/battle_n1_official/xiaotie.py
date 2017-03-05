#coding:utf-8
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
    elif you == 1 and computer ==3 or you == 2 and computer == 1 or you == 3 and computer == 2:
        return 1
    else:
        return 2


def play():
    count = 0
    yourscore = 0
    computerscore = 0
    while (count < 3):

        you = input('You choice:1.Rocl 2.Paper 3.Scissor')
        computer = random.randint(1, 3)
        result = gamer(you, computer)

        count += 1
        print"your finger is %s and computer's finger is %s " % (guess(you), guess(computer))
        if result == 2:
            computerscore += 1
            print 'Computer Score:%d'%(computerscore)

        elif result == 1:
            yourscore += 1
            print 'You Score:%d'%(yourscore)

        elif result == 0:
            print 'Tied'
    if yourscore == computerscore :
        print 'The game ended up in a tie'
    elif yourscore > computerscore :
        print 'You Win with score %d!'%(yourscore)
    else:
        print 'Computer Win with score %d!'%(computerscore)





if __name__=="__main__":
    play()


print 'The end!'
