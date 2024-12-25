import matplotlib.pyplot as plt
import squarify as sq

# Data
sizes = [50, 25, 12, 6, 4, 3]
labels = ['A', 'B', 'C', 'D', 'E', 'F']
value_labels = [f'{label}\n{size}' for label, size in zip(labels, sizes)]

# Plot
plt.figure(figsize=(10, 6))
sq.plot(sizes=sizes, label=value_labels, alpha=0.7)
plt.axis('off')
plt.show()