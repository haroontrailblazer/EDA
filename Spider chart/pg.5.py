import numpy as np
import matplotlib.pyplot as plt

# Data
labels = ['A', 'B', 'C', 'D', 'E']
values = [4, 3, 2, 5, 4]

# Number of variables
num_vars = len(labels)

# Compute angle of each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The plot is a circle, so we need to "complete the loop"
values += values[:1]
angles += angles[:1]

# Plot
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, values, color='orange', alpha=0.25)
ax.plot(angles, values, color='orange', linewidth=2)
ax.set_yticklabels(['1', '2', '3', '4', '5'], color='grey', size=12)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, color='red', size=15)

plt.show()