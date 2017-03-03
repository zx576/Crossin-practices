# coding=utf-8
import random
def load_dict_from_open(data):
    _dict={}
    try:
        with open(data,'r') as dict_data:
            for line in dict_data:
                (Cname,Ename)=line.strip().split(':')
                _dict[Cname]=Ename
    except IOError as ioerr:
        print "file %s is not exist"%(data)
    return _dict
if __name__=='__main__':
    _dict=load_dict_from_open('data.txt')
    print _dict
    print _dict.keys()

def WordGuess():
   word =random.choice(_dict.keys())
   s=_dict.get(word)
   print word
   print s
   return word

print WordGuess()


userinput=input("input the name in English:")
if _dict.get(random.choice(_dict.keys()))==userinput:
    print "Bingo"
else:
    print "Wrong"



def func1():
    return 1

def func2(x):
    return x + 1

t = func1
r = func2(t)
print(r)
