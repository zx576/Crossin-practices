#-*- coding:utf-8 -*-
from scipy.misc import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import json
import re

# 读入一组词频字典文件
text = open('words_frequency.txt').read()
content = re.sub('\'', '\"', text)
text_dict = json.loads(content)

''' 读入数据类似下表
{
'you': 2993,
'and': 6625,
'in': 2767,
'was': 2525,
'the': 7845,
}
'''

# 读入女神图片
bg_pic = imread('0170314145554.png')

# 配置词云参数
wc = WordCloud(
			# 设置字体
			font_path = 'BeaverScratches.ttf',
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
wc.generate_from_frequencies(text_dict)

# 生成图片并显示
plt.figure()
plt.imshow(wc)
plt.axis('off')
plt.show()

# 保存图片
wc.to_file('anne3.jpg')
