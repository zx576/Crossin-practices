import requests
import json
import time
from collections import Counter

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)'
    ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
# 网络请求获取数据
def req(url,id):
    # requests 请求
    res = requests.get(url,headers=headers)
    # json 处理响应
    alldata = res.json()
    # 获取歌单信息
    tracks = alldata['result']['tracks']
    track_list = []
    # 获取歌名便于后续查找建立歌单
    # 获取音乐 ID 便于统计频率
    for track in tracks:
        track_dict = {}
        track_dict[str(track['id'])] = track['name']
        track_list.append(track_dict)
        print(track_dict)
    # track_dict[str(id)] = track_list
    return track_list

# 分发歌单url,并返回所有歌曲信息
def fetchdata():
    # api 接口
    pre_url = 'http://music.163.com/api/playlist/detail?id='
    # 需要处理的歌单，手动筛选了一下
    id_list = [
                67367440,72236650,33852017,91545874,454784139,6948994,96849048,
                7311288,310128330,54748656,51747765,2372886,15603311,21031673,
                4804729,67784383,70682754,15850922,89486796,108079371,7778099,
                83848216,116124529,60544,116480266,243866,38083688,497519,24719054,
                71014645,5940079,4961063,327907266,6422170
               ]
    all = []
    # 获取所有歌单数据
    for id in id_list:
        url = pre_url + str(id)
        track_list = req(url,id)
        all += track_list
        time.sleep(2)
    return all

# 数据分析
def anlysis(data):
    # 所有的歌曲信息
    tracks = data
    # print(tracks)
    id_list = []
    # 获取所有歌曲 id
    for track in tracks:
        # print(track)
        for key in track:
            # print(key)
            id_list.append(key)
            # break
    # print(id_list)
    # 获取 id 频率
    id_counts = Counter(id_list)
    # 获取前 100 歌曲
    top_100 = id_counts.most_common(100)
    # print(top_100)
    # 通过歌曲 id 打印出歌曲名
    result = []
    for id in top_100:
        for track in tracks:
            # print('track',track)
            if id[0] in track:
                for i in track:
                    # print(track[i])
                    result.append(track[i])
    # 歌曲去重
    result = list(set(result))
    return result

def savedata(data):
    # 组装为 dict 形式
    dic = {}
    dic['result'] = data
    # json 处理之后存入，便于以后查看
    result = json.dumps(dic)
    with open('all_data.txt','w',errors='ignore',encoding='utf-8')as f:
        f.write(result)


def main():
    print('process starts')
    # 获取数据
    data = fetchdata()
    # 分析数据
    result = anlysis(data)
    # 保存分析结果
    savedata(result)

if __name__ == '__main__':
    main()
