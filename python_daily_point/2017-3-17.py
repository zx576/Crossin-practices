
# import re
# def f():
#     print('hello,world')
#
# f() # call the func
#
# ss = '12323423fdsgf'
#
# rule = re.compile(r'\d+')
#
# res = re.findall(rule,ss)[0]
#
# print(type(res))

import qrcode
# import

# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
#
# qr.add_data('Some data')
# qr.make(fit=True)
#
# img = qr.make_image(fill_color="black", back_color="white")
img = qrcode.make('Some data here')
