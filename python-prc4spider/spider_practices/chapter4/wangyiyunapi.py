import requests
import json
import pymongo

# 所有 API 接口示例页面
# srs = 'http://moonlib.com/606.html'

client = pymongo.MongoClient()
db = client.wangyi
db_playlists = db.playlists
db_lyrics = db.lyrics

headers = {
    'Cookie': 'appver=1.5.0.75771',
    'Referer':'http://music.163.com/'
}

# 搜索关键词，返回播放量最大的歌单
def search(keywords):

    url = 'http://music.163.com/api/search/pc'
    data = {'s':keywords,'offset':1,'limit':10,'type':1000}
    req = requests.post(url,data=data,headers=headers)
    content = req.json()

    playlists = []
    for item in content['result']['playlists']:
        try:
            playlists.append(item['id'])

        except Exception as e:
            print(e)
            continue


    return playlists
    

# 根据歌单 ID, 获取所歌单内歌曲信息，保存到数据库
def get_songs(ply_lists):

    url = 'http://music.163.com/api/playlist/detail?id={}&updateTime=-1'
    for id in ply_lists:
        print('正在采集歌:',id)
        s_url = url.format(id)
        req = requests.get(s_url,headers=headers)
        content = req.json()
        db_playlists.insert_one(content['result'])


# 获取歌词
def get_lyric():

    url = 'http://music.163.com/api/song/lyric?os=pc&id={}&lv=-1&kv=-1&tv=-1'

    # 针对所有的歌单
    for playlist in db_playlists.find():
        # 针对某歌单中所有的歌曲
        for track in playlist['tracks']:
            song_id = track['id']
            l_url = url.format(song_id)
            print('正在处理:',l_url)
            req = requests.get(l_url,headers=headers)
            content = req.json()

            # 使用 update_one 防止重复信息
            db_lyrics.update_one({'id':song_id},{'$set':content},upsert=True)



def main():
    ply_lists = search('古风')
    get_songs(ply_lists)
    get_lyric()


if __name__ == '__main__':
    main()
