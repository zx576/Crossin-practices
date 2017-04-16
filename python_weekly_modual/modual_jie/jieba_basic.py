#-*- coding:utf-8 -*-
import jieba
#
string = '今天天气特别好，很开心'
#
res = jieba.cut(string,cut_all=True)
# res2 = jieba.cut_for_search(string)
#
print('使用cut:',list(res))
# print('使用cut_for_search:',list(res2))
# from jieba.analyse import extract_tags
#
#
# with open('西游记.txt','r',errors='ignore')as f:
    # data = f.read()
#
# res = extract_tags(data,topK=10,withWeight=True)
# print(res)


# print(list(res))


# res = jieba.tokenize(u'%s'%data)
# res = jieba.tokenize(string)
# print(list(res))
# for i in res:
#     if '行者' in i:
#         print(i)
#         break
