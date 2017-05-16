#### 【问题描述】

在题目 xxx 中，我们已经知道如何使用网易云音乐的 API 了，本题在此基础上，分析下载的歌词文件，使用 jieba库 提取出词频最高的前 20 个词，然后使用 wordcloud 库或者 echarts ,生成词云图。

#### 【解决思路】

1. 导入 txt 文件，提取出有效信息

```python

with open('lyrics.txt','r')as f:
    data = f.readlines()
    

```

2. 切分中文词汇
使用 jieba 处理中文词汇,然后再使用 collections.Counter 统计词频

```python
import jieba
import collections.Counter

data = list(jieba.cut(string))
coun = collections.Counter(data)
m_20 = coun.most_common(20)


```


3. 生成词云图

使用 wordcloud 库生成词云图，并保存到文件。

```python
import wordcloud

wc = wordcloud.WordCloud()
wc.generate_from_frequencies(dict(data))
wc.to_file('target.png')

```
