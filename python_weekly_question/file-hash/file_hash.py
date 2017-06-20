# coding = utf-8

import hashlib
import sys

# 获取 HASH 值
def check_hash():
    res = {}
    file_path = sys.argv[1]
    source = open(file_path, 'rb').read()
    res['md5'] = hashlib.md5(source).hexdigest()
    res['sha1'] = hashlib.sha1(source).hexdigest()
    res['sha256'] = hashlib.sha256(source).hexdigest()
    res['sha512'] = hashlib.sha512(source).hexdigest()
    return res

# 打印 hash 值
if __name__ == '__main__':
    for key,value in check_hash().items():
        print(key + ":" + value)

# 使用方法
# 命令行下 python file_hash.py your_file_path
# 比较打印出的结果与网页结果

# 代码筛选
'''
徐大龙同学的代码考虑了读取大文件时优化问题：
https://github.com/PeytonXu/learn-python/blob/master/cases/hash_file/hash_file.py

Hurray同学 计算了多种 hash 算法：
https://paste.ubuntu.com/24814203/

'''
