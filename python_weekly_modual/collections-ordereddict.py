


import collections
dic = {'c':1,'a':2,'b':3}
# sorted_tuple = sorted(dic.items(),key=lambda x:x[0])
new_dic = collections.OrderedDict(dic)
print(new_dic)
#
# d = {}
# d['a'] = 1
# d['b'] = 2
# d['c'] = 3
# print(d)


# 提取 items
# print (new_dic.items())
# # 提取 keys
# print(new_dic.keys())
# # 提取 values
# print(new_dic.values())
# # 复制 字典
# print(new_dic.copy())
# popitem
# print(new_dic.popitem())
# print (new_dic)
# move_to_end()
# print(new_dic)
# new_dic.move_to_end('a')
# print(new_dic)
# while True:
