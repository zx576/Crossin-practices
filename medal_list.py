#-*- coding:utf-8 -*-

class medal(object):
    def __init__(self,country,gold,sliver,bronze):
        self.country = country
        self.gold = gold
        self.sliver = sliver
        self.bronze = bronze

    def medal_list(self,mark):
        if mark == '1':
            self.gold += 1
        elif mark == '2':
            self.sliver += 1
        elif mark == '3':
            self.bronze += 1

    @property
    #装饰器 此时count = property(count) 作用是将方法视作属性，这里可以调用medal.gold
    #medal.sliver,medal.bronze 等
    def count(self):
        return self.gold + self.sliver + self.bronze
    #直接print(medal)可调用此函数
    def __str__(self):
        return '%s:gold:%d;sliver:%d;broze:%d;total:%d' %(self.country,self.gold,self.sliver,self.bronze,self.count)


CHN = medal('中国',45,16,50)
US = medal('美国',50,2,10)
UK = medal('英国',12,13,14)
print(CHN)
print(US)
print(UK)
print(CHN.gold)
print('美国获得冠军')
US.medal_list('1')
print(US)
medallist = [CHN,US,UK]
print(medallist)
print('按金牌排序')
#sorted函数使用方法，传入三个变量，返回排序后的list
newlist = sorted(medallist,key=lambda x:x.gold, reverse=True)
for i in newlist:
    print(i)
print('按总数排序')
newlist_2 = sorted(medallist,key=lambda x:x.count, reverse=True)
for i in newlist_2:
    print(i)