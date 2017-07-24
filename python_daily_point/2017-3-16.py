# coding=utf-8
import requests

url = 'http://www.ssd.noaa.gov/flanis/flanis.swf'

req = requests.get(url)

with open('flanis.swf', 'wb')as f:
    f.write(req.content)


    
