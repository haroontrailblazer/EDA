import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 
import numpy as np 
# Generate sample data 
np.random.seed(0) 
x = np.random.rand(100) 
y = np.random.rand(100) 
z = np.random.rand(100) 
# Create a figure and a 3D axes 
fig = plt.figure(figsize=(10, 7)) 
ax = fig.add_subplot(111, projection='3d') 
# Create a 3D scatter plot 
scatter = ax.scatter(x, y, z, c='blue', marker='o') 
# Set labels and title 
ax.set_xlabel('X-axis') 
ax.set_ylabel('Y-axis') 
ax.set_zlabel('Z-axis') 
ax.set_title('3D Scatter Plot') 
# Show the plot 
plt.show() 
