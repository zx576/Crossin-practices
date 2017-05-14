'''

'''

def sum_digit(n):
    if n < 10:
        return n
    else:
        last,all_but_last = n%10,n//10
        return sum_digit(all_but_last) + last

# print(sum_digit(1343254))


def cascade(x):
    if x < 10:
        print(x)

    else:
        print(x)
        cascade(x//10)
        print(x)

# cascade(2013)

def cascade2(x):
    print(x)
    if x > 10:
        cascade2(x//10)
        print(x)

# cascade2(2013)
def player_a(n):
    if n == 0:
        print('b win')
    elif n == 2:
        print('a win')

    else:
        player_b(n-1)

def player_b(n):
    if n == 0:
        print('a win')
    elif n % 2 == 0:
        player_a(n-2)
    else:
        player_a(n-1)

player_a(20)



















#3333333333333333333
