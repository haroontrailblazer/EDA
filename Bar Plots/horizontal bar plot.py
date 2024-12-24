import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 2]

# Horizontal Bar Plot
plt.subplot(2, 2, 2)
plt.barh(categories, values, color='green')
plt.title('Horizontal Bar Plot')