# import clipboard
# import time
# import pythoncom
#
# def handle_data(user_input):
#     '''处理用户输入'''
#     print(user_input)
# def obtain_data():
#     '''
#     检测用户输入，返回数据
#     '''
#     return clipboard.paste()
#
# # clipboard.copy('dgdsg')
# while True:
#     user_c = int(input('>>>'))
#     if user_c == 1:
#         user_input = obtain_data()
#         handle_data(user_input)
#     else:
#         continue
# pythoncom.PumpMessages()
# clipboard.copy('')
#user_ine_data(user_input)
# clipboard.cop
# print('周鑫')
# a = [(x,y) for x in range(1,6) for y in range(4) ]
# print(len(a))
#
# b = [1,2,3,4,5]
#
# for i in zip(a,b):
#     print(i)
import requests
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
url = 'http://www.baidu.com'

req = requests.get(url)

print(req.text)
