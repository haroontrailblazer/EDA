from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = "Quantum Computing"
wordcloud = WordCloud(width=800, height=400, colormap='plasma').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()