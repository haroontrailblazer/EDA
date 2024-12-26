import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.arange(1, 11)
y = np.random.randint(1, 20, size=10)

# 2. Horizontal Lollipop Chart
plt.figure(figsize=(10, 6))
plt.stem(x, y, orientation='horizontal')
plt.title('Horizontal Lollipop Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()