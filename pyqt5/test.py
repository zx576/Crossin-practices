i = 0
# 循环开始，一共5次
while i < 5:
   i += 1
   for j in range(3):
       print('这是j',j)
       if j == 2:
           break
   for k in range(3):
       if k == 2:
           continue
       print('这是k',k)
   if i > 3:
       break
   print('这是i',i)

# i += 1
# for j in range(3):
#     print(j)
#     if j == 2:
#         break
# for k in range(3):
#    if k == 2:
#        continue
#    print(k)
# if i > 3:
#     break
# print(i)
# i = 0
# while i < 5:
#    i += 1
#    for k in range(3):
#        if k == 2:
#            continue
#        print(k)
