#coding:utf-8
import random
def shifouhunsangong(n=["A","2","3"]):
    gongpai = ["J","Q","K"]
    if n[0] in gongpai and n[1] in gongpai and n[2] in gongpai:
        return True
    else:
        return False

def shifouxiangtong(m=["A","2","3"]):
    if m[0]==m[1]==m[2]:
        return True
    else:
        return False

def shifoudanpai(n=["A","2","3"]):        #判断是否单牌的函数
    gongpai = ["J","Q","K"]
    if n[0] not in gongpai:
        return True
    elif n[1] not in gongpai:
        return True
    elif n[2] not in gongpai:
        return True
    else:
        return False

def sangongbijiao(player1=["A","2","3"],player2=["A","2","3"]):              #2代表庄赢，1代表闲赢，0代表平局
    cards = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13}
    nums = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10}
    if shifouxiangtong(player1):                 #判断玩家1是否三张牌相同，然后比大小
        if shifouxiangtong(player2):
            if cards[player1[0]]>cards[player2[0]]:
                return 2
            else:
                return 1
        elif not shifouxiangtong(player2):
            return 2
    elif shifouxiangtong(player2):               #若玩家1三张牌不相同，而玩家2三张牌相同
        return 1
    else:
        if shifouhunsangong(player1):            #判断玩家1是否三公
            if shifouhunsangong(player2):
                return 0
            if shifoudanpai(player2):
                return 2
        elif shifouhunsangong(player2):
            return 1
        elif  shifoudanpai(player1):
            player1_num = nums[player1[0]] + nums[player1[1]] + nums[player1[2]]
            player2_num = nums[player2[0]] + nums[player2[1]] + nums[player2[2]]
            player1_dian=player1_num % 10
            player2_dian = player2_num % 10
            if player1_dian > player2_dian:
                return 2
            if player1_dian < player2_dian:
                return 1
            if player1_dian == player2_dian:
                return 0

joker = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
JOKER = joker+joker+joker+joker
#由于未算花色，因此先简单理解为四副A~K的牌，共52张
cards = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13}
#该字典用于对比大小
nums = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10}
#该字典用于计算点数
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

if sangongbijiao(player1,player2)==2:
    print "player1 win"
if sangongbijiao(player1,player2)==1:
    print "player2 win"
if sangongbijiao(player1,player2)==0:
    print "Deuce!"
