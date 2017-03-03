# coding:utf-8
import random
# import sys
# reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
# sys.setdefaultencoding('gb18030')

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
    print(dict)

# def player_cards_n(n):                    #生成n副玩家牌
#     global dict
#     dict={}
#     for i in range(n):
#         dict[player+str(i)] = create_cards()
#     return dict
#
# players_dict = players_cards_n(n)



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

def dianshu(n=["A","2","3"]):                 #判断点数
    n_num = nums[n[0]] + nums[n[1]] + nums[n[2]]
    n_dian = n_num % 10
    return n_dian

def judge(n=["A","2","3"]):                 #2代表大小三公，1代表混三公，0代表单牌
    if n[0]==n[1]==n[2]:
        return [2,cards[n[0]]]
    if n[0] in gongpai and n[1] in gongpai and n[2] in gongpai:
        return [1,0]
    if shifoudanpai(n):
        m = dianshu(n)
        return [0,m]

def compare(player0=[0,2],player1=[0,0]):
    if player0[0]>player1[0]:
        print("庄家赢")
    if player0[0]<player1[0]:
        print("闲家赢")
    if player0[0]==player1[0]:
        if player0[0]==1:
            print("平局")
        else:
            if player0[1]==player1[1]:
                print("平局")
            if player0[1]>player1[1]:
                print("庄家赢")
            if player0[1]<player1[1]:
                print("闲家赢")


n = int(input("请输入玩家人数（大于等于2）："))
player_cards_n(n)
for i in range(n):
    print(player+str(i)+"的牌型是：",judge(dict[player+str(i)]))
for i in range(1,n):
    print("庄家player0与闲家"+player+str(i)+"的输赢是：",compare(judge(dict["player0"]),judge(dict[player+str(i)])))
