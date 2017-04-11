#coding:gbk
import random

joker = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
JOKER = joker + joker + joker + joker
# 由于未算花色，因此先简单理解为四副A~K的牌，共52张
cards = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13}
#该字典用于对比大小
nums = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10}
#该字典用于计算点数
gongpai = ["J","Q","K"]
n_num = 0
n_dian = 0
player="player"

def create_cards():                       #发牌
    cards=[]
    a = random.choice(JOKER)
    JOKER.remove(a)
    cards.append(a)
    b = random.choice(JOKER)
    JOKER.remove(b)
    cards.append(b)
    c = random.choice(JOKER)
    JOKER.remove(c)
    cards.append(c)
    return cards

def player_cards_n(n):                    #生成n副玩家牌
    global dict
    dict={}
    for i in range(n):
        dict[player+str(i)] = create_cards()
    return dict

def dianshu(n=["A","2","3"]):                 #判断点数
    n_num = nums[n[0]] + nums[n[1]] + nums[n[2]]
    n_dian = n_num % 10
    return n_dian

def judge(n=["A","2","3"]):                 #2代表大小三公，1代表混三公，0代表单牌
    if n[0]==n[1]==n[2]:
        return [2,cards[n[0]]]
    elif n[0] in gongpai and n[1] in gongpai and n[2] in gongpai:
        return [1,0]
    else:
        m = dianshu(n)
        return [0,m]

def compare(player0=[0,2],player1=[0,0]):
    if player0[0]>player1[0]:
        return "庄家赢"
    elif player0[0]<player1[0]:
        return "闲家赢"
    else:
        if player0[0]==1:
            return "平局"
        else:
            if player0[1]==player1[1]:
                return "平局"
            elif player0[1]>player1[1]:
                return "庄家赢"
            elif player0[1]<player1[1]:
                return "闲家赢"

game = "游戏说明"
Introduction = "三公游戏：三公游戏利用一副扑克牌中的52张牌（大小王除外），其中牌张A－9之间的这些牌为点数牌对应\n数字1-9，" \
               "牌张10为0点牌，牌张J、Q、K、为公牌。系统给每位玩家发完三张牌后，庄家与闲家互相比较牌的\n大小，" \
               "并根据牌型判断庄闲的输赢。其中player0是庄家，其余均为闲家。"
print game.center(100)
print Introduction
while True:
    ipt = raw_input("开始&退出Y/N\n")
    if ipt == 'Y' or ipt == 'y':
        n = input("请输入玩家人数（1~6）：")
        players_dict=player_cards_n(n)
        if n==1:
            com = create_cards()
            print "player0的牌是：",players_dict["player0"]
            print "电脑的牌是：",com
            print "庄家player0与闲家电脑的输赢是：",compare(judge(players_dict["player0"]),judge(com))
        else:
            for i in range(n):
                any = raw_input("请决定"+player+str(i)+"的玩家Y")              #可供玩家们选择玩家顺序
                print player+str(i)+"的牌是：",players_dict[player+str(i)]
            for i in range(1,n):
                print "以下是庄家和闲家的输赢结果："
                print "庄家player0与闲家"+player+str(i)+"的输赢是：",compare(judge(players_dict["player0"]),judge(players_dict[player+str(i)]))
    elif ipt == 'N' or ipt == 'n':
        print "游戏结束！谢谢参与！"
        break
