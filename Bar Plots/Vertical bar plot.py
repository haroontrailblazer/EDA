import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 2]

# Vertical Bar Plot
plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1)
plt.bar(categories, values, color='blue')
plt.title('Vertical Bar Plot')