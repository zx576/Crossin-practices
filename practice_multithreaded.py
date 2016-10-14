#-*- coding:utf-8 -*-
import threading
import time

#单线程
def s1():
    print('单线程1开始时间：' ,time.ctime())
    time.sleep(4)
    print('单线程1结束时间：',time.ctime())

def s2():
    print('单线程2开始时间：',time.ctime())
    time.sleep(2)
    print('单线程2结束时间：',time.ctime())
def single_thread():
    print('单线程测试开始...')
    s1()
    s2()


#多线程测试
def s3(loopnum,t):
    print('多线程',loopnum,'开始时间：',time.ctime())
    time.sleep(t)
    print('多线程',loopnum,'结束时间：',time.ctime())
def multi_threads():
    print('多线程开始执行')
    threads = []
    times = [4,6]
    for i in range(len(times)):
        thr = threading.Thread(target = s3,args = (i,times[i]))
        threads.append(thr)
    for i in range(len(times)):
        threads[i].start()
    for i in range(len(times)):
        threads[i].join()
    print('多线程执行结束')






single_thread()
time.sleep(2)
multi_threads()
