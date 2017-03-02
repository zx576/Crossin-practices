
def level_num(x,init_num = 0):
    if x < 10:
        return init_num*10+x
    else:
        return level_num(x//10,init_num*10+x%10)

def compare(pre_num,after_num):
    if pre_num == after_num:
        return True
    else:
        return False

def accumulate(x,init_sum=0):
    if x < 10:
        return init_sum+x
    else:
        return accumulate(x//10,init_sum+x%10)

def main(n):
    for i in range(10000,1000000):
        level_i = level_num(i)
        if compare(i,level_i):
            level_sum = accumulate(i)
            if compare(level_sum,n):
                print(i)

main(52)
