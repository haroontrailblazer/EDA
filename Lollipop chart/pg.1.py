import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.arange(1, 11)
y = np.random.randint(1, 20, size=10)

# 1. Basic Lollipop Chart
plt.figure(figsize=(10, 6))
plt.stem(x, y)
plt.title('Basic Lollipop Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()