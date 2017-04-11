import requests
import json
import time
from collections import Counter
import os
import re

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
def req(url,id):
    res = requests.get(url,headers=headers)
    try:
        alldata = res.json()
    except:
        return
    tracks = alldata['result']['tracks']
    track_list = []

    for track in tracks:
        track_dict = {}
        track_dict[str(track['id'])] = track['name']
        track_list.append(track_dict)
        print(track_dict)
    # track_dict[str(id)] = track_list
    return track_list

def savedata(content):
    dic = {}
    dic["data"] = content
    with open('alltracks.txt','a+',errors='ignore',encoding='utf-8')as f:
        f.write(str(dic))
        f.write('\n')
        print('写入ok')

def fetchdata():
    pre_url = 'http://music.163.com/api/playlist/detail?id='
    id_list = [67367440,72236650,33852017,91545874,454784139,6948994,96849048,7311288,310128330,54748656,51747765,2372886,
               15603311,21031673,4804729,67784383,70682754,15850922,89486796,108079371,7778099,83848216,116124529,60544,
               116480266,243866,38083688,497519,24719054,71014645,5940079,4961063,327907266,6422170
               ]
    all = []
    for id in id_list:
        url = pre_url + str(id)
        track_list = req(url,id)
        all += track_list
        time.sleep(2)
    savedata(all)
    return all

def anlysis(data):
    tracks = data
    # print(tracks)
    id_list = []
    for track in tracks:
        # print(track)
        for key in track:
            # print(key)
            id_list.append(key)
            break
    print(id_list)
    id_counts = Counter(id_list)
    top_100 = id_counts.most_common(100)
    print(top_100)
    #
    result = []
    result1 = set()
    for id in top_100:
        for track in tracks:
            # print('track',track)
            if id[0] in track:
                # print(track)
                result1.add(str(track))
                for i in track:
                    print(i)
                    result.append(track[i])
                    break
    result = list(set(result))
    result1 = list(result1)
    with open('result.txt','w',errors='ignore',encoding='utf-8')as f:
        f.write(str(top_100))
        f.write('\n')
        f.write(str(result))
        f.write('\n')
        f.write(str(result1))

def main():
    data = fetchdata()
    anlysis(data)

if __name__ == '__main__':
    main()
