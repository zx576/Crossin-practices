from collections import Counter
import re
with open(r'E:\GIT\practice\Crossin-practices\python_weekly_question\Jane Eyre.txt','r') as f:
    all_words = f.read()

w_com = re.compile(r'\w+',re.IGNORECASE)
words = re.findall(w_com,all_words)

c = Counter(words)
c_common = c.most_common(100)
print(c_common)


# test = '''nipped his pointed nose, shrivelled his cheek,
# stiffened his gait; made his eyes red, his thin lips blue;'''
#
# words = re.findall(r'\w+',test)
# print(words)

# def func():
#     print('abc')
# print(func())
