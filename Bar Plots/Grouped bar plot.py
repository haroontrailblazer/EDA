import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 2]

# Grouped Bar Plot
bar_width = 0.35
index = np.arange(len(categories))
plt.subplot(2, 2, 4)
plt.bar(index, values, bar_width, color='blue', label='Value 1')
plt.bar(index + bar_width, values2, bar_width, color='red', label='Value 2')
plt.title('Grouped Bar Plot')
plt.xticks(index + bar_width / 2, categories)
plt.legend()
plt.tight_layout()
plt.show()