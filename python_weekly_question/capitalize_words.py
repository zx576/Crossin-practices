#-*- coding:utf-8 -*-

quote = "How can mirrors be real if our eyes aren't real"
def fuc(string):
    '''func - 使某一字符串所有字符都大写'''
    list_new_string = [i.capitalize() for i in string.split()]
    new_string = ' '.join(c_n_s)
    return new_string

print(fuc(quote))
