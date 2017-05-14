from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = open('Jane Eyre.txt','r').read()
wordcloud = WordCloud().generate(text)

plt.imshow(wordcloud)
plt.axis('off')
plt.show()

wordcloud.to_file('test.jpg')
