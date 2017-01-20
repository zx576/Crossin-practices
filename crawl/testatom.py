import re

rule = re.compile(r'abc')

string = 'abcsdfger'

res = re.search(rule,string)

print(res)
