import matplotlib.pyplot as plt
import numpy as np

# Data
np.random.seed(0)
x = np.random.rand(10)
y = np.random.rand(10)
sizes = np.random.rand(10) * 1000
colors = np.random.rand(10)
# Bubble Chart with Color
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5, cmap='viridis')
plt.colorbar()
plt.title('Bubble Chart with Color')