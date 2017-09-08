# coding=utf-8
'''

思路：

本题的解题思路分为两步
1. 首先根据题目使用 非 逻辑可以判断某人不为某国人
2. 在 1 的基础上逐一排除

'''

def judge():

	lst_country = {'AM', 'RU', 'GE', 'FR', 'IT', 'EN'}
	lst_p = [i for i in 'ABCDEF']
	# 初始化
	dct = {}
	for p in lst_p:
		dct[p] = lst_country

	# 根据题目信息做初步筛选
	# A
	dct['A'] = dct['A'] - set(['AM', 'RU', 'GE', 'FR'])
	# E
	dct['E'] = dct['E'] - set(['AM', 'RU', 'GE'])
	# B
	dct['B'] = dct['B'] - set(['GE', 'AM'])
	# C
	dct['C'] = dct['C'] - set(['AM', 'RU', 'GE', 'IT', 'FR'])
	# F
	dct['F'] = dct['F'] - set(['GE'])

	# 字典转为 list
	lst = []
	for k, v in dct.items():
		lst.append([k,v])

	# 排序
	lst.sort(key=lambda x: len(x[1]))

	# 整理
	for i in range(len(lst)):
		set_c = lst[i][1]
		for j in range(i+1, len(lst)):
			lst[j][1] -= set_c

	# 打印输出
	for i in lst:
		print('{0} 为 {1}'.format(i[0], list(i[1])[0]))


if __name__ == '__main__':
	judge()


'''
最后的结果为

C 为 EN英国人
A 为 IT意大利人
E 为 FR法国人
B 为 RU俄罗斯人
F 为 AM美国人
D 为 GE德国人

本题看起来不难，可也不是每个小伙伴的答案都正确，同时有几位同学使用了很多层 for 循环嵌套，我们是不太推荐这样做的。
优秀的同学如下：

鼠赽 和 徐大龙 同学使用了 itertools 模块下的 permutations 函数，值得参看，代码地址分别如下：
paste.ubuntu.com/25469565
https://github.com/PeytonXu/learn-python/blob/master/cases/country_belong/country_belong.py

王任 同学的一行代码也十分惊艳，地址如下：
http://paste.ubuntu.com/25464189/


其他完成题目的同学有：

 听雨 / Seerz / Don human Edshot machine /你有靐吗

'''

