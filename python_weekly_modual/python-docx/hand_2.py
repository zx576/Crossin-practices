
from docx import Document
import re

def open_book():

    doc = Document('text.docx')
    for pa in doc.paragraphs:
        tt = pa.text
        new_words = color_words(tt)
        save_book(new_words)


def color_words(words):

    # pt1 = re.compile(r'liver cirrhosis', re.I)
    # pt2 = re.compile(r'PVT', re.I)
    # pt3 = re.compile(r'portal vein thrombosis', re.I)
    # pt4 = re.compile(r'anticoagulation', re.I)
    lst = ['liver cirrhosis', 'PVT', 'portal vein thrombosis','anticoagulation']
    new = words
    for i in lst:
        pt = re.compile(r'{}'.format(i), re.I)
        new = re.sub(pt, '<span style="color: red">{}</span>'.format(i), new)

    return new


def save_book(words):

    with open('new.html', 'a+', encoding='utf-8')as f:
        f.write(words)
        f.write('<br>')

open_book()
