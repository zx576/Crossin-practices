# -*- coding: utf-8 -*-
from scipy.misc import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
from collections import Counter

# 读入 西游记 txt 文件
text = open('西游记.txt',encoding='utf-8',errors='ignore').read()

# 使用 jieba 分词
text_jieba = list(jieba.cut(text))

# 使用 counter 做词频统计，选取出现频率前 100 的词汇
c = Counter(text_jieba)
common_c = c.most_common(100)

''' 读入数据类似下表
{
'行者': 3949,
'的': 4819,
'在': 2475,
'罢': 510,
'叫': 858,
'无': 380,
'那里': 696,
}
'''

# 读入女神图片
bg_pic = imread('0170314145554.png')

# 配置词云参数
wc = WordCloud(
			# 设置字体
			font_path = '李旭科书法1.4.ttf',
			# 设置背景色
            background_color='white',
            # 允许最大词汇
            max_words=200,
            # 词云形状
            mask=bg_pic,
            # 最大号字体
            max_font_size=100,
            )


# 生成词云
wc.generate_from_frequencies(dict(common_c))

# 生成图片并显示
plt.figure()
plt.imshow(wc)
plt.axis('off')
plt.show()

# 保存图片
wc.to_file('anne.jpg')
