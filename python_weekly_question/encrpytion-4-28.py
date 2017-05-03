#-*- coding:utf-8 -*-

import base64
import hashlib

choices = [
        '多喝热水',
        '我们在一起吧',
        '我选择原谅你',
        '别说话，吻我'
        ]

encrypted_string = 'NDRiMWZmMmVjZTk5MTFjMWI1MDNkYTY0MzZlYTAzMTA=\n'

def decrypt(choices,string):
    for i in choices:
        md5 = hashlib.md5()
        md5.update(i.encode('utf-8'))
        md5_s = md5.hexdigest()
        base64_s = base64.encodestring(md5_s.encode('utf-8'))
        if base64_s == string.encode('utf-8'):
            return i

print(decrypt(choices,encrypted_string))
