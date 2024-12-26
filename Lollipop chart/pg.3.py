import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.arange(1, 11)
y = np.random.randint(1, 20, size=10)

# 3. Lollipop Chart with Different Colors
plt.figure(figsize=(10, 6))
plt.stem(x, y, linefmt='r-', markerfmt='bo', basefmt='g-')
plt.title('Lollipop Chart with Different Colors')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()