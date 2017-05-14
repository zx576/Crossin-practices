
import requests
import json

srs = 'http://moonlib.com/606.html'

headers = {
    'Cookie': 'appver=1.5.0.75771',
    'Referer':'http://music.163.com/'
}

# 搜索关键词，返回播放量最大的歌单
def search(keywords):
    url = 'http://music.163.com/api/search/pc'
    data = {'s':keywords,'offset':10,'limit':10,'type':1000}
    req = requests.post(url,data=data,headers=headers)
    # print()
    content = req.json()
    max_count_list = 0
    max_playcount = 0
    for item in content['result']['playlists']:
        if item['playCount'] > max_playcount:
            max_playcount = item['playCount']
            max_count_list = item['id']

    return max_count_list


# 根据歌单 ID, 获取所有歌曲 ID 和歌曲名
def get_songs(ply_list):
    url = 'http://music.163.com/api/playlist/detail?id={}&updateTime=-1'

    songs_dict = {}
    # for id in ply_lists:
    s_url = url.format(ply_list)
    req = requests.get(s_url,headers=headers)
    content = req.json()
    print(content['result']['name'])
    for track in content['result']['tracks']:
        songs_dict[track['name']] = track['id']

    return songs_dict


# 获取歌词
def get_lyric(songs_dict):
    result = {}
    url = 'http://music.163.com/api/song/lyric?os=pc&id={}&lv=-1&kv=-1&tv=-1'
    for name,id in songs_dict.items():
        l_url = url.format(id)
        req = requests.get(l_url,headers=headers)
        content = req.json()
        lyric_dic = content.get('lrc',None)
        if lyric_dic:
            lyric = lyric_dic.get('lyric',None)
            if lyric:
                result[name] = lyric

        # print(content)
    return result

# 保存到文件
def save(result):
    with open('lyrics.txt','w',encoding='utf-8')as f:
        for name,lrc in result.items():
            f.write(name+'\n')
            f.write(lrc+'\n')
            # f.write('\n')

d
def main():
    max_count_list = search('古风')
    songs_dict = get_songs(max_count_list)
    result = get_lyric(songs_dict)
    save(result)

if __name__ == '__main__':
    main()
