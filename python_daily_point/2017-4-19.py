import random
import math
people = int(input('红包个数:\n'))
money = float(input('总金额:\n'))
money = int(money * 100)
print(money)


def main(people, money):
    result = []
    remain = people
    for i in range(people):
        stop = int(min(money - remain, money / remain * 2))
        print(stop)
        if remain > 1:
            m = random.randint(1, stop)
        else:
            m = money
        result.append(m / 100)
        money -= m
        remain -= 1
    return result

if __name__ == '__main__':
    print(main(people, money))
