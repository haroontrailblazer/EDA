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
ax.fill(angles, values, color='blue', alpha=0.25)
ax.plot(angles, values, color='blue', linewidth=2)
ax.set_yticklabels([])

ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

plt.show()