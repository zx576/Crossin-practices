import requests
import json


header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
                        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}


# 访问 API 地址，获取标题
def get_info(url):

    req = requests.get(url,headers=header)
    content = req.json()

    title_list = []
    for item in content['data']:
        title_list.append(item['title'])

    return title_list

# 保存到文件
def save(lst):

    with open('Nbatitles.txt','a+',encoding='utf-8')as f:
        for i in lst:
            f.write(i+'\n')


# 主函数
def main():
    url = 'https://www.toutiao.com/api/pc/feed/?category=NBA' \
          '&utm_source=toutiao&widen={}'
    for i in range(1,6):
        c_url = url.format(i)
        print(c_url)
        lst = get_info(c_url)
        save(lst)


if __name__ == '__main__':
    main()
