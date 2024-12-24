import matplotlib.pyplot as plt
import numpy as np

# Data
np.random.seed(0)
x = np.random.rand(10)
y = np.random.rand(10)
sizes = np.random.rand(10) * 1000
colors = np.random.rand(10)

# Basic Bubble Chart
plt.figure(figsize=(12, 10))
plt.subplot(2, 2, 1)
plt.scatter(x, y, s=sizes, alpha=0.5)
plt.title('Basic Bubble Chart')