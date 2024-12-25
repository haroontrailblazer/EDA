from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

text = "Quantum Computing is the future of technology"
stopwords = set(STOPWORDS)
stopwords.update(["is", "the", "of"])

wordcloud = WordCloud(width=800, height=400, stopwords=stopwords).generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()