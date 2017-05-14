#-*- coding:utf-8 -*-
import json
import urllib.request,urllib.parse

class Baidu_Api(object):
    def __init__(self):
        self.url = {'Phone_url':'http://apis.baidu.com/chazhao/mobilesearch/phonesearch?phone=',
        'IP_url':'http://apis.baidu.com/chazhao/ipsearch/ipsearch?ip=',
        'ID_url': 'http://apis.baidu.com/chazhao/idcard/idcard?idcard='}
    #百度API网页请求，变量为输入内容以及self.url中的key，以便调用，返回json数据。
    def request_url(self,value,url):
        rep = urllib.request.Request(self.url[url] + value,headers={'apikey':'2fd858449606c0d8eaaea2cea84b14c7'})
        resp = urllib.request.urlopen(rep)
        content = resp.read().decode('utf-8')
        data = json.loads(content)
        if data['error'] == 0:
            print('请求成功')
            return data
        else:
            print(data['msg'])

    #号码归属地查询函数
    def PhoneNum_check(self,num,url='Phone_url'):
        data = self.request_url(num,url='Phone_url')
        if data:
            info = data.get('data')
            print('归属地：',info['city'] + info['operator'])
        else:
            pass
    #IP地址查询函数
    def IP_check(self,num,url='IP_url'):
        data = self.request_url(num,url='IP_url')
        if data:
            info = data.get('data')
            print('归属地：', info['city'])
        else:
            pass
    #身份证号信息查询函数
    def ID_check(self,num,url='School_url'):
        data = self.request_url(num,url='ID_url')
        if data:
            info = data.get('data')
            print('性别：',info['gender'])
            print('地址：',info['address'])
            print('星座：',info['constellation'])
        else:
            pass


method = Baidu_Api()
#判断输入数据长度调用函数，默认输入参数合法
def main():
    print('程序提供 1.身份证查询，2.IP地址查询，3.手机号归属地查询')
    while True:
        args = input('>>>>>')
        if args == '1':
            value = input('输入身份证号：')
            method.ID_check(value, url='ID_url')
            break
        elif args == '3':
            value = input('输入手机号：')
            method.PhoneNum_check(value,url='Phone_url')
            break
        elif args == '2':
            value = input('IP地址：')
            method.IP_check(value,url='IP_url')
            break
        else:
            print('非法输入！！！')


while True:
    main()
