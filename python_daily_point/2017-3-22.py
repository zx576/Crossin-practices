import requests


url = 'http://www.jianshu.com/'
req = requests.get(url)

print(req.text)
