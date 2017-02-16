
'''
牛顿逼近求解平方根，立方根
2017.2.13
'''

def sqrt(x):
    # init_value = 1
    # af_value = x
    accuracy = 0.000001
    pre_value =1
    while True:
        # pre_value = af_value
        quotient = x/pre_value
        af_value = (quotient+pre_value)/2
        if 0 <  pre_value - af_value < accuracy:
            break
        pre_value = af_value

        print(af_value)

    return af_value

# a = sqrt(3)
# print(a)
# 求立方根
def li(x):
    pre_value = 90
    accuracy = 0.00001
    while True:
        af_value = (x/(pre_value*pre_value)+2*pre_value)/3
        if 0 <  pre_value - af_value < accuracy:
            break
        pre_value = af_value
        print(af_value)

    return af_value

a = li(8)
print(a)
