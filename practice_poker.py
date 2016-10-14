import random
colors = ['Heart','Spade','Diamond','Club']
points = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
def generate_poker():
    pokers = ['RedJoker', 'BlackJoker']
    for i in colors:
        for j in points:
            n = i+j
            pokers.append(n)
    #print(pokers)
    return pokers
def allocation():
    obj_a = []
    obj_b = []
    obj_c = []
    poker = generate_poker()
    random.shuffle(poker)
    hole_cards = [poker[51],poker[52],poker[53]]
    for i in range(0,51):
        if i % 3 == 0:
            obj_a.append(poker[i])
        elif i % 3 == 1:
            obj_b.append((poker[i]))
        else:
            obj_c.append(poker[i])

    print('玩家一的手牌:',obj_a)
    print('玩家二的手牌:',obj_b)
    print('玩家三的手牌:',obj_c)
    print('底牌:',hole_cards)

allocation()
