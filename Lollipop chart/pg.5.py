import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.arange(1, 11)
y = np.random.randint(1, 20, size=10)

# 5. Lollipop Chart with Custom Line Styles
plt.figure(figsize=(10, 6))
plt.stem(x, y, linefmt='--', markerfmt='D', basefmt='-')
plt.title('Lollipop Chart with Custom Line Styles')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()