import matplotlib.pyplot as plt 
import numpy as np 
# Generate random data for scatter plot 
x = np.random.rand(50)  # 50 random values for x-axis 
y = np.random.rand(50)  # 50 random values for y-axis 
# Create the scatter plot 
plt.scatter(x, y, color='blue', marker='o') 
# Add labels and title 
plt.xlabel('X-axis') 
plt.ylabel('Y-axis') 
plt.title('Simple Scatter Plot') 
# Display the plot 
plt.show()
