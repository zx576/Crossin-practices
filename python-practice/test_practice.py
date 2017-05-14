# -*- coding: utf-8 -*-
#python3.5
# def fib():
#     n = input('>>>')
#     try:
#         n = int(n)
#     except:
#         print('输入数字')
#         return
#     if n < 3:
#         print('数字要大于3')
#         return
#     else:
#         a = 0
#         b = 1
#         for i in range(n):
#             print(b)
#             a ,b = b,a+b
#
# fib()
# a = 'adfgh'
# b = a.replace('f','e')
# print(b)

# windows 下如果出现编码问题，将 utf-8 改为 cp936
# import os
#
# def findfile(key, inputdir='.'):
#     found_list = []
#     # os.walk 获取指定目录下的所有深度的文件、子目录的列表
#     for path, dirnames, filenames in os.walk(inputdir):
#         print('searching', path, '...')
#         for name in filenames:
#             full_name = path + '/' + name
#             if key in name:  # 如果文件名中有关键字
#                 found_list.append(full_name)
#             with open(full_name) as f:
#                 for l in f.readlines():
#                     if key in l:  # 如果当前行中有关键字
#                         found_list.append(full_name + ' : ' + l)
#     return found_list
# # errors = 'ignore',encoding='utf-8'
#
# # 输入搜索关键字和路径
# keyword = input('search:')
# path = input('in:')
# if not path.strip():
#     path = '.'
#
# result = findfile(keyword, path)
# #
# print('\n========== result ===========\n\n')
# for r in result:
#     print(r)

# import os
# a = os.walk('E:\GIT\practice\Crossin-practices\old_practice')
# for i,j,k in a:
#     print(i,j,k)
# a1=1
# a2=1
# i=2
# fib=[1,1]
# n=input('input a numer(>3):')
# n = int(n)
# if n>3:
#     while i != n:
#         a=a1+a2
#         fib.append(a)
#         a1=a2
#         a2=a
#         i += 1
# else:
#     print('please input a integer which >3')
#
# for k in range(1,n):
#     print(fib[k-1])

# import requests
#
# resp = requests.get(url)
#
# result = resp.json()
#
# result_data = result.get('data')
# # print result_data
#
# if result_data:
#     print '当前温度：', result_data.get('wendu'), '℃'
#     print '空气质量：', result_data.get('aqi')
#     print result_data.get('ganmao')
#     # print result_data.get('ganmao').decode('utf-8').encode('gbk')  # windows 编码参考
#
#     print '5日天气预报：'
#     forecast = result_data.get('forecast')
#     for fc in forecast:
#         print fc.get('date'), '：', fc.get('type'), '，', fc.get('low'), '，', fc.get('high')
# else:
#     print '未能获取此城市的天气情况。'
# print
# import random
# l1=range(65,91)
# l2=range(97,123)
# lst=l1+l2
# FinalCoupon=set()
# print 'Your Coupon:'
# while len(FinalCoupon)<200:
#     Coupon=set()
#     while len(Coupon)<8:
#         Coupon.add(chr(random.choice(lst)))
#     Coupon="".join(Coupon)
#     FinalCoupon.add(Coupon)
# for i in FinalCoupon:
#     print i

# dic = {'s':1,'a':{3:4}}
# #得到1
# a = dic['s']
# #得到4
# b = dic['a'][3]
#
# print(a,b)、

# import gzip
# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# import random
# import string                           # 导入random,string模块
# lst = string.ascii_letters              # 构建大小写字母列表
# FinalCoupon = set()                     # 设置存放优惠券的列表为set集合去重
# print('Your Coupon:')
# while len(FinalCoupon) < 200:           # 检测存放优惠券的列表长度小于200继续生成
#     Coupon = set()                      # 设置存放优惠券每一位的列表为set集合去重
#     while len(Coupon) < 8:              # 检测优惠券长度小于200继续生成
#         Coupon.add(random.choice(lst))  # 字母列表里随机选取一个添加至优惠券末尾
#     Coupon = "".join(Coupon)            # 长度为8后，拼接字母为优惠券
#     FinalCoupon.add(Coupon)             # 优惠券生成后，添加至存放列表的末尾
# for i in FinalCoupon:
#     print(i)

#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import random
# import string
# #  构建大小写字母列表
# lst = list(string.ascii_letters)
# #  设置存放优惠券的列表为set集合去重
# FinalCoupon = set()
# print('Your Coupon:')
# #  检测存放优惠券的列表长度小于200继续生成
# while len(FinalCoupon) < 200:
#     #  取到8个不相同的字符
#     s = random.sample(lst,8)
#     #  拼接
#     Coupon = "".join(s)
#     # 优惠券生成后，添加至存放列表的末尾
#     FinalCoupon.add(Coupon)
# #  打印
# for i in FinalCoupon:
#     print(i)

# lst = string.ascii_letters
# a = random.sample(lst,8)
# b = ''.join(a)
# print(a)
# print(b)

# class Olympic(object):
#     def __init__(self,country,gold,silver,bronze):
#         self.country = country
#         self.gold = gold
#         self.silver = silver
#         self.bronze = bronze
#     def get_place(self,place):
#         if place == 1:
#             self.gold += 1
#         elif place == 2:
#             self.silver += 1
#         else:
#             self.bronze += 1
#     @property
#     def count(self):
#         return self.gold + self.silver + self.bronze
#
#     def __str__(self):
#         return '%s:金牌：%d,银牌：%d,铜牌：%d,总奖牌：%d'%(self.country,self.gold,self.silver,self.bronze,self.count)

# import base64
#
# TEST_URL = 'thunder://QUFodHRwOi8vZGxkaXIxLnFxLmNvbS9xcWZpbGUvcXEvUVE4LjMvMTgwMzgvUVE4LjMuZXhlWlo='
#
#
# def crack_thunder(thunder_url):
#     thunder_url = thunder_url.strip()
#     # 为了提升代码的鲁棒性，我们先把输入两边的空白字符过滤掉。
#     assert thunder_url[:10] == 'thunder://'
#     # 首先我们要判断这个链接是不是迅雷链接
#     base64_str = thunder_url.split('thunder://')[1]
#     # 然后我们把后边的base64字符串部分提取出来
#     print(base64_str)
#     assert base64_str
#     org_str = base64.b64decode(base64_str).decode('gbk')
#     # 在这里，需要注意，Python 3 里的全部使用unicode来表示字符串。
#     # 而 base64.b64decode 返回的是 'bytes'，因此需要转换一下
#     assert org_str[:2] == 'AA' and org_str[-2:] == 'ZZ'
#     # 同样，我们要检查解密出来的字符串是否是合法的迅雷下载地址。
#     print(org_str)
#     return org_str[2:-2]
#
# if __name__ == '__main__':
#     print(crack_thunder(TEST_URL))
import unittest


class Dog:
    '''我们实现了一个“狗狗”类，它有几个方法和属性'''

    def __init__(self, name):
        self.name = name
        self.age = 1

    def bark(self):
        return 'My name is ' + self.name

    def grow_up(self, k):
        self.age += k

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name


class TestDog(unittest.TestCase):

    def setUp(self):
        '''每次测试前，都会调用这个函数，我们每次都新建一个狗狗对象'''
        print('Test begin!')
        self.mydog = Dog('Bob')

    def tearDown(self):
        '''每次测试后，调用这个函数，你可以在此时释放一些资源。'''
        print('Test over!')

    # 注意，所有测试方法都要以test开头，这样单元测试模块会自动调用这些方法
    def testBark(self):
        # 我们测试这只狗“叫”得是否正常
        self.assertTrue(self.mydog.bark().startswith('My name is'))
        # 我们使用单元测试模块提供的assert方法，而不是Python内建的assert
        self.assertTrue(self.mydog.bark().endswith(self.mydog.get_name()))

    def testAge(self):
        # 我们测试这只狗生长速度是否正常
        old_age = self.mydog.get_age()
        self.mydog.grow_up(3)
        self.assertEqual(old_age + 3, self.mydog.get_age())


if __name__ == '__main__':
    unittest.main()
    # 运行测试
    # 我们这里只是做了个简单示范，一般建议测试代码和程序代码分离。