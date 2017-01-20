import json
import requests

# with open('testj.txt','r',errors='ignore',encoding='utf-8')as f:
#     alldata = f.read()
#
# alldata = json.loads(alldata)
# tracks = alldata['result']['tracks']
# for track in tracks:
#     print(track['name'])
#
# url = 'http://music.163.com/api/playlist/detail?id=58451795'
# res = requests.get(url)
# print(res.json())
id_list = [67367440,72236650,33852017,91545874,454784139,6948994,96849048,7311288,310128330,54748656,51747765,2372886,
               15603311,21031673,4804729,67784383,70682754,15850922,89486796,108079371,7778099,83848216,116124529,60544,
               116480266,243866,38083688,497519,24719054,71014645,5940079,4961063,327907266,6422170
               ]

print(len(id_list))