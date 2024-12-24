import matplotlib.pyplot as plt
import numpy as np

# Data
np.random.seed(0)
x = np.random.rand(10)
y = np.random.rand(10)
sizes = np.random.rand(10) * 1000
colors = np.random.rand(10)
#Bubble Chart with Edge Colors
plt.scatter(x, y, s=sizes, alpha=0.5, edgecolors='k', linewidth=2)
plt.title('Bubble Chart with Edge Colors')