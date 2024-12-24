import matplotlib.pyplot as plt
import numpy as np

# Data
np.random.seed(0)
x = np.random.rand(10)
y = np.random.rand(10)
sizes = np.random.rand(10) * 1000
colors = np.random.rand(10)
# Bubble Chart with Different Markers
plt.subplot(2, 2, 4)
markers = ['o', 's', 'D', '^', 'v', '<', '>', 'p', '*', 'h']
for i in range(len(x)):
    plt.scatter(x[i], y[i], s=sizes[i], alpha=0.5, marker=markers[i % len(markers)], label=f'Point {i+1}')
plt.legend()
plt.title('Bubble Chart with Different Markers')