# print(b)
# print(print)
def func():
    a,b = 1,1
    while True:
        yield a
        a,b = b,a+b

c = func()
for i in func():
    if i > 100:
        break
    print i