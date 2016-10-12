import random
import functools

#传入参数后，给每个人分配一个权重，然后累加权重得到每一份所占金额，最后根据权重分配金额
def allocation(money,people):
    #每人分得一个数字
    weight_per_person = [random.randint(1,100000) for i in range(people)]
    #print(weight_per_person)
    #累加数字，得到总和
    weight = functools.reduce(lambda x,y:x+y ,weight_per_person)
    #print(weight)
    #每一份占比
    money_per_weight = money/weight
    #每人占比
    money_per_person = [round(money_per_weight * i,2) for i in weight_per_person]
    #print(money_per_person)
    #累加前n-1个数值
    total_n1 = functools.reduce(lambda x, y: x + y, money_per_person[:-1])
    #用总金额减去前n-1个数值之和，得到最后的红包金额
    money_per_person[-1] = round(money - total_n1, 2)
    #print(money_per_person)
    #为防止有红包金额为0，进行检查
    for i in range(len(money_per_person)):
        #如果有金额为0，则将其调整为0.01
        if money_per_person[i] < 0.01:
            money_per_person[i] += 0.01
            #同时将其他金额大于0.01的数减去0.01，保证总金额不变
            for j in range(len(money_per_person)):
                if money_per_person[j]  > 0.01:
                    money_per_person[j] -= 0.01
                    break
    #检查总金额是否匹配
    #total = functools.reduce(lambda x, y: x + y, money_per_person)
    #print('%0.02f'%total)
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
    while True:
        print('输入您要发出的红包总额 :')
        money = eval(input('>>>'))
        print('输入您要发出的红包个数:')
        people = eval(input('>>>'))
        if money/people >= 0.01:
            break
        else:
            print('金额过小或者个数太多，重新输入吧')

    print('选择分配方式：1.方式1,2.方式2')
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

