# -*- coding: utf-8 -*-

#coding:utf-8
import threading
threads=[]
def woca(args1):
    print("我擦%r"%args1)
def wori(args2):
    print("沃日%r"%args2)
t1=threading.Thread(target=woca,args=(1,))
t2=threading.Thread(target=wori,args=[2])
threads.append(t1)
threads.append(t2)
print (threads)
for t in threads:
    # t.setDaemon(True)
    t.start()
# for i in threads:
#     i.join()
print ('所有线程执行完毕')