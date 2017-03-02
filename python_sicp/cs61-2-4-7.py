#-*- coding:utf-8 -*-
# empty = 'empty'
# def mutable_link():
#     contents = empty
#     def dispatch(message,value=None):
#         nonlocal contents
#         if message == 'len':
#             return len_link(contents)
#         elif message == 'getitem':
#             return getitem_link(contents,value)
#
#         elif message == 'push_first':
#             contents = link(value,contents)
#
#
a = [[i for i in range(k+1)] for k in range(5)]
print(a)
