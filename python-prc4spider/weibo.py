import requests
# import

url = 'http://t.cn/RXEklZM'

req = requests.get(url)
print(req.text)
