import base64
import hashlib

string = '多喝热水'


md5 = hashlib.md5()
md5.update(string.encode('utf-8'))
md5_s = md5.hexdigest()

print(md5_s)
# print(type(md5_s))
base64_s = base64.encodestring(md5_s.encode('utf-8'))
#
print(base64_s)


base64_j = b'NDRiMWZmMmVjZTk5MTFjMWI1MDNkYTY0MzZlYTAzMTA=\n'

base64_s_s = base64.decodestring(base64_j)
print(base64_s_s)


print(md5_s.encode('utf-8')==base64_s_s)
