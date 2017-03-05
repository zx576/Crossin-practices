#coding=gbk

import requests,json
import os
import io
import sys
url = "http://api.douban.com/v2/movie/in_theaters "
req = requests.get(url)
info = req.text
info.decode("gbk")
j_info =json.loads(info)

print j_info["title"] ,j_info["total"],j_info['start'],j_info['count']
