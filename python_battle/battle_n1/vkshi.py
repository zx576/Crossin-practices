# !python2
import random
def shifoudanpai(n=["A","2","3"]):
    gongpai = ["J","Q","K"]
    if n[0] not in gongpai:
        return True
    elif n[1] not in gongpai:
        return True
    elif n[2] not in gongpai:
        return True
    else:
        return False

joker = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
JOKER = joker+joker+joker+joker
cards = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13}
nums = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10}
gongpai = ["J","Q","K"]
shuzipai = ["A","2","3","4","5","6","7","8","9","10"]
player1 = []
player2 = []
player1_num = 0
player2_num = 0
player1_dian = 0
player2_dian = 0

random.shuffle(JOKER)

for i in range (0,6):
    if (i+1)%2 == 1:
        player1.append(JOKER[i])
    else:
        player2.append(JOKER[i])
print "player1:",player1
print "player2:",player2

if cards[player1[0]]==cards[player1[1]]==cards[player1[2]]:
    if cards[player2[0]]==cards[player2[1]]==cards[player2[2]]:
        if cards[player1[0]]>cards[player2[0]]:
            print "player1 win!"
        else:
            print "player2 win!"
    elif cards[player2[0]]!=cards[player2[1]]:
        print "player1 win!"
elif cards[player2[0]]==cards[player2[1]]==cards[player2[2]]:
    print "player2 win!"
else:
    if player1[0] in gongpai and player1[1] in gongpai and player1[2] in gongpai:
        if player2[0] in gongpai and player2[1] in gongpai and player2[2] in gongpai:
            print "deuce"
        if shifoudanpai(player2):
            print "player1 win!"
    elif player2[0] in gongpai and player2[1] in gongpai and player2[2] in gongpai:
        print "player2 win!"
    elif  shifoudanpai(player1):
        player1_num = nums[player1[0]] + nums[player1[1]] + nums[player1[2]]
        player2_num = nums[player2[0]] + nums[player2[1]] + nums[player2[2]]
        player1_dian=player1_num % 10
        player2_dian = player2_num % 10
        if player1_dian > player2_dian:
            print "player1 win!"
        if player1_dian < player2_dian:
            print "player2 win!"
        if player1_dian == player2_dian:
            print "deuce"
