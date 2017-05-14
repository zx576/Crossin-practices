import urllib.request
from lxml import etree

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
                        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}


# 请求网页，获取网页内容
def req(url):

    construct_req = urllib.request.Request(url, headers=header)
    open_req = urllib.request.urlopen(construct_req)
    data = open_req.read().decode('utf-8')

    return data


# 解析网页，获取所需内容
def parse(data):

    tree = etree.HTML(data)
    xpath_div = tree.xpath('//div[@class="article block untagged mb15"]')

    data = ''
    for div in xpath_div:

        author = div.xpath('.//h2/text()')
        content = div.xpath('.//div[@class="content"]/span/text()')
        funny_count = div.xpath('.//span[@class="stats-vote"]/i/text()')
        repost_count = div.xpath('.//span[@class="stats-comments"]/a/i/text()')

        head = author[0] + '\t好笑数:' + funny_count[0] + '\t回复数:' + repost_count[0]
        content = head + '\n' + ''.join(content) + '\n'

        data += content

    return data


# 保存内容
def save(data):
    with open('qsbk.txt', 'a+', encoding='utf-8') as f:
        f.write(data)


# 主函数
def main():
    url = 'https://www.qiushibaike.com/8hr/page/{}/'
    # 逐页 请求-解析-保存
    for i in range(1, 4):
        qurl = url.format(i)
        req_data = req(qurl)
        parse_data = parse(req_data)
        save(parse_data)


if __name__ == '__main__':
    main()
