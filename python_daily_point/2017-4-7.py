import base64
# import urllib.parse as p
import requests

# import

# uni = '%3c%61%20%68%72%65%66%3d%22%68%74%74%70%3a%2f%2f%77%77%77%2e%66%72%65%65%70%72%6f%78%79%6c%69%73%74%73%2e%6e%65%74%2f%7a%68%2f%31%34%34%2e%32%31%37%2e%31%38%39%2e%32%35%30%2e%68%74%6d%6c%22%3e%31%34%34%2e%32%31%37%2e%31%38%39%2e%32%35%30%3c%2f%61%3e'
# uni = uni.replace('%','\\')
# print(p.unquote(uni))

befor = '''
authority:www.dropbox.com
method:GET
path:/s/g2h2hww7u5njwnp/9H.jpg
scheme:https
accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
accept-encoding:gzip, deflate, sdch, br
accept-language:zh-CN,zh;q=0.8,zh-TW;q=0.6
cache-control:no-cache
cookie:locale=zh_CN; gvc=MzM3MzcxMDY4ODEwNTg0NjA1MzU3NTc2ODU5NDE1MTQyNTQwOTMw; __Host-js_csrf=2-fkrlQy_yUdLNCXH-ZPncrG; t=2-fkrlQy_yUdLNCXH-ZPncrG; __Host-ss=2P1-qb5QvQ; _ga=GA1.2.1267769861.1493274266
pragma:no-cache
upgrade-insecure-requests:1
user-agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36

'''
new_s = befor.split('\n')
data = {}
for i in new_s:
    k_v = i.split(':')
    if len(k_v) == 2:
        data[k_v[0]] = k_v[1]
print(data)
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}

# req = requests.get('http://www.freeproxylists.net/zh/?page=2',headers=data)
# print(req.text)
