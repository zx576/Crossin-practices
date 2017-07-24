# coding=utf-8
# author = zhouxin
# date = 2017.7.20

import re

def open_book():

    with open('new.html', 'r', encoding='utf-8')as f:
        data = f.read()

    return data


def color_words(words):

    # pt1 = re.compile(r'liver cirrhosis', re.I)
    # pt2 = re.compile(r'PVT', re.I)
    # pt3 = re.compile(r'portal vein thrombosis', re.I)
    # pt4 = re.compile(r'anticoagulation', re.I)
    # lst = ['liver cirrhosis', 'PVT', 'portal vein thrombosis','anticoagulation']
    lst = ['cirrhosis']
    new = words
    for i in lst:
        pt = re.compile(r'{}'.format(i), re.I)
        new = re.sub(pt, '<span style="color: red">{}</span>'.format(i), new)

    return new


def save_book(words):

    with open('new_2.html', 'w', encoding='utf-8')as f:
        f.write(words)


before_words = open_book()
new_words = color_words(before_words)
save_book(new_words)
