#-*- coding:utf-8 -*-

from collections import Counter
import re

with open(r'E:\GIT\practice\Crossin-practices\python_weekly_question\Jane Eyre.txt','r') as f:
    all_words = f.read().lower()

rule = re.compile(r'\w+',re.IGNORECASE)
words = re.findall(rule,all_words)

counter_words = Counter(words)
common_words = counter_words.most_common(100)

print(dict(common_words))
print('Jane Eyre.txt\n')
print('=======================')
n = 0
for i in common_words:
    n += 1
    print(n,'\t%s\t%d'%(i[0],i[1]))
