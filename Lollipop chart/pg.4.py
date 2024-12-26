import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.arange(1, 11)
y = np.random.randint(1, 20, size=10)

# 4. Lollipop Chart with Filled Markers
plt.figure(figsize=(10, 6))
plt.stem(x, y, linefmt='-', markerfmt='o', basefmt='-')
plt.setp(plt.gca().lines, markersize=10, markerfacecolor='orange')
plt.title('Lollipop Chart with Filled Markers')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()