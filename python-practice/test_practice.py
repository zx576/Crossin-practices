import re
import shutil
import os
# shutil.move(r'E:\coding-related\pic\标贯击数的校正.docx',r'E:\coding-related')
#
#
# # print('suc')
# status = True
# path = ''
# while status:
#     path = input('>>>>>')
#     if os.path.exists(path):
#         status = False
#     else:
#         print('地址无效')
#
# print(path)


# a = ['']
#
# if a[0] :
#     print('cc')
# b = ['sss']
#
# print(a+b)
list = ['e:\\test\\IMG_7014.JPG', 'e:\\test\\IMG_7015.JPG', 'e:\\test\\IMG_7016.JPG', 'e:\\test\\IMG_7029.JPG', 'e:\\test\\IMG_7033.JPG', 'e:\\test\\IMG_7035.JPG', 'e:\\test\\list.html', 'e:\\test\\pypiwin32-219.win32-py2.7 (2).exe', 'e:\\test\\pypiwin32-219.win32-py2.7.exe', 'e:\\test\\python-2.7.12.msi', 'e:\\test\\Python-Email (1).png', 'e:\\test\\Python-Email (2).png', 'e:\\test\\Python-Email.png', 'e:\\test\\python-excel.pdf', 'e:\\test\\safds - 副本.rm', 'e:\\test\\safds.rmvb', 'e:\\test\\玩转大学静态模板006.pptx', 'e:\\test\\玩转大学静态模板007.ppt', 'e:\\test\\玩转大学静态模板008.ppt', 'e:\\test\\玩转大学静态模板009.ppt', 'e:\\test\\玩转大学静态模板010.ppt']

video_compile = re.compile(r'.+\.rmvb',re.I)

for i in list:
    video = re.findall(video_compile, i)
    print(video)



# a = ['asd.sdfa','.jpg','sdfgs.png','sdafas.jpeg']
# f = 'asd.sdfa,erew.jpg,sdfgs.png,sdafas.jpeg'
#
# c = re.compile(r'\w+\.jpg|.+\.png|.+\.jpeg')
#
# m = []
# for i in a:
#     b = re.findall(c,i)
#     print(b)
#     m += b
#
# print(m)

# def a():
#     return 1,2
#
# def b(*args):
#     p1 = a()[0]
#     print(p1)
#
# b()