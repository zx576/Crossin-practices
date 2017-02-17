#-*- coding:utf-8 -*-
import requests
# 导入提取 ip 的接口
from extract_ip import extract_ip
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




# 调用
if __name__ == '__main__':
    res = main()
    print(res)
'''
#简单示例
from extract_ip import extract_ip
new_ip = extract_ip()
print(new_ip)
'''