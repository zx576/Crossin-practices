# -*- coding: utf-8 -*-
from textblob import TextBlob


def translate(text_list):
    translated_text_list = []
    for text in text_list:
        text = text.decode('utf-8')
        translated_text = repr(TextBlob(text).translate(to='zh-CN'))
        translated_text = translated_text.replace('TextBlob("', '')
        translated_text = translated_text.replace('")', '')
        translated_text = translated_text + '\n'
        translated_text_list.append(translated_text)
    return translated_text_list


with open('original_text.txt', 'r') as f:
    original_text_list = f.readlines()

with open('translated_text.txt', 'w') as f:
    f.writelines(translate(original_text_list))

if True:
    print'翻译成功！'
