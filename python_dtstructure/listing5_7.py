# coding : utf-8
import random


# sorting methods

# insertion

lst = [i for i in range(10)]
random.shuffle(lst)

# print(lst)

def insertionsort(lst):
    length = len(lst)
    for i in range(1,length):
        value = lst[i]
        pos = i

        while pos > 0 and value < lst[pos -1]:
            print(lst)
            lst[pos] = lst[pos-1]
            print(lst)
            pos -= 1

        lst[pos] = value
        print('oneturn:',lst)



    return lst

insertionsort(lst)
