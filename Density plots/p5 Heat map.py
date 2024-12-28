import matplotlib.pyplot as plt
import numpy as np
# Plot different types of plots
# Heatmap using imshow
heatmap_data = np.random.rand(10, 10)
plt.imshow(heatmap_data, cmap='viridis')
plt.colorbar()
plt.title('Heatmap')
plt.show()