'''
练习1-12
'''
# 递归解法
def func(n,position):
    if position == 1 or position==n:
        return 1
    else:
        return func(n-1,position-1)+func(n-1,position)
print(func(5,2))

# 迭代解法
def func2(n):
    # pre = 1
    if n == 1:
        return 1
    list_p = [1,1]
    count = 2
    while count < n+1:
        list_a = []
        for i in range(count):
            if i == 0:
                list_a.append(1)
                continue
            elif i == count-1:
                list_a.append(1)
                continue
            else:
                list_a.append(list_p[i-1]+list_p[i])
        print(list_a)
        list_p = list_a
        # print(list_p)
        count += 1
    return list_p

print(func2(3))
