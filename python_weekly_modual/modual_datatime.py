#-*- coding:utf-8 -*-
from datetime import *

# print(datetime.MINYEAR)
# print(datetime.MAXYEAR)
# print(datetime.date(2017,3,5))
# print(datetime.time(14,20,50,20))
# print(datetime.datetime(2017,3,3,14,20,50,20))

# date_a = datetime.date(2017,3,5)
# date_b = datetime.date(2017,6,1)


'''
datetime
    datetime # 类似于 date 类，只是多了 hour - minute - second
        now()
        today() # 2017-03-03 16:32:54.852666

    time # 处理 hour - minute - seconds


    timedelta
        min
        max
        total_seconds
    date
        today() # 2017-03-03
        fromtimestamp(0)
        fromordinal(999999)
        属性：
        .year
        .month
        ..
        .replace(day,month,year)
        .weekday() # 返回日期实例是本周第几天，0-mon 6-sun

'''
# print(datetime.datetime.now())
# timedelta 表示一段时间
# diff = datetime.timedelta(microseconds = -1)
# print(diff)

# print(date.today())
# # 从 1970 开始算起  >>> 1970-01-01
# print(date.fromtimestamp(0))
#
# print(date.fromordinal(999999))
# a = date.today()
# print(b)
#
# print(a.min)
# print(a.replace(day=1))
# print(a.timetuple())
#
# print(a.weekday())

# a = datetime.today()
# print(a)
# b = datetime.utcnow()
# print(b)
# print(a-b)
#
# print(a.__str__())
# print(a.strftime())
# num1 = 10
# num2 = 20
# if num1 > num2:
#     print True
# else:
#     print False


# a = time(14,50)
# print(a)

a = date(2017,3,3)
c = a.__str__()
b = date.strftime(c,'%Y-%B-%d-%A')
print(b)














##############################################
