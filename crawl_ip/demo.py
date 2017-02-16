#-*- coding:utf-8 -*-
import requests

# 导入提取 ip 的接口
from extract_ip import extract_ip
# 导入抓取 ip 接口
# from fetch_ip import fetch_ip
# 多进程
import multiprocessing
import time

'''
接入 ip 示例
'''


headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1;'
                      ' en-US)AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20',
           }
# 请求部分
def req_url(url,proxy):
    try:
        req = requests.get(url,headers=headers,proxies=proxy)
        print(proxy)
        print(req)
        content = req.text
    except:
        return
    return content

# 控制部分
def main():
    url = 'http://www.baidu.com/'
    while True:
        # 获取 ip 接口
        new_ip = extract_ip()
        result = req_url(url,new_ip)
        if result:
            return result



'''
# 多进程示例
if __name__ == '__main__':

    p1 = multiprocessing.Process(target=main)
    p2 = multiprocessing.Process(target=fetch_ip)

    p2.start()
    time.sleep(10)
    p2.start()

'''
# 一般调用
if __name__ == '__main__':
    res = main()
    print(res)


