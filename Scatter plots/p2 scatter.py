import matplotlib.pyplot as plt 
import numpy as np 
# Generate random data for scatter plot 
x1 = np.random.rand(30)  # 30 random values for x1-axis 
y1 = np.random.rand(30)  # 30 random values for y1-axis 
x2 = np.random.rand(30)  # 30 random values for x2-axis 
y2 = np.random.rand(30)  # 30 random values for y2-axis 
# Create the scatter plot 
plt.scatter(x1, y1, color='blue', label='Dataset 1', marker='o') 
plt.scatter(x2, y2, color='red', label='Dataset 2', marker='x') 
# Add labels and title 
plt.xlabel('X-axis') 
plt.ylabel('Y-axis') 
plt.title('Scatter Plot of Two Datasets') 
plt.legend() 
# Display the plot 
plt.show() 
