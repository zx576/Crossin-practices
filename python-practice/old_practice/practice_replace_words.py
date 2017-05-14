#-*- coding:utf-8 -*-
#生成替换词文件
def generate_file():
    words = ['a1','b2','cc','de','23']
    with open('words.txt','w')as f:
        for i in words:
            f.write(i)
            f.write('\n')
#读取替换词文件，并写入list
def block():
    global b_words
    b_words = []
    with open('words.txt','r') as l:
        for i in l.readlines():
            if i:
                b_words.append(i.strip())
    # print(b_words)
#替换关键词
def replace(word):
    for i in b_words:
        #print(i)
        word = word.replace(i,'*'*len(i))
    print(word)

generate_file()
block()
while True:
    word = input('>>>>')
    if word:
        replace(word)
    else:
        exit()


