from collections import Counter

list = ['red','green','red']

c = Counter(list)
print(c.keys())
c = Counter('adffdsads')

print(c)

c = Counter({'red':1,'green':2})
print(c)

c = Counter(cats=4,dogs=8)
print(c)
c = Counter('adffdsads')
print(c.most_common(3))

# with open('xx.txt','r',encoding='utf-8') as f:
