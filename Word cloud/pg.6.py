from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

text = "Quantum Computing"
mask = np.array(Image.open('path/to/mask/image.png'))

wordcloud = WordCloud(width=800, height=400, mask=mask, background_color='white').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()