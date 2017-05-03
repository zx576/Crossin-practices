a# import threading
#
# def func():
#     threads = []
#     for i in range(5):
#         t = threading.Thread(target=innerfunc)
#         threads.append(t)
#
#     for i in threads:
#         i.start()
#
# def innerfunc():
#     print('xx')
#
#
# threads = []
# for i in range(5):
#     t = threading.Thread(target=func)
#     threads.append(t)
#
# for i in threads:
#     i.start()

list1 = [1,30,2,5,4]

# list1[5] = list1[4] + list1[3]
#
# count = len(list1)
#
# for i in range(count):
#     print(list1[i],'=========')
#     for j in range(i+1,count):
#         print(list1[j])
#         if list1[i] < list1[j]:
#             list1[i],list1[j] = list1[j],list1[i]
#             print(list1)
#
# print(list1)
def quickSortPython(l):
    print(l)
    assert(type(l)==type(['']))
    length = len(l)
    if length==0 or length==1:
        return l
    if len(l)<=1:
        return l
    left = [i for i in l[1:] if i>l[0]]
    right = [i for i in l[1:] if i<=l[0]]
    return quickSortPython(left) +[l[0],]+ quickSortPython(right)
print(quickSortPython(list1))
