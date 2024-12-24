import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 2]

# Stacked Bar Plot
values2 = [4, 6, 3, 4]
plt.subplot(2, 2, 3)
plt.bar(categories, values, color='blue', label='Value 1')
plt.bar(categories, values2, bottom=values, color='red', label='Value 2')
plt.title('Stacked Bar Plot')
plt.legend()
