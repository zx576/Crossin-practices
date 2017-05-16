import requests
import json
import csv

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
                        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}

max_behot_time = [1494768775]

# 访问 API 地址，获取数据
def get_info(url):
    global max_behot_time
    req = requests.get(url,headers=header)
    content = req.json()
    max_behot_time.append(content['next']['max_behot_time'])

    info = []
    for item in content['data']:
        lst = []
        try:
            lst.append(item['title'])
            lst.append(item['abstract'])
            lst.append(item['comments_count'])
            info.append(lst)
        except Exception as e:
            print(e)
            continue

    return info


# 保存到文件
def save(lst):

    with open('toutiao.csv','a+',encoding='utf-8')as f:
        writer = csv.writer(f)
        writer.writerow(['标题','概述','评论数'])
        for i in lst:
            writer.writerow(i)


# 主函数
def main():
    global max_behot_time
    url = 'https://www.toutiao.com/api/pc/feed/?category=news_sports' \
          '&utm_source=toutiao&widen={}'

    # 获取前 5 个时间戳
    for i in range(5):
        time_stamp = max_behot_time.pop()
        t_url = url.format(time_stamp)
        lst_info = get_info(t_url)
        save(lst_info)

if __name__ == '__main__':
    main()
