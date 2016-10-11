import random
import functools

#传入参数后，给每个人分配一个权重，然后累加权重得到每一份所占金额，最后根据权重分配金额
def allocation(money,people):
    #每人分得一个数字
    weight_per_person = [random.randint(1,10) for i in range(people)]
    #print(weight_per_person)
    #累加数字，得到总和
    weight = functools.reduce(lambda x,y:x+y ,weight_per_person)
    #print(weight)
    #每一份占比
    money_per_weight = money/weight
    #每人占比
    money_per_person = [round(money_per_weight * i,2) for i in weight_per_person]
    return money_per_person

#将总金额按随机数一次次减少，最后打乱结果
def allocation_2(money,people):
    mon = 0
    money_per_person = []
    remain_people = people
    for i in range(people):
        remain_people -= 1
        #print(remain_people)
        if remain_people >0:
            mon = random.randint(1, money-remain_people)
            #print(mon)
        else:
            mon = money
        money_per_person.append(round(mon/100,2))
        money = money - mon
    random.shuffle(money_per_person)
    return money_per_person

def start():
    print('how much money :')
    money = int(input('>>>'))
    print('how many people:')
    people = int(input('>>>'))
    print('1.allocation1,2.allocation2')
    while True:
        choice = input('>>>')
        if choice == '1':
            print(allocation(money,people))
            break
        elif choice == '2':
            print(allocation_2(money*100,people))
            break
        else:
            print('iuput 1 or 2')
while True:
    start()

