import queue
import threading


link = link.get('data-lazy', None) or link.get('src')

# def worker():
#     item = q.get()
#     print(item + 1)
#     return item + 1
#
# q = queue.Queue()
#
# for i in range(5):
#     q.put(i)
#
# # print(worker())
# # print(q.get())
# threads = []
# for i in range(4):
#     t = Thread(target=worker)
#     threads.append(t)
#
# for i in range(4):
#     threads[i].start()
#
# for i in range(4):
#     threads[i].join()
#
# # print(q.get(),q.get(),q.get(),q.get())
# q.put(5)
# while True:
#     if q.empty():
#         break
#     print(q.get())

# 向队列中添加元素
q = queue.Queue()
for i in range(5):
	q.put(i)

# 定义一个过程
def func():
	'''作用是从队列中获取值，然后打印'''
	item = q.get()
	print(item)

# 多线程处理
threads = []

for i in range(5):
	t = threading.Thread(target=func)
	threads.append(t)

for i in threads:
	i.start()

for i in threads:
	i.join()
