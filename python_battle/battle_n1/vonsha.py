# coding=utf-8
open ('data.txt')

f=open('data.txt')
lines = f.readlines()
print lines
for line in lines:
    fruits=line.split(':')
    print fruits

    Cname=str(fruits[0])
    Ename=str(fruits[1])
    print '%s:%s\n'%(Cname,Ename)
    try:
        if fruits==['','']:
            print fruits
    except:
        print 'list not exists'



choice = raw_input('1,开始，2.退出')
times=0
word=raw_input('请输入水果名：')
words = {}
words[fruits[0]] = [fruits[1]]
print words
while choice=='1':
    times+=1
    s=words.get(fruits[1])
    if word is None:
        print 'there is no such match!'
    elif word==s:
        print 'next'
    else:
        print 'Not correct!'
    if times>5:
        print 'You have two choices:1， restart； 2，correct the mistakes'
        break
