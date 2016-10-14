import os

cre = os.path.exists('pic')
print(cre)
if not cre:
    os.mkdir('pic')
    print('ok')
os.rmdir('pic')
print(cre)