import pyquery


url = 'http://www.baidu.com'

pq = pyquery.PyQuery(url=url)

print(pq)

import requests

req = requests.get(url,verify)
