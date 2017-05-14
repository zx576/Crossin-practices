# -*- coding: utf-8 -*-
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import collections


# 从 txt 文件中获取信息，去除不必要的信息，将歌词组成字符串
def get_data():

    with open('lyrics.txt','r',encoding='utf-8')as f:
        all_info = f.readlines()

    string = ''
    for row in all_info:
        spt_row = row.split(']')
        for info in spt_row:
            if '[' in info:
                continue
            else:
                string += info

    # 去掉一些特殊符号
    del_lst = ['）','（','】','【','\n',',','。','：','；',' ',':','…','，']
    for ele in del_lst:
        string = string.replace(ele,'')
    return string

# jieba 分词，取出词频前 20 的词汇
def jieba_h(string):

    cut_list = list(jieba.cut(string))
    counter = collections.Counter(cut_list)
    m20 = counter.most_common(20)

    return m20

# 生成词云保存到文件
def generate_ciyun(data):


    dct_data = dict(data)
    print(dct_data)
    wc = WordCloud(
    			# 设置字体
    			font_path = '汉仪行楷简.ttf',
                # font_size = 15,
    			# 设置背景色
                background_color='white',
                # 允许最大词汇
                max_words=200,
                # 最大号字体
                # max_font_size=100,
                )

    wc.generate_from_frequencies(dct_data)
    wc.to_file('ciyun.png')


def main():

    string = get_data()
    data_20 = jieba_h(string)
    generate_ciyun(data_20)

if __name__ == '__main__':
    main()
