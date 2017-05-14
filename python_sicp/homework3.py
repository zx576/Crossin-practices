#-*- coding:utf-8 -*-

##第二题

def has_seven(k):
    if k < 10 :
        if k == 7:
            return True
        else:
            return False
    if k % 10 == 7:
        return True
    else:
        return has_seven(k // 10)


# print(has_seven(123456))


def has_seven2(k):
    if '7' in str(k):
        return True
    else:
        return False


## 第三题

def pingpong(n):

    status = 1
    num = 1
    count = 1
    while True:
        if count == n:
            return num

        if '7' in str(count) or count % 7 == 0:
            status = -1*status

        if status > 0:
            num += 1
        else:
            num -= 1

        count += 1


# print(pingpong(100))

##第四题




def change(lst,s,t):
    newl = []
    def link(*subl):
        if len(subl) > 1:
            if subl[0] == s:
                newl.append(t)
            else:
                newl.append(subl[0])
            return subl[1]

        else:
            if subl[0] == s:
                newl.append(t)
            else:
                newl.append(subl[0])
    eval(lst)
    return newl[::-1]

lst = 'link(1,link(2,link(3,link(4))))'

# print(change(lst,5,1))

# print(newl)
###question7



def unpack(lst):
    res = []
    for i in lst:
        if isinstance(i,list):
            res += unpack(i)
        else:
            res.append(i)

    return res

# res = unpack([[1, [1, 1]], 1, [1, 1]])
# print(res)

###question8

def riffle(deck):
    new = []
    len_l = int(len(deck)/2)
    # print()
    l1 = deck[:len_l]
    l2 = deck[len_l:]
    for i in range(len(deck)):
        if i%2 == 0:
            new.append(l1.pop(0))
        else:
            new.append(l2.pop(0))

    return new




def ri(deck):
    return [ deck[(i % 2) * len(deck)//2 + i // 2] for i in range(len(deck)) ]


# print(ri(list(range(20))))











#####################
