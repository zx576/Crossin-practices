# coding=utf-8

# import requests
# import bs4
#
# url = 'http://http.phpddt.com/'
#
# def req_url(url):
#     req = requests.get(url)
#     print(req.encoding)
#     page = req.text.encode('ISO-8859-1')
#     # print(page)
#     soup = bs4.BeautifulSoup(page, 'lxml')
#     soup_tb = soup.find('table')
#     soup_tr = soup_tb.find_all('tr')[1:]
#     dct = {}
#     for tr in soup_tr:
#         tds = tr.find_all('td')
#         key = tds[0].string
#         value = tds[1].string.replace('\u3000','')
#         dct[key] = value
#
#     print(dct)
#     return dct
#
# req_url(url)

class Person:
    name = [1]

p1 = Person()
p2 = Person()
p1.name.append(2)

print(p1.name)
print(p2.name)
print(Person.name)

