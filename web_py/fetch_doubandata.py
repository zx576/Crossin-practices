import requests
import json
import time
import sqlite3

def downloadid():
    try:
        res = requests.get('https://api.douban.com/v2/movie/top250?start=0&count=50')
    except:
        print('请求错误')
    else:
        resp = res.text    ###https://api.douban.com/v2/movie/subject/:1292063
        print(resp)
        content = json.loads(resp)
        print(content)
        sub = content.get('subjects')
        print(sub)
        id = []
        for i in sub:
            j = i['id']
            id.append(j)
    print(id)
    return id

def download_subjects(id):
    conn = sqlite3.connect('movies.db')
    for i in id:
        url = 'https://api.douban.com/v2/movie/subject/'+i
        try:
            re = requests.get(url)
            r = re.text
            content = json.loads(r)
            #print(content)
        except:
            print(i+'\t请求错误')
            continue
        else:
            if 'code' in content :
                print('id错误')
                continue
            else:
                id = content['id']
                title = content['title']
                origin = content['original_title']
                url = content['share_url']
                rating = content['rating']['average']
                image = content['images']['medium']
                directors = '/'.join([x['name'] for x in content['directors']])
                casts = '/'.join([x['name'] for x in content['casts']])
                year = content['year']
                genres = '/'.join(content['genres'])
                countries = '/'.join(content['countries'])
                summary = content['summary']
            #print(id,title,origin,url,rating,image,directors,casts,year,genres,countries,summary)
        try:
            sql = '''
            INSERT INTO movie(id,identity,title,origin,url,rating,image_url,directors,casts,year,genres,countries,summary)
            VALUES (NULL,'%s','%s','%s','%s','%d','%s','%s','%s','%s','%s','%s','%s');
            '''%(id,title,origin,url,rating,image,directors,casts,year,genres,countries,summary)
            conn.execute(sql)
            conn.commit()
            print(title + '\t写入成功')
        except:
            print(title+'\t写入数据库错误')
        finally:
            pass
        time.sleep(0.1)
    conn.close()


id = downloadid()
#print(id)
#download_subjects(id)
