import requests
import json

header = {'User-Agent':
                  'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
          }
def fetchData():
    htmlpage = requests.get('http://rj.baidu.com/soft/ranking/1',headers=header)
    content = htmlpage.text
    print(content)


fetchData()