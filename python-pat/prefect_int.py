'''
完美数

'''
# 判断是否为完美数
def perfect_word(n):
    if n == 1:
        return True
    for i in [2,3,5]:
        # print(type((n/i)*10))
        if n//i == n/i:
            return perfect_word(n//i)
        else:
            continue
    return False

# 循环
def main(n):
    count = 0
    inc_int = 0
    while count < n:
        inc_int += 1
        if perfect_word(inc_int):
            # print(inc_int)
            count += 1
    return inc_int

print(main(11))
