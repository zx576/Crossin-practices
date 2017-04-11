import base64
# import urllib.parse as p
import requests

# import

# uni = '%3c%61%20%68%72%65%66%3d%22%68%74%74%70%3a%2f%2f%77%77%77%2e%66%72%65%65%70%72%6f%78%79%6c%69%73%74%73%2e%6e%65%74%2f%7a%68%2f%31%34%34%2e%32%31%37%2e%31%38%39%2e%32%35%30%2e%68%74%6d%6c%22%3e%31%34%34%2e%32%31%37%2e%31%38%39%2e%32%35%30%3c%2f%61%3e'
# uni = uni.replace('%','\\')
# print(p.unquote(uni))

befor = '''
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding:gzip, deflate, sdch
Accept-Language:zh-CN,zh;q=0.8,zh-TW;q=0.6
Cache-Control:no-cache
Cookie:visited=2017%2F04%2F07+14%3A17%3A22; hl=zh; pv=6; userno=20170407-011027; from=direct; __atuvc=5%7C14; __utma=251962462.2007234129.1491542245.1491542245.1491542245.1; __utmc=251962462; __utmz=251962462.1491542245.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=251962462.Canada
Host:www.freeproxylists.net
Pragma:no-cache
Proxy-Connection:keep-alive
Referer:http://www.freeproxylists.net/zh/?page=2
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36
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
