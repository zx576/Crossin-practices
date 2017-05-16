import requests


req = requests.get('http://shanghai.bitauto.com/')

print(req.text)
