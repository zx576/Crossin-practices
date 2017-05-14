import requests
import json
import bs4

url = 'https://www.linkedin.com/company-beta/3089363/'

req = requests.get(url)

print(req.text)

# page = req.text
#
# soup = bs4.BeautifulSoup(page,'lxml')
#
# soup_tbody = soup.find('tbody')
#
# soup_tr = soup_tbody.find_all('tr')
#
# for tr in soup_tr:
#     info = tr.get_text()
#     print(info)
