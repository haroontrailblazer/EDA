import matplotlib.pyplot as plt
import squarify as sq

# Data
sizes = [50, 25, 12, 6, 4, 3]
labels = ['A', 'B', 'C', 'D', 'E', 'F']
nested_sizes = [30, 20, 10, 5, 3, 2]
nested_labels = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']

# Plot
plt.figure(figsize=(10, 6))
sq.plot(sizes=sizes, label=labels, alpha=0.7)
sq.plot(sizes=nested_sizes, label=nested_labels, alpha=0.5, color=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6'])
plt.axis('off')
plt.show()