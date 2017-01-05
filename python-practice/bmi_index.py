#-*- coding:utf-8 -*-

# python3.5
#分别输入身高与体重
height = input('type in your height:')
weight = input('type in your weight:')
#算出bmi指数
bmi = weight / (height * height)

if bmi < 18.5:
    print('too light')
elif bmi > 24.5:
    print('too weight')
else:
    print('healthy')

#python2.7
#分别输入身高与体重
# height = input('type in your height:')
# weight = input('type in your weight:')
#算出bmi指数
# bmi = weight / (height * height)
# 判断并输出
# if bmi < 18.5:
#     print 'too light'
# elif bmi > 24.5:
#     print 'too weight'
# else:
#     print 'healthy'
