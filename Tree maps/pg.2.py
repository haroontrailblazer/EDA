import matplotlib.pyplot as plt
import squarify

# Data
sizes = [50, 25, 12, 6, 4, 3]
labels = ['A', 'B', 'C', 'D', 'E', 'F']
colors = ['red', 'green', 'blue', 'purple', 'orange', 'pink']

# Plot
plt.figure(figsize=(10, 6))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.7,edgecolor="black", linewidth=2)
plt.axis('off')
plt.show()